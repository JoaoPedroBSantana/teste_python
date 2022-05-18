'''from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout'''
import forca
import teste

def escolha_jogo():
    print("*********************************")
    print("Bem vindo, escolha o seu jogo!")
    print("*********************************")

    print("(1) FORCA (2) ADIVINHACAO")

    jogo = int(input("Qual o jogo? "))

    if jogo == 1:
        print("Jogando forca")
        forca.jogar()
    elif jogo == 2:
        print("Jogando adivinhaçao")
        teste.jogar()
    else:
        print("Opçao invalida")

if __name__ == "__main__":
    escolha_jogo()