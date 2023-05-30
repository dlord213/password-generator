import string
import sys
import secrets
import pyperclip
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from ui_design_ui import Ui_PasswordGeneratorWindow

class mainApp(QMainWindow, Ui_PasswordGeneratorWindow):
    
    password = None
    alphabet = string.ascii_letters + string.digits

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.generateBtn.clicked.connect(self.generatePass)
        self.copyBtn.clicked.connect(self.copyClipboard)

    def generatePass(self):
        self.password = ''.join(secrets.choice(self.alphabet) for i in range(12))

        self.generateLineEdit.setText(self.password)

    def copyClipboard(self):
        if self.password == None:
            successMsgBox = QMessageBox(self)
            successMsgBox.setWindowTitle("No generated password")
            successMsgBox.setText("Please generate a password.")
            successMsgBox.exec()
        else:
            pyperclip.copy(self.password)
            successMsgBox = QMessageBox(self)
            successMsgBox.setWindowTitle("Copied to clipboard")
            successMsgBox.setText("The password you generated is copied, simply press CTRL + V.")
            successMsgBox.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = mainApp()
    win.show()
    app.exec()