# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rps.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 599)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setWindowTitle("Janken V1.0")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/doraanak.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setAccessibleName("")
        MainWindow.setAccessibleDescription("")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Indonesian, QtCore.QLocale.Indonesia))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget.setToolTip("")
        self.centralwidget.setStatusTip("")
        self.centralwidget.setWhatsThis("")
        self.centralwidget.setAccessibleName("")
        self.centralwidget.setAccessibleDescription("")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 481, 571))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.frame.setToolTip("")
        self.frame.setStatusTip("")
        self.frame.setWhatsThis("")
        self.frame.setAccessibleName("")
        self.frame.setAccessibleDescription("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 90, 461, 151))
        font = QtGui.QFont()
        font.setFamily("AG Foreigner-Roman")
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.splitter = QtWidgets.QSplitter(self.groupBox)
        self.splitter.setGeometry(QtCore.QRect(10, 30, 441, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.splitter.setToolTip("")
        self.splitter.setStatusTip("")
        self.splitter.setWhatsThis("")
        self.splitter.setAccessibleName("")
        self.splitter.setAccessibleDescription("")
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(4)
        self.splitter.setObjectName("splitter")
        self.rock_btn = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rock_btn.sizePolicy().hasHeightForWidth())
        self.rock_btn.setSizePolicy(sizePolicy)
        self.rock_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rock_btn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.rock_btn.setToolTip("")
        self.rock_btn.setStatusTip("")
        self.rock_btn.setWhatsThis("")
        self.rock_btn.setAccessibleName("")
        self.rock_btn.setAccessibleDescription("")
        self.rock_btn.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"image: url(:/rock.png);\n"
"border-color: rgb(98, 160, 234);")
        self.rock_btn.setText("")
        self.rock_btn.setAutoDefault(True)
        self.rock_btn.setFlat(False)
        self.rock_btn.setObjectName("rock_btn")
        self.scissors_btn = QtWidgets.QPushButton(self.splitter)
        self.scissors_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scissors_btn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.scissors_btn.setToolTip("")
        self.scissors_btn.setStatusTip("")
        self.scissors_btn.setWhatsThis("")
        self.scissors_btn.setAccessibleName("")
        self.scissors_btn.setAccessibleDescription("")
        self.scissors_btn.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"image: url(:/scissors.png);\n"
"border-color: rgb(98, 160, 234);")
        self.scissors_btn.setText("")
        self.scissors_btn.setAutoDefault(True)
        self.scissors_btn.setFlat(False)
        self.scissors_btn.setObjectName("scissors_btn")
        self.paper_btn = QtWidgets.QPushButton(self.splitter)
        self.paper_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.paper_btn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.paper_btn.setToolTip("")
        self.paper_btn.setStatusTip("")
        self.paper_btn.setWhatsThis("")
        self.paper_btn.setAccessibleName("")
        self.paper_btn.setAccessibleDescription("")
        self.paper_btn.setAutoFillBackground(False)
        self.paper_btn.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"image: url(:/paper.png);\n"
"border-color: rgb(98, 160, 234);")
        self.paper_btn.setText("")
        self.paper_btn.setAutoDefault(True)
        self.paper_btn.setFlat(False)
        self.paper_btn.setObjectName("paper_btn")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setGeometry(QtCore.QRect(10, 0, 461, 81))
        self.graphicsView.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.graphicsView.setStyleSheet("border-color: rgb(119, 118, 123);\n"
"background-color: rgb(222, 221, 218);")
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setObjectName("graphicsView")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 250, 461, 181))
        font = QtGui.QFont()
        font.setFamily("AG Foreigner-Roman")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.groupBox_2.setObjectName("groupBox_2")
        self.chosen_icon_lbl = QtWidgets.QLabel(self.groupBox_2)
        self.chosen_icon_lbl.setGeometry(QtCore.QRect(10, 90, 81, 81))
        self.chosen_icon_lbl.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.chosen_icon_lbl.setToolTip("")
        self.chosen_icon_lbl.setStatusTip("")
        self.chosen_icon_lbl.setWhatsThis("")
        self.chosen_icon_lbl.setAccessibleName("")
        self.chosen_icon_lbl.setAccessibleDescription("")
        self.chosen_icon_lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chosen_icon_lbl.setFrameShadow(QtWidgets.QFrame.Plain)
        self.chosen_icon_lbl.setText("")
        self.chosen_icon_lbl.setScaledContents(True)
        self.chosen_icon_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.chosen_icon_lbl.setObjectName("chosen_icon_lbl")
        self.chosen_text_lbl = QtWidgets.QLabel(self.groupBox_2)
        self.chosen_text_lbl.setGeometry(QtCore.QRect(240, 30, 211, 141))
        font = QtGui.QFont()
        font.setFamily("Cabin")
        font.setPointSize(14)
        self.chosen_text_lbl.setFont(font)
        self.chosen_text_lbl.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.chosen_text_lbl.setToolTip("")
        self.chosen_text_lbl.setStatusTip("")
        self.chosen_text_lbl.setWhatsThis("")
        self.chosen_text_lbl.setAccessibleName("")
        self.chosen_text_lbl.setAccessibleDescription("")
        self.chosen_text_lbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chosen_text_lbl.setText("")
        self.chosen_text_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.chosen_text_lbl.setWordWrap(True)
        self.chosen_text_lbl.setObjectName("chosen_text_lbl")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.groupBox_2)
        self.graphicsView_3.setGeometry(QtCore.QRect(90, 80, 61, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_3.sizePolicy().hasHeightForWidth())
        self.graphicsView_3.setSizePolicy(sizePolicy)
        self.graphicsView_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.graphicsView_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.graphicsView_3.setToolTip("")
        self.graphicsView_3.setStatusTip("")
        self.graphicsView_3.setWhatsThis("")
        self.graphicsView_3.setAccessibleName("")
        self.graphicsView_3.setAccessibleDescription("")
        self.graphicsView_3.setStyleSheet("background-image: url(:/vs.png);")
        self.graphicsView_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.graphicsView_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_3.setRenderHints(QtGui.QPainter.TextAntialiasing)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.begin_btn = QtWidgets.QPushButton(self.frame)
        self.begin_btn.setGeometry(QtCore.QRect(40, 480, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Anna")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.begin_btn.setFont(font)
        self.begin_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.begin_btn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.begin_btn.setToolTip("")
        self.begin_btn.setStatusTip("")
        self.begin_btn.setWhatsThis("")
        self.begin_btn.setAccessibleName("")
        self.begin_btn.setAccessibleDescription("")
        self.begin_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.begin_btn.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"background-color: rgb(98, 160, 234);\n"
"background-color: rgb(87, 227, 137);\n"
"background-color: rgb(248, 228, 92);\n"
"border-color: rgb(46, 194, 126);\n"
"color: rgb(0, 0, 0);")
        self.begin_btn.setLocale(QtCore.QLocale(QtCore.QLocale.Indonesian, QtCore.QLocale.Indonesia))
        self.begin_btn.setAutoDefault(False)
        self.begin_btn.setObjectName("begin_btn")
        self.result_icon_1_lbl = QtWidgets.QLabel(self.groupBox_2)
        self.result_icon_1_lbl.setGeometry(QtCore.QRect(130, 30, 80, 80))
        self.result_icon_1_lbl.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.result_icon_1_lbl.setText("")
        self.result_icon_1_lbl.setScaledContents(True)
        self.result_icon_1_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.result_icon_1_lbl.setObjectName("result_icon_1_lbl")
        self.result_icon_2_lbl = QtWidgets.QLabel(self.groupBox_2)
        self.result_icon_2_lbl.setGeometry(QtCore.QRect(220, 30, 80, 80))
        self.result_icon_2_lbl.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.result_icon_2_lbl.setText("")
        self.result_icon_2_lbl.setScaledContents(True)
        self.result_icon_2_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.result_icon_2_lbl.setObjectName("result_icon_2_lbl")
        self.result_icon_3_lbl = QtWidgets.QLabel(self.groupBox_2)
        self.result_icon_3_lbl.setGeometry(QtCore.QRect(310, 30, 80, 80))
        self.result_icon_3_lbl.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.result_icon_3_lbl.setText("")
        self.result_icon_3_lbl.setScaledContents(True)
        self.result_icon_3_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.result_icon_3_lbl.setObjectName("result_icon_3_lbl")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_2.setGeometry(QtCore.QRect(60, 0, 81, 81))
        self.graphicsView_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.graphicsView_2.setStyleSheet("background-image: url(:/doraanak.png);\n"
"\n"
"")
        self.graphicsView_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(110, 10, 361, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Futura Bk BT")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_3.setToolTip("")
        self.label_3.setStatusTip("")
        self.label_3.setWhatsThis("")
        self.label_3.setAccessibleName("")
        self.label_3.setAccessibleDescription("")
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("color: rgb(38, 162, 105);")
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(240, 40, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label.setToolTip("")
        self.label.setStatusTip("")
        self.label.setWhatsThis("")
        self.label.setAccessibleName("")
        self.label.setAccessibleDescription("")
        self.label.setStyleSheet("color: rgb(28, 113, 216);")
        self.label.setLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 476, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.menubar.setToolTip("")
        self.menubar.setStatusTip("")
        self.menubar.setWhatsThis("")
        self.menubar.setAccessibleName("")
        self.menubar.setAccessibleDescription("")
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.statusbar.setToolTip("")
        self.statusbar.setStatusTip("")
        self.statusbar.setWhatsThis("")
        self.statusbar.setAccessibleName("")
        self.statusbar.setAccessibleDescription("")
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setObjectName("action_About")

        self.retranslateUi(MainWindow)
        self.rock_btn.clicked.connect(self.chosen_icon_lbl.clear) # type: ignore
        self.scissors_btn.clicked.connect(self.chosen_icon_lbl.clear) # type: ignore
        self.paper_btn.clicked.connect(self.chosen_icon_lbl.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("MainWindow", "Batu, Gunting, Kertas"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Hasil"))
        self.begin_btn.setText(_translate("MainWindow", "Mulai"))
        self.label_3.setText(_translate("MainWindow", "MahaKurawa.My.ID"))
        self.label.setText(_translate("MainWindow", "Janken"))
        self.action_About.setText(_translate("MainWindow", "&About"))
import rpsimages_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())