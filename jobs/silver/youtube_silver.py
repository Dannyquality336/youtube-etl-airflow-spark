import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__)
        )
    )
)

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

from config.settings import BRONZE_PATH, SILVER_PATH
from utils.logger import get_logger


logger = get_logger("silver")


def main():

    logger.info("Silver job started")

    spark = SparkSession.builder \
        .appName("youtube_silver") \
        .getOrCreate()

    df = spark.read \
        .option("multiline", "true") \
        .json(BRONZE_PATH + "/*.json")

    df.printSchema()

    exploded = df.selectExpr("explode(items) as item")

    flat = exploded.select(
        col("item.snippet.title").alias("title"),
        col("item.snippet.channelTitle").alias("channel"),
        col("item.snippet.publishedAt").alias("published")
    )

    flat.write \
        .mode("overwrite") \
        .parquet(SILVER_PATH)

    logger.info("Silver saved")

    spark.stop()


if __name__ == "__main__":
    main()