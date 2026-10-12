import sys
import json
import os
from PyQt5.QtWidgets import (QApplication,QWidget,QLineEdit,QTextEdit,
                             QPushButton,QListWidget)

class NoteApp(QWidget):
    def __init__(self):
        super().__init__()
        self.notes = []
        self.filename = "notes.json"
        self.initUI()
        self.load_notes()

    def initUI(self):
        self.setWindowTitle("Note App")
        self.setGeometry(100, 100, 600, 500)

        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText("Enter Title")
        self.title_input.setGeometry(20, 20, 560, 30)

        self.content_input = QTextEdit(self)
        self.content_input.setPlaceholderText("Enter Content")
        self.content_input.setGeometry(20, 60, 560, 200)

        self.save_button = QPushButton("Save Note", self)
        self.save_button.setGeometry(20, 270, 100, 30)
        self.save_button.clicked.connect(self.save_note)

        self.edit_button = QPushButton("Edit Note", self)
        self.edit_button.setGeometry(140, 270, 100, 30)
        self.edit_button.clicked.connect(self.edit_note)

        self.update_button = QPushButton("Update Note",self)
        self.update_button.setGeometry(260,270,100,30)
        self.update_button.clicked.connect(self.update_note)

        self.delete_button = QPushButton("Delete Note", self)
        self.delete_button.setGeometry(380,270,100,30)
        self.delete_button.clicked.connect(self.delete_note)

        self.notes_list = QListWidget(self)
        self.notes_list.setGeometry(20, 310, 560, 150)
        self.notes_list.itemClicked.connect(self.show_note)

    def save_note(self):
        title = self.title_input.text().strip()
        content = self.content_input.toPlainText().strip()
        if title and content:
            self.notes.append({"title":title, "content":content})
            self.notes_list.addItem(title)

            with open(self.filename, "w") as file:
                json.dump(self.notes,file)
            self.title_input.clear()
            self.content_input.clear()

    def load_notes(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.notes = json.load(file)
            for note in self.notes:
                self.notes_list.addItem(note["title"])

    def show_note(self,item):
        title = item.text()
        for note in self.notes:
            if note["title"] == title:
                self.content_input.setPlainText(note["content"])

    def edit_note(self):
        item = self.notes_list.currentItem()
        if item is not None:
            title = item.text()
            for note in self.notes:
                if note["title"] == title:
                    self.content_input.setPlainText(note["content"])

    def update_note(self):
        item = self.notes_list.currentItem()
        if item is not None:
            title = item.text()
            for note in self.notes:
                if note["title"] == title:
                    content = self.content_input.toPlainText().strip()
                    if content:
                        note["content"] = content

                        with open(self.filename, "w") as file:
                            json.dump(self.notes,file)
                        break

    def delete_note(self):
        item = self.notes_list.currentItem()
        if item is not None:
            title = item.text()
            for note in self.notes:
                if note["title"] == title:
                    self.notes.remove(note)
                    self.notes_list.takeItem(self.notes_list.row(item))

                    with open(self.filename, "w") as file:
                        json.dump(self.notes,file)
                    break












if __name__=="__main__":
    app = QApplication(sys.argv)
    window = NoteApp()
    window.show()
    sys.exit(app.exec_())












































if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NoteApp()
    window.show()
    sys.exit(app.exec_())