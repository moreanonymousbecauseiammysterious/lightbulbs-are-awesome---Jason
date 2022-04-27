import os
import shutil

source = input("ENTER THE SOURCE FOLDER NAME: ")
destination = input("ENTER THE DESTINATION FOLDER NAME: ")

source = source+"/"
destination = destination+"/"

list_of_files = os.listdir(source)
for file in list_of_files:
    shutil.copy((source+file),destination)