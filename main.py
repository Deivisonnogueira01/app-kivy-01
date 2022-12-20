import time
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.app import App
from flask import Flask
from random import random
# import numpy
# import cv2
from datetime import datetime
from zipfile import ZipFile

app = Flask(__name__)


# @app.route("/")
# def main():
#     return primeira_tela.py


# app.route("/cadastro", methods=["GET", "POST"])
# def cadastro():
#     if request.method == "GET":
#         return null
#     if request.method == "POST":
#         name = request.form.get('Name')
#         return null


# @app.route("/api", methods=["GET", "POST"])
# def recebaToken():
#     token = 'receba'
#     if request.method == 'GET':
#         tokenForm = request.form.get('token')
#         if tokenForm == token:
#             return null
#     return null

'''
Camera Example
==============

This example demonstrates a simple use of the camera. It shows a window with
a buttoned labelled 'play' to turn the camera on and off. Note that
not finding a camera, perhaps because gstreamer is not installed, will
throw an exception during the kv language processing.

'''


@app.route('/')
def main():
    Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")


class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()
