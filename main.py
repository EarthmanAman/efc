import os
import subprocess
import csv

if not os.path.exists("inputs_files"):
    raise Exception("Please create and put all your vidoes in assets folder!")

mkv_list = os.listdir("inputs_files")

if not os.path.exists("result"):
    os.mkdir("result")

with open("inputs.csv", "r") as file:
    reader = csv.reader(file, delimiter=",")
    for row in reader:
        input_name = row[-1] + f".{row[1]}"
        output_name = row[-1] + f".{row[-2]}"
        try:
            subprocess.run(
            ["ffmpeg", "-i", f"inputs_files/{input_name}", "-codec", "copy", f"result/{output_name}"], check=True
            )
        except:
            raise Exception(
            "Please DOWNLOAD, INSTALL & ADD the path of FFMPEG to Environment Variables!"
        )
print("Done")