import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from PIL import Image
import re


class ImageResize:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Photo resize')
        self.load_button = tk.Button(self.root, text='Load files', command=self.load_files)
        self.textbox = scrolledtext.ScrolledText(height=7, width=30)
        self.button_frame = tk.Frame(self.root)
        self.btn_300_400 = tk.Button(self.button_frame, text='Resize 300x400',
                                     command=lambda r=(300, 400): self.resize_photo(r))
        self.btn_240_320 = tk.Button(self.button_frame, text='Resize 240x320',
                                     command=lambda r=(240, 320): self.resize_photo(r))

        self.place_widgets()

    def place_widgets(self):
        self.load_button.pack(pady=5)
        self.textbox.pack(padx=10, pady=5)
        self.button_frame.pack(pady=5)
        self.btn_300_400.grid(row=0, column=0, sticky=tk.W)
        self.btn_240_320.grid(row=0, column=1, sticky=tk.E)

    def load_files(self):
        self.files = filedialog.askopenfilenames(title='Chose files')

        self.textbox.delete('1.0', tk.END)

        for file in self.files:
            filename = file.split('/')[-1]
            self.textbox.insert('1.0', filename + '\n')

    def resize_photo(self, resolution: tuple):
        destination_folder = filedialog.askdirectory()
        if not destination_folder:
            return None

        self.textbox.delete('1.0', tk.END)
        row = 1.0

        for file in self.files:
            image = Image.open(file)
            new_image = image.resize(resolution)

            filename = file.split('/')[-1]
            match = re.search(r'(\d{5})([a-z])', filename)

            if match:
                product_number = match.group(1)
                suffix = match.group(2)

                if resolution == (240, 320) and suffix != 'a':
                    continue

                suffix = suffix if resolution == (300, 400) else ''
                path = f'{destination_folder}/{product_number}{suffix}.jpg'

                new_image.save(path)

            else:
                self.textbox.insert(str(row), f'Invalid file name {filename}\n')
                row += 1

        self.textbox.insert(str(row), 'Images saved.\n')

    def run(self):
        self.root.mainloop()


image_resize = ImageResize()
image_resize.run()
