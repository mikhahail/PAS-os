# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_last.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 599)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 463))
        MainWindow.setMaximumSize(QtCore.QSize(915, 599))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1000, 617))
        self.centralwidget.setObjectName("centralwidget")
        self.page = QtWidgets.QTabWidget(self.centralwidget)
        self.page.setGeometry(QtCore.QRect(-10, 10, 931, 471))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(122, 162, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 53, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(155, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(129, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 162, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 162, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 53, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 53, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 162, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 53, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(155, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(129, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 162, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 162, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 53, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 53, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 162, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 53, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(155, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(129, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 162, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 162, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 53, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 53, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.page.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.page.setFont(font)
        self.page.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.page.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.page.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.page.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.page.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 53, 58);\n"
"font: 14pt \"Verdana\";\n"
"color: rgb(122, 162, 200);")
        self.page.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.page.setIconSize(QtCore.QSize(50, 16))
        self.page.setElideMode(QtCore.Qt.ElideNone)
        self.page.setUsesScrollButtons(True)
        self.page.setObjectName("page")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.label_4 = QtWidgets.QLabel(self.Home)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 841, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 16pt \"Verdana\";\n"
"color: rgb(122, 162, 200);")
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setObjectName("label_4")
        self.page.addTab(self.Home, "")
        self.DDNSp = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DDNSp.sizePolicy().hasHeightForWidth())
        self.DDNSp.setSizePolicy(sizePolicy)
        self.DDNSp.setSizeIncrement(QtCore.QSize(0, 0))
        self.DDNSp.setBaseSize(QtCore.QSize(0, 0))
        self.DDNSp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DDNSp.setObjectName("DDNSp")
        self.DDNS = QtWidgets.QCheckBox(self.DDNSp)
        self.DDNS.setGeometry(QtCore.QRect(50, 20, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DDNS.setFont(font)
        self.DDNS.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DDNS.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.DDNS.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.DDNS.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.DDNS.setObjectName("DDNS")
        self.gridLayoutWidget = QtWidgets.QWidget(self.DDNSp)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(51, 70, 831, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 4, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 1, 1, 1)
        self.drtg = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.drtg.setFont(font)
        self.drtg.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.drtg.setObjectName("drtg")
        self.gridLayout.addWidget(self.drtg, 4, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.DDNSipnet = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.DDNSipnet.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 11pt \"Verdana\";\n"
"color: rgb(122, 162, 200);\n"
"")
        self.DDNSipnet.setObjectName("DDNSipnet")
        self.gridLayout.addWidget(self.DDNSipnet, 1, 0, 1, 1)
        self.DDNSmask = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.DDNSmask.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 11pt \"Verdana\";\n"
"color: rgb(122, 162, 200);")
        self.DDNSmask.setObjectName("DDNSmask")
        self.gridLayout.addWidget(self.DDNSmask, 1, 1, 1, 1)
        self.DDNSserip = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.DDNSserip.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 11pt \"Verdana\";\n"
"color: rgb(122, 162, 200);")
        self.DDNSserip.setObjectName("DDNSserip")
        self.gridLayout.addWidget(self.DDNSserip, 1, 2, 1, 1)
        self.DDNSdoname = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.DDNSdoname.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 11pt \"Verdana\";\n"
"color: rgb(122, 162, 200);")
        self.DDNSdoname.setObjectName("DDNSdoname")
        self.gridLayout.addWidget(self.DDNSdoname, 3, 0, 1, 1)
        self.DDNSranstart = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.DDNSranstart.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 11pt \"Verdana\";\n"
"color: rgb(122, 162, 200);")
        self.DDNSranstart.setObjectName("DDNSranstart")
        self.gridLayout.addWidget(self.DDNSranstart, 3, 1, 1, 1)
        self.DDNSsername = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.DDNSsername.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 11pt \"Verdana\";\n"
"color: rgb(122, 162, 200);")
        self.DDNSsername.setObjectName("DDNSsername")
        self.gridLayout.addWidget(self.DDNSsername, 3, 2, 1, 1)
        self.DDNSranend = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.DDNSranend.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 11pt \"Verdana\";\n"
"color: rgb(122, 162, 200);")
        self.DDNSranend.setObjectName("DDNSranend")
        self.gridLayout.addWidget(self.DDNSranend, 5, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 5, 2, 1, 1)
        self.DDNSUmol = QtWidgets.QRadioButton(self.DDNSp)
        self.DDNSUmol.setGeometry(QtCore.QRect(310, 20, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DDNSUmol.setFont(font)
        self.DDNSUmol.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DDNSUmol.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.DDNSUmol.setObjectName("DDNSUmol")
        self.page.addTab(self.DDNSp, "")
        self.SSHp = QtWidgets.QWidget()
        self.SSHp.setObjectName("SSHp")
        self.SSH = QtWidgets.QCheckBox(self.SSHp)
        self.SSH.setGeometry(QtCore.QRect(50, 20, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.SSH.setFont(font)
        self.SSH.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SSH.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.SSH.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.SSH.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.SSH.setObjectName("SSH")
        self.formLayoutWidget = QtWidgets.QWidget(self.SSHp)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 120, 751, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.SSHuname = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.SSHuname.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 11pt \"Verdana\";\n"
"color: rgb(122, 162, 200);")
        self.SSHuname.setObjectName("SSHuname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.SSHuname)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.SSHuip = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.SSHuip.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 11pt \"Verdana\";\n"
"color: rgb(122, 162, 200);")
        self.SSHuip.setObjectName("SSHuip")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.SSHuip)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.SSHpass = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.SSHpass.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 11pt \"Verdana\";\n"
"color: rgb(122, 162, 200);")
        self.SSHpass.setObjectName("SSHpass")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.SSHpass)
        self.frame = QtWidgets.QFrame(self.formLayoutWidget)
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.frame)
        self.frame_2 = QtWidgets.QFrame(self.formLayoutWidget)
        self.frame_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.frame_2)
        self.label_17 = QtWidgets.QLabel(self.SSHp)
        self.label_17.setGeometry(QtCore.QRect(50, 300, 811, 131))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_17.setObjectName("label_17")
        self.page.addTab(self.SSHp, "")
        self.VPNp = QtWidgets.QWidget()
        self.VPNp.setObjectName("VPNp")
        self.VPN = QtWidgets.QCheckBox(self.VPNp)
        self.VPN.setGeometry(QtCore.QRect(50, 20, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.VPN.setFont(font)
        self.VPN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.VPN.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.VPN.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.VPN.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.VPN.setObjectName("VPN")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.VPNp)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(50, 120, 701, 171))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.VPNuname = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.VPNuname.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 11pt \"Verdana\";\n"
"color: rgb(122, 162, 200);")
        self.VPNuname.setObjectName("VPNuname")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.VPNuname)
        self.VPNuip = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.VPNuip.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 11pt \"Verdana\";\n"
"color: rgb(122, 162, 200);")
        self.VPNuip.setObjectName("VPNuip")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.VPNuip)
        self.label_21 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_21.setObjectName("label_21")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.VPNip_mask = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.VPNip_mask.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 11pt \"Verdana\";\n"
"color: rgb(122, 162, 200);")
        self.VPNip_mask.setObjectName("VPNip_mask")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.VPNip_mask)
        self.frame_3 = QtWidgets.QFrame(self.formLayoutWidget_2)
        self.frame_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.formLayoutWidget_2)
        self.frame_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.frame_4)
        self.label_19 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_19.setObjectName("label_19")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.page.addTab(self.VPNp, "")
        self.FireWallp = QtWidgets.QWidget()
        self.FireWallp.setObjectName("FireWallp")
        self.FW = QtWidgets.QCheckBox(self.FireWallp)
        self.FW.setGeometry(QtCore.QRect(50, 20, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.FW.setFont(font)
        self.FW.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FW.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.FW.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.FW.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.FW.setObjectName("FW")
        self.page.addTab(self.FireWallp, "")
        self.Otherp = QtWidgets.QWidget()
        self.Otherp.setObjectName("Otherp")
        self.label_2 = QtWidgets.QLabel(self.Otherp)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 811, 341))
        self.label_2.setObjectName("label_2")
        self.page.addTab(self.Otherp, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 60, 351, 351))
        self.pushButton_2.setStyleSheet("border-radius:175px;\n"
"background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt \"MS Sans Serif\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(50, 70, 431, 331))
        self.label_12.setObjectName("label_12")
        self.page.addTab(self.tab, "")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-30, 480, 1000, 5))
        self.line.setStyleSheet("\n"
"background-color: rgb(7, 40, 255);\n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.setting = QtWidgets.QPushButton(self.centralwidget)
        self.setting.setGeometry(QtCore.QRect(560, 520, 161, 41))
        self.setting.setStyleSheet("background-color: rgb(91, 91, 91);\n"
"color: rgb(122, 162, 200);\n"
"font: 16pt \"Verdana\";\n"
"")
        self.setting.setObjectName("setting")
        self.cancl = QtWidgets.QPushButton(self.centralwidget)
        self.cancl.setGeometry(QtCore.QRect(750, 520, 151, 41))
        self.cancl.setStyleSheet("background-color: rgb(91, 91, 91);\n"
"color: rgb(122, 162, 200);\n"
"font: 16pt \"Verdana\";\n"
"")
        self.cancl.setObjectName("cancl")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-4, 0, 921, 581))
        self.label.setStyleSheet("background-color: rgb(48, 48, 48);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 520, 481, 41))
        self.progressBar.setStyleSheet("font: 12pt \"Verdana\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-color: rgba(255, 255, 255, 0);\n"
"color: rgba(255, 255, 255, 0);\n"
"")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label.raise_()
        self.page.raise_()
        self.line.raise_()
        self.setting.raise_()
        self.cancl.raise_()
        self.progressBar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.page.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>Добро пожаловать в приложение автоматической </p><p>настройки операционной системы Панелька.</p><p>Выбирете интерисующие вас настройки и задайте</p><p>необходимые параметры.</p></body></html>"))
        self.page.setTabText(self.page.indexOf(self.Home), _translate("MainWindow", "Главная"))
        self.DDNS.setText(_translate("MainWindow", "настроить DDNS"))
        self.label_7.setText(_translate("MainWindow", "  ip адрес сервера"))
        self.label_6.setText(_translate("MainWindow", "  доменное имя"))
        self.label_9.setText(_translate("MainWindow", "  начало пула для dhcp"))
        self.drtg.setText(_translate("MainWindow", "  конец пула для dhcp"))
        self.label_8.setText(_translate("MainWindow", "  имя сервера"))
        self.label_3.setText(_translate("MainWindow", "  сеть для dhcp"))
        self.label_5.setText(_translate("MainWindow", "  маска сети"))
        self.DDNSUmol.setText(_translate("MainWindow", "Настройки по умолчанию"))
        self.page.setTabText(self.page.indexOf(self.DDNSp), _translate("MainWindow", "DDNS"))
        self.SSH.setText(_translate("MainWindow", "настроить SSH по ключам"))
        self.label_11.setText(_translate("MainWindow", "  имя пользователя"))
        self.label_15.setText(_translate("MainWindow", "  IP пользователя"))
        self.label_16.setText(_translate("MainWindow", "  пароль пользователя"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p>При настройке SSH по ключам вам необходимо будет </p><p>написать в командной строке yes/no для подключения </p><p>к клиенту или отказа от подключения сразу</p></body></html>"))
        self.page.setTabText(self.page.indexOf(self.SSHp), _translate("MainWindow", "SSH-KEY"))
        self.VPN.setText(_translate("MainWindow", "настроить Open VPN"))
        self.label_18.setText(_translate("MainWindow", "  имя пользователя"))
        self.label_21.setText(_translate("MainWindow", "  IP сети VPN"))
        self.label_19.setText(_translate("MainWindow", "  IP пользователя"))
        self.page.setTabText(self.page.indexOf(self.VPNp), _translate("MainWindow", "VPN"))
        self.FW.setText(_translate("MainWindow", "настроить Fire Wall"))
        self.page.setTabText(self.page.indexOf(self.FireWallp), _translate("MainWindow", "FIRE WALL"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Этот контент откроется после покупки платного дополнения </p><p>к нашему приложению</p></body></html>"))
        self.page.setTabText(self.page.indexOf(self.Otherp), _translate("MainWindow", "Другое"))
        self.pushButton_2.setText(_translate("MainWindow", "НЕ НАЖИМАТЬ"))
        self.label_12.setText(_translate("MainWindow", "Кнопка для сброса всех настроек"))
        self.page.setTabText(self.page.indexOf(self.tab), _translate("MainWindow", "Удалить"))
        self.setting.setText(_translate("MainWindow", "Настроить"))
        self.cancl.setText(_translate("MainWindow", "Отмена"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
