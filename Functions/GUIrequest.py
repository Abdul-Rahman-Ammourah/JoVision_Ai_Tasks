import tkinter as tk
from tkinter import filedialog
def open_image_file():
    # Create a Tkinter Window
    root = tk.Tk()
    root.withdraw() 

    # Open file dialog
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
    )

    if file_path:
        return file_path
    else:
        print("No file selected.")
        exit(0)