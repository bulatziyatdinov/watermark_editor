# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1333, 1200)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	padding: 10 12;\n"
"	border-radius: 5px;\n"
"	font: 500, 14px, \"Montserrat\";\n"
"}\n"
"\n"
"QPushButton:Hover {\n"
"	background-color: lightblue;\n"
"}\n"
"\n"
"QPushButton:Pressed {\n"
"	background-color: yellow;\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 600, 14px, \"Montserrat\";\n"
"}\n"
"\n"
"QCheckBox {\n"
"	font: 500, 14px, \"Montserrat\";\n"
"}")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, -1, -1, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_load_main_image = QPushButton(self.centralwidget)
        self.button_load_main_image.setObjectName(u"button_load_main_image")

        self.gridLayout.addWidget(self.button_load_main_image, 1, 1, 1, 1)

        self.line_sign_image_path = QLineEdit(self.centralwidget)
        self.line_sign_image_path.setObjectName(u"line_sign_image_path")

        self.gridLayout.addWidget(self.line_sign_image_path, 2, 0, 1, 1)

        self.line_main_image_path = QLineEdit(self.centralwidget)
        self.line_main_image_path.setObjectName(u"line_main_image_path")

        self.gridLayout.addWidget(self.line_main_image_path, 1, 0, 1, 1)

        self.button_load_sign_image = QPushButton(self.centralwidget)
        self.button_load_sign_image.setObjectName(u"button_load_sign_image")

        self.gridLayout.addWidget(self.button_load_sign_image, 2, 1, 1, 1)

        self.label_images = QLabel(self.centralwidget)
        self.label_images.setObjectName(u"label_images")
        self.label_images.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label_images, 0, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.slider_position_x = QSlider(self.centralwidget)
        self.slider_position_x.setObjectName(u"slider_position_x")
        self.slider_position_x.setMaximum(100)
        self.slider_position_x.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.slider_position_x, 3, 1, 1, 1)

        self.line_watermark_position_x_value = QLineEdit(self.centralwidget)
        self.line_watermark_position_x_value.setObjectName(u"line_watermark_position_x_value")
        self.line_watermark_position_x_value.setMaximumSize(QSize(60, 20))
        self.line_watermark_position_x_value.setInputMask(u"")
        self.line_watermark_position_x_value.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.line_watermark_position_x_value, 3, 3, 1, 1)

        self.label_watermark_position_axis_y = QLabel(self.centralwidget)
        self.label_watermark_position_axis_y.setObjectName(u"label_watermark_position_axis_y")

        self.gridLayout_2.addWidget(self.label_watermark_position_axis_y, 4, 0, 1, 1)

        self.label_watermark_position_axis_x = QLabel(self.centralwidget)
        self.label_watermark_position_axis_x.setObjectName(u"label_watermark_position_axis_x")

        self.gridLayout_2.addWidget(self.label_watermark_position_axis_x, 3, 0, 1, 1)

        self.slider_position_y = QSlider(self.centralwidget)
        self.slider_position_y.setObjectName(u"slider_position_y")
        self.slider_position_y.setMaximum(100)
        self.slider_position_y.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.slider_position_y, 4, 1, 1, 1)

        self.label_watermark_position = QLabel(self.centralwidget)
        self.label_watermark_position.setObjectName(u"label_watermark_position")
        self.label_watermark_position.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.label_watermark_position, 2, 0, 1, 4)

        self.button_position_update = QPushButton(self.centralwidget)
        self.button_position_update.setObjectName(u"button_position_update")

        self.gridLayout_2.addWidget(self.button_position_update, 6, 0, 1, 2)

        self.line_watermark_position_y_value = QLineEdit(self.centralwidget)
        self.line_watermark_position_y_value.setObjectName(u"line_watermark_position_y_value")
        self.line_watermark_position_y_value.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_2.addWidget(self.line_watermark_position_y_value, 4, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(25, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 3, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_mirror = QLabel(self.centralwidget)
        self.label_mirror.setObjectName(u"label_mirror")
        self.label_mirror.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_3.addWidget(self.label_mirror, 14, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.button_transparency_update = QPushButton(self.centralwidget)
        self.button_transparency_update.setObjectName(u"button_transparency_update")

        self.horizontalLayout_5.addWidget(self.button_transparency_update)

        self.button_transparency_undo = QPushButton(self.centralwidget)
        self.button_transparency_undo.setObjectName(u"button_transparency_undo")

        self.horizontalLayout_5.addWidget(self.button_transparency_undo)


        self.gridLayout_3.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)

        self.line_rotation_value = QLineEdit(self.centralwidget)
        self.line_rotation_value.setObjectName(u"line_rotation_value")
        self.line_rotation_value.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_3.addWidget(self.line_rotation_value, 12, 2, 1, 1)

        self.spacer2 = QLabel(self.centralwidget)
        self.spacer2.setObjectName(u"spacer2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.spacer2.sizePolicy().hasHeightForWidth())
        self.spacer2.setSizePolicy(sizePolicy1)
        self.spacer2.setMinimumSize(QSize(60, 0))

        self.gridLayout_3.addWidget(self.spacer2, 21, 2, 1, 1)

        self.line_scale_value = QLineEdit(self.centralwidget)
        self.line_scale_value.setObjectName(u"line_scale_value")
        self.line_scale_value.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_3.addWidget(self.line_scale_value, 9, 2, 1, 1)

        self.slider_scale = QSlider(self.centralwidget)
        self.slider_scale.setObjectName(u"slider_scale")
        self.slider_scale.setMinimum(25)
        self.slider_scale.setMaximum(300)
        self.slider_scale.setSingleStep(25)
        self.slider_scale.setValue(100)
        self.slider_scale.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.slider_scale, 9, 0, 1, 1)

        self.slider_transparency = QSlider(self.centralwidget)
        self.slider_transparency.setObjectName(u"slider_transparency")
        self.slider_transparency.setMaximum(100)
        self.slider_transparency.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.slider_transparency, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_rotate_minus_15 = QPushButton(self.centralwidget)
        self.button_rotate_minus_15.setObjectName(u"button_rotate_minus_15")

        self.horizontalLayout.addWidget(self.button_rotate_minus_15)

        self.button_rotate_undo = QPushButton(self.centralwidget)
        self.button_rotate_undo.setObjectName(u"button_rotate_undo")

        self.horizontalLayout.addWidget(self.button_rotate_undo)

        self.button_rotate_plus_15 = QPushButton(self.centralwidget)
        self.button_rotate_plus_15.setObjectName(u"button_rotate_plus_15")

        self.horizontalLayout.addWidget(self.button_rotate_plus_15)


        self.gridLayout_3.addLayout(self.horizontalLayout, 12, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.button_scale_update = QPushButton(self.centralwidget)
        self.button_scale_update.setObjectName(u"button_scale_update")

        self.horizontalLayout_7.addWidget(self.button_scale_update)

        self.button_scale_undo = QPushButton(self.centralwidget)
        self.button_scale_undo.setObjectName(u"button_scale_undo")

        self.horizontalLayout_7.addWidget(self.button_scale_undo)


        self.gridLayout_3.addLayout(self.horizontalLayout_7, 10, 0, 1, 1)

        self.line_save_image_path = QLineEdit(self.centralwidget)
        self.line_save_image_path.setObjectName(u"line_save_image_path")

        self.gridLayout_3.addWidget(self.line_save_image_path, 22, 0, 1, 1)

        self.button_rotation_update = QPushButton(self.centralwidget)
        self.button_rotation_update.setObjectName(u"button_rotation_update")

        self.gridLayout_3.addWidget(self.button_rotation_update, 13, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 20, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_mirror_horizontal = QPushButton(self.centralwidget)
        self.button_mirror_horizontal.setObjectName(u"button_mirror_horizontal")

        self.horizontalLayout_2.addWidget(self.button_mirror_horizontal)

        self.button_mirror_vertical = QPushButton(self.centralwidget)
        self.button_mirror_vertical.setObjectName(u"button_mirror_vertical")

        self.horizontalLayout_2.addWidget(self.button_mirror_vertical)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 15, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_special = QLabel(self.centralwidget)
        self.label_special.setObjectName(u"label_special")

        self.verticalLayout_6.addWidget(self.label_special)

        self.checkBox_fill = QCheckBox(self.centralwidget)
        self.checkBox_fill.setObjectName(u"checkBox_fill")

        self.verticalLayout_6.addWidget(self.checkBox_fill)

        self.button_fill_update = QPushButton(self.centralwidget)
        self.button_fill_update.setObjectName(u"button_fill_update")

        self.verticalLayout_6.addWidget(self.button_fill_update)


        self.gridLayout_3.addLayout(self.verticalLayout_6, 18, 0, 1, 1)

        self.line_transparency_value = QLineEdit(self.centralwidget)
        self.line_transparency_value.setObjectName(u"line_transparency_value")
        self.line_transparency_value.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_3.addWidget(self.line_transparency_value, 3, 2, 1, 1)

        self.label_transparency = QLabel(self.centralwidget)
        self.label_transparency.setObjectName(u"label_transparency")
        self.label_transparency.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_3.addWidget(self.label_transparency, 2, 0, 1, 3)

        self.label_save_result = QLabel(self.centralwidget)
        self.label_save_result.setObjectName(u"label_save_result")
        self.label_save_result.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_3.addWidget(self.label_save_result, 21, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 18, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 3, 1, 1, 1)

        self.button_save_image = QPushButton(self.centralwidget)
        self.button_save_image.setObjectName(u"button_save_image")

        self.gridLayout_3.addWidget(self.button_save_image, 22, 1, 1, 2)

        self.label_delete_bg = QLabel(self.centralwidget)
        self.label_delete_bg.setObjectName(u"label_delete_bg")
        self.label_delete_bg.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_3.addWidget(self.label_delete_bg, 0, 0, 1, 1)

        self.label_scale = QLabel(self.centralwidget)
        self.label_scale.setObjectName(u"label_scale")
        self.label_scale.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_3.addWidget(self.label_scale, 7, 0, 1, 1)

        self.label_rotation = QLabel(self.centralwidget)
        self.label_rotation.setObjectName(u"label_rotation")
        self.label_rotation.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_3.addWidget(self.label_rotation, 11, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_remove_bg = QPushButton(self.centralwidget)
        self.button_remove_bg.setObjectName(u"button_remove_bg")

        self.horizontalLayout_3.addWidget(self.button_remove_bg)

        self.button_remove_bg_undo = QPushButton(self.centralwidget)
        self.button_remove_bg_undo.setObjectName(u"button_remove_bg_undo")

        self.horizontalLayout_3.addWidget(self.button_remove_bg_undo)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 2, 1, 1)

        self.spinBox_remove_bg = QSpinBox(self.centralwidget)
        self.spinBox_remove_bg.setObjectName(u"spinBox_remove_bg")
        self.spinBox_remove_bg.setMaximum(50)

        self.gridLayout_3.addWidget(self.spinBox_remove_bg, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)


        self.gridLayout_6.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 1, 1, 1, 1)

        self.label_display_image = QLabel(self.centralwidget)
        self.label_display_image.setObjectName(u"label_display_image")
        self.label_display_image.setMinimumSize(QSize(854, 480))
        self.label_display_image.setMaximumSize(QSize(854, 480))
        self.label_display_image.setStyleSheet(u"QLabel {\n"
"background-color: white;\n"
"border: 2px solid grey;\n"
"}")

        self.gridLayout_6.addWidget(self.label_display_image, 1, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 1, 4, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(100)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_16x9 = QPushButton(self.centralwidget)
        self.btn_16x9.setObjectName(u"btn_16x9")

        self.horizontalLayout_4.addWidget(self.btn_16x9)

        self.btn_4x3 = QPushButton(self.centralwidget)
        self.btn_4x3.setObjectName(u"btn_4x3")

        self.horizontalLayout_4.addWidget(self.btn_4x3)


        self.gridLayout_6.addLayout(self.horizontalLayout_4, 0, 3, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1333, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0441 \u0432\u043e\u0434\u044f\u043d\u044b\u043c \u0437\u043d\u0430\u043a\u043e\u043c", None))
        self.button_load_main_image.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.line_sign_image_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0432\u043e\u0434\u044f\u043d\u043e\u0433\u043e \u0437\u043d\u0430\u043a\u0430", None))
        self.line_main_image_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.button_load_sign_image.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.label_images.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439", None))
        self.line_watermark_position_x_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_watermark_position_axis_y.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u044c \u0423", None))
        self.label_watermark_position_axis_x.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u044c \u0425", None))
        self.label_watermark_position.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0432\u043e\u0434\u044f\u043d\u043e\u0433\u043e \u0437\u043d\u0430\u043a\u0430", None))
        self.button_position_update.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.line_watermark_position_y_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_mirror.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0432\u043e\u0434\u044f\u043d\u043e\u0433\u043e \u0437\u043d\u0430\u043a", None))
        self.button_transparency_update.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.button_transparency_undo.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441", None))
        self.line_rotation_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.spacer2.setText("")
        self.line_scale_value.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.button_rotate_minus_15.setText(QCoreApplication.translate("MainWindow", u"-15", None))
        self.button_rotate_undo.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441", None))
        self.button_rotate_plus_15.setText(QCoreApplication.translate("MainWindow", u"+15", None))
        self.button_scale_update.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.button_scale_undo.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441", None))
        self.line_save_image_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f", None))
        self.button_rotation_update.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.button_mirror_horizontal.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0433\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u0438", None))
        self.button_mirror_vertical.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u0438", None))
        self.label_special.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043e\u0431\u043e\u0435", None))
        self.checkBox_fill.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0432\u043e\u0434\u044f\u043d\u044b\u043c \u0437\u043d\u0430\u043a\u043e\u043c", None))
        self.button_fill_update.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.line_transparency_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_transparency.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u043e\u0441\u0442\u044c \u0432\u043e\u0434\u044f\u043d\u043e\u0433\u043e \u0437\u043d\u0430\u043a\u0430", None))
        self.label_save_result.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0430", None))
        self.button_save_image.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_delete_bg.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0441 \u0432\u043e\u0434\u044f\u043d\u043e\u0433\u043e \u0437\u043d\u0430\u043a\u0430", None))
        self.label_scale.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u0448\u0442\u0430\u0431 \u0432\u043e\u0434\u044f\u043d\u043e\u0433\u043e \u0437\u043d\u0430\u043a\u0430", None))
        self.label_rotation.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0430\u0449\u0435\u043d\u0438\u0435 \u0432\u043e\u0434\u044f\u043d\u043e\u0433\u043e \u0437\u043d\u0430\u043a\u0430 (\u0432 \u0433\u0440\u0430\u0434\u0443\u0441\u0430\u0445)", None))
        self.button_remove_bg.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0446\u0432\u0435\u0442", None))
        self.button_remove_bg_undo.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c \u0446\u0432\u0435\u0442", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0430\u0445", None))
        self.label_display_image.setText("")
        self.btn_16x9.setText(QCoreApplication.translate("MainWindow", u"16x9", None))
        self.btn_4x3.setText(QCoreApplication.translate("MainWindow", u"4x3", None))
    # retranslateUi

