import tkinter as tk
from tkinter import Frame
from side_menu import SideMenu
from search_bar import SearchBar
from video_gallery import VideoGallery

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("YouTube Fake")
        self.geometry("1000x600")
        self.configure(bg="white")

        # Panel que contiene el menú lateral
        self.side_menu = SideMenu(self)
        self.side_menu.pack(side="left", fill="y")

        # Contenedor principal
        main_container = Frame(self, bg="white")
        main_container.pack(side="right", fill="both", expand=True)

        # Barra de búsqueda
        self.search_bar = SearchBar(main_container)
        self.search_bar.pack(fill="x")

        # Sección que contiene los videos
        self.video_gallery = VideoGallery(main_container)
        self.video_gallery.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
