# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Jorge\Desktop\xtracursos\howtoPywinauto\02-creatingTheUi\creatingTheUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainWIn = QtWidgets.QFrame(self.centralwidget)
        self.mainWIn.setGeometry(QtCore.QRect(20, 30, 761, 511))
        self.mainWIn.setStyleSheet("background-color: rgb(188, 176, 183); \n"
"border-radius:15px;")
        self.mainWIn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainWIn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainWIn.setObjectName("mainWIn")
        self.titleBar = QtWidgets.QFrame(self.mainWIn)
        self.titleBar.setGeometry(QtCore.QRect(0, 0, 761, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.titleBar.setFont(font)
        self.titleBar.setStyleSheet("background-color: rgb(232, 232, 232);\n"
"")
        self.titleBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.titleBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titleBar.setObjectName("titleBar")
        self.closeBtn = QtWidgets.QPushButton(self.titleBar)
        self.closeBtn.setGeometry(QtCore.QRect(733, 10, 16, 16))
        self.closeBtn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 59, 41);\n"
"    border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(197, 37, 37);\n"
"    border-radius:8px;\n"
"}")
        self.closeBtn.setText("")
        self.closeBtn.setObjectName("closeBtn")
        self.minBtn = QtWidgets.QPushButton(self.titleBar)
        self.minBtn.setGeometry(QtCore.QRect(709, 10, 16, 16))
        self.minBtn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 220, 17);\n"
"    border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(212, 182, 28);\n"
"    border-radius:8px;\n"
"}")
        self.minBtn.setText("")
        self.minBtn.setObjectName("minBtn")
        self.appName = QtWidgets.QLabel(self.titleBar)
        self.appName.setGeometry(QtCore.QRect(20, 0, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.appName.setFont(font)
        self.appName.setObjectName("appName")
        self.tableWidget = QtWidgets.QTableWidget(self.mainWIn)
        self.tableWidget.setGeometry(QtCore.QRect(30, 70, 701, 401))
        self.tableWidget.setStyleSheet("background-color:rgb(204, 204, 204);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.saveBtn = QtWidgets.QPushButton(self.mainWIn)
        self.saveBtn.setGeometry(QtCore.QRect(654, 480, 61, 23))
        self.saveBtn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(85,255,127);\n"
"    border-radius: 11px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(66,198,97);\n"
"    border-radius: 11px;\n"
"}")
        self.saveBtn.setObjectName("saveBtn")
        self.addBtn = QtWidgets.QPushButton(self.mainWIn)
        self.addBtn.setGeometry(QtCore.QRect(530, 480, 111, 23))
        self.addBtn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(85,255,127);\n"
"    border-radius: 11px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(66,198,97);\n"
"    border-radius: 11px;\n"
"}")
        self.addBtn.setObjectName("addBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.appName.setText(_translate("MainWindow", "ZoomBot"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Password"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Date and Time"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "No Audio"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "No Video"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Delete"))
        self.saveBtn.setText(_translate("MainWindow", "Save"))
        self.addBtn.setText(_translate("MainWindow", "Add New Meeting"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())