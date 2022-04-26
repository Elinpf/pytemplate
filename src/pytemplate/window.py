import sys
from PyQt5 import QtWidgets
from pytemplate.gui.generate import Ui_Form
from pytemplate.main import load_template, ExcelDataGenerator, write_template


class PyTemplateWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(PyTemplateWindow, self).__init__()
        self.setupUi(self)
        QtWidgets.QApplication.setStyle('Fusion')

        self.toolButton_template.clicked.connect(self.get_file)
        self.toolButton_data.clicked.connect(self.get_file)
        self.toolButton_output.clicked.connect(self.get_directory)
        self.pushButton_generate.clicked.connect(self.generate)
        self.pushButton_exit.clicked.connect(self.close)

    def get_file(self):
        obj = self.sender().objectName().split('_')[-1]
        f_name = QtWidgets.QFileDialog.getOpenFileName()
        getattr(self, 'lineEdit_' + obj).setText(f_name[0])

    def get_directory(self):
        obj = self.sender().objectName().split('_')[-1]
        f_name = QtWidgets.QFileDialog.getExistingDirectory()
        getattr(self, 'lineEdit_' + obj).setText(f_name)

    def generate(self):
        template_file = self.lineEdit_template.text()
        data_file = self.lineEdit_data.text()
        output_directory = self.lineEdit_output.text()

        if not (template_file and data_file and output_directory):
            QtWidgets.QMessageBox.warning(self, '警告', '请选择文件')
            return

        try:
            g = ExcelDataGenerator()
            g.load(data_file)
            template_str = load_template(template_file)

            for ds, info in g.data:
                write_template(
                    template_str, '{}/{}.txt'.format(output_directory, ds), info)

        except KeyError as e:
            QtWidgets.QMessageBox.critical(self, '错误', f'模板中变量不存在：{e}')
            return

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, '错误', '生成失败：{}'.format(e))
            return

        QtWidgets.QMessageBox.information(self, '提示', '生成完成')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = PyTemplateWindow()
    win.show()
    sys.exit(app.exec_())
