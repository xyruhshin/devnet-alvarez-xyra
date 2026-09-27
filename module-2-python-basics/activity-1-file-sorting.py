"""
Module 2 — Activity: File Sorting with os and shutil
Student: Xyra Shannel B. Alvarez
Date: September 27, 2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================

Simple file organizer that sorts files from my downloads folder
into different folders. it checks the file extension and moves
.jpg and .png files into the Images folder, while .pdf and .docx
files are moved into the Documents folder.


============================================
KEY VOCABULARY
============================================
- os module: module used to interact with the operating system, such as managing files and directories
- shutil module: module used to copy, move, rename, and delete files or directories
- file path: location or address of a file on a computer
- directory: folder used to organize and store files or other folders
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

folder = "Downloads"

for file in os.listdir(folder):
    file_path = os.path.join(folder, file)

    if file.endswith(".jpg") or file.endswith(".png"):
        destination = os.path.join(folder, "Images")
        os.makedirs(destination, exist_ok=True)
        shutil.move(file_path, destination)

    elif file.endswith(".pdf") or file.endswith(".docx"):
        destination = os.path.join(folder, "Documents")
        os.makedirs(destination, exist_ok=True)
        shutil.move(file_path, destination)


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]

The mistake I made is forgetting that the destination folders
needed to exist before moving the files. I realized that before 
moving anything, I need to check or create folder first.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
