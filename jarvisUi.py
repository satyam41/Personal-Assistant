# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvisUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JarvisAI(object):
    def setupUi(self, JarvisAI):
        JarvisAI.setObjectName("JarvisAI")
        JarvisAI.resize(656, 600)
        self.centralwidget = QtWidgets.QWidget(JarvisAI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 501, 571))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Img/R.gif"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 20, 401, 111))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Img/T8bahf.gif"))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(400, 30, 171, 61))
        self.textBrowser.setStyleSheet("background:transpranet;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:20px")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 527, 93, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 527, 93, 31))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        JarvisAI.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(JarvisAI)
        self.statusbar.setObjectName("statusbar")
        JarvisAI.setStatusBar(self.statusbar)

        self.retranslateUi(JarvisAI)
        QtCore.QMetaObject.connectSlotsByName(JarvisAI)

    def retranslateUi(self, JarvisAI):
        _translate = QtCore.QCoreApplication.translate
        JarvisAI.setWindowTitle(_translate("JarvisAI", "MainWindow"))
        self.textBrowser.setHtml(_translate("JarvisAI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("JarvisAI", "Run"))
        self.pushButton_2.setText(_translate("JarvisAI", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JarvisAI = QtWidgets.QMainWindow()
    ui = Ui_JarvisAI()
    ui.setupUi(JarvisAI)
    JarvisAI.show()
    sys.exit(app.exec_())
