from PyQt5.QtWidgets import QApplication, QWidget

def run_gui():
    app = QApplication([])

    window = QWidget()
    window.show()

    app.exec()
