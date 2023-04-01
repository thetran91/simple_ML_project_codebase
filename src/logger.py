"""
Every execution information can be retrieved into logging system. E.g. error, success, data processing step, etc.
--> will be call every time we need in every execution/files
getcwd() returns current working directory (cwd)

"""
import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # log files format
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) # create the name for the log files
os.makedirs(logs_path,exist_ok=True) # create folder for the log files

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

## create logging by logging package
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


# if __name__ == "__main__":
#     logging.info("Logging is started")