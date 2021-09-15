from PySide2 import QtWidgets
from collections import OrderedDict


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setWindowTitle("pyTictactoe")
        self.setFixedWidth(480)
        self.css()
        self.center()

    def setup_ui(self):
        self.create_widgets()
        self.setup_icon()
        self.modify_widgets()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.toolBar = QtWidgets.QToolBar()
        self.center_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout(self.center_widget)

        # CENTER LAYOUT
        self.btn_dict = [i + 1 for i in range(9)]
        self.btn_dict = OrderedDict({i: self.MyPushButton("") for i in self.btn_dict})

        # BOT INFOS PLAYERS
        self.lbl_player_play = QtWidgets.QLabel("PLAYER1 TO PLAY")

        self.init_shortcuts()

    def init_shortcuts(self):
        # KEYBOARD SHORTCUTS
        self.btn_dict[1].setShortcut("7")
        self.btn_dict[2].setShortcut("8")
        self.btn_dict[3].setShortcut("9")
        self.btn_dict[4].setShortcut("4")
        self.btn_dict[5].setShortcut("5")
        self.btn_dict[6].setShortcut("6")
        self.btn_dict[7].setShortcut("1")
        self.btn_dict[8].setShortcut("2")
        self.btn_dict[9].setShortcut("3")

    def css(self):
        with open("style.css", "r") as f:
            self.setStyleSheet(f.read())

    def modify_widgets(self):
        self.reload = self.toolBar.addAction(self.reload, "RELOAD")
        self.toolBar.addSeparator()
        self.toolBar.setFixedHeight(50)
        self.toolBar.setFloatable(False)
        self.toolBar.setMovable(False)

    def setup_icon(self):
        self.reload = self.style().standardIcon(QtWidgets.QStyle.SP_BrowserReload)

    def add_widgets_to_layouts(self):
        self.addToolBar(self.toolBar)
        self.setCentralWidget(self.center_widget)

        # CENTER LAYOUT
        self.main_layout.addWidget(self.btn_dict[1], 0, 0, 1, 1)
        self.main_layout.addWidget(self.btn_dict[2], 0, 1, 1, 1)
        self.main_layout.addWidget(self.btn_dict[3], 0, 2, 1, 1)
        self.main_layout.addWidget(self.btn_dict[4], 1, 0, 1, 1)
        self.main_layout.addWidget(self.btn_dict[5], 1, 1, 1, 1)
        self.main_layout.addWidget(self.btn_dict[6], 1, 2, 1, 1)
        self.main_layout.addWidget(self.btn_dict[7], 2, 0, 1, 1)
        self.main_layout.addWidget(self.btn_dict[8], 2, 1, 1, 1)
        self.main_layout.addWidget(self.btn_dict[9], 2, 2, 1, 1)
        self.main_layout.addWidget(self.lbl_player_play, 3, 0, 1, 1)

    def setup_connections(self):
        self.reload.triggered.connect(self.reload_game)
        self.btn_dict[1].clicked.connect(self.button1_clicked)
        self.btn_dict[2].clicked.connect(self.button2_clicked)
        self.btn_dict[3].clicked.connect(self.button3_clicked)
        self.btn_dict[4].clicked.connect(self.button4_clicked)
        self.btn_dict[5].clicked.connect(self.button5_clicked)
        self.btn_dict[6].clicked.connect(self.button6_clicked)
        self.btn_dict[7].clicked.connect(self.button7_clicked)
        self.btn_dict[8].clicked.connect(self.button8_clicked)
        self.btn_dict[9].clicked.connect(self.button9_clicked)

    def button1_clicked(self):
        self.checked_button(1)

    def button2_clicked(self):
        self.checked_button(2)

    def button3_clicked(self):
        self.checked_button(3)

    def button4_clicked(self):
        self.checked_button(4)

    def button5_clicked(self):
        self.checked_button(5)

    def button6_clicked(self):
        self.checked_button(6)

    def button7_clicked(self):
        self.checked_button(7)

    def button8_clicked(self):
        self.checked_button(8)

    def button9_clicked(self):
        self.checked_button(9)

    def checked_button(self, num):
        if self.btn_dict[num].text() in ["X", "O"]:
            return
        if self.lbl_player_play.text() == "PLAYER1 TO PLAY":
            self.btn_dict[num].setText("X")
            self.btn_dict[num].colored("LightGreen")
            self.lbl_player_play.setText("PLAYER2 TO PLAY")
        else:
            self.btn_dict[num].setText("O")
            self.btn_dict[num].colored("orange")
            self.lbl_player_play.setText("PLAYER1 TO PLAY")
        self.check_win()

    def reload_game(self):
        for value in self.btn_dict:
            self.btn_dict[value].setText("")
            self.btn_dict[value].colored("default")
        if self.lbl_player_play.text()[0:11] == "PLAYER1 WIN":
            self.lbl_player_play.setText("PLAYER2 TO PLAY")
        elif self.lbl_player_play.text()[0:11] == "PLAYER2 WIN":
            self.lbl_player_play.setText("PLAYER1 TO PLAY")
        self.init_shortcuts()
        self.show_winner(visible=True)

    def show_winner(self, visible=False):
        for value in self.btn_dict:
            if visible:
                self.btn_dict[value].show()
            else:
                self.btn_dict[value].hide()

    def check_win(self):
        def checked(num1, num2, num3):
            if self.btn_dict[num1].text() == self.btn_dict[num2].text() == self.btn_dict[num3].text():
                player_win = self.btn_dict[num1].text()
                if player_win == "X":
                    self.lbl_player_play.setText("PLAYER1 WIN\nReload the game for play again")
                    self.show_winner()
                elif player_win == "O":
                    self.lbl_player_play.setText("PLAYER2 WIN\nReload the game for play again")
                    self.show_winner()

        checked(1, 2, 3)
        checked(4, 5, 6)
        checked(7, 8, 9)
        checked(1, 5, 9)
        checked(3, 5, 7)
        checked(1, 4, 7)
        checked(2, 5, 8)
        checked(3, 6, 9)

    def center(self):
        qtrectangle = self.frameGeometry()
        centerpoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtrectangle.moveCenter(centerpoint)
        self.move(qtrectangle.topLeft())

    class MyPushButton(QtWidgets.QPushButton):
        def __init__(self, text):
            super().__init__()
            self.setFixedSize(150, 150)
            self.setText(text)

        def colored(self, color):
            if color == "LightGreen":
                self.setStyleSheet("background-color: LightGreen;")
            if color == "orange":
                self.setStyleSheet("background-color: orange;")
            if color == "default":
                self.setStyleSheet("background-color: #303030;")


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec_()
