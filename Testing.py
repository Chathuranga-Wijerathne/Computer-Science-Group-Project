
import sys
from PyQt5.QtWidgets import QApplication, QWidget


class CreatingObjects():
    def __init__(self):
        label1 = self.label()











def main():

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(750, 650)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()