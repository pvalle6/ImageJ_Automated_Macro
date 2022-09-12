// This script is edited from an original script by Pablo Hofbauer created for Phillip Jung by 
// Pablo Hofbauer
// This script is implemented into another script "search_convert_copyimage" by Peter Vallet
// for Lane Yutzy
// this script will be called by search convert copy on recursive directories
Dialog.create("Image Processing Macro_Python_Peter");
Dialog.addMessage("Choose the function that you want to apply to an image directory! \n \n Note: choose directories that contain only images! \n \n Pablo Hofbauer, 9/30/15");

//save as jpg and auto adjust brightness (autoadjust removed in this verision of the script)
function action(input, output, filename) {
        open(input + filename);
		//run("Brightness/Contrast...");
		//run("Enhance Contrast", "saturated=0.35");
        saveAs("Jpeg", output + filename);
        close();
}

// runs the script to convert
input = getDirectory("Choose an Input Directory");

output = getDirectory("Choose an Output Directory");

setBatchMode(true); 
	list = getFileList(input);
	for (i = 0; i < list.length; i++)
action(input, output, list[i]);
	setBatchMode(false);

exit("Files succesfully saved!")

	 	


   



