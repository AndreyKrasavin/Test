from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(352, 507)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(249, 249, 249);\n"
"border-radius: 12;")
        self.lineEdit.setMaxLength(16)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy)
        self.btn_plus.setObjectName("btn_plus")
        self.gridLayout.addWidget(self.btn_plus, 3, 3, 1, 1)
        self.btn_plus_or_min = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_plus_or_min.sizePolicy().hasHeightForWidth())
        self.btn_plus_or_min.setSizePolicy(sizePolicy)
        self.btn_plus_or_min.setObjectName("btn_plus_or_min")
        self.gridLayout.addWidget(self.btn_plus_or_min, 6, 0, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy)
        self.btn_minus.setObjectName("btn_minus")
        self.gridLayout.addWidget(self.btn_minus, 2, 3, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 6, 1, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 3, 2, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 3, 1, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)
        self.btn_ravno = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ravno.sizePolicy().hasHeightForWidth())
        self.btn_ravno.setSizePolicy(sizePolicy)
        self.btn_ravno.setObjectName("btn_ravno")
        self.gridLayout.addWidget(self.btn_ravno, 6, 3, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 0, 1, 1, 1)
        self.btn_clear_all = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear_all.sizePolicy().hasHeightForWidth())
        self.btn_clear_all.setSizePolicy(sizePolicy)
        self.btn_clear_all.setObjectName("btn_clear_all")
        self.gridLayout.addWidget(self.btn_clear_all, 0, 0, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setStyleSheet("QPushButton {\n"
"    font: 900 15pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border:2px solid #c8c8c8;\n"
"    border-radius: 15;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(53, 53, 53);\n"
"    \n"
"    \n"
"    \n"
"}")
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)
        self.btn_umojit = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_umojit.sizePolicy().hasHeightForWidth())
        self.btn_umojit.setSizePolicy(sizePolicy)
        self.btn_umojit.setObjectName("btn_umojit")
        self.gridLayout.addWidget(self.btn_umojit, 1, 3, 1, 1)
        self.btn_steret = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_steret.sizePolicy().hasHeightForWidth())
        self.btn_steret.setSizePolicy(sizePolicy)
        self.btn_steret.setObjectName("btn_steret")
        self.gridLayout.addWidget(self.btn_steret, 0, 2, 1, 1)
        self.btn_delit = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_delit.sizePolicy().hasHeightForWidth())
        self.btn_delit.setSizePolicy(sizePolicy)
        self.btn_delit.setObjectName("btn_delit")
        self.gridLayout.addWidget(self.btn_delit, 0, 3, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    font: 900 15pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border:2px solid #c8c8c8;\n"
"    border-radius: 15;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(53, 53, 53);\n"
"    \n"
"    \n"
"    \n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 6, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 352, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.btn_7.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
"    font: 900 15pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border:2px solid #c8c8c8;\n"
"    border-radius: 15;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(53, 53, 53);\n"
"    \n"
"    \n"
"    \n"
"}"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_7.setShortcut(_translate("MainWindow", "7"))
        self.btn_8.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
"    font: 900 15pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border:2px solid #c8c8c8;\n"
"    border-radius: 15;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(53, 53, 53);\n"
"    \n"
"    \n"
"    \n"
"}"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_8.setShortcut(_translate("MainWindow", "8"))
        self.btn_plus.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
"    font: 900 15pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border:2px solid #c8c8c8;\n"
"    border-radius: 15;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(53, 53, 53);\n"
"    \n"
"    \n"
"    \n"
"}"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_plus.setShortcut(_translate("MainWindow", "+"))
        self.btn_plus_or_min.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
"    font: 900 15pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border:2px solid #c8c8c8;\n"
"    border-radius: 15;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(53, 53, 53);\n"
"    \n"
"    \n"
"    \n"
"}"))
        self.btn_plus_or_min.setText(_translate("MainWindow", "+/-"))
        self.btn_4.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
"    font: 900 15pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border:2px solid #c8c8c8;\n"
"    border-radius: 15;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(53, 53, 53);\n"
"    \n"
"    \n"
"    \n"
"}"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_4.setShortcut(_translate("MainWindow", "4"))
        self.btn_minus.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
"    font: 900 15pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border:2px solid #c8c8c8;\n"
"    border-radius: 15;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(53, 53, 53);\n"
"    \n"
"    \n"
"    \n"
"}"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_minus.setShortcut(_translate("MainWindow", "-"))
        self.btn_0.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
"    font: 900 15pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border:2px solid #c8c8c8;\n"
"    border-radius: 15;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(53, 53, 53);\n"
"    \n"
"    \n"
"    \n"
"}"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_0.setShortcut(_translate("MainWindow", "0"))
        self.btn_3.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
"    font: 900 15pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border:2px solid #c8c8c8;\n"
"    border-radius: 15;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(53, 53, 53);\n"
"    \n"
"    \n"
"    \n"
"}"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_3.setShortcut(_translate("MainWindow", "3"))
        self.btn_2.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
"    font: 900 15pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border:2px solid #c8c8c8;\n"
"    border-radius: 15;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(53, 53, 53);\n"
"    \n"
"    \n"
"    \n"
"}"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_2.setShortcut(_translate("MainWindow", "2"))
        self.btn_1.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
"    font: 900 15pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border:2px solid #c8c8c8;\n"
"    border-radius: 15;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(53, 53, 53);\n"
"    \n"
"    \n"
"    \n"
"}"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_1.setShortcut(_translate("MainWindow", "1"))
        self.btn_5.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
"    font: 900 15pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border:2px solid #c8c8c8;\n"
"    border-radius: 15;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(53, 53, 53);\n"
"    \n"
"    \n"
"    \n"
"}"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_5.setShortcut(_translate("MainWindow", "5"))
        self.btn_6.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
"    font: 900 15pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border:2px solid #c8c8c8;\n"
"    border-radius: 15;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(53, 53, 53);\n"
"    \n"
"    \n"
"    \n"
"}"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_6.setShortcut(_translate("MainWindow", "6"))
        self.btn_ravno.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
"    font: 900 15pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border:2px solid #c8c8c8;\n"
"    border-radius: 15;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(53, 53, 53);\n"
"    \n"
"    \n"
"    \n"
"}"))
        self.btn_ravno.setText(_translate("MainWindow", "="))
        self.btn_ravno.setShortcut(_translate("MainWindow", "="))
        self.btn_clear.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
"    font: 900 15pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border:2px solid #c8c8c8;\n"
"    border-radius: 15;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(53, 53, 53);\n"
"    \n"
"    \n"
"    \n"
"}"))
        self.btn_clear.setText(_translate("MainWindow", "C"))
        self.btn_clear_all.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
"    font: 900 15pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border:2px solid #c8c8c8;\n"
"    border-radius: 15;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(53, 53, 53);\n"
"    \n"
"    \n"
"    \n"
"}"))
        self.btn_clear_all.setText(_translate("MainWindow", "CE"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_9.setShortcut(_translate("MainWindow", "9"))
        self.btn_umojit.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
"    font: 900 15pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border:2px solid #c8c8c8;\n"
"    border-radius: 15;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(53, 53, 53);\n"
"    \n"
"    \n"
"    \n"
"}"))
        self.btn_umojit.setText(_translate("MainWindow", "*"))
        self.btn_umojit.setShortcut(_translate("MainWindow", "*"))
        self.btn_steret.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
"    font: 900 15pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border:2px solid #c8c8c8;\n"
"    border-radius: 15;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(53, 53, 53);\n"
"    \n"
"    \n"
"    \n"
"}"))
        self.btn_steret.setText(_translate("MainWindow", ">"))
        self.btn_delit.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
"    font: 900 15pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border:2px solid #c8c8c8;\n"
"    border-radius: 15;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(53, 53, 53);\n"
"    \n"
"    \n"
"    \n"
"}"))
        self.btn_delit.setText(_translate("MainWindow", "/"))
        self.btn_delit.setShortcut(_translate("MainWindow", "/"))
        self.pushButton_9.setText(_translate("MainWindow", "."))
        self.pushButton_9.setShortcut(_translate("MainWindow", "."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
