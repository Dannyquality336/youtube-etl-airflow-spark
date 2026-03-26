# config/settings.py

import os

# -----------------------
# API CONFIG
# -----------------------

YOUTUBE_API_KEY = "AIzaSyD-ZiqFGqlNYCICFmoPtTQUxT6UtHLw6NU"

PLAYLIST_ID = "PLBCF2DAC6FFB574DE"


# -----------------------
# PATH CONFIG
# -----------------------

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

BRONZE_PATH = os.path.join(BASE_DIR, "data/bronze/youtube")

SILVER_PATH = os.path.join(BASE_DIR, "data/silver/youtube")

GOLD_PATH = os.path.join(BASE_DIR, "data/gold/youtube")


# -----------------------
# APP CONFIG
# -----------------------

APP_NAME = "YOUTUBE_ETL_PIPELINE"