from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import re

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
        Dialog.setWindowTitle(_translate("Dialog", "DES"))
        self.label.setText(_translate("Dialog", "明文："))
        self.label_2.setText(_translate("Dialog", "密钥："))
        self.label_3.setText(_translate("Dialog", "密文："))
        self.label_4.setText(_translate("Dialog", "解密文："))
        self.pushButton.setText(_translate("Dialog", "加密"))
        self.pushButton_2.setText(_translate("Dialog", "解密"))
        self.pushButton_3.setText(_translate("Dialog", "清空"))
        self.pushButton_4.setText(_translate("Dialog", "退出"))

class MyDes(QtWidgets.QWidget,Ui_Dialog):
    def __init__(self):
        super(MyDes, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.all_message_encrypt)
        self.pushButton_2.clicked.connect(self.all_message_decrypt)
        self.pushButton_3.clicked.connect(self.clear)
        self.pushButton_4.clicked.connect(self.exit)
        self.size = 0
        self.message_ = ''
        self.key_ = ''
        self.cipher = ''
        self.plain = ''
        self.sub_key = []
        self.IP_Table = [
            58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7
        ]
        self.IPInv_Table = [
            40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25
        ]
        self.E_Table = [
            32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9,
            8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1
        ]
        self.P_Table = [
            16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
            2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25
        ]
        self.PC1_Table = [
            57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
        ]
        self.PC2_Table = [
            14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
        ]
        self.LS_Table = [
            1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
        ]
        self.S_Box = [
            #S1
             [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
	          [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
	          [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
	          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
            #S2
            [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
             [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
             [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
             [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
            #S3
            [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
             [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
             [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
             [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
            #S4
            [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
             [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
             [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
             [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
            #S5
            [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
             [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
             [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
             [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
            #S6
            [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
             [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
             [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
             [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
            #S7
            [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
             [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
             [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
             [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
            #S8
            [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
             [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
             [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
             [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
        ]

    def gen_key(self, key):
        key = str2bin(key)
        key = input_key_judge(key)
        divide_output = transform(key, self.PC1_Table, 56)
        key_C0 = divide_output[0:28]
        key_D0 = divide_output[28:]
        for i in self.LS_Table:
            key_c = left_turn(key_C0, i)
            key_d = left_turn(key_D0, i)
            key_output = transform(key_c + key_d, self.PC2_Table, 48)
            self.sub_key.append(key_output)

    def s_box(self, my_str):
        res = ""
        c = 0
        for i in range(0, len(my_str), 6):
            now_str = my_str[i:i + 6]
            row = int(now_str[0] + now_str[5], 2)
            col = int(now_str[1:5], 2)
            num = bin(self.S_Box[c][row][col])[2:]
            for gz in range(0, 4 - len(num)):
                num = '0' + num
            res += num
            c += 1
        return res

    def fun_f(self, bin_str, key):
        first_output = transform(bin_str, self.E_Table, 48)
        second_output = str_xor(first_output, key)
        third_output = self.s_box(second_output)
        last_output = transform(third_output, self.P_Table, 32)
        return last_output

    def all_message_encrypt(self):
        self.gen_key(self.key.toPlainText())
        self.message_ = self.message.toPlainText()
        bin_mess = deal_mess(str2bin(self.message_))
        res = ''
        tmp = re.findall(r'.{64}', bin_mess)
        for i in tmp:
            res += ''.join(str(i) for i in self.des_encrypt_one(i, 1))
        self.cipher = bin2str(res)
        self.ciphermessage.insertPlainText(bin2str(res))

    def all_message_decrypt(self):
        self.gen_key(self.key.toPlainText())
        bin_mess = deal_mess(str2bin(self.cipher))
        res = ""
        tmp = re.findall(r'.{64}', bin_mess)
        for i in tmp:
            res += ''.join(str(i) for i in self.des_encrypt_one(i, 0))
        self.plainmessage.insertPlainText(bin2str(res))

    def des_encrypt_one(self, bin_message, pattern):
        if pattern == 1:
            mes_ip_bin = transform(bin_message, self.IP_Table, 64)
            key_lst = self.sub_key
            mes_left = mes_ip_bin[0:32]
            mes_right = mes_ip_bin[32:]
            for i in range(0, 15):
                mes_tmp = mes_right
                f_result = self.fun_f(mes_tmp, key_lst[i])
                mes_right = str_xor(f_result, mes_left)
                mes_left = mes_tmp
            f_result = self.fun_f(mes_right, key_lst[15])
            mes_fin_left = str_xor(mes_left, f_result)
            mes_fin_right = mes_right
            fin_message = transform(mes_fin_left + mes_fin_right, self.IPInv_Table, 64)
        else:
            mes_ip_bin = transform(bin_message, self.IP_Table, 64)
            key_lst = self.sub_key
            mes_left = mes_ip_bin[0:32]
            mes_right = mes_ip_bin[32:]
            for i in range(1, 16):
                mes_tmp = mes_right
                f_result = self.fun_f(mes_tmp, key_lst[16 - i])
                mes_right = str_xor(f_result, mes_left)
                mes_left = mes_tmp
            f_result = self.fun_f(mes_right, key_lst[0])
            mes_fin_left = str_xor(mes_left, f_result)
            mes_fin_right = mes_right
            fin_message = transform(mes_fin_left + mes_fin_right, self.IPInv_Table, 64)
        return fin_message

    def exit(self):
        exit()

    def clear(self):
        self.message.clear()
        self.ciphermessage.clear()
        self.key.clear()
        self.plainmessage.clear()

def left_turn(my_str,num):
    left_res = my_str[num:len(my_str)]
    left_res = left_res+my_str[0:num]
    return left_res

def str_xor(my_str1,my_str2):
    res = ""
    for i in range(0,len(my_str1)):
        xor_res = int(my_str1[i],10)^int(my_str2[i],10)
        if xor_res == 1:
            res += '1'
        if xor_res == 0:
            res += '0'
    return res

def transform(input_array, table, length):
    return [input_array[table[i] - 1] for i in range(length)]

def str2bin(message):
    res = ""
    for i in message:
        tmp = bin(ord(i))[2:]
        for j in range(0,8-len(tmp)):
            tmp = '0'+ tmp
        res += tmp
    return res

def bin2str(bin_str):
    res = ""
    tmp = re.findall(r'.{8}',bin_str)
    for i in tmp:
        res += chr(int(i,2))
    return res

def deal_mess(bin_mess):
    ans = len(bin_mess)
    if ans % 64 != 0:
        for i in range( 64 - (ans%64)):
            bin_mess += '0'
    return bin_mess

def input_key_judge(bin_key):
    ans = len(bin_key)
    if len(bin_key) < 64:
        if ans % 64 != 0:
            for i in range(64 - (ans % 64)):
                bin_key += '0'
    return bin_key

if __name__ == '__main__':
    app =  QtWidgets.QApplication(sys.argv)
    ui = MyDes()
    ui.show()
    sys.exit(app.exec_())

