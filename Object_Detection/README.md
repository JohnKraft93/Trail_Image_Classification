This is the README file for object detection and all the necessary steps.

Step 0: File Directory should look like this after 

	~ data

		- object-detection.pbtxt

		- train.record

		- test.record

		- all_labels.csv

		- train_label.csv

		- test_label.csv

	~ images

		- unlabel images (.jpg files)

	~ annotations

		- labeled data (.xml files)

	~ ssd_mobilenet_v1_coco_2018_01_28

	        - pipeline.config

	~ training

		- ssd_mobilenet_v1_pets.config (You can use other config. files from TensorFlow)

	- generate_tfrecord.py: Uses .csv file to produce .RECORD files (From TensorFlow)

	- split_labels.IPYNB : Split data into training and testing data

	- xml_to_cvs.py : Convert xml labeled data to a cvs file

	- train.py : Get from tensorflow

	- ModelTrainingOnColab.IPYNB


Step 1: Need to label the data with labelImg.py file where you put boxes around the objects you are trying to classify
	For TrailImageClass. Either download all the files within the repository or run command git clone https://github.com/tzutalin/labelImg.git
	Step 1a: - classes are motorized, nonMotorized, mechanical, hybrid, vehicles, and dogs. Save files as .xml(PascalVOC)
	- Git repository: https://github.com/tzutalin/labelImg.git
	Step 1b: Change save directory to annotations for your .xml files

Step 2: Once you have labeled a considerate amount of photos, put .jpgs and .xml files in appropriate directories. .jpg files go into
	images directory and .xml files go into annotations directory

Step 3: Convert annotation directory to all_labels.csv file with xml_to_csv.py

Step 4: Split the all_label.csv file into a training and testing dataset with split_labels.IPYNB
	This is where you'll produce train_labels.csv and test_labels.csv

Step 5: Next it's time to generate the .record files with generate_tfrecord.py file. Necessary edits: command line options and
	class_text_to_int defition to match all position object classes

	Step 5a: command line prompt for train.record -
		 python generate_tfrecord.py --csv_input=data/train_labels.csv --output_path=data/train.record --image_dir=.\images

	Step 5b: command line prompt for test.record -
		 python generate_tfrecord.py --csv_input=data/test_labels.csv --output_path=data/test.record --image_dir=.\images

	NOTE : If an error pops up saying the csv_input is defined twice, clear your console and it should work.

Step 6: Make object-detection.pbtxt file that contains all the classes. 

	Ex. item { 

		id: 1

		name: 'motorized'

	    }

	    item {

		id: 2

		name: 'nonMotorized'

	    }

	    etc...

Step 7: Must edit ssd_mobilenet_v1_pets.config

	Step 7a: Change num_classes to the number of classes

	Step 7b: Set fine_tune_checkpoint: "ssd_mobilenet_v1_coco_2018_01_28/model.ckpt"

	Step 7c: Change input_path in train_input_reader to "data/train.record" (Or the file location of your train.record file)

	Step 7d: Change input_path in eval_input_reader to "data/test.record" (Or the file location of your test.record file)

	Step 7e: Must change the label_map_path to "data/object-detection.pbtxt" (Or the file location of your *.pbtxt file)

	Step 7f: If you're having memory issues, you could try to make the batch_size to smaller, but note, this wil cause your estimate gradient to be less accurate

Step 7: Train model using google colab with ModelTrainingOnColab.IPYNB.

	Step 7a: Add all files in directory to TensorFlow models git repository and then upload repository to google drive.

	Step 7b: If you have already uploaded TensorFlow models git repository then you only need to upload your training and data directories.

Step 9: Run through ModelTrainingOnColab.ipynb and here are few things to note

	Step 9a: Run through adding all the necessary libraries

	Step 9b: Must mount your google drive folder to access all necessary directories and files

	Step 9c: The free version of Google colab provides only ~12 GB of RAM. From experience, I was not able to training a model sucessfully because I needed more RAM.

		 However, the paid version did work for me to train.

Step 10: Training command - python train.py --train_dir=training/ --pipeline_config_path=training/ssd_mobilenet_v1_pets.config 

	NOTE: After a certain amount of passes, it will save a model.ckpt-**** in your training directory. You will use this model to update your resulting *.ckpt model

Step 11: Command to update your final *.ckpt - python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/ssd_mobilenet_v1_pets.config --trained_checkpoint_prefix training/model.ckpt-21892 --output_directory new_graph

Step 12: Once you have your final *.ckpt, zip up the new_graph directory and save it locally. From there we will use a python script to predict on new photo to test to see how well it performs on other photos

Step 13: Use custom_model_images.py to test on new photos. Changes necessary:

	Step 13a: If necessary, change MODEL_NAME to the directory you downloaded from your google drive containing your model.ckpt and other files

	Step 13b: Set NUM_CLASSES to the number of classes you're predicting on 0

	Step 13c: Set PATH_TO_TEST_IMAGES_DIR equal to the directory of images you want to test on

	Step 13d: Classes list contains the identity of the potential objects in the image

	Step 13e: Scores list contains the confidence score of the objects from the classes list

	Step 13f: For instance, if classes= [[1, 2, 2, 3, 1...]] and scores=[[.9823, .8423, .0523, ...]]. Therefore, the only two objects that the model is confident exists are the objects with an id of 1 and 2.
	
	Step 13g: You can change the confidence score to change which objects are detected on the images










