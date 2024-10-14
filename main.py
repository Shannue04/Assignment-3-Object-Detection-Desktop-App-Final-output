import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog

from PIL import Image, ImageTk
from widgets import Label, Button, Slider
from formater import Formater
from object_detector import ObjectDetector


def on_generate_click():
    print('Generating')
    detector = ObjectDetector.get_instance()
    print('instance created')
    threshold = slider.get()
    print(threshold)
    output_path = detector.detect('temp/temp_image.jpg', threshold=threshold)
    print(f'output path {output_path}')

    image = Image.open(output_path)

    tk_image = ImageTk.PhotoImage(image=image)
    canvas.image = tk_image
    canvas.create_image(0,0,anchor="nw", image=tk_image)


def upload_image():
    root.title('Image uploaed')
    image_path = filedialog.askopenfilename()
    copy_path = Formater.get_a_coppied_path(path=image_path)

    image = Image.open(copy_path)

    tk_image = ImageTk.PhotoImage(image=image)
    canvas.image = tk_image
    canvas.create_image(0,0,anchor="nw", image=tk_image)
    


root = ctk.CTk()
root.title("Peack Image")

ctk.set_appearance_mode("dark")

visible_area = ctk.CTkFrame(root)
visible_area.pack(side="top", expand=True, padx=10, pady=10)

canvas = tk.Canvas(visible_area, width=512, height=512)
canvas.pack(side="left")

buttons_area = ctk.CTkFrame(root)
buttons_area.pack(side="bottom", expand=True,  padx=20, pady=20)

title_label = Label(buttons_area, 'Upload an Image and detect it\'s Objects', 0, 0)
title_label.build()
upload_button = Button(buttons_area, 'Upload', 1, upload_image)
upload_button.build()
threshold_slider = Slider(buttons_area, "Threshold : ", 2, 0.1, 1.0, 1000)
slider = threshold_slider.build()
generate_button = Button(buttons_area, 'Detect Objects', 3, on_click=on_generate_click)
generate_button.build()


root.mainloop()
