import tkinter as tk
from tkinter import Entry, Button, Frame

class SearchBar(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white", height=50)

        self.pack_propagate(False)

        # Cuadro para ingresar la busqueda
        self.search_entry = Entry(self, width=50, font=("Arial", 14))
        self.search_entry.pack(side="left", padx=10, pady=10)

        # Botón
        self.search_button = Button(self, text="Buscar", bg="blue", fg="white", font=("Arial", 12))
        self.search_button.pack(side="right", padx=10)
