from pdf2image import convert_from_path
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def pdf2img():
    try:
        images = convert_from_path(file_location.get(), 500, poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
        for i, image in enumerate(images):
            file_name = 'image' + str(i) + '.png'
            image.save(file_name, "PNG")
    except:
        result = "No PDF Found"
        messagebox.showinfo("Result", result)
    else:
        result = "The file is successfully converted."
        messagebox.showinfo("Result", result)


# UI
root = tk.Tk()
root.title('PDF Extract App')

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=4)

# logo
logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.grid(column=1, row=0, columnspan= 2)

# instructions
instructions = tk.Label(root, text='Paste the file location to convert.')
instructions.grid(columnspan=4, column=0, row=1)

# File location entry
file_location = tk.Entry(root)
file_location.grid(column=1, row=2, sticky= "E")

# Convert button
convert_button = tk.Button(root, text='Convert', command=pdf2img)
convert_button.grid(row=2, column=2, padx=5, pady=5, sticky= "W")

root.mainloop()
