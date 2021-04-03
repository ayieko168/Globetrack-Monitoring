# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/royalstate/Projects and Research/Python Projects/Globetrack-Monitoring/monitoring/utils/main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 649)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.loading_page = QtWidgets.QWidget()
        self.loading_page.setObjectName("loading_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.loading_page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.loading_page)
        self.frame.setStyleSheet("background-color: rgb(19, 8, 12);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.globetrack_logo_label = QtWidgets.QLabel(self.frame)
        self.globetrack_logo_label.setStyleSheet("image: url(:/images/photo.jpg);")
        self.globetrack_logo_label.setObjectName("globetrack_logo_label")
        self.verticalLayout_3.addWidget(self.globetrack_logo_label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.getting_ready_label = QtWidgets.QLabel(self.frame)
        self.getting_ready_label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.getting_ready_label.setFont(font)
        self.getting_ready_label.setObjectName("getting_ready_label")
        self.verticalLayout_3.addWidget(self.getting_ready_label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.frame)
        self.stackedWidget.addWidget(self.loading_page)
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.main_page)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.main_page)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.splitter = QtWidgets.QSplitter(self.frame_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(8)
        self.splitter.setObjectName("splitter")
        self.frame_3 = QtWidgets.QFrame(self.splitter)
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.channels_combo = QtWidgets.QComboBox(self.frame_3)
        self.channels_combo.setMinimumSize(QtCore.QSize(0, 23))
        self.channels_combo.setMaximumSize(QtCore.QSize(16777215, 23))
        self.channels_combo.setObjectName("channels_combo")
        self.channels_combo.addItem("")
        self.channels_combo.addItem("")
        self.channels_combo.addItem("")
        self.verticalLayout_8.addWidget(self.channels_combo)
        self.channel_recordings_listwidget = QtWidgets.QListWidget(self.frame_3)
        self.channel_recordings_listwidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.channel_recordings_listwidget.setAlternatingRowColors(True)
        self.channel_recordings_listwidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.channel_recordings_listwidget.setObjectName("channel_recordings_listwidget")
        item = QtWidgets.QListWidgetItem()
        self.channel_recordings_listwidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.channel_recordings_listwidget.addItem(item)
        self.verticalLayout_8.addWidget(self.channel_recordings_listwidget)
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.videoframe = QtWidgets.QFrame(self.widget)
        self.videoframe.setMinimumSize(QtCore.QSize(640, 480))
        self.videoframe.setObjectName("videoframe")
        self.verticalLayout_5.addWidget(self.videoframe)
        self.frame_5 = QtWidgets.QFrame(self.widget)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_5.setStyleSheet("/*background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.timer_slider = QtWidgets.QSlider(self.frame_5)
        self.timer_slider.setMaximumSize(QtCore.QSize(16777215, 23))
        self.timer_slider.setOrientation(QtCore.Qt.Horizontal)
        self.timer_slider.setObjectName("timer_slider")
        self.horizontalLayout.addWidget(self.timer_slider)
        spacerItem3 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.timer_label = QtWidgets.QLabel(self.frame_5)
        self.timer_label.setMaximumSize(QtCore.QSize(70, 23))
        self.timer_label.setObjectName("timer_label")
        self.horizontalLayout.addWidget(self.timer_label)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.play_button = QtWidgets.QPushButton(self.frame_5)
        self.play_button.setMinimumSize(QtCore.QSize(51, 23))
        self.play_button.setMaximumSize(QtCore.QSize(51, 23))
        self.play_button.setObjectName("play_button")
        self.horizontalLayout_2.addWidget(self.play_button)
        self.mark_in_button = QtWidgets.QPushButton(self.frame_5)
        self.mark_in_button.setMinimumSize(QtCore.QSize(51, 23))
        self.mark_in_button.setMaximumSize(QtCore.QSize(51, 23))
        self.mark_in_button.setObjectName("mark_in_button")
        self.horizontalLayout_2.addWidget(self.mark_in_button)
        self.mark_out_button = QtWidgets.QPushButton(self.frame_5)
        self.mark_out_button.setMinimumSize(QtCore.QSize(55, 23))
        self.mark_out_button.setMaximumSize(QtCore.QSize(55, 23))
        self.mark_out_button.setObjectName("mark_out_button")
        self.horizontalLayout_2.addWidget(self.mark_out_button)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.save_button = QtWidgets.QPushButton(self.frame_5)
        self.save_button.setMinimumSize(QtCore.QSize(92, 23))
        self.save_button.setMaximumSize(QtCore.QSize(100, 23))
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_2.addWidget(self.save_button)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.previous_clip_button = QtWidgets.QPushButton(self.frame_5)
        self.previous_clip_button.setMinimumSize(QtCore.QSize(75, 23))
        self.previous_clip_button.setMaximumSize(QtCore.QSize(80, 23))
        self.previous_clip_button.setObjectName("previous_clip_button")
        self.horizontalLayout_2.addWidget(self.previous_clip_button)
        self.next_clip_button = QtWidgets.QPushButton(self.frame_5)
        self.next_clip_button.setMinimumSize(QtCore.QSize(61, 23))
        self.next_clip_button.setMaximumSize(QtCore.QSize(65, 23))
        self.next_clip_button.setObjectName("next_clip_button")
        self.horizontalLayout_2.addWidget(self.next_clip_button)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.seek_to_button = QtWidgets.QPushButton(self.frame_5)
        self.seek_to_button.setMinimumSize(QtCore.QSize(51, 23))
        self.seek_to_button.setMaximumSize(QtCore.QSize(51, 23))
        self.seek_to_button.setObjectName("seek_to_button")
        self.horizontalLayout_4.addWidget(self.seek_to_button)
        self.seek_to_entry = QtWidgets.QLineEdit(self.frame_5)
        self.seek_to_entry.setMinimumSize(QtCore.QSize(0, 21))
        self.seek_to_entry.setMaximumSize(QtCore.QSize(70, 21))
        self.seek_to_entry.setObjectName("seek_to_entry")
        self.horizontalLayout_4.addWidget(self.seek_to_entry)
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.backward_button = QtWidgets.QPushButton(self.frame_5)
        self.backward_button.setMinimumSize(QtCore.QSize(30, 23))
        self.backward_button.setMaximumSize(QtCore.QSize(30, 23))
        self.backward_button.setObjectName("backward_button")
        self.horizontalLayout_4.addWidget(self.backward_button)
        self.backward_button_2 = QtWidgets.QPushButton(self.frame_5)
        self.backward_button_2.setMinimumSize(QtCore.QSize(30, 23))
        self.backward_button_2.setMaximumSize(QtCore.QSize(30, 23))
        self.backward_button_2.setObjectName("backward_button_2")
        self.horizontalLayout_4.addWidget(self.backward_button_2)
        self.forward_button = QtWidgets.QPushButton(self.frame_5)
        self.forward_button.setMinimumSize(QtCore.QSize(30, 23))
        self.forward_button.setMaximumSize(QtCore.QSize(30, 23))
        self.forward_button.setObjectName("forward_button")
        self.horizontalLayout_4.addWidget(self.forward_button)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addWidget(self.frame_5)
        self.verticalLayout_6.addWidget(self.splitter)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.main_page)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.globetrack_logo_label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#fbbe18;\">Globe Track International</span></p></body></html>"))
        self.getting_ready_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#fbbe18;\">Getting Everything Ready...</span></p></body></html>"))
        self.channels_combo.setPlaceholderText(_translate("MainWindow", "Select Channel"))
        self.channels_combo.setItemText(0, _translate("MainWindow", "KTN News"))
        self.channels_combo.setItemText(1, _translate("MainWindow", "KTN Home"))
        self.channels_combo.setItemText(2, _translate("MainWindow", "NTV"))
        __sortingEnabled = self.channel_recordings_listwidget.isSortingEnabled()
        self.channel_recordings_listwidget.setSortingEnabled(False)
        item = self.channel_recordings_listwidget.item(0)
        item.setText(_translate("MainWindow", "KTN35feg"))
        item = self.channel_recordings_listwidget.item(1)
        item.setText(_translate("MainWindow", "fg425251gh"))
        self.channel_recordings_listwidget.setSortingEnabled(__sortingEnabled)
        self.timer_label.setText(_translate("MainWindow", "00:00:00"))
        self.play_button.setText(_translate("MainWindow", "Play"))
        self.mark_in_button.setText(_translate("MainWindow", "Mark In"))
        self.mark_out_button.setText(_translate("MainWindow", "Mark Out"))
        self.save_button.setText(_translate("MainWindow", "SAVE"))
        self.previous_clip_button.setText(_translate("MainWindow", "Previous Clip"))
        self.next_clip_button.setText(_translate("MainWindow", "Next Clip"))
        self.seek_to_button.setText(_translate("MainWindow", "Seek To:"))
        self.label_5.setText(_translate("MainWindow", " Seconds "))
        self.backward_button.setText(_translate("MainWindow", "<-"))
        self.backward_button_2.setText(_translate("MainWindow", "||"))
        self.forward_button.setText(_translate("MainWindow", "->"))
from . import resources
