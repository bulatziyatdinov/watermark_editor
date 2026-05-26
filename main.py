from PIL import Image, ImageQt

from PySide6.QtCore import QEvent
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

from mainwindow import Ui_MainWindow
import utils


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.main_image = None
        self.sign_image = None
        self.sign_image_copy = None
        self.result_image = None
        self.save_filepath = ''

        self.sign_image_x = 0
        self.sign_image_y = 0
        self.transparency = 0
        self.rotation_angle = 0
        self.scale = 100
        self.horizontal = False
        self.vertical = False

        self.connect_handlers()

        self.ui.btn_16x9.setVisible(False)
        self.ui.btn_4x3.setVisible(False)
        #self.ui.button_remove_bg_undo.setVisible(False)

        self.ui.button_load_sign_image.setDisabled(True)
        self.ui.line_sign_image_path.setDisabled(True)

        self.ui.button_save_image.setDisabled(True)
        self.ui.line_save_image_path.setDisabled(True)

        self.ui.line_rotation_value.setReadOnly(True)

    def connect_handlers(self):
        self.ui.line_main_image_path.installEventFilter(self)
        self.ui.line_sign_image_path.installEventFilter(self)

        self.ui.button_load_main_image.clicked.connect(self.load_main_image_btn_handler)
        self.ui.button_load_sign_image.clicked.connect(self.load_sign_image_btn_handler)

        self.ui.btn_16x9.clicked.connect(lambda x: self.set_display_size(640, 360))
        self.ui.btn_4x3.clicked.connect(lambda x: self.set_display_size(640, 480))

        self.ui.button_save_image.clicked.connect(self.button_save_image_handler)
        self.ui.line_save_image_path.installEventFilter(self)

        self.ui.button_mirror_horizontal.clicked.connect(self.button_mirror_horizontal_handler)
        self.ui.button_mirror_vertical.clicked.connect(self.button_mirror_vertical_handler)

        self.ui.button_remove_bg.clicked.connect(self.button_remove_bg_handler)
        self.ui.button_remove_bg_undo.clicked.connect(self.button_remove_bg_undo_handler)

        self.ui.slider_position_x.valueChanged.connect(self.slider_position_x_handler)
        self.ui.slider_position_y.valueChanged.connect(self.slider_position_y_handler)
        self.ui.button_position_update.clicked.connect(self.button_position_update_handler)

        self.ui.slider_transparency.valueChanged.connect(self.slider_transparency_handler)
        self.ui.button_transparency_update.clicked.connect(self.button_transparency_update_handler)
        self.ui.button_transparency_undo.clicked.connect(self.button_transparency_undo_handler)

        self.ui.slider_scale.valueChanged.connect(self.slider_scale_handler)
        self.ui.button_scale_update.clicked.connect(self.button_scale_update_handler)
        self.ui.button_scale_undo.clicked.connect(self.button_scale_undo_handler)

        self.ui.button_rotate_minus_15.clicked.connect(self.button_rotate_minus_15_handler)
        self.ui.button_rotate_plus_15.clicked.connect(self.button_rotate_plus_15_handler)
        self.ui.button_rotate_undo.clicked.connect(self.button_rotate_undo_handler)
        self.ui.button_rotation_update.clicked.connect(self.button_rotation_update_handler)

        self.ui.button_fill_update.clicked.connect(self.button_fill_update_handler)

    def eventFilter(self, obj, event):
        if obj == self.ui.line_main_image_path and event.type() == QEvent.Type.MouseButtonDblClick:
            self.choose_main_image_handler()
            return True
        if obj == self.ui.line_sign_image_path and event.type() == QEvent.Type.MouseButtonDblClick:
            self.choose_sign_image_handler()
            return True
        if obj == self.ui.line_save_image_path and event.type() == QEvent.Type.MouseButtonDblClick:
            self.choose_save_image_handler()
            return True
        return super().eventFilter(obj, event)

    def update_image_display(self):
        if self.sign_image is None:
            self.result_image = self.main_image
        else:
            sign_image_temp = self.sign_image.copy()

            sign_image_temp = sign_image_temp.convert('RGBA')
            sign_image_temp = utils.change_alpha(sign_image_temp, self.transparency)

            if self.scale != 100:
                sign_image_temp = utils.scale(sign_image_temp, self.scale / 100)

            if self.rotation_angle != 0:
                sign_image_temp = utils.rotate(sign_image_temp, self.rotation_angle)

            if self.horizontal:
                sign_image_temp = utils.mirror_horizontal(sign_image_temp)
            if self.vertical:
                sign_image_temp = utils.mirror_vertical(sign_image_temp)

            if self.ui.checkBox_fill.isChecked():
                self.result_image = utils.fill_image(self.main_image, sign_image_temp)
            else:
                self.result_image = utils.blend_images(
                    self.main_image, sign_image_temp,
                    (self.sign_image_x, self.sign_image_y))

        pixmap = QPixmap.fromImage(ImageQt.ImageQt(self.result_image))
        self.ui.label_display_image.setPixmap(pixmap)
        self.ui.label_display_image.setScaledContents(True)

    def load_main_image_btn_handler(self):
        filepath = self.ui.line_main_image_path.text()
        try:
            self.main_image = Image.open(filepath)
            self.main_image = self.main_image.convert('RGBA')

            self.ui.button_load_sign_image.setDisabled(False)
            self.ui.line_sign_image_path.setDisabled(False)

            self.ui.button_save_image.setDisabled(False)
            self.ui.line_save_image_path.setDisabled(False)

            self.update_image_display()
            self.ui.slider_position_x.setMaximum(self.main_image.width)
            self.ui.slider_position_y.setMaximum(self.main_image.height)
        except Exception as ex:
            QMessageBox.critical(
                self,
                'Ошибка',
                'Проблемы с открытием файла. Проверьте формат файла '
                'и его наличие\n' + str(ex),
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok
            )

    def load_sign_image_btn_handler(self):
        filepath = self.ui.line_sign_image_path.text()
        try:
            self.sign_image = Image.open(filepath)
            #self.sign_image = self.sign_image.convert('RGBA')
            self.sign_image_copy = self.sign_image.copy()
            self.update_image_display()
        except Exception as ex:
            QMessageBox.critical(
                self,
                'Ошибка',
                'Проблемы с открытием файла. Проверьте формат файла '
                'и его наличие\n' + str(ex),
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok
            )

    def set_display_size(self, width, height):
        self.ui.label_display_image.setMinimumSize(width, height)
        self.ui.label_display_image.setMaximumSize(width, height)

    def choose_main_image_handler(self):
        filepath, _ = QFileDialog.getOpenFileName(
            self,
            'Выберите файл',
            '',
            'Все графические файлы (*.png *.jpg *.jpeg);;'
            'Изображения PNG (*.png);;Изображения JPG (*.jpg *.jpeg);;Все файлы (*)'
        )
        if filepath:
            self.ui.line_main_image_path.setText(filepath)
            self.load_main_image_btn_handler()

    def choose_sign_image_handler(self):
        filepath, _ = QFileDialog.getOpenFileName(
            self,
            'Выберите файл',
            '',
            'Все графические файлы (*.png *.jpg *.jpeg);;'
            'Изображения PNG (*.png);;Изображения JPG (*.jpg *.jpeg);;Все файлы (*)'
        )
        if filepath:
            self.ui.line_sign_image_path.setText(filepath)
            self.load_sign_image_btn_handler()

    def choose_save_image_handler(self):
        self.save_filepath, _ = QFileDialog.getSaveFileName(
            self,
            'Выберите место сохранения файла',
            '',
            'Изображения PNG (*.png);;Изображения JPG (*.jpg *.jpeg);;Все файлы (*)'
        )
        if self.save_filepath:
            self.ui.line_save_image_path.setText(self.save_filepath)

    def button_save_image_handler(self):
        try:
            image = self.result_image.copy()
            path = self.save_filepath.lower()
            if '.jpg' in path or '.jpeg' in path:
                image = image.convert('RGB')
            image.save(path)
            QMessageBox.information(
                self,
                'Файл сохранён успешно',
                'Файл сохранён по пути:\n' + self.save_filepath,
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok
            )
        except Exception as ex:
            QMessageBox.critical(
                self,
                'Ошибка',
                'Проблемы с сохранением файла\n' + str(ex),
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok
            )

    def button_mirror_horizontal_handler(self):
        if self.sign_image is not None:
            self.horizontal = not self.horizontal
            self.update_image_display()

    def button_mirror_vertical_handler(self):
        if self.sign_image is not None:
            self.vertical = not self.vertical
            self.update_image_display()

    def button_remove_bg_handler(self):
        if self.sign_image is not None:
            self.sign_image = utils.remove_background(
                self.sign_image,
                color_area=self.ui.spinBox_remove_bg.value()
            )
            self.update_image_display()

    def button_remove_bg_undo_handler(self):
        if self.sign_image is not None:
            self.sign_image = self.sign_image_copy.copy()
            self.update_image_display()

    def button_position_update_handler(self):
        try:
            self.sign_image_x = int(self.ui.line_watermark_position_x_value.text())
            self.ui.slider_position_x.setValue(self.sign_image_x)

            self.sign_image_y = int(self.ui.line_watermark_position_y_value.text())
            self.ui.slider_position_y.setValue(self.sign_image_y)

            self.update_image_display()
        except Exception as ex:
            QMessageBox.critical(
                self,
                'Ошибка',
                'Проблемы в вводимых значениях\n' + str(ex),
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok
            )

    def slider_position_x_handler(self):
        self.ui.line_watermark_position_x_value.setText(
            str(self.ui.slider_position_x.value()) )

    def slider_position_y_handler(self):
        self.ui.line_watermark_position_y_value.setText(
            str(self.ui.slider_position_y.value()))

    def slider_transparency_handler(self):
        self.ui.line_transparency_value.setText(
            str(self.ui.slider_transparency.value()))

    def button_transparency_update_handler(self):
        if self.sign_image is not None:
            try:
                self.transparency = int(self.ui.line_transparency_value.text())
                self.ui.slider_transparency.setValue(self.transparency)
                self.update_image_display()
            except Exception:
                self.button_transparency_undo_handler()

    def button_transparency_undo_handler(self):
        if self.sign_image is not None:
            self.transparency = 0
            self.ui.line_transparency_value.setText('0')
            self.ui.slider_transparency.setValue(0)
            self.update_image_display()

    def button_rotate_minus_15_handler(self):
        if self.sign_image is not None:
            if self.rotation_angle >= -345:
                self.rotation_angle -= 15
                self.ui.line_rotation_value.setText(str(self.rotation_angle))

    def button_rotate_plus_15_handler(self):
        if self.sign_image is not None:
            if self.rotation_angle <= 345:
                self.rotation_angle += 15
                self.ui.line_rotation_value.setText(str(self.rotation_angle))

    def button_rotate_undo_handler(self):
        if self.sign_image is not None:
            self.rotation_angle = 0
            self.ui.line_rotation_value.setText(str(self.rotation_angle))

    def button_rotation_update_handler(self):
        if self.sign_image is not None:
            self.update_image_display()

    def slider_scale_handler(self):
        if self.sign_image is not None:
            self.ui.line_scale_value.setText(
                str(self.ui.slider_scale.value()))

    def button_scale_update_handler(self):
        if self.sign_image is not None:
            try:
                self.scale = int(self.ui.line_scale_value.text())
                self.scale = min(self.scale, 300)
                self.scale = max(self.scale, 25)
                self.ui.line_scale_value.setText(str(self.scale))
                self.ui.slider_scale.setValue(self.scale)
                self.update_image_display()
            except Exception as ex:
                QMessageBox.critical(
                    self,
                    'Ошибка',
                    'Проблемы в вводимых значениях\n' + str(ex),
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Ok
                )

    def button_scale_undo_handler(self):
        self.scale = 100
        self.ui.line_scale_value.setText("100")
        self.ui.slider_scale.setValue(100)

    def button_fill_update_handler(self):
        if self.sign_image is not None:
            self.update_image_display()


def main():
    app = QApplication()
    window = MainWindow()
    window.setWindowIcon(QPixmap('icon.svg'))
    window.showMaximized()
    app.exec()


if __name__ == '__main__':
    main()
