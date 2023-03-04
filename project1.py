# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import searchMatch
import time
import json


class Ui_MainWindow(object):
    # main window setup
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1265, 847)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_2.setStyleSheet("#frame_2{\n"
                                   "    \n"
                                   "    background-color: rgb(170, 255, 255);\n"
                                   "    \n"
                                   "    border-bottom: 3px solid rgb(0, 170, 255);\n"
                                   "}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_6.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_6)
        self.pushButton.setStyleSheet("#pushButton{\n"
                                      "    border:none;\n"
                                      "    \n"
                                      "    \n"
                                      "}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("picture/24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(70, 70))
        self.pushButton.setObjectName("pushButton")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.horizontalLayout.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_7)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
                                        "    color : rgb(255, 255, 255);\n"
                                        "    \n"
                                        "    background-color: rgb(170, 255, 255);\n"
                                        "    border : none;\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.horizontalLayout.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_8.setStyleSheet("#frame_8{\n"
                                   "    border:none;\n"
                                   "}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.formLayout = QtWidgets.QFormLayout(self.frame_8)
        self.formLayout.setObjectName("formLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_3.setStyleSheet("#pushButton_3{\n"
                                        "    border:none;\n"
                                        "    \n"
                                        "    \n"
                                        "}")
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("picture/23.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pushButton_3)
        self.horizontalLayout.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_9.setStyleSheet("QPushButton:pressed{\n"
                                   "    padding-top:5px;\n"
                                   "    padding-left:5px;\n"
                                   "}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_6.setStyleSheet("#pushButton_6{\n"
                                        "    border:none;\n"
                                        "    \n"
                                        "    \n"
                                        "}")
        self.pushButton_6.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("picture/27.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_5.setStyleSheet("#pushButton_5{\n"
                                        "    border:none;\n"
                                        "    \n"
                                        "    \n"
                                        "}")
        self.pushButton_5.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("picture/26.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_4.setStyleSheet("#pushButton_4{\n"
                                        "    border:none;\n"
                                        "    \n"
                                        "    \n"
                                        "}")
        self.pushButton_4.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("picture/25.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.horizontalLayout.addWidget(self.frame_9)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_13 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setStyleSheet("#frame_13{\n"
                                    "    background-color:rgb(170, 255, 255);\n"
                                    "    border-right: 3px solid rgb(0, 170, 255);\n"
                                    "}")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_15 = QtWidgets.QFrame(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setStyleSheet("QPushButton:pressed{\n"
                                    "    padding-top:5px;\n"
                                    "    padding-left:5px;\n"
                                    "}")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_15)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("#pushButton_9{\n"
                                        "    color:rgb(255, 255, 255);\n"
                                        "    border:none;\n"
                                        "    background-color: rgb(170, 255, 255);\n"
                                        "\n"
                                        "\n"
                                        "}    \n"
                                        "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("picture/29.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon5)
        self.pushButton_9.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_5.addWidget(self.pushButton_9)
        self.verticalLayout_3.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setStyleSheet("QPushButton:pressed{\n"
                                    "    padding-top:5px;\n"
                                    "    padding-left:5px;\n"
                                    "}")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_16)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("#pushButton_10{\n"
                                         "    color:rgb(255, 255, 255);\n"
                                         "    border:none;\n"
                                         "    background-color: rgb(170, 255, 255);\n"
                                         "\n"
                                         "}\n"
                                         "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("picture/30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon6)
        self.pushButton_10.setIconSize(QtCore.QSize(55, 55))
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_6.addWidget(self.pushButton_10)
        self.verticalLayout_3.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_3.addWidget(self.frame_17)
        self.frame_18 = QtWidgets.QFrame(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_3.addWidget(self.frame_18)
        self.horizontalLayout_4.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setStyleSheet("#frame_14{\n"
                                    "    \n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "}")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_14)
        self.stackedWidget.setStyleSheet("#page{\n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "}\n"
                                         "\n"
                                         "#page_2{\n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "}\n"
                                         "\n"
                                         "#page_3{\n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "}\n"
                                         "\n"
                                         "#page_4{\n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton_11 = QtWidgets.QPushButton(self.page)
        self.pushButton_11.setGeometry(QtCore.QRect(30, 100, 281, 261))
        self.pushButton_11.setStyleSheet("\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "border:none")
        self.pushButton_11.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("picture/yasuo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon7)
        self.pushButton_11.setIconSize(QtCore.QSize(300, 300))
        self.pushButton_11.setObjectName("pushButton_11")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setGeometry(QtCore.QRect(530, 210, 371, 71))
        self.lineEdit.setStyleSheet("\n"
                                    "    border : 3px solid rgb(211, 217, 255);\n"
                                    "")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_12 = QtWidgets.QPushButton(self.page)
        self.pushButton_12.setGeometry(QtCore.QRect(350, 0, 461, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_12.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("#pushButton_12{\n"
                                         "    color : rgb(0, 0, 0);\n"
                                         "    \n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "    border : none;\n"
                                         "}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.comboBox_3 = QtWidgets.QComboBox(self.page)
        self.comboBox_3.setGeometry(QtCore.QRect(390, 210, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("    background-color: rgb(255, 255, 255);\n"
                                      "    border : 3px solid rgb(211, 217, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton_15 = QtWidgets.QPushButton(self.page)
        self.pushButton_15.setGeometry(QtCore.QRect(540, 340, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("    border : 3px solid rgb(211, 217, 255);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(550, 220, 371, 71))
        self.lineEdit_2.setStyleSheet("\n"
                                      "    border : 3px solid rgb(211, 217, 255);\n"
                                      "")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.page_2)
        self.comboBox_2.setGeometry(QtCore.QRect(410, 220, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("    background-color: rgb(255, 255, 255);\n"
                                      "    border : 3px solid rgb(211, 217, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_13 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_13.setGeometry(QtCore.QRect(440, 40, 461, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_13.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("#pushButton_13{\n"
                                         "    color : rgb(0, 0, 0);\n"
                                         "    \n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "    border : none;\n"
                                         "}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_14.setGeometry(QtCore.QRect(30, 100, 261, 251))
        self.pushButton_14.setStyleSheet("\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "border:none")
        self.pushButton_14.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("picture/TFT.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon8)
        self.pushButton_14.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_16 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_16.setGeometry(QtCore.QRect(600, 330, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("    border : 3px solid rgb(211, 217, 255);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 995, 568))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setGeometry(QtCore.QRect(10, 210, 941, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(941, 0))
        self.groupBox.setStyleSheet("background-color: rgb(137, 194, 255);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.frame_23 = QtWidgets.QFrame(self.groupBox)
        self.frame_23.setGeometry(QtCore.QRect(649, 20, 281, 161))
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_24 = QtWidgets.QFrame(self.frame_23)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.pushButton_30 = QtWidgets.QPushButton(self.frame_24)
        self.pushButton_30.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.pushButton_30.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("champion-icon/26.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_30.setIcon(icon9)
        self.pushButton_30.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.frame_24)
        self.pushButton_31.setGeometry(QtCore.QRect(0, 30, 31, 31))
        self.pushButton_31.setText("")
        self.pushButton_31.setIcon(icon9)
        self.pushButton_31.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.frame_24)
        self.pushButton_32.setGeometry(QtCore.QRect(0, 60, 31, 31))
        self.pushButton_32.setText("")
        self.pushButton_32.setIcon(icon9)
        self.pushButton_32.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(self.frame_24)
        self.pushButton_33.setGeometry(QtCore.QRect(0, 90, 31, 31))
        self.pushButton_33.setText("")
        self.pushButton_33.setIcon(icon9)
        self.pushButton_33.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.frame_24)
        self.pushButton_34.setGeometry(QtCore.QRect(0, 120, 31, 31))
        self.pushButton_34.setText("")
        self.pushButton_34.setIcon(icon9)
        self.pushButton_34.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_34.setObjectName("pushButton_34")
        self.label_8 = QtWidgets.QLabel(self.frame_24)
        self.label_8.setGeometry(QtCore.QRect(40, 10, 90, 18))
        self.label_8.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_24)
        self.label_9.setGeometry(QtCore.QRect(40, 40, 90, 18))
        self.label_9.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_24)
        self.label_10.setGeometry(QtCore.QRect(40, 70, 90, 18))
        self.label_10.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_24)
        self.label_11.setGeometry(QtCore.QRect(40, 100, 90, 18))
        self.label_11.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_24)
        self.label_12.setGeometry(QtCore.QRect(40, 130, 90, 18))
        self.label_12.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.frame_24)
        self.frame_25 = QtWidgets.QFrame(self.frame_23)
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.pushButton_35 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_35.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.pushButton_35.setText("")
        self.pushButton_35.setIcon(icon9)
        self.pushButton_35.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_36 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_36.setGeometry(QtCore.QRect(0, 30, 31, 31))
        self.pushButton_36.setText("")
        self.pushButton_36.setIcon(icon9)
        self.pushButton_36.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_37 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_37.setGeometry(QtCore.QRect(0, 60, 31, 31))
        self.pushButton_37.setText("")
        self.pushButton_37.setIcon(icon9)
        self.pushButton_37.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_38 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_38.setGeometry(QtCore.QRect(0, 90, 31, 31))
        self.pushButton_38.setText("")
        self.pushButton_38.setIcon(icon9)
        self.pushButton_38.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_39.setGeometry(QtCore.QRect(0, 120, 31, 31))
        self.pushButton_39.setText("")
        self.pushButton_39.setIcon(icon9)
        self.pushButton_39.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_39.setObjectName("pushButton_39")
        self.label_13 = QtWidgets.QLabel(self.frame_25)
        self.label_13.setGeometry(QtCore.QRect(40, 10, 90, 18))
        self.label_13.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_25)
        self.label_14.setGeometry(QtCore.QRect(40, 40, 90, 18))
        self.label_14.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_25)
        self.label_15.setGeometry(QtCore.QRect(40, 70, 90, 18))
        self.label_15.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_25)
        self.label_16.setGeometry(QtCore.QRect(40, 100, 90, 18))
        self.label_16.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_25)
        self.label_17.setGeometry(QtCore.QRect(40, 130, 90, 18))
        self.label_17.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_8.addWidget(self.frame_25)
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(250, 20, 371, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_21 = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.pushButton_25 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_25.setGeometry(QtCore.QRect(30, 0, 61, 61))
        self.pushButton_25.setStyleSheet("    QPushButton {\n"
                                         "        border-radius: 50px;\n"
                                         "        \n"
                                         "    }")
        self.pushButton_25.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("champion-icon/13.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_25.setIcon(icon10)
        self.pushButton_25.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_25.setObjectName("pushButton_25")
        self.label_5 = QtWidgets.QLabel(self.frame_21)
        self.label_5.setGeometry(QtCore.QRect(30, 70, 61, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_26 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_26.setGeometry(QtCore.QRect(100, 0, 31, 34))
        self.pushButton_26.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("profileicon/4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_26.setIcon(icon11)
        self.pushButton_26.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_27.setGeometry(QtCore.QRect(100, 30, 31, 34))
        self.pushButton_27.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("profileicon/5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_27.setIcon(icon12)
        self.pushButton_27.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_27.setObjectName("pushButton_27")
        self.label_6 = QtWidgets.QLabel(self.frame_21)
        self.label_6.setGeometry(QtCore.QRect(230, 20, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_21)
        self.label_7.setGeometry(QtCore.QRect(240, 60, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_28 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_28.setGeometry(QtCore.QRect(140, 0, 31, 34))
        self.pushButton_28.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("profileicon/6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_28.setIcon(icon13)
        self.pushButton_28.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_29.setGeometry(QtCore.QRect(140, 30, 31, 34))
        self.pushButton_29.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("profileicon/10.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_29.setIcon(icon14)
        self.pushButton_29.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_29.setObjectName("pushButton_29")
        self.verticalLayout_6.addWidget(self.frame_21)
        self.frame_22 = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_18.setGeometry(QtCore.QRect(30, 10, 41, 41))
        self.pushButton_18.setText("")
        self.pushButton_18.setIcon(icon9)
        self.pushButton_18.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_19.setGeometry(QtCore.QRect(70, 10, 41, 41))
        self.pushButton_19.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("champion-icon/6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_19.setIcon(icon15)
        self.pushButton_19.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_20.setGeometry(QtCore.QRect(110, 10, 41, 41))
        self.pushButton_20.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("champion-icon/1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_20.setIcon(icon16)
        self.pushButton_20.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_21.setGeometry(QtCore.QRect(150, 10, 41, 41))
        self.pushButton_21.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("champion-icon/8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_21.setIcon(icon17)
        self.pushButton_21.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_22.setGeometry(QtCore.QRect(190, 10, 41, 41))
        self.pushButton_22.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("champion-icon/11.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_22.setIcon(icon18)
        self.pushButton_22.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_23.setGeometry(QtCore.QRect(230, 10, 41, 41))
        self.pushButton_23.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("champion-icon/3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_23.setIcon(icon19)
        self.pushButton_23.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_24.setGeometry(QtCore.QRect(280, 10, 41, 41))
        self.pushButton_24.setStyleSheet("    QPushButton {\n"
                                         "        border-radius: 16px;\n"
                                         "        \n"
                                         "        \n"
                                         "    background-color: rgb(0, 170, 255);\n"
                                         "    }")
        self.pushButton_24.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("profileicon/5506.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_24.setIcon(icon20)
        self.pushButton_24.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_24.setObjectName("pushButton_24")
        self.verticalLayout_6.addWidget(self.frame_22)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 191, 161))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_19 = QtWidgets.QFrame(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.label = QtWidgets.QLabel(self.frame_19)
        self.label.setGeometry(QtCore.QRect(10, 40, 181, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.frame_19)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 111, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.frame_19)
        self.frame_20 = QtWidgets.QFrame(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.label_2 = QtWidgets.QLabel(self.frame_20)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 70, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_20)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 70, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.frame_20)
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 400, 938, 131))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 10, 941, 171))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_26 = QtWidgets.QFrame(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_26)
        self.pushButton_17.setGeometry(QtCore.QRect(10, 0, 101, 101))
        self.pushButton_17.setIcon(icon13)
        self.pushButton_17.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_17.setObjectName("pushButton_17")
        self.label_18 = QtWidgets.QLabel(self.frame_26)
        self.label_18.setGeometry(QtCore.QRect(20, 110, 81, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_26)
        self.label_19.setGeometry(QtCore.QRect(120, 9, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.pushButton_40 = QtWidgets.QPushButton(self.frame_26)
        self.pushButton_40.setGeometry(QtCore.QRect(170, 100, 112, 34))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_40.setFont(font)
        self.pushButton_40.setStyleSheet("background-color: rgb(137, 194, 255);\n"
                                         "color : rgb(255, 255, 255);")
        self.pushButton_40.setObjectName("pushButton_40")
        self.horizontalLayout_9.addWidget(self.frame_26)
        self.frame_27 = QtWidgets.QFrame(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy)
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.pushButton_41 = QtWidgets.QPushButton(self.frame_27)
        self.pushButton_41.setGeometry(QtCore.QRect(40, 0, 101, 101))
        self.pushButton_41.setText("")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("profileicon/5290.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_41.setIcon(icon21)
        self.pushButton_41.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_41.setObjectName("pushButton_41")
        self.label_20 = QtWidgets.QLabel(self.frame_27)
        self.label_20.setGeometry(QtCore.QRect(40, 110, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_9.addWidget(self.frame_27)
        self.frame_28 = QtWidgets.QFrame(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy)
        self.frame_28.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.pushButton_42 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_42.setGeometry(QtCore.QRect(40, 0, 131, 131))
        self.pushButton_42.setText("")
        self.pushButton_42.setIcon(icon11)
        self.pushButton_42.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_42.setObjectName("pushButton_42")
        self.horizontalLayout_9.addWidget(self.frame_28)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setGeometry(QtCore.QRect(20, 180, 931, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_5.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.horizontalLayout_7.addWidget(self.stackedWidget)
        self.horizontalLayout_4.addWidget(self.frame_14)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.frame_4.setFont(font)
        self.frame_4.setStyleSheet("#frame_4{\n"
                                   "    \n"
                                   "    background-color: rgb(255, 255, 255);\n"
                                   "}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(0, 13, 0, 13)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_10 = QtWidgets.QFrame(self.frame_4)
        self.frame_10.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_10.setStyleSheet("QPushButton:pressed{\n"
                                    "    padding-top:5px;\n"
                                    "    padding-left:5px;\n"
                                    "}")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 10, 41, 41))
        self.pushButton_7.setStyleSheet("#pushButton_7{\n"
                                        "    border:none;\n"
                                        "    \n"
                                        "    \n"
                                        "    \n"
                                        "}")
        self.pushButton_7.setText("")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("picture/音乐开始.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon22)
        self.pushButton_7.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_8.setGeometry(QtCore.QRect(80, 10, 41, 41))
        self.pushButton_8.setStyleSheet("#pushButton_8{\n"
                                        "    border:none;\n"
                                        "    \n"
                                        "    \n"
                                        "}")
        self.pushButton_8.setText("")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("picture/28.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon23)
        self.pushButton_8.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_3.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_4)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_3.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_4)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_3.addWidget(self.frame_12)
        self.verticalLayout.addWidget(self.frame_4)
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1265, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # All functions
        # button functions
        self.pushButton_4.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.pushButton_10.clicked.connect(self.display)
        self.pushButton_9.clicked.connect(self.display2)
        self.pushButton_15.clicked.connect(self.search_lol_name)
        self.pushButton_40.clicked.connect(self.search_lol_name)

    # change region buttons
    def display(self):
        self.stackedWidget.setCurrentIndex(1)

    def display2(self):
        self.stackedWidget.setCurrentIndex(0)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Match Up History "))
        self.pushButton_9.setText(_translate("MainWindow", " LOL"))
        self.pushButton_10.setText(_translate("MainWindow", " TFT"))
        self.pushButton_12.setText(_translate("MainWindow", "Search for Legue of Legends"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "North America"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Brazil"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "EU Nordic & East"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "EU West"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Japan"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "Korea"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "Latin America North"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "Latin America South"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "Oceania"))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "PBE(public beta enviroment)"))
        self.comboBox_3.setItemText(10, _translate("MainWindow", "Philippines"))
        self.comboBox_3.setItemText(11, _translate("MainWindow", "Russia"))
        self.comboBox_3.setItemText(12, _translate("MainWindow", "Singapore"))
        self.comboBox_3.setItemText(13, _translate("MainWindow", "Thailand"))
        self.comboBox_3.setItemText(14, _translate("MainWindow", "Turkey"))
        self.comboBox_3.setItemText(15, _translate("MainWindow", "Taiwan"))
        self.comboBox_3.setItemText(16, _translate("MainWindow", "Vietnam"))
        self.pushButton_15.setText(_translate("MainWindow", "Search"))
        self.lineEdit_2.setText(_translate("MainWindow", "saosijja"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "North America"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Brazil"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "EU Nordic & East"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "EU West"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Japan"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Korea"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Latin America North"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Latin America South"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "Oceania"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "PBE(public beta enviroment)"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "Philippines"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "Russia"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "Singapore"))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "Thailand"))
        self.comboBox_2.setItemText(14, _translate("MainWindow", "Turkey"))
        self.comboBox_2.setItemText(15, _translate("MainWindow", "Taiwan"))
        self.comboBox_2.setItemText(16, _translate("MainWindow", "Vietnam"))
        self.pushButton_13.setText(_translate("MainWindow", "Search for Teamfight Tactics"))
        self.pushButton_16.setText(_translate("MainWindow", "Search"))
        self.label_8.setText(_translate("MainWindow", "sadssadsdssd"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "TextLabel"))
        self.label_12.setText(_translate("MainWindow", "TextLabel"))
        self.label_13.setText(_translate("MainWindow", "TextLabel"))
        self.label_14.setText(_translate("MainWindow", "TextLabel"))
        self.label_15.setText(_translate("MainWindow", "TextLabel"))
        self.label_16.setText(_translate("MainWindow", "TextLabel"))
        self.label_17.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "lv:17"))
        self.label_6.setText(_translate("MainWindow", "12 / 0 / 11"))
        self.label_7.setText(_translate("MainWindow", "9.0 KDA"))
        self.label.setText(_translate("MainWindow", "hours ago"))
        self.label_4.setText(_translate("MainWindow", "Ranked solo"))
        self.label_2.setText(_translate("MainWindow", "Victory"))
        self.label_3.setText(_translate("MainWindow", "40m 10s"))
        self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox"))
        self.pushButton_40.setText(_translate("MainWindow", "Renew"))

    # functions after user clicked search button
    # retrieve information for two input bar to create searchMatch based on given information
    def search_lol_name(self):
        # Get the sender object and print its name or text
        # push_button_15

        # Get the search query from the search bar
        lol_query = self.lineEdit.text()
        lol_region_text = self.comboBox_3.currentText()
        if lol_query == "":
            print("False")
        else:
            self.Summoner = searchMatch.SearchMatch(lol_region_text, 'lol', lol_query)
            if not self.Summoner.searchComplete:
                print("wrong name entered")
            else:
                self.present_info()
                self.present_img()
                self.stackedWidget.setCurrentIndex(2)
                print("right name entered")

    # retrieve information for two input bar to create searchMatch based on given information
    def search_tft_name(self):
        # search function for tft
        tft_query = self.lineEdit_2.text()
        tft_region_text = self.comboBox_2.currentText()
        if tft_query == "":
            print("False")
        else:
            self.Summoner = searchMatch.SearchMatch(tft_region_text, 'tft', tft_query)
            if self.Summoner.errorCase == -1:
                print("wrong name entered")
            else:
                print("right name entered")

    # return the index of the in-match data of the summoner being searched
    def find_self_participant(self):
        participants_list = self.Summoner.match_details[0]['info']['participants']
        for participant in participants_list:
            if participant['summonerName'] == self.Summoner.summonerName:
                return participants_list.index(participant)

    # return victory or lost based on the win boolean retrieved from api
    def win_or_lose(self, bool):
        if bool:
            return "Victory"
        else:
            return "Lost"

    # helper function to determine how long since the indicated game finished
    def time_previous(self, gameTime):
        currentTime = time.time()
        timeDiff = int(currentTime) - int(gameTime / 1000)
        if timeDiff < 3600:
            return f"{int(timeDiff / 60)} minutes ago"
        elif 3600 < timeDiff < 86400:
            return f"{int(timeDiff / 3600)} hours ago"
        elif timeDiff > 86400:
            return f"{int(timeDiff / 86400)} days ago"

    # create images relates to all text display in league of legends match history page
    def present_info(self):
        _translate = QtCore.QCoreApplication.translate
        try:
            self.label_8.setText(
                _translate("MainWindow",
                           f"{self.Summoner.match_details[0]['info']['participants'][0]['summonerName']}"))
        except KeyError:
            self.label_8.setText(_translate("MainWindow", "N/A"))
        try:
            self.label_9.setText(
                _translate("MainWindow",
                           f"{self.Summoner.match_details[0]['info']['participants'][1]['summonerName']}"))
        except KeyError:
            self.label_9.setText(_translate("MainWindow", "N/A"))
        try:
            self.label_10.setText(
                _translate("MainWindow",
                           f"{self.Summoner.match_details[0]['info']['participants'][2]['summonerName']}"))
        except KeyError:
            self.label_10.setText(_translate("MainWindow", "N/A"))
        try:
            self.label_11.setText(
                _translate("MainWindow",
                           f"{self.Summoner.match_details[0]['info']['participants'][3]['summonerName']}"))
        except KeyError:
            self.label_11.setText(_translate("MainWindow", "N/A"))
        try:
            self.label_12.setText(
                _translate("MainWindow",
                           f"{self.Summoner.match_details[0]['info']['participants'][4]['summonerName']}"))
        except KeyError:
            self.label_12.setText(_translate("MainWindow", "N/A"))
        try:
            self.label_13.setText(
                _translate("MainWindow",
                           f"{self.Summoner.match_details[0]['info']['participants'][5]['summonerName']}"))
        except KeyError:
            self.label_13.setText(_translate("MainWindow", "N/A"))
        try:
            self.label_14.setText(
                _translate("MainWindow",
                           f"{self.Summoner.match_details[0]['info']['participants'][6]['summonerName']}"))
        except KeyError:
            self.label_14.setText(_translate("MainWindow", "N/A"))
        try:
            self.label_15.setText(
                _translate("MainWindow",
                           f"{self.Summoner.match_details[0]['info']['participants'][7]['summonerName']}"))
        except KeyError:
            self.label_15.setText(_translate("MainWindow", "N/A"))
        try:
            self.label_16.setText(
                _translate("MainWindow",
                           f"{self.Summoner.match_details[0]['info']['participants'][8]['summonerName']}"))
        except KeyError:
            self.label_16.setText(_translate("MainWindow", "N/A"))
        try:
            self.label_17.setText(
                _translate("MainWindow",
                           f"{self.Summoner.match_details[0]['info']['participants'][9]['summonerName']}"))
        except KeyError:
            self.label_17.setText(_translate("MainWindow", "N/A"))
        try:
            self.label_5.setText(
                _translate("MainWindow",
                           f"lv:{self.Summoner.match_details[0]['info']['participants'][0]['champLevel']}"))
        except KeyError:
            self.label_5.setText(_translate("MainWindow", "lv:"))
        try:
            self.label_6.setText(_translate("MainWindow",
                                            f"{self.Summoner.match_details[0]['info']['participants'][self.find_self_participant()]['kills']} "
                                            f"/ {self.Summoner.match_details[0]['info']['participants'][self.find_self_participant()]['deaths']} "
                                            f"/ {self.Summoner.match_details[0]['info']['participants'][self.find_self_participant()]['assists']}"))
        except KeyError:
            self.label_6.setText(_translate("MainWindow", "N/A / N/A / N/A"))
        try:
            kill = self.Summoner.match_details[0]['info']['participants'][self.find_self_participant()]['kills']
            death = self.Summoner.match_details[0]['info']['participants'][self.find_self_participant()]['deaths']
            assist = self.Summoner.match_details[0]['info']['participants'][self.find_self_participant()]['assists']
            kda = self.cal_KDA(kill, death, assist)
            kda_text = str(kda) + " KDA"
            self.label_7.setText(kda_text)
        except KeyError:
            self.label_7.setText(_translate("MainWindow", "N/A KDA"))
        self.label.setText(
            _translate("MainWindow",
                       f"{self.time_previous(self.Summoner.match_details[0]['info']['gameEndTimestamp'])}"))
        try:
            self.label_4.setText(_translate("MainWindow", "Ranked solo"))
        except KeyError:
            self.label_4.setText(_translate("MainWindow", "Ranked solo"))
        try:
            self.label_2.setText(
                _translate("MainWindow",
                           f"{self.win_or_lose(self.Summoner.match_details[0]['info']['participants'][self.find_self_participant()]['win'])}"))
        except KeyError:
            self.label_2.setText(_translate("MainWindow", "N/A"))
        try:
            self.label_3.setText(_translate("MainWindow",
                                            f"{int(self.Summoner.match_details[0]['info']['gameDuration'] / 60)}m {self.Summoner.match_details[0]['info']['gameDuration'] % 60}s"))
        except KeyError:
            self.label_3.setText(_translate("MainWindow", "N/Am N/As"))
        try:
            self.label_18.setText(_translate("MainWindow", f"lv : {self.Summoner.me['summonerLevel']}"))
        except KeyError:
            self.label_18.setText(_translate("MainWindow", "lv : N/A"))
        try:
            self.label_19.setText(_translate("MainWindow", f"{self.Summoner.summonerName}"))
        except KeyError:
            self.label_19.setText(_translate("MainWindow", "N/A"))
        try:
            self.label_20.setText(_translate("MainWindow", f"{self.Summoner.rankedInfo[0]['tier']}"))
        except KeyError:
            self.label_20.setText(_translate("MainWindow", "N/A"))

    # create images relates to all image display in league of legends match history page
    def present_img(self):
        champID = self.Summoner.match_details[0]['info']['participants'][self.find_self_participant()]['championId']
        items = []
        champs = []
        for i in range(7):
            items.append(
                self.Summoner.match_details[0]['info']['participants'][self.find_self_participant()][f'item{i}'])
        for x in range(10):
            champs.append(self.Summoner.match_details[0]['info']['participants'][x]['championId'])
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"champion-icon/{champID}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_25.setIcon(icon)

        # set the in-game items graphics
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"item/{items[0]}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_18.setIcon(icon)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(f"item/{items[1]}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_19.setIcon(icon1)

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(f"item/{items[2]}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_20.setIcon(icon2)

        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(f"item/{items[3]}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_21.setIcon(icon3)

        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(f"item/{items[4]}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_22.setIcon(icon4)

        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(f"item/{items[5]}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_23.setIcon(icon5)

        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(f"item/{items[6]}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_24.setIcon(icon6)

        # champions graphic on the right side
        # left half
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(f"champion-icon/{champs[0]}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_30.setIcon(icon7)

        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(f"champion-icon/{champs[1]}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_31.setIcon(icon8)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(f"champion-icon/{champs[2]}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_32.setIcon(icon9)

        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(f"champion-icon/{champs[3]}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_33.setIcon(icon10)

        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(f"champion-icon/{champs[4]}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_34.setIcon(icon11)

        # right half
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(f"champion-icon/{champs[5]}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_35.setIcon(icon12)

        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(f"champion-icon/{champs[6]}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_36.setIcon(icon13)

        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(f"champion-icon/{champs[7]}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_37.setIcon(icon14)

        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(f"champion-icon/{champs[8]}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_38.setIcon(icon15)

        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(f"champion-icon/{champs[9]}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_39.setIcon(icon16)

        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(f"profileicon/{self.Summoner.me['profileIconId']}.png"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.pushButton_17.setIcon(icon17)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(f"ranked-emblem/emblem-{self.Summoner.rankedInfo[0]['tier']}.png"),
                         QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.pushButton_41.setIcon(icon18)

    # calculate the KDA given kill death assists
    def cal_KDA(self, kill, death, assist):
        if (death == 0):
            return "Perfect KDA"
        else:
            return ((kill + assist) / death)

    def get_queues(self):
        with open('queues.json') as json_file:
            self.queues = json.load(json_file)

    def get_summonerSpell(self):
        with open('summoner.json') as json_file:
            self.summonerSpell = json.load(json_file)

    def output(self):
        print(self.summonerSpell['data']['SummonerBarrier'])
        return None

    def identify_queue(self, queueID):
        print(self.queues[queueID])


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.get_summonerSpell()
    ui.get_queues()
    ui.identify_queue(420)
    MainWindow.show()
    sys.exit(app.exec_())
