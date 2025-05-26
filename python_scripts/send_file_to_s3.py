"""
========================================================== 
Changes the format of the file and send it to an S3 bucket. This copies the file with the correct headers and sends it to an S3 bucket.
==========================================================
"""

from project_root.python_scripts.common import get_secret, setup_logging
import boto3, pandas as pd, logging
from io import BytesIO
import os

def run_transfer():
    setup_logging()
    try:
        secrets = get_secret("credentials")
        destination_s3 = boto3.client(
            's3',
            aws_access_key_id=secrets["<S3 key saved in secret manager>"], 
            aws_secret_access_key=secrets["<S3 secret saved in secret manager>"],
            region_name='<aws region>'
        )

        destination_bucket = "s3-uploads"
        destination_key = "production/filename.csv"

        response = source_s3.get_object(Bucket=source_bucket, Key=source_key)
        df = pd.read_csv('../utility/importer_file.csv')

        correct_headers = [
            "identifier", "disabled", "personal:email", "personal:first_name", "personal:last_name", "personal:middle_name",
            "username"
        ]
        df.columns = correct_headers

        buffer = BytesIO()
        df.to_csv(buffer, index=False)
        buffer.seek(0)

        destination_s3.put_object(Bucket=destination_bucket, Key=destination_key, Body=buffer.getvalue())
        logging.info(f"File transferred to {destination_bucket}/{destination_key}")

        os.remove('../utility/importer_file.csv')
        logging.info(f"Local file deleted after upload.")

    except Exception as e:
        logging.exception("Error in file_transfer")

if __name__ == "__main__":
    run_transfer()
