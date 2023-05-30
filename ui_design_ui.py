# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_design.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_PasswordGeneratorWindow(object):
    def setupUi(self, PasswordGeneratorWindow):
        if not PasswordGeneratorWindow.objectName():
            PasswordGeneratorWindow.setObjectName(u"PasswordGeneratorWindow")
        PasswordGeneratorWindow.resize(800, 266)
        PasswordGeneratorWindow.setMinimumSize(QSize(800, 266))
        PasswordGeneratorWindow.setMaximumSize(QSize(800, 266))
        self.mainWidget = QWidget(PasswordGeneratorWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        self.verticalLayout = QVBoxLayout(self.mainWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QFrame(self.mainWidget)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setStyleSheet(u"QFrame {\n"
"	color: #CFDBD5;\n"
"	background-color: #333533\n"
"}")
        self.headerFrame.setFrameShape(QFrame.NoFrame)
        self.headerFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.headerFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.headerLbl = QLabel(self.headerFrame)
        self.headerLbl.setObjectName(u"headerLbl")
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(24)
        font.setBold(True)
        self.headerLbl.setFont(font)

        self.verticalLayout_2.addWidget(self.headerLbl)


        self.verticalLayout.addWidget(self.headerFrame)

        self.generatorFrame = QFrame(self.mainWidget)
        self.generatorFrame.setObjectName(u"generatorFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generatorFrame.sizePolicy().hasHeightForWidth())
        self.generatorFrame.setSizePolicy(sizePolicy)
        self.generatorFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #242423;\n"
"	color: #E8EDDF\n"
"}\n"
"QPushButton {\n"
"	background-color: #F5CB5C;\n"
"	color: black;\n"
"	border-radius: 12px\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #333533;\n"
"	color: white;\n"
"}\n"
"QLineEdit {\n"
"	background-color: #E8EDDF;\n"
"	color: #242423;\n"
"	border-radius: 12px;\n"
"}\n"
"")
        self.generatorFrame.setFrameShape(QFrame.NoFrame)
        self.generatorFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.generatorFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.generateLineEdit = QLineEdit(self.generatorFrame)
        self.generateLineEdit.setObjectName(u"generateLineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.generateLineEdit.sizePolicy().hasHeightForWidth())
        self.generateLineEdit.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.generateLineEdit.setFont(font1)
        self.generateLineEdit.setCursor(QCursor(Qt.ArrowCursor))
        self.generateLineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.generateLineEdit)

        self.btnsFrame = QFrame(self.generatorFrame)
        self.btnsFrame.setObjectName(u"btnsFrame")
        self.btnsFrame.setFrameShape(QFrame.NoFrame)
        self.btnsFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.btnsFrame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.generateBtn = QPushButton(self.btnsFrame)
        self.generateBtn.setObjectName(u"generateBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.generateBtn.sizePolicy().hasHeightForWidth())
        self.generateBtn.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Inter"])
        font2.setPointSize(18)
        self.generateBtn.setFont(font2)
        self.generateBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.generateBtn)

        self.copyBtn = QPushButton(self.btnsFrame)
        self.copyBtn.setObjectName(u"copyBtn")
        sizePolicy2.setHeightForWidth(self.copyBtn.sizePolicy().hasHeightForWidth())
        self.copyBtn.setSizePolicy(sizePolicy2)
        self.copyBtn.setFont(font2)
        self.copyBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.copyBtn)


        self.verticalLayout_3.addWidget(self.btnsFrame)

        self.disclaimerLbl = QLabel(self.generatorFrame)
        self.disclaimerLbl.setObjectName(u"disclaimerLbl")
        font3 = QFont()
        font3.setFamilies([u"Inter"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.disclaimerLbl.setFont(font3)
        self.disclaimerLbl.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.disclaimerLbl)


        self.verticalLayout.addWidget(self.generatorFrame)

        PasswordGeneratorWindow.setCentralWidget(self.mainWidget)

        self.retranslateUi(PasswordGeneratorWindow)

        QMetaObject.connectSlotsByName(PasswordGeneratorWindow)
    # setupUi

    def retranslateUi(self, PasswordGeneratorWindow):
        PasswordGeneratorWindow.setWindowTitle(QCoreApplication.translate("PasswordGeneratorWindow", u"Password Generator", None))
        self.headerLbl.setText(QCoreApplication.translate("PasswordGeneratorWindow", u"Password Generator", None))
        self.generateBtn.setText(QCoreApplication.translate("PasswordGeneratorWindow", u"GENERATE", None))
        self.copyBtn.setText(QCoreApplication.translate("PasswordGeneratorWindow", u"COPY TO CLIPBOARD", None))
        self.disclaimerLbl.setText(QCoreApplication.translate("PasswordGeneratorWindow", u"For educational purposes only, it uses the secrets module to manage a basic level of security for generating passwords and hashing passwords.", None))
    # retranslateUi

