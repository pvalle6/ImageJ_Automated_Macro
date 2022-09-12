import os
import shutil
import pyimagej

# Peter Vallet, Jung Lab, 2022 
# Search_Convert_CopyImage V1
# Script to convert TIF2JPEGs
# 1. Copies Parent Folder to renamed Parent Folder
# 2. Recursively Searches and runs Image Conversion Macro on TIF
# 3. Prints message Confirming Success
# Final is UNIX/MACOS compatible

ij = imagej.init('sc.fiji:fiji')

## 		set this equal to parent folder of where you want to convert
OG_parent_path = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\laneTestInput\tif_files" #<<<<<<this one
######################
## 		don't touch below
new_parent_path = R"C:\Users\valle\OneDrive\Documents\EP-DE\data\laneTestInput\jpep_files"
##		creates a list from the subdirectories in given parent
##		creates an empty list to iterate new path files into 
OGsubdirectories = os.listdir(OG_parent_path)
newsubdirectories = []
## 		checks for the parent folder with images and names a copied
##					folder if found
##		does this by looping through original using x, y for copy creation
for x, y in enumerate(subdirectories):
	if not (os.path.isdir(OGsubdirectories[x])):
		raise ValueError("Original Path Name does not Exist. ~Search_Convert_Copy")
	else:
		#pretty sure that new_parent_path needs to be calling a list of changning subparents
		newsubdirectories[y] = (x+ R'\_JPEG_converted')

## 		checks if a new folder exists, if not, makes it based on
## 					original folders name 

##		possible not needed if already implemented into macro 
##					Image_Processing_Pablo_for_Phillip.ijm
## 					runs using ijm
if not (os.path.isdir(new_parent_path)):
	os.makedirs(new_parent_path)
## 		copies over file into renamed alternative folder
#copy_tree(OG_parent_path, new_parent_path)

# IMPLEMENT OS.WALK TO SEARCH PARENT DIRECTORY 
# AND CREATE A TUPLE WITH SUBDIRECTORIES


##		Code below is modified from a script by Pablo Hofbauer for Phillip Jung
## 		Code takes a ImageJ macro as a string, then by use of arguments 
##					in a dictionary, calls new folder name the macro 
##					is then run on that folder, converting to JPEG
##					and then saving to a new folder

# macro = """ 
# #@input 
# #@output
# #@folderCount
# function action(input, output, filename) 
# {
#         open(input + filename);
#         saveAs("Jpeg", output + filename);
#         close();
# }
# // runs the script to convert
# setBatchMode(true); 
# 	list = getFileList(input);
# 	for (i = 0; i < list.length; i++)
# action(input, output, list[i]);
# 	setBatchMode(false);

# exit("Files succesfully saved!")
# """
# count = 0
# args = {
# 	'input': OGsubdirectories[count],
# 	'output': newsubdirectories[count],
#  	'folderCount': count++ 
# }



# # NEED TO IMPLEMENT FUNCTION CALL FOR EVERY 
# # FOLDER IN DIRECTORY THAT NEEDS TO BE CONVERTED

# ij.py.run_macro(macro, args)