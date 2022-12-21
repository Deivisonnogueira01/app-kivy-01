from kivy.app import App
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.image import AsyncImage
from kivy.app import App
from kivy.lang import Builder
import os
import random
import requests


ip_url="http://192.168.43.23:5000"


user1=None
user2=None


class AppCamera(ScreenManager):
  pass

class Home(Screen):
  pass

""" class Chat(Screen):
  pass
class CameraClick(Screen):
  pass """

class MeuAplicativo(App):
    def build(self):
        self.file = Builder.load_file("sala.kv")
        return self.file
  
    def nova_sala(self):
        request=requests.get(ip_url+"/nova-sala")
        json = request.json()
        chave_acesso = json['path']
        self.file.get_screen('home').ids['idsala'].text=f'Seu Código {chave_acesso}'
        return  
  
    def velha_sala(self):
        cod_room = {"data":self.file.get_screen('home').ids["inpt_codigo_room"].text}
        print(cod_room)
        response=requests.post(ip_url+"/join_room",json=cod_room)
        message = response.json()
        if message['message'] ==True:
            print(message['message'])  
        if message['message'] ==False:
            self.file.get_screen('home').ids['idsala'].text=f'Erro'


    def capture(self):
        cod_room = self.file.get_screen('home').ids["inpt_codigo_room"].text
        user = "user2"
        print(cod_room)
        if user =="user1":
            camera = self.file.get_screen('camera').ids['camera']
            camera.export_to_png("user1.png")
            files = {
                "file":"/home/cbyk-dev/Documents/api-py-teti/static/fotos/foto-user1.png",
                "code_room":cod_room,
                "user":user
            }
        if user =="user2":
            camera = self.file.get_screen('camera').ids['camera']
            camera.export_to_png("user2.png")
            files = {
            "file":"/home/cbyk-dev/Documents/api-py-teti/static/fotos/foto-user1.png",
            "code_room":cod_room,
            "user":user
            }
        print(files)
        requests.post(ip_url+"/new_message",json=files)


    def capture(self):
        cod_room = self.file.get_screen('home').ids["inpt_codigo_room"].text
        user = "user2"
        print(cod_room)
        if user =="user1":
            camera = self.file.get_screen('home').ids['camera']
            camera.export_to_png("user1.png")
            files = {
                "file":"/home/cbyk-dev/Documents/api-py-teti/user1.png",
                "code_room":cod_room,
                "user":user
            }
        if user =="user2":
            camera = self.file.get_screen('home').ids['camera']
            camera.export_to_png("user2.png")
            files = {
            "file":"/home/cbyk-dev/Documents/api-py-teti/user2.png",
            "code_room":cod_room,
            "user":user
            }
        print(files)
        requests.post(ip_url+"/new_message",json=files)
    
    def get_message(self):
        request=requests.get(ip_url+"/get_message")
        json = request.json()
        chave_sala = json['path']
        print(chave_sala)
        self.file.get_screen('home').ids['imguser'].source = chave_sala  

MeuAplicativo().run()

       