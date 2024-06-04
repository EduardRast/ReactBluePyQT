import sys
from qtpy.QtWidgets import (QApplication, QLabel, QWidget,
                            QVBoxLayout, QPushButton, QTextEdit)

import time

app = QApplication([])
layout = QVBoxLayout()
widget = QWidget()

def say_hello(label):
    layout.removeWidget(label)
    label.hide()
    # for i in range(layout.count()):
    #     print(layout.itemAt(i))
    #     if layout.itemAt(i) == label:
    #         layout.removeItem(label)

def say_hell(text):
    inpout = text.toPlainText()
    print(inpout)


if __name__ == '__main__':
    print("Hello World")

    # Initialize application

    # Create label widget
    label1 = QLabel('Hello, world!\nHello, world!')
    label2 = QLabel('Hello, world!\nHello, world!')
    text = QTextEdit()

    button = QPushButton('Press me!')
    button.clicked.connect(lambda: say_hell(text))


    # Create layout and add widgets

    layout.addWidget(label1)
    layout.addWidget(label2)
    layout.addWidget(button)
    layout.addWidget(text)

    # Apply layout to widget

    widget.setLayout(layout)

    widget.show()

    sys.exit(app.exec_())

