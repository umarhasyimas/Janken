from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QPixmap, QImage, QPainter, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QGroupBox, QAction, QDialog
import random as rand
from rpsui import Ui_MainWindow  # Import the generated UI class
from AboutUI import Ui_Dialog
import rpsimages_rc

class RockPaperScissors(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.rock_btn.clicked.connect(lambda: self.choose_icon("rock"))
        self.ui.paper_btn.clicked.connect(lambda: self.choose_icon("paper"))
        self.ui.scissors_btn.clicked.connect(lambda: self.choose_icon("scissors"))
        self.ui.begin_btn.clicked.connect(self.begin_game)

        help_menu = self.menuBar().addMenu("&Help")

        about_action = QtWidgets.QAction("&About", self)
        help_menu.addAction(about_action)
        about_action.triggered.connect(self.show_about_dialog)

        self.choices = ["rock", "paper", "scissors"]
        self.result_texts = {
            "rock": {"rock": "It's a tie!\n(Seimbang)", "paper": "You lost!\n(Kalah)", "scissors": "You win!\n(Menang)"},
            "paper": {"paper": "It's a tie!\n(Seimbang)", "scissors": "You lost!\n(Kalah)", "rock": "You win!\n(Menang)"},
            "scissors": {"scissors": "It's a tie!\n(Seimbang)", "rock": "You lost!\n(Kalah)", "paper": "You win!\n(Menang)"},
        }

        self.chosen_icon = None
        self.ui.chosen_text_lbl.setText("Choose an icon\n(Pilih icon)")

    def choose_icon(self, icon):
        self.chosen_icon = icon
        self.ui.chosen_icon_lbl.setPixmap(QtGui.QPixmap(f":/{icon}.png").scaled(151, 121))
        self.ui.chosen_text_lbl.setText(f"So, you choose {icon}\nItu yang kamu pilih?")
        self.ui.begin_btn.setEnabled(True)

    def begin_game(self):
        if self.chosen_icon:
            result = rand.choice(self.choices)
            self.show_result(result)
            self.ui.begin_btn.setEnabled(False)

    def show_result(self, result):
        text = self.result_texts[self.chosen_icon][result]
        self.ui.result_icon_1_lbl.setPixmap(QtGui.QPixmap(f":/{result}.png").scaled(80, 80))
        self.ui.chosen_text_lbl.setText(text)

    def show_about_dialog(self):
        about_dialog = Ui_Dialog(self)
        about_dialog.setupUi(about_dialog)
        about_dialog.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    game = RockPaperScissors()
    game.show()
    sys.exit(app.exec_())
