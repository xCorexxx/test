# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1062, 776)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Century Gothic;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: none;\n"
"border: 0\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.kbsh = QFrame(self.frame_3)
        self.kbsh.setObjectName(u"kbsh")
        self.kbsh.setStyleSheet(u"background-color: rgba(255,255,255,30%);\n"
"border: 1px solid rgba(255,255,255,40%);\n"
"border-radius: 7px;")
        self.kbsh.setFrameShape(QFrame.StyledPanel)
        self.kbsh.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.kbsh)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_kbsh = QFrame(self.kbsh)
        self.frame_kbsh.setObjectName(u"frame_kbsh")
        self.frame_kbsh.setStyleSheet(u"background-color: none;\n"
"border: 0\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.frame_kbsh)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.le_all = QLabel(self.frame_kbsh)
        self.le_all.setObjectName(u"le_all")
        self.le_all.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border:  none;\n"
"")

        self.verticalLayout_4.addWidget(self.le_all)

        self.all_type = QFrame(self.frame_kbsh)
        self.all_type.setObjectName(u"all_type")
        self.all_type.setStyleSheet(u"background-color: none;\n"
"border: none\n"
"")
        self.horizontalLayout = QHBoxLayout(self.all_type)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.type = QVBoxLayout()
        self.type.setObjectName(u"type")
        self.le_mulcher = QLabel(self.all_type)
        self.le_mulcher.setObjectName(u"le_mulcher")
        self.le_mulcher.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border:  none;\n"
"")

        self.type.addWidget(self.le_mulcher)

        self.le_ech = QLabel(self.all_type)
        self.le_ech.setObjectName(u"le_ech")
        self.le_ech.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border:  none;\n"
"")

        self.type.addWidget(self.le_ech)

        self.le_davs = QLabel(self.all_type)
        self.le_davs.setObjectName(u"le_davs")
        self.le_davs.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border:  none;\n"
"")

        self.type.addWidget(self.le_davs)

        self.le_pod = QLabel(self.all_type)
        self.le_pod.setObjectName(u"le_pod")
        self.le_pod.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border:  none;\n"
"")

        self.type.addWidget(self.le_pod)


        self.horizontalLayout.addLayout(self.type)

        self.plan = QVBoxLayout()
        self.plan.setObjectName(u"plan")
        self.le_plan_mulcher = QLabel(self.all_type)
        self.le_plan_mulcher.setObjectName(u"le_plan_mulcher")
        self.le_plan_mulcher.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border:  none;\n"
"")

        self.plan.addWidget(self.le_plan_mulcher)

        self.le_plan_ech = QLabel(self.all_type)
        self.le_plan_ech.setObjectName(u"le_plan_ech")
        self.le_plan_ech.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border:  none;\n"
"")

        self.plan.addWidget(self.le_plan_ech)

        self.le_plan_davs = QLabel(self.all_type)
        self.le_plan_davs.setObjectName(u"le_plan_davs")
        self.le_plan_davs.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border:  none;\n"
"")

        self.plan.addWidget(self.le_plan_davs)

        self.le_plan_pod = QLabel(self.all_type)
        self.le_plan_pod.setObjectName(u"le_plan_pod")
        self.le_plan_pod.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border:  none;\n"
"")

        self.plan.addWidget(self.le_plan_pod)


        self.horizontalLayout.addLayout(self.plan)

        self.fact = QVBoxLayout()
        self.fact.setObjectName(u"fact")
        self.le_fact_mulcher = QLabel(self.all_type)
        self.le_fact_mulcher.setObjectName(u"le_fact_mulcher")
        self.le_fact_mulcher.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border:  none;\n"
"")

        self.fact.addWidget(self.le_fact_mulcher)

        self.le_fact_ech = QLabel(self.all_type)
        self.le_fact_ech.setObjectName(u"le_fact_ech")
        self.le_fact_ech.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border:  none;\n"
"")

        self.fact.addWidget(self.le_fact_ech)

        self.le_fact_davs = QLabel(self.all_type)
        self.le_fact_davs.setObjectName(u"le_fact_davs")
        self.le_fact_davs.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border:  none;\n"
"")

        self.fact.addWidget(self.le_fact_davs)

        self.le_fact_pod = QLabel(self.all_type)
        self.le_fact_pod.setObjectName(u"le_fact_pod")
        self.le_fact_pod.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border:  none;\n"
"")

        self.fact.addWidget(self.le_fact_pod)


        self.horizontalLayout.addLayout(self.fact)


        self.verticalLayout_4.addWidget(self.all_type)


        self.verticalLayout_5.addWidget(self.frame_kbsh)


        self.horizontalLayout_2.addWidget(self.kbsh)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.btn_all = QFrame(self.frame_3)
        self.btn_all.setObjectName(u"btn_all")
        self.btn_all.setStyleSheet(u"background-color: none;\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.btn_all)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_add = QPushButton(self.btn_all)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.btn_add)

        self.btn_edit = QPushButton(self.btn_all)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.btn_edit)

        self.btn_delete = QPushButton(self.btn_all)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.btn_delete)


        self.verticalLayout_6.addWidget(self.btn_all)


        self.verticalLayout.addWidget(self.frame_3)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid  rgba(255,255,255,40);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"\n"
"QTableView::section {\n"
"background-color: rgba(53,53,53);\n"
"color: white;\n"
"borber: none;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"QTableView::item {\n"
"border-style: none;\n"
"border-bottom: rgba(255,255,255,30); \n"
"}\n"
"\n"
"QTableView::item:select {\n"
"border: none;\n"
"color: rgba(255,255,255);\n"
"background-color: rgba(255,255,255,50);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.le_all.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0411\u0428 \u041d\u0422\u042d", None))
        self.le_mulcher.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0443\u043b\u044c\u0447\u0435\u0440", None))
        self.le_ech.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043b. \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b", None))
        self.le_davs.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0410\u0412\u0421", None))
        self.le_pod.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0440\u044f\u0434\u043d\u044b\u0435 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.le_plan_mulcher.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.le_plan_ech.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.le_plan_davs.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.le_plan_pod.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.le_fact_mulcher.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.le_fact_ech.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.le_fact_davs.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.le_fact_pod.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0447\u0430\u0441\u0442\u043e\u043a", None))
        self.btn_edit.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0443\u0447\u0430\u0441\u0442\u043e\u043a", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0443\u0447\u0430\u0441\u0442\u043e\u043a", None))
    # retranslateUi

