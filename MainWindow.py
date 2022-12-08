# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QPushButton, QGridLayout, QMessageBox
#
#
# class MenuBar(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Arduino Code Generator')
#         # self.resize(600, 500) # To set the window size
#
#         self.menuBar = self.menuBar()
#         self.showMaximized()
#
#         filemenu = self.menuBar.addMenu('File')
#
#         new_project_action = QAction('New Project', self)
#         new_project_action.setShortcut('Ctrl+N')
#         new_project_action.triggered.connect(lambda: QApplication.quit())
#         filemenu.addAction(new_project_action)
#
#         # Creating a separator action
#         separator = QAction(self)
#         separator.setSeparator(True)
#         # Adding the separator to the menu
#         filemenu.addAction(separator)
#
#         open_project_action = QAction('Open Project', self)
#         open_project_action.setShortcut('Ctrl+O')
#         open_project_action.triggered.connect(lambda: QApplication.quit())
#         filemenu.addAction(open_project_action)
#
#         open_template_action = QAction('Open Template', self)
#         open_template_action.setShortcut('Ctrl+T')
#         open_template_action.triggered.connect(lambda: QApplication.quit())
#         filemenu.addAction(open_template_action)
#
#         # Creating a separator action
#         separator = QAction(self)
#         separator.setSeparator(True)
#         # Adding the separator to the menu
#         filemenu.addAction(separator)
#
#         save_project_action = QAction('Save Project', self)
#         save_project_action.setShortcut('Ctrl+S')
#         save_project_action.triggered.connect(lambda: QApplication.quit())
#         filemenu.addAction(save_project_action)
#
#         # Creating a separator action
#         separator = QAction(self)
#         separator.setSeparator(True)
#         # Adding the separator to the menu
#         filemenu.addAction(separator)
#
#         settings_action = QAction('Settings', self)
#         # settings_action.setShortcut('')
#         settings_action.triggered.connect(lambda: QApplication.quit())
#         filemenu.addAction(settings_action)
#
#         # Creating a separator action
#         separator = QAction(self)
#         separator.setSeparator(True)
#         # Adding the separator to the menu
#         filemenu.addAction(separator)
#
#         exit_action = QAction('Exit', self)
#         exit_action.setShortcut('Alt+F4')
#         exit_action.triggered.connect(lambda: QApplication.quit())
#         filemenu.addAction(exit_action)
#
#         editmenu = self.menuBar.addMenu('Edit')
#
#         # undodeletemenu = editmenu.addMenu('Undo')
#         # yes_action = QAction('Yes', self)
#         # no_action = QAction('No', self)
#         # undodeletemenu.addAction(yes_action)
#         # undodeletemenu.addAction(no_action)
#
#         undo_action = QAction('Undo', self)
#         undo_action.setShortcut('Ctrl+Z')
#         undo_action.triggered.connect(lambda: QApplication.quit())
#         editmenu.addAction(undo_action)
#
#         redo_action = QAction('Redo', self)
#         redo_action.setShortcut('Ctrl+Y')
#         redo_action.triggered.connect(lambda: QApplication.quit())
#         editmenu.addAction(redo_action)
#
#         # Creating a separator action
#         separator = QAction(self)
#         separator.setSeparator(True)
#         # Adding the separator to the menu
#         editmenu.addAction(separator)
#
#         cut_action = QAction('Cut', self)
#         cut_action.setShortcut('Ctrl+X')
#         cut_action.triggered.connect(lambda: QApplication.quit())
#         editmenu.addAction(cut_action)
#
#         copy_action = QAction('Copy', self)
#         copy_action.setShortcut('Ctrl+C')
#         copy_action.triggered.connect(lambda: QApplication.quit())
#         editmenu.addAction(copy_action)
#
#         paste_action = QAction('Paste', self)
#         paste_action.setShortcut('Ctrl+V')
#         paste_action.triggered.connect(lambda: QApplication.quit())
#         editmenu.addAction(paste_action)
#
#         # selectmenu = self.menuBar.addMenu('Select')
#
#         helpmenu = self.menuBar.addMenu('Help')
#
#         device_list_action = QAction('Device List', self)
#         # device_list_action.setShortcut('Ctrl+V')
#         device_list_action.triggered.connect(lambda: QApplication.quit())
#         helpmenu.addAction(device_list_action)
#
#         how_to_use_action = QAction('How to Use', self)
#         # how_to_use_action.setShortcut('Ctrl+V')
#         how_to_use_action.triggered.connect(lambda: QApplication.quit())
#         helpmenu.addAction(how_to_use_action)
#
#         # Creating a separator action
#         separator = QAction(self)
#         separator.setSeparator(True)
#         # Adding the separator to the menu
#         helpmenu.addAction(separator)
#
#         report_issue_action = QAction('Report Issue', self)
#         # report_issue_action.setShortcut('Ctrl+R')
#         report_issue_action.triggered.connect(lambda: QApplication.quit())
#         helpmenu.addAction(report_issue_action)
#
#         check_for_updates_action = QAction('Check For Updates', self)
#         # check_for_updates_action.setShortcut('Ctrl+V')
#         check_for_updates_action.triggered.connect(lambda: QApplication.quit())
#         helpmenu.addAction(check_for_updates_action)
#
#         # Creating a separator action
#         separator = QAction(self)
#         separator.setSeparator(True)
#         # Adding the separator to the menu
#         helpmenu.addAction(separator)
#
#         about_action = QAction('About', self)
#         # about_action.setShortcut('Ctrl+V')
#         about_action.triggered.connect(lambda: QApplication.quit())
#         helpmenu.addAction(about_action)
#
#     def shortcut_menu(self):
#         # super().__init__()
#         # self.setWindowTitle("My App")
#
#         button = QPushButton("Press me for a dialog!")
#         button.clicked.connect(self.button_clicked)
#         # self.setCentralWidget(button)
#
#     def button_clicked(self, s):
#         dlg = QMessageBox(self)
#         dlg.setWindowTitle("I have a question!")
#         dlg.setText("This is a simple dialog")
#         button = dlg.exec()
#
#         if button == QMessageBox.StandardButton.Ok:
#             print("OK!")
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     menubar = MenuBar()
#     menubar.show()
#
#     # shortcutmenu = ShortcutMenu()
#     # shortcutmenu.show()
#
#     sys.exit(app.exec())
#
#
#
#
#
#
#
#
#
#
#
#


# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QFrame, QHBoxLayout
# from PyQt6.QtGui import QIcon, QFont
#
# import sys
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.setGeometry(200, 200, 700, 400)  # set the window size
#         self.setWindowTitle("Arduino Code Generator")  # set the window title
#         self.setWindowIcon(QIcon('python.png'))  # set the window icon
#
#         hbox = QHBoxLayout()
#
#         frame = QFrame()
#         frame.setFrameShape(QFrame)
#         hbox.addWidget(frame)
#
#         self.setLayout(hbox)
#
#         label = QLabel("Python GUI Development", self)
#         # label.setText("New Text is Here")
#         # label.move(100,100)
#         label.setFont(QFont("Sanserif", 15))
#         label.setStyleSheet('color:red')
#
#         # label.setText(str(12))
#         # label.setNum(15)
#         # label.clear()
#
#
# app = QApplication(sys.argv)
# window = Window()
# window.show()
# sys.exit(app.exec())

# Dragging and droppping code as follows. not editted code. It must customize.

import sys
import os
import glob
from PyQt6.QtWidgets import QApplication, QWidget, QListView, QAbstractItemView, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QStandardItemModel, QIcon, QStandardItem, QKeyEvent


class ListView_Left(QListView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.m_model = QStandardItemModel(self)
        self.setModel(self.m_model)
        self.setAcceptDrops(True)
        self.setIconSize(QSize(150, 150))
        self.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.setResizeMode(QListView.ResizeMode.Adjust)
        self.setViewMode(QListView.ViewMode.IconMode)

    def dropEvent(self, event):
        super().dropEvent(event)
        self.parent.listViewRight.model().removeRow(self.parent.listViewRight.currentIndex().row())


class ListView_Right(QListView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.m_model = QStandardItemModel(self)
        self.setModel(self.m_model)
        self.setAcceptDrops(True)
        self.setIconSize(QSize(150, 150))
        self.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.setResizeMode(QListView.ResizeMode.Adjust)
        self.setViewMode(QListView.ViewMode.IconMode)
        self.installEventFilter(self)

    def eventFilter(self, source, event):
        if event.type() == QKeyEvent.Type.KeyPress and event.key() == Qt.Key.Key_Delete:
            if source == self:
                row_indx = self.currentIndex().row()
                self.model().remove().removeRow(row_indx)
        return super().eventFilter(source, event)

    def dropEvent(self, event):
        super().dropEvent(event)
        self.parent.listViewLeft.model().removeRow(self.parent.listViewLeft.currentIndex().row())


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 1400, 500
        self.resize(self.window_width, self.window_height)

        layout = QHBoxLayout()
        self.setLayout(layout)

        self.listViewLeft = ListView_Left(self)
        layout.addWidget(self.listViewLeft)

        self.listViewRight = ListView_Right(self)
        layout.addWidget(self.listViewRight)

        self.loadIcons()

    def loadIcons(self):
        icon_folder = os.path.join(os.getcwd(), 'icons')
        for icon in glob.glob(os.path.join(icon_folder, '*.ico')):
            item = QStandardItem()
            item.setIcon(QIcon(icon))
            self.listViewLeft.m_model.appendRow(item)


if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 17px;
        }
    ''')

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')


# End of the drag and drop code


# line creating code starts from here,
#
#
# import sys
# from PyQt5 import QtWidgets, QtCore, QtGui
#
#
# class Scene(QtWidgets.QGraphicsScene):
#     def __init__(self, *args, **kwargs):
#         super(Scene, self).__init__(*args, **kwargs)
#
#         self.setSceneRect(QtCore.QRectF(0, 0, 500, 500))
#
#         self.line = None
#         self.graphics_line = None
#
#         self.start_point = QtCore.QPointF()
#         self.end_point = QtCore.QPointF()
#
#     def mousePressEvent(self, event):
#         self.start_point = event.scenePos()
#         self.end_point = self.start_point
#
#         self.line = QtCore.QLineF(self.start_point, self.end_point)
#         self.graphics_line = QtWidgets.QGraphicsLineItem(self.line)
#
#         self.update_path()
#         super().mousePressEvent(event)
#
#     def mouseMoveEvent(self, event):
#         if event.buttons() & QtCore.Qt.LeftButton:
#             self.end_point = event.scenePos()
#             self.update_path()
#         super(Scene, self).mouseMoveEvent(event)
#
#     def mouseReleaseEvent(self, event):
#         self.end_point = event.scenePos()
#         self.update_path()
#
#         super(Scene, self).mouseReleaseEvent(event)
#
#     def update_path(self):
#         if not self.start_point.isNull() and not self.end_point.isNull():
#             self.line.setP2(self.end_point)
#             self.graphics_line.setLine(self.line)
#             self.addItem(self.graphics_line)
#
#
# def main():
#     app = QtWidgets.QApplication(sys.argv)
#
#     view = QtWidgets.QGraphicsView()
#     view.setRenderHint(QtGui.QPainter.Antialiasing)
#
#     view.setMouseTracking(True)
#     scene = Scene()
#
#     view.setScene(scene)
#     view.show()
#
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()


# line creating code end
