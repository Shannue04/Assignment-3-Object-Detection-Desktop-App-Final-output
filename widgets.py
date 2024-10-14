import customtkinter as ctk
import tkinter as tk
import cv2
from PIL import Image, ImageTk

#encapsulation
#Generalization
class Widget:
    root = None
    title = None
    row = None
    padx = 10
    pady = 10
    def __init__(self, root, title, row):
        self.root = root
        self.title = title
        self.row = row
    
    def build(self):
        pass

#inheritance
class Label(Widget):
    col = None
    def __init__(self, root, title, row, col):
        super().__init__(root, title, row)
        self.col = col
    #polymorphism and method overriding
    def build(self):
        _label = ctk.CTkLabel(self.root, text=self.title)
        _label.grid(row=self.row, column=self.col, padx=self.padx, pady=self.pady)
        return _label



#inheritance
class Slider(Widget):
    from_ = None
    to = None
    number_of_steps = None
    label = None

    def __init__(self, root, title, row, from_, to, number_of_steps):
        super().__init__(root, title, row)
        self.from_ = from_
        self.to = to
        self.number_of_steps = number_of_steps

    def sliderc(self, pp):
        self.label = Label(self.root, self.title+f"({pp*100:.2f} %)", row=self.row, col=0)
        self.label.build()

    #polymorphism and method overriding
    def build(self):
        self.label = Label(self.root, self.title+f"({50} %)", self.row, 0)
        self.label.build()
        _slider = ctk.CTkSlider(self.root, from_=self.from_, to=self.to, number_of_steps=self.number_of_steps, command=self.sliderc)
        _slider.grid(row=self.row, column=1, padx=self.padx, pady=self.pady)
        return _slider
    

#inheritance
class Button(Widget):
    on_click = None

    def __init__(self, root, title, row, on_click):
        super().__init__(root, title, row)
        self.on_click = on_click

    #polymorphism and method overriding
    def build(self):
        _button = ctk.CTkButton(self.root, text=self.title, command=self.on_click)
        _button.grid(row=self.row, column=0, columnspan=2, sticky="news", padx=self.padx, pady=self.pady)
        return _button
        
