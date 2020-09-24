import os


class Config((object)):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1262230516:AAHTyQGYtzoxxmS1Ak69c-XhEY9R8qIfY-I")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 1650886))
    API_HASH = os.environ.get("API_HASH", "ed3539071edfe2cf8cae10bfb7965d1d")
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = {int(x) for x in os.environ.get("AUTH_CHANNEL", "-1001274688892").split()}
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./JiraiyaBot"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get(
        "DEF_THUMB_NAIL_VID_S",
        "https://placehold.it/90x90")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    ARIA_TWO_STARTED_PORT = int(os.environ.get("ARIA_TWO_STARTED_PORT", 6800))
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(
        os.environ.get("MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START", 600))
    MAX_TG_SPLIT_FILE_SIZE = int(
        os.environ.get(
            "MAX_TG_SPLIT_FILE_SIZE",
            1072864000))
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "█")
    UN_FINISHED_PROGRESS_STR = os.environ.get("UN_FINISHED_PROGRESS_STR", "░")
    # add offensive API
    TG_OFFENSIVE_API = os.environ.get("TG_OFFENSIVE_API", None)
    CUSTOM_FILE_NAME = os.environ.get("CUSTOM_FILE_NAME", "")
    RCLONE_CONFIG = os.environ.get("RCLONE_CONFIG", "[starboyjiraiyabot]
type = drive
client_id = 710784367903-dlhk5phgct49urah3j6i8log4ee21u7l.apps.googleusercontent.com
client_secret = yGCae6lheNdF-ODMTqIhVFjS
scope = drive
token = {"access_token":"ya29.a0AfH6SMA-DIbkoLItSUNfUv-nZqZawMnE6YdcGNB5Z4p8TRscxu8UElGg0F2mlNsnn_Gocto_1m3is1DUJBIodFqRtqYzLkHzgIMfVkac0f0Sjh5xUKonNJUBxw2wR4TH2eyccDOwYeFi7dVvv8zLBDV6U-mltUqEz4Q","token_type":"Bearer","refresh_token":"1//0g0OqapcEQ6TYCgYIARAAGBASNgF-L9IrjkMb9gwcaY9kWbyonULVvy0Q9MqbGI2r2JhsLTUZGGzNzJ9SSJD58VmKs8DBVMcYqw","expiry":"2020-09-24T12:30:57.0673738+05:30"}")
    DESTINATION_FOLDER = os.environ.get(
        "DESTINATION_FOLDER", "TorrentLeech-Gdrive")
    INDEX_LINK = os.environ.get("INDEX_LINK", "https://starboy.noobz.workers.dev")
