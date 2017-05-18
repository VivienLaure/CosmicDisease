# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/MainWindowQtdesigner.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(344, 191)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 321, 171))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.size_label = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.size_label.setAlignment(QtCore.Qt.AlignCenter)
        self.size_label.setObjectName(_fromUtf8("size_label"))
        self.horizontalLayout.addWidget(self.size_label)
        self.size_comboBox = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.size_comboBox.setObjectName(_fromUtf8("size_comboBox"))
        self.size_comboBox.addItem(_fromUtf8(""))
        self.size_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.size_comboBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.le_nbr_form_1 = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.le_nbr_form_1.setObjectName(_fromUtf8("le_nbr_form_1"))
        self.horizontalLayout_4.addWidget(self.le_nbr_form_1)
        self.label_name_form_1 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_name_form_1.setObjectName(_fromUtf8("label_name_form_1"))
        self.horizontalLayout_4.addWidget(self.label_name_form_1)
        self.button_path_form_1 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.button_path_form_1.setObjectName(_fromUtf8("button_path_form_1"))
        self.horizontalLayout_4.addWidget(self.button_path_form_1)
        self.button_display_form_1 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.button_display_form_1.setObjectName(_fromUtf8("button_display_form_1"))
        self.horizontalLayout_4.addWidget(self.button_display_form_1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.le_nbr_form_2 = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.le_nbr_form_2.setObjectName(_fromUtf8("le_nbr_form_2"))
        self.horizontalLayout_2.addWidget(self.le_nbr_form_2)
        self.label_name_form_2 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_name_form_2.setObjectName(_fromUtf8("label_name_form_2"))
        self.horizontalLayout_2.addWidget(self.label_name_form_2)
        self.button_path_form_2 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.button_path_form_2.setObjectName(_fromUtf8("button_path_form_2"))
        self.horizontalLayout_2.addWidget(self.button_path_form_2)
        self.button_display_form_2 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.button_display_form_2.setObjectName(_fromUtf8("button_display_form_2"))
        self.horizontalLayout_2.addWidget(self.button_display_form_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.le_nbr_form_3 = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.le_nbr_form_3.setObjectName(_fromUtf8("le_nbr_form_3"))
        self.horizontalLayout_3.addWidget(self.le_nbr_form_3)
        self.label_name_form_3 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_name_form_3.setObjectName(_fromUtf8("label_name_form_3"))
        self.horizontalLayout_3.addWidget(self.label_name_form_3)
        self.button_path_form_3 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.button_path_form_3.setObjectName(_fromUtf8("button_path_form_3"))
        self.horizontalLayout_3.addWidget(self.button_path_form_3)
        self.button_display_form_3 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.button_display_form_3.setObjectName(_fromUtf8("button_display_form_3"))
        self.horizontalLayout_3.addWidget(self.button_display_form_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.generate_button = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.generate_button.setObjectName(_fromUtf8("generate_button"))
        self.verticalLayout_5.addWidget(self.generate_button)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.size_label.setText(_translate("MainWindow", "Size", None))
        self.size_comboBox.setItemText(0, _translate("MainWindow", "20X30", None))
        self.size_comboBox.setItemText(1, _translate("MainWindow", "30X30", None))
        self.le_nbr_form_1.setText(_translate("MainWindow", "0", None))
        self.label_name_form_1.setText(_translate("MainWindow", "TextLabel", None))
        self.button_path_form_1.setText(_translate("MainWindow", "Path", None))
        self.button_display_form_1.setText(_translate("MainWindow", "Sample", None))
        self.le_nbr_form_2.setText(_translate("MainWindow", "0", None))
        self.label_name_form_2.setText(_translate("MainWindow", "TextLabel", None))
        self.button_path_form_2.setText(_translate("MainWindow", "Path", None))
        self.button_display_form_2.setText(_translate("MainWindow", "Sample", None))
        self.le_nbr_form_3.setText(_translate("MainWindow", "0", None))
        self.label_name_form_3.setText(_translate("MainWindow", "TextLabel", None))
        self.button_path_form_3.setText(_translate("MainWindow", "Path", None))
        self.button_display_form_3.setText(_translate("MainWindow", "Sample", None))
        self.generate_button.setText(_translate("MainWindow", "Generate", None))

