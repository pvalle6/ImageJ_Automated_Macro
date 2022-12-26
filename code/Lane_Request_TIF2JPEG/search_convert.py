import os #used in date, directory naming
from datetime import date
import imagej #imports necessary imagej module
day = date.today()

ij = imagej.init('sc.fiji:fiji') #activates imagej

# MACRO USED IN PyImageJ
MACRO = """
#@ String input
#@ String output
#@output Object greeting
open(input);
        saveAs("Jpeg", output);
        close();
"""
day = date.today()
def search_copy(sub_loc): 
        """ Searches and Copies a Directory while running each file through PyImageJ """
        new_directory = os.path.join(os.path.dirname(sub_loc),('JPEG_Formatted_ImageJ_' + str(day)))
        for dirpath, dirnames, filenames in os.walk(sub_loc):
                new_loc = new_directory + '/' + os.path.basename(dirpath)
                os.makedirs(new_loc)
                for files in filenames:  
                    args ={
                    'input': os.path.join(dirpath,files),
                    'output': os.path.join(new_loc, files)}
                    ij.py.run_macro(MACRO, args)
DIRECTORY_LOC = '/workspaces/ImageJ_Automated_Macro/code/test_dir/omega' # directory to be copied
search_copy(DIRECTORY_LOC)
