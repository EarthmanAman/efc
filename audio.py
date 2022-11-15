import os
import subprocess
import csv

def audio_converter(row):
    input_name = row[-1] + f".{row[1]}"
    output_name = row[-1] + f".{row[-2]}"
    try:
        subprocess.run(
        ["ffmpeg", "-i", f"inputs_files/{input_name}", "-vn", f"result/{output_name}"], check=True
        )
    except:
        raise Exception(
        "Please DOWNLOAD, INSTALL & ADD the path of FFMPEG to Environment Variables!"
    )
audio_converter(["audio", "mp3", "ogg", "test"])