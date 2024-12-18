from datetime import datetime

DATE_FORMAT_DATETIME = "%d-%m-%Y %H:%M:%S"
DATE_FORMAT_DATE = "%d-%m-%Y"

def current_timestamp():
    return datetime.now().strftime(DATE_FORMAT_DATETIME)