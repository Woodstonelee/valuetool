from builtins import object
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_valuewidgetbase.ui'
#
# Created: Sat May 24 12:46:42 2014
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from qgis.PyQt import QtCore, QtGui
from qgis.PyQt.QtCore import QTranslator, QCoreApplication

from qgis.PyQt.QtWidgets import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QCoreApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QCoreApplication.translate(context, text, disambig)

class Ui_ValueWidgetBase(object):
    def setupUi(self, ValueWidgetBase):
        ValueWidgetBase.setObjectName(_fromUtf8("ValueWidgetBase"))
        ValueWidgetBase.resize(343, 335)
        self.verticalLayout = QVBoxLayout(ValueWidgetBase)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cbxEnable = QCheckBox(ValueWidgetBase)
        self.cbxEnable.setObjectName(_fromUtf8("cbxEnable"))
        self.verticalLayout.addWidget(self.cbxEnable)
        self.tabWidget = QTabWidget(ValueWidgetBase)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(_fromUtf8("tabWidgetPage1"))
        self.verticalLayout_2 = QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.widget = QWidget(self.tabWidgetPage1)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.cbxDigits = QCheckBox(self.widget)
        self.cbxDigits.setObjectName(_fromUtf8("cbxDigits"))
        self.horizontalLayout_3.addWidget(self.cbxDigits)
        self.spinDigits = QSpinBox(self.widget)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinDigits.sizePolicy().hasHeightForWidth())
        self.spinDigits.setSizePolicy(sizePolicy)
        self.spinDigits.setMaximum(99)
        self.spinDigits.setProperty("value", 2)
        self.spinDigits.setObjectName(_fromUtf8("spinDigits"))
        self.horizontalLayout_3.addWidget(self.spinDigits)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.widget)
        self.tableWidget = QTableWidget(self.tabWidgetPage1)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.tabWidgetPage1, _fromUtf8(""))
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(_fromUtf8("tabWidgetPage2"))
        self.verticalLayout_3 = QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.graphControls = QWidget(self.tabWidgetPage2)
        self.graphControls.setObjectName(_fromUtf8("graphControls"))
        self.horizontalLayout_2 = QHBoxLayout(self.graphControls)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cbxStats = QCheckBox(self.graphControls)
        self.cbxStats.setObjectName(_fromUtf8("cbxStats"))
        self.horizontalLayout_2.addWidget(self.cbxStats)
        self.label = QLabel(self.graphControls)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.leYMin = QLineEdit(self.graphControls)
        self.leYMin.setObjectName(_fromUtf8("leYMin"))
        self.horizontalLayout_2.addWidget(self.leYMin)
        self.label_2 = QLabel(self.graphControls)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.leYMax = QLineEdit(self.graphControls)
        self.leYMax.setObjectName(_fromUtf8("leYMax"))
        self.horizontalLayout_2.addWidget(self.leYMax)
        self.plotSelector = QComboBox(self.graphControls)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotSelector.sizePolicy().hasHeightForWidth())
        self.plotSelector.setSizePolicy(sizePolicy)
        self.plotSelector.setObjectName(_fromUtf8("plotSelector"))
        self.horizontalLayout_2.addWidget(self.plotSelector)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.graphControls)
        self.stackedWidget = QStackedWidget(self.tabWidgetPage2)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.tabWidget.addTab(self.tabWidgetPage2, _fromUtf8(""))
        self.tabWidgetPage3 = QWidget()
        self.tabWidgetPage3.setObjectName(_fromUtf8("tabWidgetPage3"))
        self.verticalLayout_4 = QVBoxLayout(self.tabWidgetPage3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.cbxClick = QCheckBox(self.tabWidgetPage3)
        self.cbxClick.setObjectName(_fromUtf8("cbxClick"))
        self.verticalLayout_4.addWidget(self.cbxClick)
        self.line_2 = QFrame(self.tabWidgetPage3)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_4.addWidget(self.line_2)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QLabel(self.tabWidgetPage3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 1)
        self.label_3 = QLabel(self.tabWidgetPage3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.cbxLayers = QComboBox(self.tabWidgetPage3)
        self.cbxLayers.setObjectName(_fromUtf8("cbxLayers"))
        self.cbxLayers.addItem(_fromUtf8(""))
        self.cbxLayers.addItem(_fromUtf8(""))
        self.cbxLayers.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.cbxLayers, 1, 1, 1, 1)
        self.cbxBands = QComboBox(self.tabWidgetPage3)
        self.cbxBands.setObjectName(_fromUtf8("cbxBands"))
        self.cbxBands.addItem(_fromUtf8(""))
        self.cbxBands.addItem(_fromUtf8(""))
        self.cbxBands.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.cbxBands, 2, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.line = QFrame(self.tabWidgetPage3)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_4.addWidget(self.line)
        self.label_5 = QLabel(self.tabWidgetPage3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_4.addWidget(self.label_5)
        self.tableWidget2 = QTableWidget(self.tabWidgetPage3)
        self.tableWidget2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget2.setObjectName(_fromUtf8("tableWidget2"))
        self.tableWidget2.setColumnCount(4)
        self.tableWidget2.setRowCount(0)
        item = QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableWidget2.setHorizontalHeaderItem(3, item)
        self.verticalLayout_4.addWidget(self.tableWidget2)
        spacerItem3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.tabWidget.addTab(self.tabWidgetPage3, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.labelStatus = QLabel(ValueWidgetBase)
        self.labelStatus.setText(_fromUtf8(""))
        self.labelStatus.setObjectName(_fromUtf8("labelStatus"))
        self.verticalLayout.addWidget(self.labelStatus)

        self.retranslateUi(ValueWidgetBase)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(ValueWidgetBase)

    def retranslateUi(self, ValueWidgetBase):
        ValueWidgetBase.setWindowTitle(_translate("ValueWidgetBase", "Form", None))
        self.cbxEnable.setToolTip(_translate("ValueWidgetBase", "Can also be enabled using the \"Value Tool\" toolbar icon", None))
        self.cbxEnable.setText(_translate("ValueWidgetBase", "Enable", None))
        self.cbxDigits.setToolTip(_translate("ValueWidgetBase", "Specify how many digits to show in table", None))
        self.cbxDigits.setText(_translate("ValueWidgetBase", "Decimals", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ValueWidgetBase", "Layer", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ValueWidgetBase", "Value", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ValueWidgetBase", "Sample", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ValueWidgetBase", "Line", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("ValueWidgetBase", "Table", None))
        self.cbxStats.setToolTip(_translate("ValueWidgetBase", "Compute min/max when layers are loaded", None))
        self.cbxStats.setText(_translate("ValueWidgetBase", "Stats", None))
        self.label.setText(_translate("ValueWidgetBase", "Y min", None))
        self.label_2.setText(_translate("ValueWidgetBase", "Y max", None))
        self.plotSelector.setToolTip(_translate("ValueWidgetBase", "Select plotting toolkit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), _translate("ValueWidgetBase", "Graph", None))
        self.cbxClick.setToolTip(_translate("ValueWidgetBase", "Replaces active map tool. Use this to select a particular point or if plotting is slow (e.g. when using mpl Graph).", None))
        self.cbxClick.setText(_translate("ValueWidgetBase", "Plot values only when mouse is clicked", None))
        self.label_4.setText(_translate("ValueWidgetBase", "Show bands:", None))
        self.label_3.setText(_translate("ValueWidgetBase", "Show layers:", None))
        self.cbxLayers.setItemText(0, _translate("ValueWidgetBase", "Visible layers", None))
        self.cbxLayers.setItemText(1, _translate("ValueWidgetBase", "All layers", None))
        self.cbxLayers.setItemText(2, _translate("ValueWidgetBase", "Selected layers", None))
        self.cbxBands.setItemText(0, _translate("ValueWidgetBase", "All bands", None))
        self.cbxBands.setItemText(1, _translate("ValueWidgetBase", "Active bands", None))
        self.cbxBands.setItemText(2, _translate("ValueWidgetBase", "Selected bands", None))
        self.label_5.setText(_translate("ValueWidgetBase", "Select active layers and display options:", None))
        item = self.tableWidget2.horizontalHeaderItem(0)
        item.setToolTip(_translate("ValueWidgetBase", "Select layers", None))
        item = self.tableWidget2.horizontalHeaderItem(1)
        item.setText(_translate("ValueWidgetBase", "Layer", None))
        item = self.tableWidget2.horizontalHeaderItem(2)
        item.setText(_translate("ValueWidgetBase", "#", None))
        item.setToolTip(_translate("ValueWidgetBase", "Select bands", None))
        item = self.tableWidget2.horizontalHeaderItem(3)
        item.setText(_translate("ValueWidgetBase", "Bands", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), _translate("ValueWidgetBase", "Options", None))

