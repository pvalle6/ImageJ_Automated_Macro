# Peter Vallet, Jung Lab, 2022
# Search_Convert_CopyImage V1
# Script to convert TIF2JPEGs
# 1. Copies Parent Folder to renamed Parent Folder
# 2. Recursively Searches and runs Image Conversion Macro on TIF
# 3. Prints message Confirming Success
# Final is UNIX/MACOS compatible

import imagej #imports necessary imagej module

ij = imagej.init('sc.fiji:fiji') #activates imagej

##		Code below is modified from a script by Pablo Hofbauer for Phillip Jung
## 		Code takes a ImageJ macro as a string, then by use of arguments
##					in a dictionary, calls new folder name the macro
##					is then run on that folder, converting to JPEG
##					and then saving to a new folder

TP1 = '/workspaces/ImageJ_Automated_Macro/code/test_dir/omega/n1/'
TP2 = '/workspaces/ImageJ_Automated_Macro/code/test_dir/nu/n1/'
F1 = 'at3_1m4_03.tif'

macro = """
#@ String name
#@ int age
#@ String city
#@output Object greeting
greeting = "Hello " + name + ". You are " + age + " years old, and live in " + city + "."
"""
args = {
    'name': 'Chuckles',
    'age': 13,
    'city': 'Nowhere'
}
result = ij.py.run_macro(macro, args)
#print(result.getOutput('greeting'))