import glob
import os
import shutil

'''
Tool that reads a text file with numbers of images in them line by line.
Once read, it goes to the target directory and checks if the image number
is in the directory. If it is, it copies that file into the destination
directory.

Common image names from camera exports have a
prefix, a number, and then the image format.
(example: DSC01923.PNG)

Used on Mac OS, can be modified for windows easily by changing path formats.
'''

def main():

    dest_path = "" # example: "/Users/username/desktop/folder")
    target_path = "" # example: "/Users/username/desktop/folder"
    img_names_file = ""# example: "namesFile.txt"
    image_format = "" # example: ".ARW", ".JPG", ".PNG"
    image_prefix = "" # example: "DSC"

    with open(img_names_file) as f:
        lines = f.readlines()
    file_names = []
    for line in lines:
        file_names.append(image_prefix +line.rstrip() + image_format)
    for foto in (glob.glob(target_path + "/*" + image_format)):
        for name in file_names:
            if (name in foto):
                fullp = os.path.join(target_path,name)
                shutil.copy(fullp,dest_path)



main()
