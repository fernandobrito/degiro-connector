import os

from typing import List


""" Migrate from 1.0.4 to 1.0.5

This script will do the following changes :
- Replace `Chart.Period` with `Chart.Interval`
- Replace `Chart.Resolution` with `Chart.Interval`
"""


def get_files_list(root_path=".") -> List[str]:
    files_list = list()

    for root, directories, files in os.walk(root_path):
        for name in files:
            if (
                name.endswith(".py")
                and ".tox" not in root
                and ".git" not in root
                and ".egg-info" not in root
                and "\\build\\lib" not in root
                and not name.endswith("setup.py")
            ):
                files_list.append(os.path.join(root, name))

    return files_list


def process(files_list: List[str]):
    print("Processing the following files : ")

    for file_path in files_list:
        if os.path.realpath(file_path) != os.path.realpath(__file__):
            with open(file_path, "r+") as f:
                file_source = f.read()
                replace_string = file_source
                replace_string = replace_string.replace(
                    "Chart.Period",
                    "Chart.Interval",
                )
                replace_string = replace_string.replace(
                    "Chart.Resolution",
                    "Chart.Interval",
                )

                if replace_string != file_source:
                    print("CHANGED   :", file_path)
                    f.seek(0)
                    f.write(replace_string)
                    f.truncate()
                else:
                    print("UNCHANGED :", file_path)


files_list = get_files_list(root_path=".")
process(files_list=files_list)
