#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import pdb

#Resolve cast problem beween Qstring and python str
import sip
sip.setapi('QString', 2)

from PyQt4 import QtGui, QtCore
from matplotlib import pyplot as plt
import numpy as np
from cv2 import *
#to display a random sample :
import random

from package.ui import main_window, display_drawing
from package.image_processing.ip_func import *

def run():
	app = QtGui.QApplication(sys.argv)
	screen_resolution = app.desktop().screenGeometry()
	cda = CosmicDiseaseApp(screen_resolution.height(), screen_resolution.width()) 
	cda.show()                         
	app.exec_() 

class DisplayDrawing(QtGui.QDialog, display_drawing.Ui_Dialog):
	def __init__(self, width, height, screen_width, screen_height, forms):
	
		super(DisplayDrawing, self).__init__()
		self.setupUi(self)
		self.drawing = Drawing(height, width, forms)
		
		cd = self.drawing.cosmic_disease
		
		image = QtGui.QImage(cd, cd.shape[1], cd.shape[0], cd.shape[1] * 3,QtGui.QImage.Format_RGB888)
		self.cosmic_disease = QtGui.QPixmap(image)
		
		self.draw_label.setPixmap(self.cosmic_disease.scaled(self.draw_label.size(), QtCore.Qt.KeepAspectRatio))
		self.draw_label.setAlignment(QtCore.Qt.AlignCenter)
		
		p = self.palette()
		p.setColor(self.backgroundRole(), QtCore.Qt.black)
		self.setPalette(p)
		
		self.showMaximized()
		self.regen_button.clicked.connect(lambda: self.regenerate(height, width, forms))
		self.save_button.clicked.connect(self.save_draw)
		
	
	def resizeEvent(self, resizeEvent):
		self.draw_label.setPixmap(self.cosmic_disease.scaled(self.draw_label.size(), QtCore.Qt.KeepAspectRatio))

	def regenerate(self, height, width, forms):
		self.drawing.draw(height, width, forms)
		cd = self.drawing.cosmic_disease
		
		image = QtGui.QImage(cd, cd.shape[1], cd.shape[0], cd.shape[1] * 3,QtGui.QImage.Format_RGB888)
		pix = QtGui.QPixmap(image)
		
		self.draw_label.setPixmap(pix.scaled(self.draw_label.size(), QtCore.Qt.KeepAspectRatio))
		
	def save_draw(self):
		self.drawing.save_draw()
		

class CosmicDiseaseApp(QtGui.QMainWindow, main_window.Ui_MainWindow):
	def __init__(self, screen_height, screen_width, parent = None):
	
		super(CosmicDiseaseApp, self).__init__(parent)
		self.setupUi(self)
		
		self.screen_height = screen_height
		self.screen_width = screen_width
		self.forms = [form("database/FormA", "FormA", 1), form("database/FormB", "FormB", 2), \
					  form("database/FormC", "FormC", 3)]
		
		self.label_name_form_1.setText(os.path.basename(self.forms[0].path))
		self.label_name_form_2.setText(os.path.basename(self.forms[1].path))
		self.label_name_form_3.setText(os.path.basename(self.forms[2].path))
		
#		limit the number of forms the user can display actualy 10 (should depend on the number of form available)
		self.le_nbr_form_1.setValidator(QtGui.QIntValidator(0, 10))
		self.le_nbr_form_2.setValidator(QtGui.QIntValidator(0, 10))
		self.le_nbr_form_3.setValidator(QtGui.QIntValidator(0, 10))
		
		self.generate_button.clicked.connect(self.generate)
		self.button_path_form_1.clicked.connect(lambda: self.update_path(1))
		self.button_path_form_2.clicked.connect(lambda: self.update_path(2))
		self.button_path_form_3.clicked.connect(lambda: self.update_path(3))
		
		self.button_display_form_1.clicked.connect(self.forms[0].display_rand_sample)
		self.button_display_form_2.clicked.connect(self.forms[1].display_rand_sample)
		self.button_display_form_3.clicked.connect(self.forms[2].display_rand_sample)
		
		self.le_nbr_form_1.textChanged.connect(lambda: self.update_nbr(1))
		self.le_nbr_form_2.textChanged.connect(lambda: self.update_nbr(2))
		self.le_nbr_form_3.textChanged.connect(lambda: self.update_nbr(3))

	def generate(self):
		# be aware that the format 20X30 gives width before height #
		drawing_width, drawing_height = get_size_in_pixel(str(self.size_comboBox.currentText()))
		display_drawing = DisplayDrawing(drawing_width, drawing_height, \
										self.screen_width, self.screen_height, \
										self.forms)
		display_drawing.exec_()
	
	def update_path(self, num_):
		w = QtGui.QWidget()
#		Set window size. 
		w.resize(320, 240) 
#		Set window title 
		w.setWindowTitle("Path to form :" + str(num_))
		path_ = QtGui.QFileDialog.getExistingDirectory(w, 'Open File', '/')
		name_ = os.path.basename(path_)
		
		if(num_ == 1):
			self.label_name_form_1.setText(name_)
			self.forms[0].path = path_
			self.forms[0].name = name_
		elif(num_ == 2):
			self.label_name_form_2.setText(name_)
			self.forms[1].path = path_
			self.forms[1].name = name_
		elif(num_ == 3):
			self.label_name_form_3.setText(name_)
			self.forms[2].path = path_
			self.forms[2].name = name_
	
	def update_nbr(self, num_):
		
		if(num_ == 1):
			text_ = self.le_nbr_form_1.text()
			if text_:  
				self.forms[0].nbr = int(text_)
#				self.forms[0].print_form()
		elif(num_ == 2):
			text_ = self.le_nbr_form_2.text()
			if text_:  
				self.forms[1].nbr = int(text_)
#				self.forms[1].print_form()
		elif(num_ == 3):
			text_ = self.le_nbr_form_3.text()
			if text_:  
				self.forms[2].nbr = int(text_)
#				self.forms[2].print_form()
									
		
def get_size_in_pixel(string_size):
	size = map(int, string_size.split("X"))
	return cmtopixels(size[0],300), cmtopixels(size[1],300) # scanner Dpi = 300  #

class form:
	def __init__(self, path_, name_, num_, nbr_ = 0):
		self.path = path_
		self.name = name_
		self.num = num_
		self.nbr = nbr_
	
	def display_rand_sample(self):
	 	random_filename = random.choice([ x for x in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, x))])
		sample = imread(self.path + "/" + random_filename)
		imshow(random_filename, sample)		
		
	def print_form(self):
		print("Form {} : {} {}'".format(self.num, self.nbr, self.name))
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

