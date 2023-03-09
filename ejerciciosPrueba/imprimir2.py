import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SERVICE OFFERS')
        self.resize(500, 120)

        layout = QGridLayout()

        label_name = QLabel('<font size="4"> Nombre del producto </font>')
        self.lineEdit_name = QLineEdit()
        self.lineEdit_name.setPlaceholderText('introduce nombre')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_name, 0, 1)

        label_service = QLabel('<font size="4"> servicio </font>')
        self.lineEdit_service = QLineEdit()
        self.lineEdit_service.setPlaceholderText('introduce servicio aplicado')
        layout.addWidget(label_service, 1, 0)
        layout.addWidget(self.lineEdit_service, 1, 1)

      



        button_PDF = QPushButton('crear PDF')
        button_PDF.clicked.connect(self.create_pdf)
        layout.addWidget(button_PDF, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    def create_pdf(self):
        msg = QMessageBox()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = LoginForm()
    form.show()

    sys.exit(app.exec_())  