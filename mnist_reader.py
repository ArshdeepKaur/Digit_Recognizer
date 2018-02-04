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
num_images = 0

#Waiting Time in Seconds between each displayed image
wait_time = 0.5

print("****************************** Data/Image Structure")
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
	
'''
Function to pick n random images from each label
INPUTS: n=number of random images required for each label  
OUTPUTS: NA
RETURN: 
'''
def  randomly_choose_n_images(n): # inputs: n (number of images)
	random_training_data_by_labels = [[]] * 10 #lists of 10 lists
	
	#initialize dynamic lists
	label_count = 0
	while (label_count < 10):
		random_training_data_by_labels[label_count] = list()
		#print ( "Label ID:", label_count, ", List ID:", id(random_training_data_by_labels[label_count]))
		label_count+=1	
	itr = 0
	label_count = 0
	while (label_count < 10):
		random_values = []
		random_values = random.sample(range(1, len(training_data_by_labels[label_count])), n) #This just picks up every nth number from 1:size_of_data_for_a_label	
		#print ("The random values generated are: ", random_values)
		while (itr < len(random_values)):
			random_training_data_by_labels[label].append(training_data_by_labels[label][itr]) #Again this list implementation won't work
			itr+=1
		label_count+=1
	return random_training_data_by_labels

#Function Call to Plot Each Digit Image
show_images()

start_time = time.time()
print ("\n****************************** Method 1: LIST IMPLEMENTATION")
im_count=0
training_data_by_labels = [[]] * 10 #lists of 10 lists

#initialize dynamic lists
label_count = 0
while (label_count < 10):
	training_data_by_labels[label_count] = list()
	#print ( "Label ID:", label_count, ", List ID:", id(training_data_by_labels[label_count]))
	label_count+=1

while im_count<len(training_data[1]):
	label = np.array(training_data[1][im_count])	
	training_data_by_labels[label].append(np.array(training_data[0][im_count])) #split data by labels
	im_count+=1	

list_implementation_time = time.time()
for i in range(10):
	print ("[METHOD 1]: Length of Class: ",i," is: ", len(training_data_by_labels[i]))
	
im_count=0
#Dictionary Implementation
print ("\n****************************** Method 2: DICTIONARY IMPLEMENTATION")
training_data_by_labels_dict = {}
while im_count<len(training_data[1]):
	label = training_data[1][im_count]			#extract label for image
	try:
		curr_list = training_data_by_labels_dict[label] #Get the current list of images for a particular label
		curr_list.append(training_data[0][im_count])	#Append the new image to the bigger list for dictionary
		temp_dict = {label:curr_list}					#Create a temporary small dictionary
		training_data_by_labels_dict.update(temp_dict)	#Update master dictionary
	except:												#If no data found for that label
		curr_list = [training_data[0][im_count]]
		temp_dict = {label:curr_list}
		training_data_by_labels_dict.update(temp_dict)
	
	im_count+=1	
	
dict_implementation_time		= time.time()	

final_dict_len = len(training_data_by_labels_dict)
print ("Length of Dictionary is: ", final_dict_len)
for i in range(final_dict_len):
	print ("[METHOD 2]: Length of Class: ",i," is: ", len(training_data_by_labels_dict[i]))
	
#Or better still Just get the indices and choose from amongst them randomly
print ("\n****************************** Method 3: Cherry Picking")
labels = np.array(training_data[1])
for i in range(10):
	label_index = np.where(labels==i)
	print ("[Method 3]: Length of Class: ",i," is: ", len(label_index[0]))
func_time_begin 				= time.time()
random_training_data_by_labels 	= randomly_choose_n_images(5)
func_time 						= time.time()
list_elapsed 					= list_implementation_time - start_time
dict_elapsed 					= dict_implementation_time - list_implementation_time
func_elapsed					= func_time - func_time_begin

print ("\n\nTime Elapsed in list implementation: ", time.strftime("%H:%M:%S", time.gmtime(list_elapsed)))
print ("Time Elapsed in dict implementation: ", time.strftime("%H:%M:%S", time.gmtime(dict_elapsed)))
print ("Time Elapsed in function: ", time.strftime("%H:%M:%S", time.gmtime(func_elapsed)))
