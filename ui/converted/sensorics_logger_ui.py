# Form implementation generated from reading ui file 'd:\work\Soft\ADCS_connector\ui\sensorics_logger.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.StartStopBtn = QtWidgets.QPushButton(parent=self.groupBox)
        self.StartStopBtn.setObjectName("StartStopBtn")
        self.gridLayout_3.addWidget(self.StartStopBtn, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(True)
        self.groupBox_2.setChecked(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.R_lbl = QtWidgets.QLabel(parent=self.groupBox_2)
        self.R_lbl.setObjectName("R_lbl")
        self.gridLayout_2.addWidget(self.R_lbl, 0, 0, 1, 3)
        self.R_x = QtWidgets.QDoubleSpinBox(parent=self.groupBox_2)
        self.R_x.setFrame(True)
        self.R_x.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.R_x.setKeyboardTracking(False)
        self.R_x.setMinimum(-99.99)
        self.R_x.setSingleStep(0.01)
        self.R_x.setObjectName("R_x")
        self.gridLayout_2.addWidget(self.R_x, 1, 0, 1, 1)
        self.V_lbl = QtWidgets.QLabel(parent=self.groupBox_2)
        self.V_lbl.setObjectName("V_lbl")
        self.gridLayout_2.addWidget(self.V_lbl, 2, 0, 1, 3)
        self.R_z = QtWidgets.QDoubleSpinBox(parent=self.groupBox_2)
        self.R_z.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.R_z.setKeyboardTracking(False)
        self.R_z.setMinimum(-99.99)
        self.R_z.setSingleStep(0.01)
        self.R_z.setObjectName("R_z")
        self.gridLayout_2.addWidget(self.R_z, 1, 2, 1, 1)
        self.R_y = QtWidgets.QDoubleSpinBox(parent=self.groupBox_2)
        self.R_y.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.R_y.setKeyboardTracking(False)
        self.R_y.setMinimum(-99.99)
        self.R_y.setSingleStep(0.01)
        self.R_y.setObjectName("R_y")
        self.gridLayout_2.addWidget(self.R_y, 1, 1, 1, 1)
        self.V_x = QtWidgets.QDoubleSpinBox(parent=self.groupBox_2)
        self.V_x.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.V_x.setKeyboardTracking(False)
        self.V_x.setMinimum(-99.99)
        self.V_x.setSingleStep(0.01)
        self.V_x.setObjectName("V_x")
        self.gridLayout_2.addWidget(self.V_x, 3, 0, 1, 1)
        self.V_y = QtWidgets.QDoubleSpinBox(parent=self.groupBox_2)
        self.V_y.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.V_y.setKeyboardTracking(False)
        self.V_y.setMinimum(-99.99)
        self.V_y.setSingleStep(0.01)
        self.V_y.setObjectName("V_y")
        self.gridLayout_2.addWidget(self.V_y, 3, 1, 1, 1)
        self.V_z = QtWidgets.QDoubleSpinBox(parent=self.groupBox_2)
        self.V_z.setFrame(True)
        self.V_z.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.V_z.setKeyboardTracking(False)
        self.V_z.setMinimum(-99.99)
        self.V_z.setSingleStep(0.01)
        self.V_z.setObjectName("V_z")
        self.gridLayout_2.addWidget(self.V_z, 3, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.logTE = QtWidgets.QTextBrowser(parent=Form)
        self.logTE.setObjectName("logTE")
        self.gridLayout.addWidget(self.logTE, 0, 1, 3, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.groupBox_2, self.R_x)
        Form.setTabOrder(self.R_x, self.R_y)
        Form.setTabOrder(self.R_y, self.R_z)
        Form.setTabOrder(self.R_z, self.V_x)
        Form.setTabOrder(self.V_x, self.V_y)
        Form.setTabOrder(self.V_y, self.V_z)
        Form.setTabOrder(self.V_z, self.logTE)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Управление"))
        self.StartStopBtn.setText(_translate("Form", "Start"))
        self.groupBox_2.setTitle(_translate("Form", "Nadir"))
        self.R_lbl.setText(_translate("Form", "Вращать вектор"))
        self.V_lbl.setText(_translate("Form", "Вокруг вектора"))
