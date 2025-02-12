import tkinter as tk
from tkinter import Label, Frame, Canvas
from PIL import Image, ImageTk
import os 

class VideoCard(Frame):
    def __init__(self, parent, image_path, title):
        super().__init__(parent, bg="white", padx=10, pady=10)

        if os.path.exists(image_path):
            img = Image.open(image_path)
            img = img.resize((150, 100), Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(img)

            
            self.image_label = Label(self, image=self.img)
            self.image_label.pack()
        else:
            # Si la imagen no existe, remplazarlo con un color de fondo
            self.image_label = Canvas(self, width=150, height=100, bg="gray")
            self.image_label.create_text(75, 50, text="Sin imagen", fill="white", font=("Arial", 10, "bold"))
            self.image_label.pack()

        # Etiqueta de título
        self.title_label = Label(self, text=title, bg="white", font=("Arial", 12, "bold"), wraplength=150)
        self.title_label.pack(pady=5)
