import pdb

from PyQt4.QtCore import pyqtRemoveInputHook
import numpy as np
from cv2 import *
from random import randint


class Drawing(object):
	def __init__(self, height, width):
		self.numxdf = 0
		self.numdfr = 0
		self.numhhh = 10
		
		self.draw(height, width)
		
	def draw(self, height, width):
		cosmic_disease = 255 * np.ones((height,width,3), np.uint8)
		
		path = "database/hhh/"
		
		figname = "hhh"
		for i in xrange(self.numhhh):
			num = randint(3,4)
			disease = imread(path + figname + str(num) + ".jpg")
			
			disease = bgrtorgb(disease)
			disease = self.normalize_disease(disease)
			
			disease_gray = cvtColor(disease, COLOR_BGR2GRAY)
			ret2,th = threshold(disease_gray,0,255,THRESH_BINARY+THRESH_OTSU)
			rows, colums = np.where(th == 255)
			
			disease[rows, colums, :] = (255,255,255)
			
#			pyqtRemoveInputHook()	
#			pdb.set_trace()	
			imshow('disease', disease)
			
			cosmic_disease = self.add_disease(cosmic_disease, disease)
		
		self.cosmic_disease = cosmic_disease
	
	def add_disease(self, cosmic_disease, disease):	
	
		y_max = cosmic_disease.shape[0]
		x_max = cosmic_disease.shape[1]
		
		disease_height = disease.shape[0]
		disease_width = disease.shape[1]
	
		y = randint(0, y_max)
		x = randint(0, x_max)
		
		## Y ##
		y_start = y - disease_height/2
		y1_start = 0
		
		if y_start < 0:
			y1_start = abs(y_start)
			y_start = 0
		
		y_end = y + disease_height/2
		y1_end = disease_height
		
		if y_end > y_max:
			y_end = y_max
			y1_end = disease_height/2 + y_max - y
			
		## X ##
		x_start = x - disease_width/2
		x1_start = 0
	
		if x_start < 0:
			x1_start = abs(x_start)
			x_start = 0
		
		x_end = x + disease_width/2
		x1_end = disease_width
		
		if x_end > x_max:
			x_end = x_max
			x1_end = disease_width/2 + x_max - x
		
#		print("cosmic_disease : x_start = {}, x_end = {}, y_start = {}, y_end = {}".format(x_start, x_end, y_start, y_end))
#		print("disease : x_start = {}, x_end = {}, y_start = {}, y_end = {}".format(x1_start, x1_end, y1_start, y1_end))
#		pyqtRemoveInputHook()	
#		pdb.set_trace()	
			
		cosmic_disease[y_start:y_end+1,x_start:x_end+1,:] = np.where(disease[y1_start:y1_end,x1_start:x1_end,:] != (255,255,255), 
																	disease[y1_start:y1_end,x1_start:x1_end,:],  
																	cosmic_disease[y_start:y_end+1,x_start:x_end+1,:])
		
		return cosmic_disease
		
	def normalize_disease(self, disease):
	
		height = n_height = disease.shape[0]
		width = n_width = disease.shape[1]
		if height % 2 == 0:
			n_height = height + 1
		if width % 2 == 0:
			n_width = width + 1
		
		normalized_disease = 255 * np.ones((n_height,n_width,3), np.uint8)
		
		normalized_disease[:height, :width, :] = disease[:,:,:]
		
		return normalized_disease 
		
	def save_draw(self):
		imwrite('color_img.jpg', rgbtobgr(self.cosmic_disease))
		

def cmtopixels(cm, dpi):
	return int(cm * dpi / 2.54) 
	
def bgrtorgb(image):
	R = image[:,:,0]
	image[:,:,2] = image[:,:,0]
	image[:,:,0] = R
	
	return image

def rgbtobgr(image):
	B = image[:,:,0]
	image[:,:,0] = image[:,:,2]
	image[:,:,2] = B
	
	return image


#		pyqtRemoveInputHook()	
#		pdb.set_trace()		
