import tkinter as tk
from tkinter import Frame
from video_card import VideoCard

class VideoGallery(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")

        # Lista de videos
        videos = [
            ("video1.jpg", "Tutorial"),
            ("video2.jpg", "Lana del Rey"),
            ("video3.jpg", "¡Como dejar de procastinar?"),
            ("video4.jpg", "Bad Bunny"),
            ("inexistente.jpg", "Video sin imagen disponible"), 
            ("video5.jpg", "Caifanes")  
        ]

        # Agregar videos en un cuadro
        row, col = 0, 0
        for image, title in videos:
            video_card = VideoCard(self, image, title)
            video_card.grid(row=row, column=col, padx=10, pady=10)

            col += 1
            if col >= 3:  # Cantidad de videos que tendra cada fila
                col = 0
                row += 1
