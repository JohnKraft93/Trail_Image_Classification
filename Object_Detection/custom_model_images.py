import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import zipfile
import pandas as pd

from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
import PIL.ImageFont as ImageFont


from object_detection.utils import label_map_util

from object_detection.utils import visualization_utils as vis_util

# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")


# script repurposed from sentdex's edits and TensorFlow's example script. Pretty messy as not all unnecessary
# parts of the original have been removed




# # Model preparation

# ## Variables
#
# Any model exported using the `export_inference_graph.py` tool can be loaded here simply by changing `PATH_TO_CKPT` to point to a new .pb file.
#
# By default we use an "SSD with Mobilenet" model here. See the [detection model zoo](https://github.com/tensorflow/models/blob/master/object_detection/g3doc/detection_model_zoo.md) for a list of other models that can be run out-of-the-box with varying speeds and accuracies.



# What model to download.
MODEL_NAME = 'new_graph'  # change to whatever folder has the new graph
# MODEL_FILE = MODEL_NAME + '.tar.gz'   # these lines not needed as we are using our own model
# DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'

# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join('training', 'object-detection.pbtxt')  # our labels are in training/object-detection.pbkt

NUM_CLASSES = 4  # we only are using one class at the moment (mask at the time of edit)


# ## Download Model


# opener = urllib.request.URLopener()   # we don't need to download model since we have our own
# opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)
# tar_file = tarfile.open(MODEL_FILE)
# for file in tar_file.getmembers():
#     file_name = os.path.basename(file.name)
#     if 'frozen_inference_graph.pb' in file_name:
#         tar_file.extract(file, os.getcwd())


# ## Load a (frozen) Tensorflow model into memory.


detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')


# ## Loading label map
# Label maps map indices to category names, so that when our convolution network predicts `5`, we know that this corresponds to `airplane`.  Here we use internal utility functions, but anything that returns a dictionary mapping integers to appropriate string labels would be fine

# In[7]:

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)





def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, 3)).astype(np.uint8)




# For the sake of simplicity we will use only 2 images:
# image1.jpg
# image2.jpg
# If you want to test the code with your images, just add path to the images to the TEST_IMAGE_PATHS.
PATH_TO_TEST_IMAGES_DIR = 'imgs'

TEST_IMAGE_PATHS = [os.path.join(PATH_TO_TEST_IMAGES_DIR, f) for f in os.listdir(PATH_TO_TEST_IMAGES_DIR)]
#TEST_IMAGE_PATHS = [os.path.join(PATH_TO_TEST_IMAGES_DIR, 'image{}.jpg'.format(i)) for i in range(1, 8)]  # adjust range for # of images in folder

# Size, in inches, of the output images.
IMAGE_SIZE = (12, 8)

#For DataFrame 1
image_name = []
personCount = []
dogCount = []
snowmobileCount = []
groomerCount = []

# For DataFrame 2
image_name2 = []
objectType = []
confScore = []

confidence_score = 0.5

with detection_graph.as_default():
    with tf.Session(graph=detection_graph) as sess:
        i = 0
        for image_path in TEST_IMAGE_PATHS:
            print(image_path)
            image = Image.open(image_path)
            # the array based representation of the image will be used later in order to prepare the
            # result image with boxes and labels on it.
            image_np = load_image_into_numpy_array(image)
            # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
            image_np_expanded = np.expand_dims(image_np, axis=0)
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            # Each box represents a part of the image where a particular object was detected.
            boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            # Each score represent how level of confidence for each of the objects.
            # Score is shown on the result image, together with the class label.
            scores = detection_graph.get_tensor_by_name('detection_scores:0')
            classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')
            # Actual detection.
            (boxes, scores, classes, num_detections) = sess.run(
                [boxes, scores, classes, num_detections],
                feed_dict={image_tensor: image_np_expanded})
            
            # Visualization of the results of a detection.
            vis_util.visualize_boxes_and_labels_on_image_array(
                image_np,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=10,
                min_score_thresh=confidence_score)
            
            print(scores)
            print(classes)
            image_name.append(image_path[5:])
            
            dogCount.append(0)
            personCount.append(0)
            snowmobileCount.append(0)
            groomerCount.append(0)
            
            for j in range(len(scores[0])):
                if(scores[0][j] > confidence_score):
                    if(int(classes[0][j]) == 1):
                        personCount[i] += 1
                    elif(int(classes[0][j]) == 2):
                        dogCount[i] += 1
                    elif(int(classes[0][j]) == 3):
                        snowmobileCount[i] += 1
                    elif(int(classes[0][j]) == 4):
                        groomerCount[i] += 1
                    image_name2.append(image_path[5:])
                    objectType.append(classes[0][j])
                    confScore.append(scores[0][j])
                    
                    
            
            fig = plt.figure(figsize=IMAGE_SIZE)
            plt.imshow(image_np)    # matplotlib is configured for command line only so we save the outputs instead
            plt.savefig("outputs2/-" + str(TEST_IMAGE_PATHS[i][5:]) + "{}.png".format(i))  # create an outputs folder for the images to be saved
            plt.close(fig)
            i = i+1  # this was a quick fix for iteration, create a pull request if you'd like
            
            if(i ==1):
                break

            
d = {'filename': image_name, 'personCount': personCount,'dogCount': dogCount, 'snowmobileCount': snowmobileCount, 'groomerCount': groomerCount}
d2 = {'filename': image_name2, 'objectType' : objectType, 'confidenceScore': confScore}
df = pd.DataFrame(data=d)
df2 = pd.DataFrame(data=d2)


df.to_csv("dataframe1.csv")
df2.to_csv("dataframe2.csv")




'''
#For DataFrame 1
image_name = []
motorizedCount = []
nonMotorizedCount = []
mechanicalCount = []
hybridCount = []
vehicaleCount = []
dogCount = []

# For DataFrame 2
image_name2 = []
objectType = []
confScore = []

confidence_score = 0.5

with detection_graph.as_default():
    with tf.Session(graph=detection_graph) as sess:
        i = 0
        for image_path in TEST_IMAGE_PATHS:
            print(image_path)
            image = Image.open(image_path)
            # the array based representation of the image will be used later in order to prepare the
            # result image with boxes and labels on it.
            image_np = load_image_into_numpy_array(image)
            # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
            image_np_expanded = np.expand_dims(image_np, axis=0)
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            # Each box represents a part of the image where a particular object was detected.
            boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            # Each score represent how level of confidence for each of the objects.
            # Score is shown on the result image, together with the class label.
            scores = detection_graph.get_tensor_by_name('detection_scores:0')
            classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')
            # Actual detection.
            (boxes, scores, classes, num_detections) = sess.run(
                [boxes, scores, classes, num_detections],
                feed_dict={image_tensor: image_np_expanded})
            
            # Visualization of the results of a detection.
            vis_util.visualize_boxes_and_labels_on_image_array(
                image_np,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=10,
                min_score_thresh=confidence_score)
            
            print(scores)
            print(classes)
            image_name.append(image_path[5:])
                
            image_name.append(0)
            motorizedCount.append(0)
            nonMotorizedCount.append(0)
            mechanicalCount.append(0)
            hybridCount.append(0)
            vehicaleCount.append(0)
            dogCount.append(0)
            
            
            for j in range(len(scores[0])):
                if(scores[0][j] > confidence_score):
                    if(int(classes[0][j]) == 1):
                        personCount[i] += 1
                    elif(int(classes[0][j]) == 2):
                        dogCount[i] += 1
                    elif(int(classes[0][j]) == 3):
                        snowmobileCount[i] += 1
                    elif(int(classes[0][j]) == 4):
                        groomerCount[i] += 1
                    image_name2.append(image_path[5:])
                    objectType.append(classes[0][j])
                    confScore.append(scores[0][j])
                    
                    
            
            fig = plt.figure(figsize=IMAGE_SIZE)
            plt.imshow(image_np)    # matplotlib is configured for command line only so we save the outputs instead
            plt.savefig("outputs2/-" + str(TEST_IMAGE_PATHS[i][5:]) + "{}.png".format(i))  # create an outputs folder for the images to be saved
            plt.close(fig)
            i = i+1
            if(i ==1):
                break

            
d = {'filename': image_name, 'motorizedCount': motorizedCount,'nonMotorizedCount': nonMotorizedCount, 'mechanicalCount': mechanicalCount,
     'hybridCount': hybridCount, 'vehicleCount': vehicaleCount, 'dogCount': dogCount}
d2 = {'filename': image_name, 'objectType' : objectType, 'confidenceScore': confScore}
df = pd.DataFrame(data=d)
df2 = pd.DataFrame(data=d2)


df.to_csv("dataframe1.csv")
df2.to_csv("dataframe2.csv")

'''













