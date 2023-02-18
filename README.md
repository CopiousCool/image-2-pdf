# image-2-pdf
Small script that converts image files .jpg .jpeg .png into .pdf files
This code performs the following tasks:

It imports necessary libraries - os, sys, traceback from Python Standard Library, and PIL (Python Imaging Library) which is a third-party library for image processing.
It checks whether a folder named "results" exists in the current working directory. If not, it creates the folder.
It creates a subdirectory in the "results" folder with the current date and time as the folder name. This folder will store the converted PDF files.
It creates a subdirectory in the above-created folder named "logs" that will store the logs generated while processing the image files.
It opens two log files - "successful_conversions.txt" and "failed_conversions.txt" - inside the "logs" folder.
It iterates through all the files in the current working directory and attempts to convert each image file (JPG, JPEG, PNG) into a PDF file using the PIL library.
If the image conversion is successful, the corresponding file name is written to the "successful_conversions.txt" log file.
If the image conversion fails, the corresponding file name is written to the "failed_conversions.txt" log file along with the error details.
After all the files have been processed, the log files are closed.
