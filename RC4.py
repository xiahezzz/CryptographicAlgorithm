from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_RC4(object):
    def setupUi(self, RC4):
        RC4.setObjectName("RC4")
        RC4.resize(752, 814)
        self.ketext = QtWidgets.QLabel(RC4)
        self.ketext.setGeometry(QtCore.QRect(70, 60, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.ketext.setFont(font)
        self.ketext.setObjectName("ketext")
        self.ketext_2 = QtWidgets.QLabel(RC4)
        self.ketext_2.setGeometry(QtCore.QRect(40, 190, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.ketext_2.setFont(font)
        self.ketext_2.setObjectName("ketext_2")
        self.ketext_3 = QtWidgets.QLabel(RC4)
        self.ketext_3.setGeometry(QtCore.QRect(70, 320, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.ketext_3.setFont(font)
        self.ketext_3.setObjectName("ketext_3")
        self.ketext_4 = QtWidgets.QLabel(RC4)
        self.ketext_4.setGeometry(QtCore.QRect(70, 500, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.ketext_4.setFont(font)
        self.ketext_4.setObjectName("ketext_4")
        self.ketext_5 = QtWidgets.QLabel(RC4)
        self.ketext_5.setGeometry(QtCore.QRect(40, 620, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.ketext_5.setFont(font)
        self.ketext_5.setObjectName("ketext_5")
        self.keyedit = QtWidgets.QTextEdit(RC4)
        self.keyedit.setGeometry(QtCore.QRect(170, 40, 511, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.keyedit.setFont(font)
        self.keyedit.setObjectName("keyedit")
        self.keystream = QtWidgets.QTextEdit(RC4)
        self.keystream.setGeometry(QtCore.QRect(170, 160, 511, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.keystream.setFont(font)
        self.keystream.setObjectName("keystream")
        self.messagetext = QtWidgets.QTextEdit(RC4)
        self.messagetext.setGeometry(QtCore.QRect(170, 290, 511, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.messagetext.setFont(font)
        self.messagetext.setObjectName("messagetext")
        self.messagetext_2 = QtWidgets.QTextEdit(RC4)
        self.messagetext_2.setGeometry(QtCore.QRect(170, 480, 511, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.messagetext_2.setFont(font)
        self.messagetext_2.setObjectName("messagetext_2")
        self.messagetext_3 = QtWidgets.QTextEdit(RC4)
        self.messagetext_3.setGeometry(QtCore.QRect(170, 600, 511, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.messagetext_3.setFont(font)
        self.messagetext_3.setObjectName("messagetext_3")
        self.widget = QtWidgets.QWidget(RC4)
        self.widget.setGeometry(QtCore.QRect(310, 420, 195, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.widget1 = QtWidgets.QWidget(RC4)
        self.widget1.setGeometry(QtCore.QRect(490, 740, 195, 31))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.widget2 = QtWidgets.QWidget(RC4)
        self.widget2.setGeometry(QtCore.QRect(80, 740, 200, 31))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        self.retranslateUi(RC4)
        QtCore.QMetaObject.connectSlotsByName(RC4)

    def retranslateUi(self, RC4):
        _translate = QtCore.QCoreApplication.translate
        RC4.setWindowTitle(_translate("RC4", "RC4"))
        self.ketext.setText(_translate("RC4", "密钥"))
        self.ketext_2.setText(_translate("RC4", "密钥流"))
        self.ketext_3.setText(_translate("RC4", "明文"))
        self.ketext_4.setText(_translate("RC4", "密文"))
        self.ketext_5.setText(_translate("RC4", "解密文"))
        self.pushButton.setText(_translate("RC4", "加密"))
        self.pushButton_2.setText(_translate("RC4", "解密"))
        self.pushButton_3.setText(_translate("RC4", "清空"))
        self.pushButton_4.setText(_translate("RC4", "退出程序"))

class rc4(QtWidgets.QWidget,Ui_RC4):
    def __init__(self):
        super(rc4, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.encryption)
        self.pushButton_2.clicked.connect(self.decryption)
        self.pushButton_3.clicked.connect(self.clear)
        self.pushButton_4.clicked.connect(self.exit)
        self.key_text = []
        self.stream_key = self.keystream.toPlainText()
        self.message = ''
        self.cipher_text = ''
        self.s_box = [chr(i) for i in range(256)]

    def encryption(self):
        self.messagetext_2.clear()
        self.keystream.clear()
        for i in self.keyedit.toPlainText():
            if i.isalpha():
                self.key_text += [ord(i)]
            else:
                self.key_text += [int(i)]
        self.message = self.messagetext.toPlainText()
        message_size = len(self.messagetext.toPlainText())
        key_size = len(self.keyedit.toPlainText())
        self.cipher_text = ''
        self.stream_key = ''
        j = 0
        for i in range(256):
            j = (j + ord(self.s_box[i]) + int(self.key_text[i % key_size])) % 256
            self.s_box[i], self.s_box[j] = self.s_box[j], self.s_box[i]
        m = 0
        n = 0
        for t in range(message_size):
            m = (m + 1) % 256
            n = (n + ord(self.s_box[m]) ) % 256
            self.s_box[m], self.s_box[n] = self.s_box[n], self.s_box[m]
            self.stream_key += self.s_box[(ord(self.s_box[m]) + ord(self.s_box[n])) % 256]
        self.keystream.setPlainText(self.stream_key)
        for t in range(message_size):
            self.cipher_text += chr(ord(self.message[t]) ^ ord(self.stream_key[t]))
        self.messagetext_2.insertPlainText(self.cipher_text)

    def decryption(self):
        self.message = ''
        cipher_size = len(self.messagetext_2.toPlainText())
        self.cipher_text = self.messagetext_2.toPlainText()
        self.message = ''
        self.stream_key = self.keystream.toPlainText()
        for t in range(cipher_size):
            self.message += chr(ord(self.cipher_text[t]) ^ ord(self.stream_key[t]))
        self.messagetext_3.insertPlainText(self.message)

    def clear(self):
        self.messagetext.clear()
        self.messagetext_3.clear()
        self.messagetext_2.clear()
        self.keystream.clear()
        self.keyedit.clear()

    def exit(self):
        exit(0)

if __name__ == '__main__':
    app =  QtWidgets.QApplication(sys.argv)
    ui = rc4()
    ui.show()
    sys.exit(app.exec_())
