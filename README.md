# Demystifying the code

## IMPORTANT NOTES:
- generate the venv from [requirements.txt](./project_root/requirements.txt) file by running the following scripts **one by one** from within the root folder of the project: 
```Bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    deactivate
  ```
- Build the folder structure you see in the image:
![folder_structure](./project_root/Images/folder_structure.png)

- Provide execute permission to runner.sh: chmod +x runner.sh.
- Edit the AWS_REGION entry inside the [.env](./project_root/.env) file as needed. For example, us-east-1 or us-east-2 (create a .env file inside the project's root folder if it doesn't exist).

## Code flow explained
The bash file [runner.sh](./project_root/runner.sh) is called from terminal with one of the following parameters:
- **test** for running the [test_import_file.py](./project_root/python_scripts/test_import_file.py) script.
- **transfer** for running the [send_file_to_s3.py](./project_root/python_scripts/send_file_to_s3.py) script which formats the file and sends it to S3.

The bash starts the venv and runs the [runner.py](./project_root/python_scripts/runner.py) code.

[runner.py](./project_root/python_scripts/runner.py) takes in the task parameter and routes to the proper script.

[common.py](./project_root/python_scripts/common.py) has the common utility functions. At this time, it pulls credentials from AWS secret manager and sets up logging.

## Logging
The python scripts are set to log messages in scripts.log file. However, you can set it up to any other log files and on the console as well. 
You can look at [test_import_file.py](./project_root/python_scripts//test_import_file.py) for an example.

## Security measures
The credentials have been added to AWS secret manager and policy has been set to only provide read access to the role running inside the Secure Agent.

The bash file [runner.sh](./project_root/runner.sh) has execute permissions; all other files are read only.
