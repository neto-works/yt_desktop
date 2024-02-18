from PyQt5 import QtCore, QtGui, QtWidgets
import os
from pytube import YouTube


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_download = QtWidgets.QPushButton(self.centralwidget)
        self.bt_download.setGeometry(QtCore.QRect(340, 480, 121, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.bt_download.setFont(font)
        self.bt_download.setObjectName("bt_download")
        self.rb_mp3 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_mp3.setGeometry(QtCore.QRect(328, 380, 56, 21))
        self.rb_mp3.setObjectName("rb_mp3")
        self.rb_mp4 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_mp4.setGeometry(QtCore.QRect(420, 380, 56, 21))
        self.rb_mp4.setObjectName("rb_mp4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 801, 481))
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 10, 601, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txt_link = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_link.setObjectName("txt_link")
        self.horizontalLayout.addWidget(self.txt_link)
        self.label_2.raise_()
        self.bt_download.raise_()
        self.rb_mp3.raise_()
        self.rb_mp4.raise_()
        self.layoutWidget.raise_()
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
        self.bt_download.clicked.connect(self.download)

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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_download.setText(_translate("MainWindow", "Download"))
        self.rb_mp3.setText(_translate("MainWindow", "mp3"))
        self.rb_mp4.setText(_translate("MainWindow", "mp4"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/logo/logo.png\"/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "link:"))
        
import logo


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())