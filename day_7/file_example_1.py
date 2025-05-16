# Example 1 for file handling

# check whether log directory exists, if not create the log directory

import os
import pathlib
import shutil

source = pathlib.Path("logs")
source.mkdir(exist_ok=True)

log_path = pathlib.Path("logs/samplefile.log")
log_path.touch(0o666, exist_ok=True)

with open("logs/samplefile.log", "a") as f:
    f.write(", Thank you for adding content in file")

shutil.copy("logs/samplefile.log", "logs/samplefilecopy.log")

shutil.make_archive("logs", "zip", source)