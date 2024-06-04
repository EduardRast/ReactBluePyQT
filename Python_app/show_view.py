import sys
import os
import json
import random
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QStackedWidget
from PyQt5.QtGui import QPixmap, QImage, QColor
from PyQt5.QtCore import Qt


colors = {
  "red": "#FF0000",
  "green": "#008000",
  "blue": "#0000FF",
  "yellow": "#FFFF00",
  "cyan": "#00FFFF",
  "magenta": "#FF00FF",
  "black": "#000000",
  "white": "#FFFFFF",
  "gray": "#808080",
  "maroon": "#800000",
  "olive": "#808000",
  "purple": "#800080",
  "teal": "#008080",
  "navy": "#000080",
  "silver": "#C0C0C0",
  "lime": "#00FF00",
  "aqua": "#00FFFF",
  "fuchsia": "#FF00FF",
  "orange": "#FFA500",
  "brown": "#A52A2A",
  "coral": "#FF7F50",
  "gold": "#FFD700",
  "indigo": "#4B0082",
  "pink": "#FFC0CB",
  "violet": "#EE82EE"
}

class HomeScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        button = QPushButton('Go to Input Screen', self)
        button.clicked.connect(self.go_to_input_screen)
        layout.addWidget(button)

    def go_to_input_screen(self):
        self.stacked_widget.setCurrentIndex(1)

class InputScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.json_input = QLineEdit(self)
        self.json_input.setPlaceholderText("Enter JSON string here")
        layout.addWidget(self.json_input)

        button = QPushButton('Convert to JSON and Go to Display Screen', self)
        button.clicked.connect(self.convert_to_json)
        layout.addWidget(button)

    def convert_to_json(self):
        json_str = self.json_input.text()
        try:
            json_obj = json.loads(json_str)
            self.stacked_widget.widget(2).set_json(json_obj)
            self.stacked_widget.setCurrentIndex(2)
        except json.JSONDecodeError:
            self.json_input.setText("Invalid JSON string!")

class DisplayScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        greeting = "Hello "
        speach = ", Is this your favourite drink?"
        self.name_label = QLabel(self)
        self.layout.addWidget(self.name_label)
        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

    def set_json(self, json_obj):
        greeting = "Hello "
        speach = ", Is this your favourite drink?"
        self.name_label.setText(greeting+json_obj.get('name', 'Unknown')+speach)
        aColourValue = json_obj.get('color', '#FFFFFF')
        color = colors.get('color', '#FFFFFF')
        self.setStyleSheet(f'background-color: {color};')
        drink = json_obj.get('favorite_drink', 'water')
        self.load_image(drink)

    def load_image(self, drink):
        image_url = f"https://source.unsplash.com/featured/?{drink}"
        response = requests.get(image_url)
        image = QImage()
        image.loadFromData(response.content)
        pixmap = QPixmap(image)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)
        pixmap_resized = pixmap.scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(pixmap_resized)
        self.image_label.setAlignment(Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)

    qss_file = os.path.join(os.path.dirname(__file__), 'style.qss')
    with open(qss_file, "r") as f:
        app.setStyleSheet(f.read())

    stacked_widget = QStackedWidget()

    home_screen = HomeScreen(stacked_widget)
    input_screen = InputScreen(stacked_widget)
    display_screen = DisplayScreen()

    stacked_widget.addWidget(home_screen)
    stacked_widget.addWidget(input_screen)
    stacked_widget.addWidget(display_screen)

    stacked_widget.setCurrentIndex(0)

    main_window = QWidget()
    main_layout = QVBoxLayout()
    main_layout.addWidget(stacked_widget)
    main_window.setLayout(main_layout)

    main_window.setWindowTitle('JSON Viewer')
    main_window.resize(400, 300)
    main_window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


{
    "name": "Ed",
    "favorite_drink":"grean tea",
    "color":"pink"
}