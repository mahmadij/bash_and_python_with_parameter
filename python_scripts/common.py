"""
========================================================== 
This is a utility function that is used by multiple scripts. In order to follow DRY (Don't Repeat Yourself) rule and it makes it easier to manage code.
==========================================================
"""

import json
import boto3
from pathlib import Path
from dotenv import load_load_dotenv
import logging
import osfrom dotenv import load_dotenv


def get_secret(secret_name): 
    load_dotenv()
    region = os.getenv("AWS_REGION", "<optional default region>")  # Fallback to default_region if not set.
    client = boto3.client("secretsmanager", region_name=region) # Read from secret manager
    response = client.get_secret_value(SecretId=secret_name)
    return json.loads(response["SecretString"])

def setup_logging(debug=False,logfile=None):
    # Get the root project directory (two levels up from here)
    project_root = Path(__file__).resolve().parents[1]

    # Set the default log file path to <project_root>/logs/scripts.log
    if logfile is None:
        logfile = project_root / "logs" / "scripts.log"
    else:
        logfile = Path(logfile)

    logging.basicConfig(
        filename=logfile,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    if debug is True:
        logging.getLogger().addHandler(logging.StreamHandler())  # Also print to the console
