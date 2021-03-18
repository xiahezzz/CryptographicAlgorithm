from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_CaesarCipher(object):
    def setupUi(self, CaesarCipher):
        CaesarCipher.setObjectName("CaesarCipher")
        CaesarCipher.resize(680, 858)
        CaesarCipher.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.plaintext = QtWidgets.QTextEdit(CaesarCipher)
        self.plaintext.setGeometry(QtCore.QRect(140, 120, 501, 131))
        self.plaintext.setObjectName("plaintext")
        self.ciphertext = QtWidgets.QTextEdit(CaesarCipher)
        self.ciphertext.setGeometry(QtCore.QRect(140, 301, 501, 131))
        self.ciphertext.setObjectName("ciphertext")
        self.message1 = QtWidgets.QLabel(CaesarCipher)
        self.message1.setGeometry(QtCore.QRect(40, 160, 82, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.message1.setFont(font)
        self.message1.setObjectName("message1")
        self.message2 = QtWidgets.QLabel(CaesarCipher)
        self.message2.setGeometry(QtCore.QRect(40, 330, 82, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.message2.setFont(font)
        self.message2.setObjectName("message2")
        self.key = QtWidgets.QLabel(CaesarCipher)
        self.key.setGeometry(QtCore.QRect(40, 40, 82, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.key.setFont(font)
        self.key.setObjectName("key")
        self.keytext = QtWidgets.QTextEdit(CaesarCipher)
        self.keytext.setGeometry(QtCore.QRect(140, 30, 201, 71))
        self.keytext.setObjectName("keytext")
        self.layoutWidget = QtWidgets.QWidget(CaesarCipher)
        self.layoutWidget.setGeometry(QtCore.QRect(400, 820, 195, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.clearButton = QtWidgets.QPushButton(self.layoutWidget)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_3.addWidget(self.clearButton)
        self.exitButton = QtWidgets.QPushButton(self.layoutWidget)
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout_3.addWidget(self.exitButton)
        self.layoutWidget1 = QtWidgets.QWidget(CaesarCipher)
        self.layoutWidget1.setGeometry(QtCore.QRect(290, 260, 195, 30))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton1 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton1.setObjectName("pushButton1")
        self.horizontalLayout_2.addWidget(self.pushButton1)
        self.pushButton2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton2.setObjectName("pushButton2")
        self.horizontalLayout_2.addWidget(self.pushButton2)
        self.message2_2 = QtWidgets.QLabel(CaesarCipher)
        self.message2_2.setGeometry(QtCore.QRect(10, 600, 181, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.message2_2.setFont(font)
        self.message2_2.setObjectName("message2_2")
        self.suspectedtext = QtWidgets.QTextEdit(CaesarCipher)
        self.suspectedtext.setGeometry(QtCore.QRect(140, 480, 501, 331))
        self.suspectedtext.setObjectName("suspectedtext")
        self.crackButton = QtWidgets.QPushButton(CaesarCipher)
        self.crackButton.setGeometry(QtCore.QRect(330, 440, 93, 28))
        self.crackButton.setObjectName("crackButton")
        self.widget = QtWidgets.QWidget(CaesarCipher)
        self.widget.setGeometry(QtCore.QRect(40, 820, 200, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_4.addWidget(self.progressBar)

        self.retranslateUi(CaesarCipher)
        QtCore.QMetaObject.connectSlotsByName(CaesarCipher)

    def retranslateUi(self, CaesarCipher):
        _translate = QtCore.QCoreApplication.translate
        CaesarCipher.setWindowTitle(_translate("CaesarCipher", "CeasarCipher"))
        self.plaintext.setHtml(_translate("CaesarCipher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.ciphertext.setHtml(_translate("CaesarCipher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.message1.setText(_translate("CaesarCipher", "明文"))
        self.message2.setText(_translate("CaesarCipher", "密文"))
        self.key.setText(_translate("CaesarCipher", "密钥"))
        self.keytext.setHtml(_translate("CaesarCipher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.clearButton.setText(_translate("CaesarCipher", "清空所有"))
        self.exitButton.setText(_translate("CaesarCipher", "退出程序"))
        self.pushButton1.setText(_translate("CaesarCipher", "加密"))
        self.pushButton2.setText(_translate("CaesarCipher", "解密"))
        self.message2_2.setText(_translate("CaesarCipher", "可能明文"))
        self.suspectedtext.setHtml(_translate("CaesarCipher", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.crackButton.setText(_translate("CaesarCipher", "暴力破解"))
        self.label.setText(_translate("CaesarCipher", "完成进度："))

class mywindow(QtWidgets.QWidget, Ui_CaesarCipher):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.pushButton1.clicked.connect(self.encryption)
        self.pushButton2.clicked.connect(self.decryption)
        self.clearButton.clicked.connect(self.clearmessage)
        self.exitButton.clicked.connect(self.exitapp)
        self.crackButton.clicked.connect(self.crack_text)
        self.key_message = self.keytext.toPlainText()
        self.plain_text = self.plaintext.toPlainText()
        self.cipher_text = self.ciphertext.toPlainText()
        self.crack_text = ''
        self.progressBar.setValue(0)

    def encryption(self):
        self.progressBar.setValue(0)
        self.key_message = self.keytext.toPlainText()
        self.plain_text = self.plaintext.toPlainText()
        progress_num = 0
        for i in self.plain_text:
            if i.isalpha():
                i_lower = i.lower()
                key_ = ord(i_lower) + int(self.key_message)
                while key_ > 122:
                    key_ -= 26
                if i.islower():
                    self.ciphertext.insertPlainText(chr(key_))
                else:
                    self.ciphertext.insertPlainText(chr(key_).upper())
                progress_num += 1 / len(self.plain_text) * 100
                self.progressBar.setValue(progress_num)
            else:
                self.ciphertext.insertPlainText(i)
                progress_num += 1 / len(self.plain_text) * 100
                self.progressBar.setValue(progress_num)
        self.progressBar.setValue(100)

    def decryption(self):
        self.progressBar.setValue(0)
        progress_num = 0
        self.key_message = 26 - int(self.keytext.toPlainText())
        self.cipher_text = self.ciphertext.toPlainText()
        for i in self.cipher_text:
            if i.isalpha():
                i_lower = i.lower()
                key_ = ord(i_lower) + int(self.key_message)
                if key_ > 122 and i.islower():
                    self.plaintext.insertPlainText(chr(key_ - 26))
                elif key_ > 122 and i.isupper():
                    self.plaintext.insertPlainText(chr(key_ - 26).upper())
                elif i.islower():
                    self.plaintext.insertPlainText(chr(ord(i_lower) + int(self.key_message)))
                elif i.isupper():
                    self.plaintext.insertPlainText(chr(ord(i_lower) + int(self.key_message)).upper())
                progress_num += 1 / len(self.cipher_text) * 100
                self.progressBar.setValue(progress_num)
            else:
                self.plaintext.insertPlainText(i)
                progress_num += 1 / len(self.cipher_text) * 100
                self.progressBar.setValue(progress_num)
        self.progressBar.setValue(100)

    def crack_text(self):
        self.progressBar.setValue(0)
        self.cipher_text = self.ciphertext.toPlainText()
        progress_num = 0
        for key in range(1, 26):
            for i in self.cipher_text:
                if i.isalpha():
                    i_lower = i.lower()
                    key_ = ord(i_lower) + key
                    if key_ > 122 and i.islower():
                        self.suspectedtext.insertPlainText(chr(key_ - 26))
                    elif key_ > 122 and i.isupper():
                        self.suspectedtext.insertPlainText(chr(key_ - 26).upper())
                    elif i.islower():
                        self.suspectedtext.insertPlainText(chr(ord(i_lower) + key))
                    elif i.isupper():
                        self.suspectedtext.insertPlainText(chr(ord(i_lower) + key).upper())
                    progress_num += 1 / (len(self.cipher_text) * 25) * 100
                    self.progressBar.setValue(progress_num)
                else:
                    self.suspectedtext.insertPlainText(i)
                    progress_num += 1 / (len(self.cipher_text) * 25) * 100
                    self.progressBar.setValue(progress_num)
            self.suspectedtext.insertPlainText('\n')
        self.progressBar.setValue(100)


    def clearmessage(self):
        self.progressBar.setValue(0)
        self.ciphertext.clear()
        self.plaintext.clear()
        self.keytext.clear()
        self.suspectedtext.clear()

    def exitapp(self):
        exit()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    sys.exit(app.exec_())
