# Peter Vallet, Jung Lab, 2022
# Search_Convert_CopyImage 
# Script to convert TIF2JPEGs
# 1. Copies Parent Folder to renamed Parent Folder
# 2. Recursively Searches and runs Image Conversion Macro on TIF
# 3. Prints message Confirming Success
# Final is UNIX/MACOS compatible

import imagej #imports necessary imagej module
import os #used in date, directory naming
from datetime import date
day = date.today()

ij = imagej.init('sc.fiji:fiji') #activates imagej

# MACRO USED IN PyImageJ
macro = """
#@ String input
#@ String output
#@output Object greeting
open(input);
        saveAs("Jpeg", output);
        close();
"""

def search_copy(subLoc): ## function used 
    New_Directory = os.path.join(os.path.dirname(subLoc),('JPEG_Formatted_ImageJ_' + str(day)))
    for dirpath, dirnames, filenames in os.walk(subLoc):
        New_Loc = New_Directory + '/' + os.path.basename(dirpath)
        os.makedirs(New_Loc)
        #print(New_Loc)
        for files in filenames:  
            args ={
            'input': os.path.join(dirpath,files),
            'output': os.path.join(New_Loc, files)}
            ij.py.run_macro(macro, args)
directoryLoc = '/workspaces/ImageJ_Automated_Macro/code/test_dir/omega' # directory to be copied
search_copy(directoryLoc)
