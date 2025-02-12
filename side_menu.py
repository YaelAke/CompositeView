import tkinter as tk
from tkinter import Button, Frame

class SideMenu(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="gray", width=200)

        self.pack_propagate(False)  

        # Botones para el menu lateral
        btn_inicio = Button(self, text="Inicio", bg="white", fg="black", height=2, width=20)
        btn_historial = Button(self, text="Favoritos", bg="white", fg="black", height=2, width=20)
        btn_perfil = Button(self, text="Historial", bg="white", fg="black", height=2, width=20)
        btn_perfil = Button(self, text="Perfil", bg="white", fg="black", height=2, width=20)
        btn_cerrar = Button(self, text="Cerrar Sesión", bg="red", fg="white", height=2, width=20)

        btn_inicio.pack(pady=10)
        btn_historial.pack(pady=10)
        btn_perfil.pack(pady=10)
        btn_cerrar.pack(pady=20)
