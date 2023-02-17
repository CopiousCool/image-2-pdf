import os
import sys
import traceback
from PIL import Image
from datetime import datetime

# Create the results folder if it doesn't exist
if not os.path.exists("results"):
    os.mkdir("results")

# Create a subdirectory in the results folder with the current date and time
date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
result_folder = "results/" + date_time
if not os.path.exists(result_folder):
    os.mkdir(result_folder)

# Create the log folder in the same place as the result folder
log_folder = result_folder + "/logs"
if not os.path.exists(log_folder):
    os.mkdir(log_folder)

# Open the log files
success_log = open(log_folder + "/successful_conversions.txt", "w")
fail_log = open(log_folder + "/failed_conversions.txt", "w")

# Iterate through all files in the current directory
for file_name in os.listdir():
    try:
        # Check if the file is an image
        if not (file_name.endswith(".jpeg") or file_name.endswith(".jpg") or file_name.endswith(".png")):
            continue

        # Open the image file
        img = Image.open(file_name)

        # Convert the image to RGB
        img = img.convert("RGB")

        # Save the image to a PDF
        pdf_file_name = result_folder + "/" + os.path.splitext(file_name)[0] + ".pdf"
        img.save(pdf_file_name, "PDF" ,resolution=100.0)

        # Log the successful conversion
        success_log.write(file_name + "\n")
    except:
        # Log the failed conversion
        fail_log.write(file_name + "\n")
        fail_log.write("Error details: " + traceback.format_exc() + "\n")

# Close the log files
success_log.close()
fail_log.close()
