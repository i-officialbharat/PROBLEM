# Q {3}.WRITE A PYTHON PROGRAM TO PRINT THE CONTENT OF DIRECTORY USING OS MODULE import os

# I USED CHAT GPT
import os
# Specify the directory path
directory = input("/PYTHON")

# Check if the directory exists
if os.path.exists(directory):
    print("\nContents of the directory:")
    
    # List all files and folders
    for item in os.listdir(directory):
        print(item)
else:
    print  ("content")