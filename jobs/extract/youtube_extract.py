import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__)
        )
    )
)
import requests
import json
import os
from datetime import datetime

from config.settings import YOUTUBE_API_KEY, PLAYLIST_ID, BRONZE_PATH
from utils.logger import get_logger


logger = get_logger("extract")


def fetch_data():

    url = "https://www.googleapis.com/youtube/v3/playlistItems"

    params = {
        "part": "snippet",
        "playlistId": PLAYLIST_ID,
        "maxResults": 50,
        "key": YOUTUBE_API_KEY,
    }

    r = requests.get(url, params=params)

    data = r.json()

    return data


def save_raw(data):

    if not os.path.exists(BRONZE_PATH):
        os.makedirs(BRONZE_PATH)

    now = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = os.path.join(
        BRONZE_PATH,
        f"youtube_{now}.json"
    )

    with open(file_path, "w") as f:
        json.dump(data, f)

    logger.info(f"Saved raw file: {file_path}")


def main():

    logger.info("Extract started")

    data = fetch_data()
    print(data)

    save_raw(data)

    logger.info("Extract finished")


if __name__ == "__main__":
    main()