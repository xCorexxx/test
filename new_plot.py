# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new-plot.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(396, 276)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Century Gothic;")
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255,255,255,20);\n"
"border: 1px solid rgba(255,255,255,40%);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border:  none;\n"
"")

        self.verticalLayout.addWidget(self.label)

        self.data = QDateEdit(self.frame)
        self.data.setObjectName(u"data")
        self.data.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")
        self.data.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.data.setDateTime(QDateTime(QDate(2022, 12, 31), QTime(6, 0, 0)))

        self.verticalLayout.addWidget(self.data)

        self.cb_prod = QComboBox(self.frame)
        self.cb_prod.addItem("")
        self.cb_prod.addItem("")
        self.cb_prod.addItem("")
        self.cb_prod.addItem("")
        self.cb_prod.setObjectName(u"cb_prod")
        self.cb_prod.setToolTipDuration(0)
        self.cb_prod.setStyleSheet(u"QComboBox {\n"
"font-size: 16 pt;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBoxCox:item {\n"
"color: black;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.cb_prod)

        self.le_plot = QLineEdit(self.frame)
        self.le_plot.setObjectName(u"le_plot")
        self.le_plot.setStyleSheet(u"font-size: 16 pt;\n"
"color: white;\n"
"padding-left: 10 px;")

        self.verticalLayout.addWidget(self.le_plot)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.le_plot_2 = QLineEdit(self.frame)
        self.le_plot_2.setObjectName(u"le_plot_2")
        self.le_plot_2.setStyleSheet(u"font-size: 16 pt;\n"
"color: white;\n"
"padding-left: 10 px;")

        self.horizontalLayout_2.addWidget(self.le_plot_2)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border:  none;\n"
"")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_plot_3 = QLineEdit(self.frame)
        self.le_plot_3.setObjectName(u"le_plot_3")
        self.le_plot_3.setStyleSheet(u"font-size: 16 pt;\n"
"color: white;\n"
"padding-left: 10 px;")

        self.horizontalLayout_2.addWidget(self.le_plot_3)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border:  none;\n"
"")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.le_plot_4 = QLineEdit(self.frame)
        self.le_plot_4.setObjectName(u"le_plot_4")
        self.le_plot_4.setStyleSheet(u"font-size: 16 pt;\n"
"color: white;\n"
"padding-left: 10 px;")

        self.horizontalLayout_3.addWidget(self.le_plot_4)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border:  none;\n"
"")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.le_plot_5 = QLineEdit(self.frame)
        self.le_plot_5.setObjectName(u"le_plot_5")
        self.le_plot_5.setStyleSheet(u"font-size: 16 pt;\n"
"color: white;\n"
"padding-left: 10 px;")

        self.horizontalLayout_3.addWidget(self.le_plot_5)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border:  none;\n"
"")

        self.horizontalLayout_3.addWidget(self.label_5)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.le_tree_2 = QLineEdit(self.frame)
        self.le_tree_2.setObjectName(u"le_tree_2")
        self.le_tree_2.setStyleSheet(u"font-size: 16 pt;\n"
"color: white;\n"
"padding-left: 10 px;")

        self.horizontalLayout_5.addWidget(self.le_tree_2)

        self.le_tree = QLineEdit(self.frame)
        self.le_tree.setObjectName(u"le_tree")
        self.le_tree.setStyleSheet(u"font-size: 16 pt;\n"
"color: white;\n"
"padding-left: 10 px;")

        self.horizontalLayout_5.addWidget(self.le_tree)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.btn_save = QPushButton(self.frame)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid  rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,70);\n"
"}")

        self.verticalLayout.addWidget(self.btn_save)


        self.horizontalLayout_6.addLayout(self.verticalLayout)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.cb_prod.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0447\u0430\u0441\u0442\u043e\u043a", None))
        self.cb_prod.setItemText(0, QCoreApplication.translate("Dialog", u"\u041c\u0443\u043b\u044c\u0447\u0435\u0440", None))
        self.cb_prod.setItemText(1, QCoreApplication.translate("Dialog", u"\u042d\u043a\u0441\u043f. \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b", None))
        self.cb_prod.setItemText(2, QCoreApplication.translate("Dialog", u"\u0414\u0410\u0412\u0421", None))
        self.cb_prod.setItemText(3, QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434. \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f", None))

        self.cb_prod.setCurrentText("")
        self.cb_prod.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0418\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c", None))
        self.le_plot.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0423\u0447\u0430\u0441\u0442\u043e\u043a", None))
        self.le_plot_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0423\u0447\u0430\u0441\u0442\u043e\u043a", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u043a\u043c", None))
        self.le_plot_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0423\u0447\u0430\u0441\u0442\u043e\u043a", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041f\u041a", None))
        self.le_plot_4.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0423\u0447\u0430\u0441\u0442\u043e\u043a", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u043a\u043c", None))
        self.le_plot_5.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0423\u0447\u0430\u0441\u0442\u043e\u043a", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u041f\u041a", None))
        self.le_tree_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0440\u0443\u0431\u043b\u0435\u043d\u043e, \u043a\u043c", None))
        self.le_tree.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u0435\u0440\u0435\u0432\u044c\u0435\u0432", None))
        self.btn_save.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

