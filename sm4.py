import re
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(744, 461)
        self.message = QtWidgets.QTextEdit(Dialog)
        self.message.setGeometry(QtCore.QRect(140, 50, 501, 51))
        self.message.setObjectName("message")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 60, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 140, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.key = QtWidgets.QTextEdit(Dialog)
        self.key.setGeometry(QtCore.QRect(140, 140, 501, 51))
        self.key.setObjectName("key")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 220, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ciphermessage = QtWidgets.QTextEdit(Dialog)
        self.ciphermessage.setGeometry(QtCore.QRect(140, 220, 501, 51))
        self.ciphermessage.setObjectName("ciphermessage")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 310, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.plainmessage = QtWidgets.QTextEdit(Dialog)
        self.plainmessage.setGeometry(QtCore.QRect(140, 300, 501, 51))
        self.plainmessage.setObjectName("plainmessage")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(170, 390, 397, 32))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SM4"))
        self.label.setText(_translate("Dialog", "明文："))
        self.label_2.setText(_translate("Dialog", "密钥："))
        self.label_3.setText(_translate("Dialog", "密文："))
        self.label_4.setText(_translate("Dialog", "解密文："))
        self.pushButton.setText(_translate("Dialog", "加密"))
        self.pushButton_2.setText(_translate("Dialog", "解密"))
        self.pushButton_3.setText(_translate("Dialog", "清空"))
        self.pushButton_4.setText(_translate("Dialog", "退出"))

class MySM4(QtWidgets.QWidget,Ui_Dialog):
    def __init__(self):
        super(MySM4, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.encryption)
        self.pushButton_2.clicked.connect(self.decryption)
        self.pushButton_3.clicked.connect(self.clear)
        self.pushButton_4.clicked.connect(self.exit)
        self.S_Box = [
            0xd6, 0x90, 0xe9, 0xfe, 0xcc, 0xe1, 0x3d, 0xb7, 0x16, 0xb6, 0x14, 0xc2, 0x28, 0xfb, 0x2c, 0x05,
            0x2b, 0x67, 0x9a, 0x76, 0x2a, 0xbe, 0x04, 0xc3, 0xaa, 0x44, 0x13, 0x26, 0x49, 0x86, 0x06, 0x99,
            0x9c, 0x42, 0x50, 0xf4, 0x91, 0xef, 0x98, 0x7a, 0x33, 0x54, 0x0b, 0x43, 0xed, 0xcf, 0xac, 0x62,
            0xe4, 0xb3, 0x1c, 0xa9, 0xc9, 0x08, 0xe8, 0x95, 0x80, 0xdf, 0x94, 0xfa, 0x75, 0x8f, 0x3f, 0xa6,
            0x47, 0x07, 0xa7, 0xfc, 0xf3, 0x73, 0x17, 0xba, 0x83, 0x59, 0x3c, 0x19, 0xe6, 0x85, 0x4f, 0xa8,
            0x68, 0x6b, 0x81, 0xb2, 0x71, 0x64, 0xda, 0x8b, 0xf8, 0xeb, 0x0f, 0x4b, 0x70, 0x56, 0x9d, 0x35,
            0x1e, 0x24, 0x0e, 0x5e, 0x63, 0x58, 0xd1, 0xa2, 0x25, 0x22, 0x7c, 0x3b, 0x01, 0x21, 0x78, 0x87,
            0xd4, 0x00, 0x46, 0x57, 0x9f, 0xd3, 0x27, 0x52, 0x4c, 0x36, 0x02, 0xe7, 0xa0, 0xc4, 0xc8, 0x9e,
            0xea, 0xbf, 0x8a, 0xd2, 0x40, 0xc7, 0x38, 0xb5, 0xa3, 0xf7, 0xf2, 0xce, 0xf9, 0x61, 0x15, 0xa1,
            0xe0, 0xae, 0x5d, 0xa4, 0x9b, 0x34, 0x1a, 0x55, 0xad, 0x93, 0x32, 0x30, 0xf5, 0x8c, 0xb1, 0xe3,
            0x1d, 0xf6, 0xe2, 0x2e, 0x82, 0x66, 0xca, 0x60, 0xc0, 0x29, 0x23, 0xab, 0x0d, 0x53, 0x4e, 0x6f,
            0xd5, 0xdb, 0x37, 0x45, 0xde, 0xfd, 0x8e, 0x2f, 0x03, 0xff, 0x6a, 0x72, 0x6d, 0x6c, 0x5b, 0x51,
            0x8d, 0x1b, 0xaf, 0x92, 0xbb, 0xdd, 0xbc, 0x7f, 0x11, 0xd9, 0x5c, 0x41, 0x1f, 0x10, 0x5a, 0xd8,
            0x0a, 0xc1, 0x31, 0x88, 0xa5, 0xcd, 0x7b, 0xbd, 0x2d, 0x74, 0xd0, 0x12, 0xb8, 0xe5, 0xb4, 0xb0,
            0x89, 0x69, 0x97, 0x4a, 0x0c, 0x96, 0x77, 0x7e, 0x65, 0xb9, 0xf1, 0x09, 0xc5, 0x6e, 0xc6, 0x84,
            0x18, 0xf0, 0x7d, 0xec, 0x3a, 0xdc, 0x4d, 0x20, 0x79, 0xee, 0x5f, 0x3e, 0xd7, 0xcb, 0x39, 0x48
        ]
        self.FK = [
            '0xa3b1bac6', '0x56aa3350', '0x677d9197', '0xb27022dc'
        ]
        self.CK = [0] * 32
        self.K = ['0'] * 36
        self.RK = ['0'] * 32
        self.des_key = ''
        self.plain_text = ''
        self.cipher_text = ''
        self.decryption_text = ''
        self.is_alpha = False

    def set_round_key(self):
        self.des_key = self.key.toPlainText()
        key_temp = '0x'
        if self.des_key[0:2] != '0x':
            for i in self.des_key:
                if i.isalpha():
                    key_temp += str(byte2hex(i))[2:]
                else:
                    key_temp += str(hex(int(i)))[2:]
        self.des_key = hex2bin(self.des_key)
        if len(self.des_key) < 128:
            self.des_key += '0' * (128 - len(self.des_key))
        SK = re.findall('.{32}', self.des_key)
        for i in range(4):
            self.K[i] = xor_str(SK[i], hex2bin(self.FK[i]))
        for i in range(32):
            self.K[i + 4] = xor_str(self.K[i], self.t1(xor_str(self.K[i + 1], self.K[i + 2], self.K[i + 3], hex2bin(self.CK[i]))))
            self.RK[i] = self.K[i + 4]

    def set_ck(self):
        tmp = 0
        for i in range(32):
            for j in range(4):
                tmp = 7 * (4 * i + j) & 0xFF
                tmp = tmp << (24 - 8 * j)
                self.CK[i] = self.CK[i] + tmp
        for i in range(32):
            self.CK[i] = hex(self.CK[i])
            if len(str(self.CK[i])) <= 10:
                self.CK[i] = '0x' + '0' * (10 - len(str(self.CK[i]))) + str(self.CK[i])[2:]

    def s_fun(self, in_str):
        out = '0x'
        temp = 0
        for i in range(4):
            temp = int(in_str[i * 8:(i + 1) * 8], 2) & 0xFF
            if len(str(hex(self.S_Box[temp]))[2:]) < 2:
                out = out + '0' + str(hex(self.S_Box[temp])[2:])
            else:
                out += str(hex(self.S_Box[temp])[2:])
        return hex2bin(out)

    def t(self, in_str):
        return l_fun(self.s_fun(in_str))

    def t1(self, in_str):
        return l1_fun(self.s_fun(in_str))

    def crypt(self, in_str, flag):
        state = ['0'] * 36
        for i in range(4):
            state[i] = in_str[i]
        for j in range(32):
            if flag == 1:
                state[j + 4] = xor_str(state[j], self.t(xor_str(state[j + 1], state[j + 2], state[j + 3], self.RK[j])))
            elif flag == 0:
                state[j + 4] = xor_str(state[j], self.t(xor_str(state[j + 1], state[j + 2], state[j + 3], self.RK[31 - j])))
        return ''.join(state[35 - i] for i in range(4))

    def encryption(self):
        self.plain_text = self.message.toPlainText()
        res = ''
        self.set_ck()
        if self.plain_text[0:2] != '0x':
            self.plain_text = byte2hex(self.plain_text)
            self.is_alpha = True
        self.plain_text = hex2bin(self.plain_text)
        self.set_round_key()
        block_text = []
        size = len(self.plain_text)
        block = (size - 1) // 128 + 1
        self.plain_text += '0' * (block * 128 - size)
        x_text = ['0'] * 4
        for i in range(block):
            block_text.append(self.plain_text[i * 128:(i + 1) * 128])
            for j in range(4):
                x_text[j] = block_text[i][j * 32:(j + 1) * 32]
            self.cipher_text += self.crypt(x_text, 1)
        res = bin2hex(self.cipher_text)
        self.ciphermessage.insertPlainText(res)

    def decryption(self):
        block = len(self.cipher_text) // 128
        block_text = []
        x_text = ['0'] * 4
        for i in range(block):
            block_text.append(self.cipher_text[i * 128:(i + 1) * 128])
            for j in range(4):
                x_text[j] = block_text[i][j * 32:(j + 1) * 32]
            self.decryption_text += self.crypt(x_text, 0)
        res = bin2hex(self.decryption_text)
        if self.is_alpha:
            res = hex2byte(res[2:])
        self.plainmessage.insertPlainText(res)

    def clear(self):
        self.message.clear()
        self.ciphermessage.clear()
        self.key.clear()
        self.plainmessage.clear()

    def exit(self):
        exit()

def left_turn(my_str,num):
    left_res = my_str[num:len(my_str)]
    left_res = left_res + my_str[0:num]
    return left_res

def right_turn(my_str, num):
    right_res = my_str[-num:]
    right_res = right_res + my_str[0:-num]
    return right_res

def hex2bin(hex_str):
    res = ''
    for i in hex_str[2:]:
        i = int(i, 16)
        if len(bin(i)[2:]) < 4:
            res += '0' * (4 - len(bin(i)[2:])) + bin(i)[2:]
        else:
            res += bin(i)[2:]
    return res

def l_fun(in_str):
    return xor_str(in_str, left_turn(in_str, 2), left_turn(in_str, 10),  left_turn(in_str, 18), left_turn(in_str, 24))

def l1_fun(in_str):
    return xor_str(in_str, left_turn(in_str, 13), left_turn(in_str, 23))

def xor_str(*in_str):
    res = ''
    tmp = list(in_str[0])
    num = len(in_str)
    for j in range(len(in_str[0])):
        for i in range(1, num):
            tmp[j] = str(int(tmp[j]) ^ int(in_str[i][j]))
        res += tmp[j]
    return res

def add_xor(in_a, in_b):
    res = ''
    for i in range(len(in_a)):
        res += str(int(in_a[0]) + int(in_b[0]))
    return res

def byte2hex(in_str):
    res = '0x'
    for i in in_str:
        if len(hex(ord(i))[2:]) < 2:
            res += '0' * (2 - len(hex(ord(i))[2:])) + hex(ord(i))[2:]
        else:
            res += hex(ord(i))[2:]
    return res

def hex2byte(in_str):
    res = ''
    temp = re.findall('.{2}', in_str)
    for i in temp:
        i = int(i, 16)
        res += chr(i)
    return res

def bin2hex(in_str):
    temp = re.findall('.{4}', in_str)
    res = '0x'
    for i in temp:
        res += hex(int(i, 2))[2:]
    return res


if __name__ == '__main__':
    app =  QtWidgets.QApplication(sys.argv)
    ui = MySM4()
    ui.show()
    sys.exit(app.exec_())

