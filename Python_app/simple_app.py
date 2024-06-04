import sys
import os
from qtpy.QtWidgets import (QApplication, QLabel, QWidget,
                            QVBoxLayout, QPushButton, QTextEdit, QHBoxLayout)


class Widget(QWidget):
    # First, we create a widget layouts 
    #and assign the parent calss to be the original QWidget 
    def __init__(self, parent = None):
        super(Widget,self).__init__(parent) 

        helloLavble = QLabel("Hello World, I am a label") # create a text label 
        startButton = QPushButton("Press me to start!") # Create a button with a 

        self.nameLable = QLabel() # A placeholder lable
        self.nameEntry = QTextEdit() # Create a text entry
        self.nameRequestLable = QLabel("Please enter your name")
        self.nameRequestButton = QPushButton("Press to learn your name")

        self.layoutMain = QHBoxLayout() # create a layout
        self.layoutName = QVBoxLayout() # create a layout,
        """ there are different types of layouts:
        Vertical layout
        Horizontal layout
        Grid layout,
        ...
        Docs: https://doc.qt.io/qt-6/layout.html
        """
        self.layoutMain.addWidget(helloLavble)
        self.layoutMain.addWidget(startButton) # populate the layout with the elements

        self.layoutName.addWidget(self.nameLable)
        self.layoutName.addWidget(self.nameRequestLable)
        self.layoutName.addWidget(self.nameEntry)
        self.layoutName.addWidget(self.nameRequestButton)

        # Create an event handler for buttons
        startButton.clicked.connect(self.__startNames)
        self.nameRequestButton.clicked.connect(self.__setName)

        # set the default layout to main
        self.setLayout(self.layoutMain)

        # Set window properties
        self.setWindowTitle('My App')
        self.setGeometry(500, 500, 500, 500)
    
    # Chages the start window to a name request window
    def __startNames(self):
        self.__clear_layout(self.layoutMain)
        self.setLayout(self.layoutName)

    # Collects text fdrom entry and puts in a lable
    def __setName(self):
        aName = self.nameEntry.toPlainText() # get the text
        self.nameLable.setText("Your name is: "+aName)

    def __clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
            QWidget().setLayout(layout)  # Remove the layout from any widget it's set to

if __name__ == '__main__':

    app = QApplication([]) # initialize the app

    w = Widget() # initialize the widget
    w.show() # show the contents of the widget

    # To add style to the window, it is possible to use the methods inside the class
    #or apply them using the qss file, similar to css
    qss_file = os.path.join(os.path.dirname(__file__), 'style.qss')
    with open(qss_file, "r") as f:
        app.setStyleSheet(f.read())

    
    sys.exit(app.exec_()) # run a loop of the application. exit when wiindow closed

