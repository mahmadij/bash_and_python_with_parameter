"""
========================================================== 
Changes the format of the file and saves it in the same S3 as test.csv. The purpose of this module is for testing only. 
==========================================================
"""

from project_root.python_scripts.common import get_secret, setup_logging
import boto3, pandas as pd, logging
from io import BytesIO
import os

def run_test():
    setup_logging(True,"../logs/test.log")
    try:
        source_key = "importer_file.csv"
        destination_key = "test.csv"

        df = pd.read_csv('../utility/importer_file.csv')
        correct_headers = [
            "identifier", "disabled", "personal:email", "personal:first_name", "personal:last_name", "personal:middle_name",
            "username"
        ]
        df.columns = correct_headers

        buffer = BytesIO()
        df.to_csv(buffer, index=False)
        buffer.seek(0)

        with open('.../utility/test.csv', "wb") as f:
            f.write(buffer.getvalue())
        logging.info(f"File saved locally")

        os.remove('../utility/importer_file.csv')
        logging.info(f"Local file deleted after upload.")

    except Exception as e:
        logging.exception("Error in file_transfer")

if __name__ == "__main__":
    run_test()