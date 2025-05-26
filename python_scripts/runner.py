"""
========================================================== 
This is a utility script that routes incoming requests to the proper script to run. We can use the same script with different parameters.
==========================================================
"""

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", required=True, help="Specify the task to run (transfer/latest/test)")
    args = parser.parse_args()

    match args.task:
        case "transfer":
            from project_root.python_scripts.send_file_to_s3 import run_transfer
            run_transfer()
        case "test":
            from test_import_file import run_test
            run_test()
        case _:
            raise ValueError(f"Unknown task: {args.task}")

if __name__ == "__main__":
    main()
