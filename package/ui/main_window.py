# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowQtdesigner.ui'
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
        MainWindow.resize(308, 278)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.generate_button = QtGui.QPushButton(self.centralwidget)
        self.generate_button.setGeometry(QtCore.QRect(210, 240, 91, 31))
        self.generate_button.setObjectName(_fromUtf8("generate_button"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 131, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.size_label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.size_label.setAlignment(QtCore.Qt.AlignCenter)
        self.size_label.setObjectName(_fromUtf8("size_label"))
        self.horizontalLayout.addWidget(self.size_label)
        self.size_comboBox = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.size_comboBox.setObjectName(_fromUtf8("size_comboBox"))
        self.size_comboBox.addItem(_fromUtf8(""))
        self.size_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.size_comboBox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.generate_button.setText(_translate("MainWindow", "Generate", None))
        self.size_label.setText(_translate("MainWindow", "Size", None))
        self.size_comboBox.setItemText(0, _translate("MainWindow", "20X30", None))
        self.size_comboBox.setItemText(1, _translate("MainWindow", "30X30", None))

