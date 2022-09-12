Dialog.create("Image Processing Macro");
Dialog.addMessage("Choose the function that you want to apply to an image directory! \n \n Note: choose directories that contain only images! \n \n Pablo Hofbauer, 9/30/15");

Dialog.addChoice("Function:", newArray("Convert to 8-bit (TIFF)", "Auto adjust brightness and convert to JPG", "Save all open images to a directory","Apply 10 Threshold for DAPI Images","Apply Threshold for TRITC Images","Measure Images"));

Dialog.show();

choice = Dialog.getChoice();




//save as jpg and auto adjust brightness
function action(input, output, filename) {
        open(input + filename);
		//run("Brightness/Contrast...");
		run("Enhance Contrast", "saturated=0.35");
        saveAs("Jpeg", output + filename);
        close();
}

//save as 8-bit tiff
function action2(input, output, filename)
		{
        open(input + filename);
		run("8-bit");
        saveAs("Tiff", output + filename);
        close();
		}

////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////DAPI Threshold////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////
		function action3(input, output, filename)
		{
        open(input + filename);
		setMinAndMax(10, 255);
		run("Apply LUT");
        saveAs("Tiff", output + filename);
        close();
		}

////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////TRITC Threshold////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////

		function action4(input, output, filename)
		{
        open(input + filename);
		setMinAndMax(40, 255);
		run("Apply LUT");
        saveAs("Tiff", output + filename);
        close();
		}

		
		function action5(input, filename)
		{
        open(input + filename);
		run("Measure");
		//wait(100);
        close();
		}

/*		function action6(input, output, filename)
		{
        var amin = 0;
        open(input + filename);
		setMinAndMax(amin, 255);
		run("Apply LUT");
        saveAs("Tiff", output + filename);
        close();
		}
*/
//save Video as AVI
//function action3(input, output)
//		{
//			run("Image Sequence...", "open=[input] sort");
//			run("Enhance Contrast", "saturated=0.35");
//			run("AVI...", "frame=7 save=[output]");
 //       
//		}


if (choice=="Convert to 8-bit (TIFF)")
	{

		input = getDirectory("Choose an Input Directory");

		output = getDirectory("Choose an Output Directory");
		
    	setBatchMode(true); 
		list = getFileList(input);
		for (i = 0; i < list.length; i++)
        action2(input, output, list[i]);
		setBatchMode(false);

		exit("Files succesfully saved!")

	} 
		
	else {
    		if(choice=="Auto adjust brightness and convert to JPG")
    		{
            	input = getDirectory("Choose an Input Directory");

				output = getDirectory("Choose an Output Directory");
            	
            	setBatchMode(true); 
				list = getFileList(input);
				for (i = 0; i < list.length; i++)
        		action(input, output, list[i]);
				setBatchMode(false);

				exit("Files succesfully saved!")
   			 } 
   			 	
  		else {
        		if (choice=="Save all open images to a directory")
        		{
 				
 				// get image IDs of all open images 
					dir = getDirectory("Choose a directory to save the open images to"); 
					ids=newArray(nImages); 
					for (i=0;i<nImages;i++) { 
					        selectImage(i+1); 
					        title = getTitle;  
					        ids[i]=getImageID; 
					
					        saveAs("tiff", dir+title); 
					}
       	    	 }
         	   
         else {
        		if (choice=="Apply 10 Threshold for DAPI Images")
        		{
 				
            	input = getDirectory("Choose an Input Directory");

				output = getDirectory("Choose an Output Directory");
            	
            	setBatchMode(true); 
				list = getFileList(input);
				for (i = 0; i < list.length; i++)
        		action3(input, output, list[i]);
				setBatchMode(false);

				exit("Files succesfully saved!")
					}
			
				else {
        		if (choice=="Apply Threshold for TRITC Images")
        		{
 				
            	input = getDirectory("Choose an Input Directory");

				output = getDirectory("Choose an Output Directory");
            	
            	setBatchMode(true); 
				list = getFileList(input);
				for (i = 0; i < list.length; i++)
        		action4(input, output, list[i]);
				setBatchMode(false);

				exit("Files succesfully saved!")
					}

				else {
        		if (choice=="Measure Images")
        		{
 				
            	input = getDirectory("Choose an Input Directory");
            	
            	setBatchMode(true); 
				list = getFileList(input);
				for (i = 0; i < list.length; i++)
        		action5(input, list[i]);
				setBatchMode(false);

				exit("Files succesfully measured!")
					}
				

         	   

    }

