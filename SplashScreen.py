import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar, QLabel, QFrame, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer


class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Arduino Code Generator')
        self.setFixedSize(1100, 500)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.counter = 0
        self.n = 300  # total instance

        self.initUI()

        self.timer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(30)

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.frame = QFrame()
        layout.addWidget(self.frame)

        self.labelTitle = QLabel(self.frame)
        self.labelTitle.setObjectName('LabelTitle')

        # center labels
        self.labelTitle.resize(self.width() - 10, 150)
        self.labelTitle.move(0, 40)  # x, y
        self.labelTitle.setText('Arduino Code Generator')
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.labelDescription = QLabel(self.frame)
        self.labelDescription.resize(self.width() - 10, 50)
        self.labelDescription.move(0, self.labelTitle.height())
        self.labelDescription.setObjectName('LabelDesc')
        self.labelDescription.setText('<strong>Create Arduino projects</strong>')
        self.labelDescription.setAlignment(Qt.AlignCenter)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.resize(self.width() - 200 - 10, 50)
        self.progressBar.move(100, self.labelDescription.y() + 130)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setFormat('%p%')
        self.progressBar.setTextVisible(True)
        self.progressBar.setRange(0, self.n)
        self.progressBar.setValue(20)

        self.labelLoading = QLabel(self.frame)
        self.labelLoading.resize(self.width() - 10, 50)
        self.labelLoading.move(0, self.progressBar.y() + 70)
        self.labelLoading.setObjectName('LabelLoading')
        self.labelLoading.setAlignment(Qt.AlignCenter)
        self.labelLoading.setText('loading...')

    def loading(self):
        self.progressBar.setValue(self.counter)

        if self.counter == int(self.n * 0.3):
            self.labelDescription.setText('<strong>With your own idea</strong>')
        elif self.counter == int(self.n * 0.6):
            self.labelDescription.setText('<strong>Do easily and creatively with us</strong>')
        elif self.counter >= self.n:
            self.timer.stop()
            self.close()

            time.sleep(1)

            self.myApp = MyApp()
            self.myApp.show()

        self.counter += 1


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 1200, 800
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)


if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    app.setStyleSheet('''
        #LabelTitle {
            font-size: 60px;
            color: #93deed;
        }

        #LabelDesc {
            font-size: 30px;
            color: #c2ced1;
        }

        #LabelLoading {
            font-size: 30px;
            color: #e8e8eb;
        }

        QFrame {
            background-color: #2F4454;
            color: rgb(220, 220, 220);
        }

        QProgressBar {
            background-color: #DA7B93;
            color: rgb(200, 200, 200);
            border-style: none;
            border-radius: 10px;
            text-align: center;
            font-size: 30px;
        }

        QProgressBar::chunk {
            border-radius: 10px;
            background-color: qlineargradient(spread:pad x1:0, x2:1, y1:0.511364, y2:0.523, stop:0 #1C3334, stop:1 #376E6F);
        }
    ''')

    splash = SplashScreen()
    splash.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')





# start object detection code
#
# import tensorflow_hub as hub
# import cv2
# import numpy
# import tensorflow as tf
# import pandas as pd
#
# # Carregar modelos
# detector = hub.load("https://tfhub.dev/tensorflow/efficientdet/lite2/detection/1")
# labels = pd.read_csv('labels.csv', sep=';', index_col='ID')
# labels = labels['OBJECT (2017 REL.)']
#
# cap = cv2.VideoCapture(0)
#
# width = 512
# height = 512
#
# while (True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#
#     # Resize to respect the input_shape
#     inp = cv2.resize(frame, (width, height))
#
#     # Convert img to RGB
#     rgb = cv2.cvtColor(inp, cv2.COLOR_BGR2RGB)
#
#     # Is optional but i recommend (float convertion and convert img to tensor image)
#     rgb_tensor = tf.convert_to_tensor(rgb, dtype=tf.uint8)
#
#     # Add dims to rgb_tensor
#     rgb_tensor = tf.expand_dims(rgb_tensor, 0)
#
#     boxes, scores, classes, num_detections = detector(rgb_tensor)
#
#     pred_labels = classes.numpy().astype('int')[0]
#
#     pred_labels = [labels[i] for i in pred_labels]
#     pred_boxes = boxes.numpy()[0].astype('int')
#     pred_scores = scores.numpy()[0]
#
#     # loop throughout the detections and place a box around it
#     for score, (ymin, xmin, ymax, xmax), label in zip(pred_scores, pred_boxes, pred_labels):
#         if score < 0.5:
#             continue
#
#         score_txt = f'{100 * round(score, 0)}'
#         img_boxes = cv2.rectangle(rgb, (xmin, ymax), (xmax, ymin), (0, 255, 0), 1)
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         cv2.putText(img_boxes, label, (xmin, ymax - 10), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
#         cv2.putText(img_boxes, score_txt, (xmax, ymax - 10), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
#
#     # Display the resulting frame
#     cv2.imshow('black and white', img_boxes)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()


# end object detection code


# !/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt6 import *



# import sys
# from random import randint
# from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget)
#
#
# class AnotherWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.label = QLabel("Another Window % d" % randint(0, 100))
#         layout.addWidget(self.label)
#         self.setLayout(layout)
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.window1 = AnotherWindow()
#         self.window2 = AnotherWindow()
#
#         l = QVBoxLayout()
#         button1 = QPushButton("Push for Window 1")
#         button1.clicked.connect(self.toggle_window1)
#         l.addWidget(button1)
#
#         button2 = QPushButton("Push for Window 2")
#         button2.clicked.connect(self.toggle_window2)
#         l.addWidget(button2)
#
#         w = QWidget()
#         w.setLayout(l)
#         self.setCentralWidget(w)
#
#     def toggle_window1(self, checked):
#         if self.window1.isVisible():
#             self.window1.hide()
#         else:
#             self.window1.show()
#
#     def toggle_window2(self, checked):
#         if self.window2.isVisible():
#             self.window2.hide()
#         else:
#             self.window2.show()
#
#
# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# app.exec()








