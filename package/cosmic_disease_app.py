#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pdb

from PyQt4 import QtGui, QtCore
from matplotlib import pyplot as plt
import numpy as np
from cv2 import *

from package.ui import main_window, display_drawing
from package.image_processing.ip_func import *

def run():
	app = QtGui.QApplication(sys.argv)
	screen_resolution = app.desktop().screenGeometry()
	cda = CosmicDiseaseApp(screen_resolution.height(), screen_resolution.width()) 
	cda.show()                         
	app.exec_() 

class DisplayDrawing(QtGui.QDialog, display_drawing.Ui_Dialog):
	def __init__(self, width, height, screen_width, screen_height):
	
		super(DisplayDrawing, self).__init__()
		self.setupUi(self)
		self.drawing = Drawing(height, width)
		
		cd = self.drawing.cosmic_disease
		
		image = QtGui.QImage(cd, cd.shape[1], cd.shape[0], cd.shape[1] * 3,QtGui.QImage.Format_RGB888)
		self.cosmic_disease = QtGui.QPixmap(image)
		
		self.draw_label.setPixmap(self.cosmic_disease.scaled(self.draw_label.size(), QtCore.Qt.KeepAspectRatio))
		self.draw_label.setAlignment(QtCore.Qt.AlignCenter)
		
		p = self.palette()
		p.setColor(self.backgroundRole(), QtCore.Qt.black)
		self.setPalette(p)
		
		self.showMaximized()
		self.regen_button.clicked.connect(lambda: self.regenerate(height, width))
		self.save_button.clicked.connect(self.save_draw)
		
	
	def resizeEvent(self, resizeEvent):
		self.draw_label.setPixmap(self.cosmic_disease.scaled(self.draw_label.size(), QtCore.Qt.KeepAspectRatio))

	def regenerate(self, height, width):
		self.drawing.draw(height, width)
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
		
		self.generate_button.clicked.connect(self.generate)

	def generate(self):
		# be aware that the format 20X30 gives width before height #
		drawing_width, drawing_height = get_size_in_pixel(str(self.size_comboBox.currentText()))
		display_drawing = DisplayDrawing(drawing_width, drawing_height, \
										self.screen_width, self.screen_height)
		display_drawing.exec_()
		
def get_size_in_pixel(string_size):
	size = map(int, string_size.split("X"))
	return cmtopixels(size[0],300), cmtopixels(size[1],300) # Dpi = 300 scanner #
	

