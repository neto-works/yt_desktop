from PyQt5 import QtCore, QtGui, QtWidgets
import os
from pytube import YouTube
from PyQt5.QtGui import QIcon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("border:none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hl_link = QtWidgets.QHBoxLayout()
        self.hl_link.setObjectName("hl_link")
        self.lb_link = QtWidgets.QLabel(self.frame)
        self.lb_link.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_link.setFont(font)
        self.lb_link.setObjectName("lb_link")
        self.hl_link.addWidget(self.lb_link)
        self.txt_link = QtWidgets.QLineEdit(self.frame)
        self.txt_link.setMinimumSize(QtCore.QSize(0, 30))
        self.txt_link.setObjectName("txt_link")
        self.hl_link.addWidget(self.txt_link)
        self.verticalLayout.addLayout(self.hl_link)
        self.lb_image = QtWidgets.QLabel(self.frame)
        self.lb_image.setObjectName("lb_image")
        self.verticalLayout.addWidget(self.lb_image)
        self.verticalLayout_2.addWidget(self.frame)
        self.fr_radio_buttons = QtWidgets.QFrame(self.centralwidget)
        self.fr_radio_buttons.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_radio_buttons.setStyleSheet("border:none;")
        self.fr_radio_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_radio_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_radio_buttons.setObjectName("fr_radio_buttons")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.fr_radio_buttons)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.rb_mp3 = QtWidgets.QRadioButton(self.fr_radio_buttons)
        self.rb_mp3.setObjectName("rb_mp3")
        self.horizontalLayout_3.addWidget(self.rb_mp3)
        self.rb_mp4 = QtWidgets.QRadioButton(self.fr_radio_buttons)
        self.rb_mp4.setObjectName("rb_mp4")
        self.horizontalLayout_3.addWidget(self.rb_mp4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.fr_radio_buttons)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setStyleSheet("border:none;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_dowload = QtWidgets.QPushButton(self.frame_2)
        self.btn_dowload.setMinimumSize(QtCore.QSize(200, 50))
        self.btn_dowload.setMaximumSize(QtCore.QSize(500, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.btn_dowload.setFont(font)
        self.btn_dowload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_dowload.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_dowload.setStyleSheet("border:1px solid #ae00ad;\n"
"border-radius:15px;")
        self.btn_dowload.setObjectName("btn_dowload")
        self.horizontalLayout.addWidget(self.btn_dowload)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ### fazer action do botão --> função Download ###
        self.btn_dowload.clicked.connect(self.download)

    ### Função download ###
    def download(self):
        if self.rb_mp4.isChecked() == True:
            url = self.txt_link.text()
            yt = YouTube(url)
            video = yt.streams.get_highest_resolution()
            video.download()
        elif self.rb_mp3.isChecked() == True:
            try:
                url = self.txt_link.text()
                yt = YouTube(url)
                audio = yt.streams.filter(only_audio=True).first()
                out_file = audio.download()
                # Salvando arquivo formato .mp3
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
            except:
                pass
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PlayTubeDownload"))
        self.lb_link.setText(_translate("MainWindow", "Link:"))
        self.lb_image.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/logo/logo.png\"/></p></body></html>"))
        self.rb_mp3.setText(_translate("MainWindow", "mp3"))
        self.rb_mp4.setText(_translate("MainWindow", "mp4"))
        self.frame_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.btn_dowload.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.btn_dowload.setText(_translate("MainWindow", "Download"))
import logo


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    
    MainWindow.setWindowTitle("PlayTubeDownload")
    MainWindow.setWindowIcon(QIcon('./assets/icon.ico'))
    
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
