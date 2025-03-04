from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/view/templates/settings.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_settings(object):
    def setupUi(self, settings):
        settings.setObjectName("settings")
        settings.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        settings.resize(600, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(settings.sizePolicy().hasHeightForWidth())
        settings.setSizePolicy(sizePolicy)
        settings.setMinimumSize(QtCore.QSize(600, 450))
        settings.setMaximumSize(QtCore.QSize(600, 450))
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(settings)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(35, 35))
        self.label.setMaximumSize(QtCore.QSize(35, 35))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./zapzap/view/templates/../assets/icons/tray/tray.svg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.line = QtWidgets.QFrame(settings)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(settings)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.disableTrayIcon = QtWidgets.QCheckBox(self.groupBox)
        self.disableTrayIcon.setObjectName("disableTrayIcon")
        self.gridLayout.addWidget(self.disableTrayIcon, 3, 0, 1, 1)
        self.start_system = QtWidgets.QCheckBox(self.groupBox)
        self.start_system.setObjectName("start_system")
        self.gridLayout.addWidget(self.start_system, 0, 0, 1, 2)
        self.symbolic_icon = QtWidgets.QCheckBox(self.groupBox)
        self.symbolic_icon.setObjectName("symbolic_icon")
        self.gridLayout.addWidget(self.symbolic_icon, 6, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 2)
        self.keepBackground = QtWidgets.QCheckBox(self.groupBox)
        self.keepBackground.setChecked(True)
        self.keepBackground.setObjectName("keepBackground")
        self.gridLayout.addWidget(self.keepBackground, 2, 0, 1, 2)
        self.night_mode = QtWidgets.QCheckBox(self.groupBox)
        self.night_mode.setObjectName("night_mode")
        self.gridLayout.addWidget(self.night_mode, 6, 0, 1, 1)
        self.start_hide = QtWidgets.QCheckBox(self.groupBox)
        self.start_hide.setEnabled(False)
        self.start_hide.setObjectName("start_hide")
        self.gridLayout.addWidget(self.start_hide, 1, 0, 1, 2)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(settings)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.notify_desktop = QtWidgets.QCheckBox(self.groupBox_2)
        self.notify_desktop.setChecked(True)
        self.notify_desktop.setObjectName("notify_desktop")
        self.verticalLayout.addWidget(self.notify_desktop)
        self.line_4 = QtWidgets.QFrame(self.groupBox_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.show_photo = QtWidgets.QCheckBox(self.groupBox_2)
        self.show_photo.setEnabled(True)
        self.show_photo.setChecked(True)
        self.show_photo.setObjectName("show_photo")
        self.verticalLayout.addWidget(self.show_photo)
        self.show_name = QtWidgets.QCheckBox(self.groupBox_2)
        self.show_name.setEnabled(True)
        self.show_name.setChecked(True)
        self.show_name.setObjectName("show_name")
        self.verticalLayout.addWidget(self.show_name)
        self.show_msg = QtWidgets.QCheckBox(self.groupBox_2)
        self.show_msg.setEnabled(True)
        self.show_msg.setChecked(True)
        self.show_msg.setObjectName("show_msg")
        self.verticalLayout.addWidget(self.show_msg)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.retranslateUi(settings)
        QtCore.QMetaObject.connectSlotsByName(settings)

    def retranslateUi(self, settings):
        
        settings.setWindowTitle(_("Settings"))
        self.label_2.setText(_("Zapzap Settings"))
        self.groupBox.setTitle(_("System integration"))
        self.disableTrayIcon.setText(_("Disable tray icon"))
        self.start_system.setText(_("Start ZapZap with the system"))
        self.symbolic_icon.setText(_("Symbolic icon"))
        self.keepBackground.setText(_("Hide on close"))
        self.night_mode.setText(_("Night mode"))
        self.start_hide.setText(_("Start minimized"))
        self.groupBox_2.setTitle(_("Chat notifications"))
        self.notify_desktop.setText(_("Notifications on the desktop"))
        self.show_photo.setText(_("Show the photo of the sender"))
        self.show_name.setText(_("Show the sender\'s name"))
        self.show_msg.setText(_("Show message preview"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    settings = QtWidgets.QWidget()
    ui = Ui_settings()
    ui.setupUi(settings)
    settings.show()
    sys.exit(app.exec())
