# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/qos_qos_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_qqos_Dialog(object):
    def setupUi(self, qqos_Dialog):
        qqos_Dialog.setObjectName("qqos_Dialog")
        qqos_Dialog.resize(510, 316)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(qqos_Dialog.sizePolicy().hasHeightForWidth())
        qqos_Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(qqos_Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_dialog_virt_disk_wizard = QtWidgets.QFrame(qqos_Dialog)
        self.frame_dialog_virt_disk_wizard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dialog_virt_disk_wizard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dialog_virt_disk_wizard.setProperty("paintme01", True)
        self.frame_dialog_virt_disk_wizard.setObjectName("frame_dialog_virt_disk_wizard")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_dialog_virt_disk_wizard)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_dialog_qos_qos_maxrate = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_qos_qos_maxrate.setEnabled(False)
        self.lineEdit_dialog_qos_qos_maxrate.setClearButtonEnabled(True)
        self.lineEdit_dialog_qos_qos_maxrate.setObjectName("lineEdit_dialog_qos_qos_maxrate")
        self.gridLayout.addWidget(self.lineEdit_dialog_qos_qos_maxrate, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.lineEdit_dialog_qos_qos_cbs = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_qos_qos_cbs.setEnabled(False)
        self.lineEdit_dialog_qos_qos_cbs.setClearButtonEnabled(True)
        self.lineEdit_dialog_qos_qos_cbs.setObjectName("lineEdit_dialog_qos_qos_cbs")
        self.gridLayout.addWidget(self.lineEdit_dialog_qos_qos_cbs, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.lineEdit_dialog_qos_qos_perturb = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_qos_qos_perturb.setEnabled(False)
        self.lineEdit_dialog_qos_qos_perturb.setClearButtonEnabled(True)
        self.lineEdit_dialog_qos_qos_perturb.setObjectName("lineEdit_dialog_qos_qos_perturb")
        self.gridLayout.addWidget(self.lineEdit_dialog_qos_qos_perturb, 4, 1, 1, 1)
        self.lineEdit_dialog_qos_qos_cir = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_qos_qos_cir.setEnabled(False)
        self.lineEdit_dialog_qos_qos_cir.setClearButtonEnabled(True)
        self.lineEdit_dialog_qos_qos_cir.setObjectName("lineEdit_dialog_qos_qos_cir")
        self.gridLayout.addWidget(self.lineEdit_dialog_qos_qos_cir, 2, 1, 1, 1)
        self.comboBox_dialog_qos_qos_type = QtWidgets.QComboBox(self.frame_dialog_virt_disk_wizard)
        self.comboBox_dialog_qos_qos_type.setObjectName("comboBox_dialog_qos_qos_type")
        self.comboBox_dialog_qos_qos_type.addItem("")
        self.comboBox_dialog_qos_qos_type.setItemText(0, "")
        self.comboBox_dialog_qos_qos_type.addItem("")
        self.comboBox_dialog_qos_qos_type.addItem("")
        self.comboBox_dialog_qos_qos_type.addItem("")
        self.comboBox_dialog_qos_qos_type.addItem("")
        self.comboBox_dialog_qos_qos_type.addItem("")
        self.comboBox_dialog_qos_qos_type.addItem("")
        self.comboBox_dialog_qos_qos_type.addItem("")
        self.gridLayout.addWidget(self.comboBox_dialog_qos_qos_type, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit_dialog_qos_qos_quantum = QtWidgets.QLineEdit(self.frame_dialog_virt_disk_wizard)
        self.lineEdit_dialog_qos_qos_quantum.setEnabled(False)
        self.lineEdit_dialog_qos_qos_quantum.setClearButtonEnabled(True)
        self.lineEdit_dialog_qos_qos_quantum.setObjectName("lineEdit_dialog_qos_qos_quantum")
        self.gridLayout.addWidget(self.lineEdit_dialog_qos_qos_quantum, 5, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_dialog_virt_disk_wizard)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_dialog_virt_disk_wizard)
        self.buttonBox = QtWidgets.QDialogButtonBox(qqos_Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(qqos_Dialog)
        self.buttonBox.accepted.connect(qqos_Dialog.accept)
        self.buttonBox.rejected.connect(qqos_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(qqos_Dialog)

    def retranslateUi(self, qqos_Dialog):
        _translate = QtCore.QCoreApplication.translate
        qqos_Dialog.setWindowTitle(_translate("qqos_Dialog", "New QOS"))
        self.label_7.setText(_translate("qqos_Dialog", "cbs:"))
        self.comboBox_dialog_qos_qos_type.setItemText(1, _translate("qqos_Dialog", "linux-htb"))
        self.comboBox_dialog_qos_qos_type.setItemText(2, _translate("qqos_Dialog", "linux-hfsc"))
        self.comboBox_dialog_qos_qos_type.setItemText(3, _translate("qqos_Dialog", "linux-sfq"))
        self.comboBox_dialog_qos_qos_type.setItemText(4, _translate("qqos_Dialog", "linux-codel"))
        self.comboBox_dialog_qos_qos_type.setItemText(5, _translate("qqos_Dialog", "linux-fq_codel"))
        self.comboBox_dialog_qos_qos_type.setItemText(6, _translate("qqos_Dialog", "linux-noop"))
        self.comboBox_dialog_qos_qos_type.setItemText(7, _translate("qqos_Dialog", "egress-policer"))
        self.label_6.setText(_translate("qqos_Dialog", "cir:"))
        self.label_5.setText(_translate("qqos_Dialog", "max-rate:"))
        self.label_4.setText(_translate("qqos_Dialog", "type:"))
        self.label_8.setText(_translate("qqos_Dialog", "perturb:"))
        self.label_9.setText(_translate("qqos_Dialog", "quantum:"))

