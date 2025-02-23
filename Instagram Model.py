



from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from os import system
import sys


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""background-color: rgb(255,67,67);
                                   font-size: 35px;""")
        self.setWindowTitle("Instagram")
        self.class_ = None
        self.main = None
        self.qh8 = None
        self.qh9 = None
        self.qh7 = None
        self.qh6 = None
        self.qh5 = None
        self.qh4 = None
        self.qh3 = None
        self.qh2 = None
        self.register_btn = None
        self.qh_sign19 = None
        self.username_lbl = None
        self.sign_password_line = None
        self.email_line = None
        self.email_lbl = None
        self.username_line = None
        self.qh_sign18 = None
        self.qh_sign17 = None
        self.qh_sign16 = None
        self.qh_sign15 = None
        self.qh_sign14 = None
        self.qh_sign13 = None
        self.qh_sign12 = None
        self.qh_sign11 = None
        self.qh_sign10 = None
        self.qh_sign9 = None
        self.qh_sign7 = None
        self.qh_sign8 = None
        self.qh_sign6 = None
        self.qh_sign5 = None
        self.qh_sign4 = None
        self.qh_sign3 = None
        self.qh_sign2 = None
        self.qh_sign1 = None
        self.agree = None
        self.repeat_password_line = None
        self.repeat_password_lbl = None
        self.fullname_line = None
        self.signup_lbl = None
        self.fullname = None
        self.log_lbl = QLabel("Login")
        self.log_lbl.setFont(QFont("Arial", 32))
        self.username = QLabel("Username")
        self.username.setFont(QFont("Arial", 16))
        self.password_lbl = QLabel("Password")
        self.password_lbl.setFont(QFont("Arial", 16))
        self.log_line = QLineEdit()
        self.log_line.setPlaceholderText("Enter your username")
        self.pass_line = QLineEdit()
        self.pass_line.setPlaceholderText("Enter your password")
        self.login_btn = QPushButton("LOGIN")
        self.login_btn.setStyleSheet("color: white;"
                                     "font-weight: bold;"
                                     "text-align: center;"
                                     "font-size:24px;"
                                     "border-radius: 10px;")
        self.forgot_password = QPushButton("Forgot Password")
        self.signup_btn = QPushButton("     SIGN UP     ")
        self.signup_btn.setStyleSheet("color: white;"
                                      "font-weight: bold;"
                                      "font-size:24px;"
                                      "border-radius: 10px;"
                                      "border:3px solid white")
        self.creator_lbl = QLabel("Made via Python by Eshboyev Mukhtor")
        self.creator_lbl.setFont(QFont("Arial", 10))
        self.creator_lbl.setStyleSheet("color:white;"
                                       "font-weight:bold;"
                                       "font-size:12px;")

        self.ask = QLabel("Hello, friend!")
        self.ask.setStyleSheet("color:white;"
                               "font-weight:bold;")
        self.ask.setFont(QFont("Arial", 24))

        self.details_lbl1 = QLabel("Enter your personal details and start ")
        self.details_lbl2 = QLabel("your journey with us")
        self.details_lbl1.setFont(QFont("Arial", 15))
        self.details_lbl2.setFont(QFont("Arial", 15))
        self.details_lbl1.setStyleSheet("color:white;"
                                        "font-weight:bold;"
                                        "font-size:15px;")
        self.details_lbl2.setStyleSheet("color:white;"
                                        "font-weight:bold;"
                                        "font-size:15px;")

        self.lbl_before_login = QLabel("Have an account?")
        self.lbl_before_login.setFont(QFont("Arial", 18))
        self.lbl_before_login.setStyleSheet("color:white;"
                                            "font-weight:bold;"
                                            "font-size:15px;")

        self.start_qh1 = QHBoxLayout()
        self.start_qh3 = QHBoxLayout()
        self.start_qh4 = QHBoxLayout()
        self.start_qh5 = QHBoxLayout()
        self.start_qh6 = QHBoxLayout()
        self.start_qh7 = QHBoxLayout()

        self.start_qh1.addStretch()
        self.start_qh1.addWidget(self.ask)
        self.start_qh1.addStretch()

        self.start_qh7.addWidget(self.creator_lbl)
        self.start_qh7.addStretch()
        self.start_qh7.addStretch()
        self.start_qh7.addWidget(self.lbl_before_login)
        self.start_qh7.addWidget(self.login_btn)

        self.start_qh3.addStretch()
        self.start_qh3.addWidget(self.signup_btn)
        self.start_qh3.addStretch()

        self.start_qh5.addStretch()
        self.start_qh5.addWidget(self.details_lbl1)
        self.start_qh5.addStretch()

        self.start_qh6.addStretch()
        self.start_qh6.addWidget(self.details_lbl2)
        self.start_qh6.addStretch()

        self.main = QVBoxLayout()
        self.main.addStretch()
        self.main.addStretch()
        self.main.addLayout(self.start_qh1)
        self.main.addStretch()
        self.main.addLayout(self.start_qh5)
        self.main.addLayout(self.start_qh6)
        self.main.addStretch()
        self.main.addLayout(self.start_qh3)
        self.main.addStretch()
        self.main.addLayout(self.start_qh7)

        self.setLayout(self.main)

        self.login_btn.clicked.connect(self.log_in)
        self.signup_btn.clicked.connect(self.signup)

    def log_in(self):
        self.class_ = Login()
        self.close()
        self.class_.show()

    def signup(self):
        self.class_ = Signup()
        self.close()
        self.class_.show()


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.class_login = None
        self.main = None
        self.qh8 = None
        self.qh9 = None
        self.qh7 = None
        self.qh6 = None
        self.qh5 = None
        self.qh4 = None
        self.qh3 = None
        self.qh2 = None
        self.register_btn = None
        self.qh_sign19 = None
        self.username_lbl = None
        self.sign_password_line = None
        self.email_line = None
        self.email_lbl = None
        self.username_line = None
        self.qh_sign18 = None
        self.qh_sign17 = None
        self.qh_sign16 = None
        self.qh_sign15 = None
        self.qh_sign14 = None
        self.qh_sign13 = None
        self.qh_sign12 = None
        self.qh_sign11 = None
        self.qh_sign10 = None
        self.qh_sign9 = None
        self.qh_sign7 = None
        self.qh_sign8 = None
        self.qh_sign6 = None
        self.qh_sign5 = None
        self.qh_sign4 = None
        self.qh_sign3 = None
        self.qh_sign2 = None
        self.qh_sign1 = None
        self.agree = None
        self.repeat_password_line = None
        self.repeat_password_lbl = None
        self.fullname_line = None
        self.signup_lbl = None
        self.fullname = None
        self.log_lbl = QLabel("Login")
        self.log_lbl.setFont(QFont("Arial", 32))
        self.log_lbl.setStyleSheet("font-weight: bold")
        self.username = QLabel("Username")
        self.username.setFont(QFont("Arial", 16))
        self.username.setStyleSheet("font-weight: bold")
        self.password_lbl = QLabel("Password")
        self.password_lbl.setFont(QFont("Arial", 16))
        self.password_lbl.setStyleSheet("font-weight: bold")
        self.log_line = QLineEdit()
        self.log_line.setPlaceholderText("Enter your username")
        self.log_line.setStyleSheet("text-align: center;"
                                    "color: black;"
                                    "border-radius: 3px;")
        self.pass_line = QLineEdit()
        self.pass_line.setPlaceholderText("Enter your password")
        self.pass_line.setStyleSheet("text-align: center;"
                                     "color: black;"
                                     "border-radius: 3px;")

        self.login_btn = QPushButton("LOGIN")
        self.login_btn.setStyleSheet("color: white;"
                                     "font-weight: bold;"
                                     "text-align: center;"
                                     "font-size:24px;"
                                     "border-radius: 10px;"
                                     "background-color: rgb(255,100,43);")
        self.forgot_password = QPushButton("Forgot Password")
        self.forgot_password.setStyleSheet("font-weight: bold;"
                                           "text-align: center;"
                                           "font-size:15px;"
                                           "border-radius: 5px;")
        self.signup_btn = QPushButton("   Sign Up   ")
        self.signup_btn.setStyleSheet("color: white;"
                                      "font-weight: bold;"
                                      "text-align: center;"
                                      "font-size:24px;"
                                      "border-radius: 10px;"
                                      "background-color: green;")

        self.qh1 = QHBoxLayout()
        self.qh2 = QHBoxLayout()
        self.qh3 = QHBoxLayout()
        self.qh4 = QHBoxLayout()
        self.qh5 = QHBoxLayout()
        self.qh6 = QHBoxLayout()
        self.qh7 = QHBoxLayout()
        self.qh8 = QHBoxLayout()
        self.qh9 = QHBoxLayout()

        self.qh1.addStretch()
        self.qh1.addWidget(self.log_lbl)
        self.qh1.addStretch()

        self.qh2.addWidget(self.username)
        self.qh2.addStretch()
        self.qh2.addStretch()

        self.qh3.addWidget(self.log_line)

        self.qh4.addWidget(self.password_lbl)
        self.qh4.addStretch()
        self.qh4.addStretch()

        self.qh5.addWidget(self.pass_line)

        self.qh6.addStretch()
        self.qh6.addStretch()
        self.qh6.addWidget(self.forgot_password)

        self.qh7.addWidget(self.login_btn)

        self.qh8.addStretch()
        self.qh8.addStretch()
        self.qh8.addStretch()

        self.qh9.addStretch()
        self.qh9.addWidget(self.signup_btn)
        self.qh9.addStretch()

        self.main = QVBoxLayout()
        self.main.addLayout(self.qh1)
        self.main.addLayout(self.qh2)
        self.main.addLayout(self.qh3)
        self.main.addLayout(self.qh4)
        self.main.addLayout(self.qh5)
        self.main.addLayout(self.qh6)
        self.main.addLayout(self.qh7)
        self.main.addLayout(self.qh8)
        self.main.addLayout(self.qh9)
        self.setLayout(self.main)

        self.signup_btn.clicked.connect(self.signup)
        self.login_btn.clicked.connect(self.login)
        self.forgot_password.clicked.connect(self.forgot)

    def forgot(self):
        msg = QMessageBox()
        msg.setWindowTitle("Forgot Password")
        msg.setIcon(QMessageBox.Information)
        msg.setText("We advise you to create a new account if you forgot your password or username")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def login(self):
        with open("app_users.txt", "r") as f:
            f.seek(0)
            for line in f:
                lst = line.split("///")
                if lst[2] == self.log_line.text() and lst[3] == self.pass_line.text():
                    self.class_login = Main()
                    self.class_login.show()
                    msg = QMessageBox()
                    msg.setText("Success, you have successfully logged in!")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
                    self.close()

                elif lst[2] != self.log_line.text():
                    msg = QMessageBox()
                    msg.setText("Error, User does not exist")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()

                elif lst[3] != self.pass_line.text():
                    msg = QMessageBox()
                    msg.setText("Error, Incorrect password")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()

    def signup(self):
        self.class_login = Signup()
        self.close()
        self.class_login.show()


class Signup(QWidget):
    def __init__(self):
        super().__init__()
        self.class_ = None
        self.main = None
        self.qh8 = None
        self.qh9 = None
        self.qh7 = None
        self.qh6 = None
        self.qh5 = None
        self.qh4 = None
        self.qh3 = None
        self.qh2 = None
        self.register_btn = None
        self.qh_sign19 = None
        self.username_lbl = None
        self.sign_password_line = None
        self.email_line = None
        self.email_lbl = None
        self.username_line = None
        self.qh_sign18 = None
        self.qh_sign17 = None
        self.qh_sign16 = None
        self.qh_sign15 = None
        self.qh_sign14 = None
        self.qh_sign13 = None
        self.qh_sign12 = None
        self.qh_sign11 = None
        self.qh_sign10 = None
        self.qh_sign9 = None
        self.qh_sign7 = None
        self.qh_sign8 = None
        self.qh_sign6 = None
        self.qh_sign5 = None
        self.qh_sign4 = None
        self.qh_sign3 = None
        self.qh_sign2 = None
        self.qh_sign1 = None
        self.agree = None
        self.repeat_password_line = None
        self.repeat_password_lbl = None
        self.fullname_line = None
        self.signup_lbl = None
        self.fullname = None
        self.log_lbl = QLabel("Login")
        self.log_lbl.setFont(QFont("Arial", 32))
        self.username = QLabel("Username")
        self.username.setFont(QFont("Arial", 16))
        self.password_lbl = QLabel("Password")
        self.password_lbl.setFont(QFont("Arial", 16))
        self.password_lbl.setStyleSheet("font-weight: bold")
        self.log_line = QLineEdit()
        self.log_line.setPlaceholderText("Enter your username")
        self.pass_line = QLineEdit()
        self.pass_line.setPlaceholderText("Enter your password")
        self.login_btn = QPushButton("LOGIN")
        self.forgot_password = QPushButton("Forgot Password")
        self.signup_btn = QPushButton("Sign Up")

        self.ask = QLabel("Welcome to the application")
        self.ask.setFont(QFont("Arial", 24))

        self.signup_lbl = QLabel("Create Account")
        self.signup_lbl.setFont(QFont("Arial", 32))
        self.signup_lbl.setStyleSheet("font-weight: bold")
        self.fullname = QLabel("Full Name")
        self.fullname.setFont(QFont("Arial", 16))
        self.fullname.setStyleSheet("font-weight: bold")
        self.fullname_line = QLineEdit()
        self.fullname_line.setStyleSheet("text-align: center;"
                                         "color: black;"
                                         "border-radius: 3px;")
        self.fullname_line.setPlaceholderText("Name...")
        self.email_lbl = QLabel("Email")
        self.email_lbl.setFont(QFont("Arial", 16))
        self.email_lbl.setStyleSheet("font-weight: bold")
        self.email_line = QLineEdit()
        self.email_line.setStyleSheet("text-align: center;"
                                      "color: black;"
                                      "border-radius: 3px;")
        self.email_line.setPlaceholderText("Email address...")
        self.username_lbl = QLabel("Username")
        self.username_lbl.setFont(QFont("Arial", 16))
        self.username_lbl.setStyleSheet("font-weight: bold")
        self.username_line = QLineEdit()
        self.username_line.setStyleSheet("text-align: center;"
                                         "color: black;"
                                         "border-radius: 3px;")
        self.username_line.setPlaceholderText("Username...")
        self.sign_password_line = QLineEdit()
        self.sign_password_line.setStyleSheet("text-align: center;"
                                              "color: black;"
                                              "border-radius: 3px;")
        self.sign_password_line.setPlaceholderText("****************")
        self.repeat_password_lbl = QLabel("Repeat Password")
        self.repeat_password_lbl.setFont(QFont("Arial", 16))
        self.repeat_password_lbl.setStyleSheet("font-weight: bold")
        self.repeat_password_line = QLineEdit()
        self.repeat_password_line.setStyleSheet("text-align: center;"
                                                "color: black;"
                                                "border-radius: 3px;")
        self.repeat_password_line.setPlaceholderText("****************")
        self.agree = QRadioButton("I agree to the TERMS OF USERS")
        self.agree.setStyleSheet("font-weight: Bold;")
        self.register_btn = QPushButton("    SIGN UP    ")
        self.register_btn.setStyleSheet("color: white;"
                                        "font-weight: bold;"
                                        "font-size:24px;"
                                        "border-radius: 10px;"
                                        "border:3px solid white;"
                                        "background-color: rgb(255,100,43);")

        self.qh_sign1 = QHBoxLayout()
        self.qh_sign2 = QHBoxLayout()
        self.qh_sign3 = QHBoxLayout()
        self.qh_sign4 = QHBoxLayout()
        self.qh_sign5 = QHBoxLayout()
        self.qh_sign6 = QHBoxLayout()
        self.qh_sign7 = QHBoxLayout()
        self.qh_sign8 = QHBoxLayout()
        self.qh_sign9 = QHBoxLayout()
        self.qh_sign10 = QHBoxLayout()
        self.qh_sign11 = QHBoxLayout()
        self.qh_sign12 = QHBoxLayout()
        self.qh_sign13 = QHBoxLayout()
        self.qh_sign14 = QHBoxLayout()
        self.qh_sign15 = QHBoxLayout()
        self.qh_sign16 = QHBoxLayout()
        self.qh_sign17 = QHBoxLayout()
        self.qh_sign18 = QHBoxLayout()
        self.qh_sign19 = QHBoxLayout()

        self.qh_sign1.addStretch()
        self.qh_sign1.addWidget(self.signup_lbl)
        self.qh_sign1.addStretch()

        self.qh_sign2.addStretch()
        self.qh_sign2.addStretch()
        self.qh_sign2.addStretch()

        self.qh_sign3.addWidget(self.fullname)
        self.qh_sign3.addStretch()
        self.qh_sign3.addStretch()

        self.qh_sign4.addWidget(self.fullname_line)

        self.qh_sign5.addStretch()
        self.qh_sign5.addStretch()
        self.qh_sign5.addStretch()

        self.qh_sign6.addWidget(self.email_lbl)
        self.qh_sign6.addStretch()
        self.qh_sign6.addStretch()

        self.qh_sign7.addWidget(self.email_line)

        self.qh_sign8.addStretch()
        self.qh_sign8.addStretch()
        self.qh_sign8.addStretch()

        self.qh_sign9.addWidget(self.username_lbl)
        self.qh_sign9.addStretch()
        self.qh_sign9.addStretch()

        self.qh_sign10.addWidget(self.username_line)

        self.qh_sign11.addStretch()
        self.qh_sign11.addStretch()
        self.qh_sign11.addStretch()

        self.qh_sign12.addWidget(self.password_lbl)
        self.qh_sign12.addStretch()
        self.qh_sign12.addStretch()

        self.qh_sign13.addWidget(self.sign_password_line)

        self.qh_sign14.addStretch()
        self.qh_sign14.addStretch()
        self.qh_sign14.addStretch()

        self.qh_sign15.addWidget(self.repeat_password_lbl)
        self.qh_sign15.addStretch()
        self.qh_sign15.addStretch()

        self.qh_sign16.addWidget(self.repeat_password_line)

        self.qh_sign17.addStretch()
        self.qh_sign17.addStretch()
        self.qh_sign17.addStretch()

        self.qh_sign18.addWidget(self.agree)

        self.qh_sign19.addStretch()
        self.qh_sign19.addWidget(self.register_btn)
        self.qh_sign19.addStretch()

        self.main = QVBoxLayout()
        self.main.addLayout(self.qh_sign1)
        self.main.addLayout(self.qh_sign2)
        self.main.addLayout(self.qh_sign3)
        self.main.addLayout(self.qh_sign4)
        self.main.addLayout(self.qh_sign5)
        self.main.addLayout(self.qh_sign6)
        self.main.addLayout(self.qh_sign7)
        self.main.addLayout(self.qh_sign8)
        self.main.addLayout(self.qh_sign9)
        self.main.addLayout(self.qh_sign10)
        self.main.addLayout(self.qh_sign11)
        self.main.addLayout(self.qh_sign12)
        self.main.addLayout(self.qh_sign13)
        self.main.addLayout(self.qh_sign14)
        self.main.addLayout(self.qh_sign15)
        self.main.addLayout(self.qh_sign16)
        self.main.addLayout(self.qh_sign17)
        self.main.addLayout(self.qh_sign18)
        self.main.addLayout(self.qh_sign19)
        self.setLayout(self.main)

        self.login_btn.clicked.connect(self.log_in)
        self.register_btn.clicked.connect(self.sign_up)

    def sign_up_check(self):
        with open("app_users.txt") as f:
            for line in f:
                lst = line.split("///")
                if lst[2] == self.username_line.text():
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Username already exists!")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
                    return False
            if len(self.sign_password_line.text()) < 6:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Password too short!")
                msg.setDetailedText("You need at least 6 characters in your password")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return False
            if self.sign_password_line.text() != self.repeat_password_line.text():
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Passwords do not match!")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return False
            return True

    def sign_up(self):
        checker = self.sign_up_check()
        if checker:
            with open("app_users.txt", "a") as f:
                f.write(
                    f"{self.fullname_line.text()}///{self.email_line.text()}///{self.username_line.text()}///{self.sign_password_line.text()}///\n")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Account created!")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                self.class_ = Login()
                self.close()
                self.class_.show()
        else:
            pass

    def log_in(self):
        self.class_ = Login()
        self.close()
        self.class_.show()


if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec_())









































