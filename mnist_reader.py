###########################################
#		Script By Arshi and Rishi		  #
#										  #
###########################################

from mnist import MNIST
import numpy as np
import time
import matplotlib.pyplot as plt
import random

from pandas import DataFrame
import pandas as pd

#Use the following to isntall this MNIST Reading Library
#pip install python-mnist
mndata = MNIST('./Data/MNIST')		   #Specify your path to the ubyte files here
training_data = mndata.load_training() #training_data[0] contains 60K images in 60Kx784 format and 60K Labels in 60K x 1 format
testing_data = mndata.load_testing()   #training_data[0] contains 10K images in 10Kx784 format and 10K Labels in 10K x 1 format

#Number of Images you want to Display
num_images = 10

#Waiting Time in Seconds between each displayed image
wait_time = 0.5

print ("Images Structure: ", np.shape(training_data[0]))
print ("Label Structure: ", np.shape(training_data[1]))


'''
Function to Display Images
'''
def show_images():
	im_count=0
	while im_count<num_images:
		img = np.array(training_data[0][im_count]) 		#img is 1 x 784
		label = np.array(training_data[1][im_count])	#label for img
		np.resize(img,(28,28))				#1 x 784 -> 28 x 28
		img = np.reshape(img, (28, 28))
		plt.imshow(img, cmap='gray', interpolation='nearest')
		plt.show(block=False)				#Show Image
		im_count+=1
		print ("Image Label: ", label)		#Print Image Label
		time.sleep(wait_time)
		plt.close()

num_training_examples = len(training_data[0])
num_testing_examples = len(testing_data[0])
num_input_neurons = len(training_data[0][0])

print ("Size Of Training Data:", num_training_examples)
print ("Size Of Testing Data:", num_testing_examples)
print ("NO. of Input Neurons:", num_input_neurons)

#Function Call to Plot Each Digit Image
show_images()


im_count=0
training_data_by_labels = [[]] * 10 #lists of 10 lists

while im_count<len(training_data[1]):
	label = np.array(training_data[1][im_count])	#extract label for image
	training_data_by_labels[label].append(np.array(training_data[0][im_count])) 
	im_count+=1

'''
Function to pick n random images from each label
'''
def  randomly_choose_n_images(n): # inputs: n (number of images)
	random_training_data_by_labels = [[]] * 10 #lists of 10 lists
	random_values = []
	random_values = range(1, len(training_data_by_labels[label]), n)
	itr = 0
	label_count = 0
	while (label_count < 10):
    		while (itr < len(random_values)):
	    		random_training_data_by_labels[label].append(training_data_by_labels[label][itr])
	    		itr+=1
	    	label_count+=1
	return random_training_data_by_labels
	
random_training_data_by_labels = randomly_choose_n_images(20)
	    
