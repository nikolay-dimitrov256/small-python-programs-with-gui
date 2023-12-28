import datetime
import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import json
import os

from encoder import Encoder
from decoder import Decoder


class EncodingDecodingApp:
    def __init__(self, title: str, encoder: Encoder, decoder: Decoder):
        self.encoder = encoder
        self.decoder = decoder
        self.window = tk.Tk()
        self.window.title(title)
        self.system_entry = ttk.Entry(self.window, foreground='green', width=50)
        self.message_entry = ttk.Entry(self.window, width=50)
        self.result_box = scrolledtext.ScrolledText(self.window, width=50, height=10)
        self.render_widgets()

    def render_widgets(self):
        ttk.Separator(self.window).grid(row=0, columnspan=2, sticky='we', pady=5)
        self.system_entry.grid(row=1, columnspan=2, sticky='we', padx=5)
        self.system_entry.insert(0, 'Please load or create encoding table.')
        self.system_entry['state'] = 'readonly'
        ttk.Button(self.window, text='Load encoding table', command=self.load_table).grid(
            row=2, column=0, padx=5, sticky='w')
        ttk.Button(self.window, text='Create encoding table', command=self.create_table).grid(
            row=2, column=1, padx=5, pady=5, sticky='e')
        ttk.Separator(self.window).grid(row=3, columnspan=2, sticky='we', pady=5)
        ttk.Label(self.window, text='Enter your message here:', foreground='green').grid(
            row=4, columnspan=2, sticky='we', padx=5)
        self.message_entry.grid(row=5, columnspan=2, sticky='we', padx=5)
        ttk.Button(self.window, text='Encode', command=self.encode_message).grid(
            row=6, column=0, padx=5, pady=5, sticky='w')
        ttk.Button(self.window, text='Decode', command=self.decode_message).grid(
            row=6, column=1, padx=5, pady=5, sticky='e')
        ttk.Separator(self.window).grid(row=7, columnspan=2, sticky='we', pady=5)
        ttk.Label(self.window, text='Result:', foreground='green').grid(
            row=8, column=0, sticky='w', padx=5)
        self.result_box.grid(row=9, columnspan=2, sticky='we', padx=5, pady=5)

    def output_message(self, message: str, color: str = 'black'):
        self.system_entry['state'] = 'normal'
        self.system_entry.delete(0, tk.END)
        self.system_entry.insert(0, message)
        self.system_entry['foreground'] = color
        self.system_entry['state'] = 'readonly'

    def output_result(self, text: str):
        self.result_box.delete('1.0', tk.END)
        self.result_box.insert('1.0', text)


    def load_table(self):
        result = filedialog.askopenfilename()
        if result is None:
            return None

        try:
            with open(result, 'r') as file:
                self.encoder.encoding_table = json.loads(file.read())
                self.decoder.create_decoding_table(self.encoder.encoding_table)
                self.output_message('Encoding table successfully loaded', 'green')

        except Exception:
            self.output_message('There was a problem loading the table. Please try again.', 'red')

    def create_table(self):
        current_time = datetime.datetime.now()
        date = current_time.strftime('%d-%b-%Y')
        file_name = f'Encoding table {date}.txt'

        if os.path.exists(file_name):
            overwrite = messagebox.askyesno('Existing table', message=f'{file_name} already exists. Overwrite?')
            if not overwrite:
                self.output_message('New encoding table not created')
                return None

        encoding_table = self.encoder.create_encoding_table()
        self.encoder.encoding_table = encoding_table
        self.decoder.create_decoding_table(encoding_table)

        with open(file_name, 'w') as file:
            file.write(json.dumps(encoding_table))

        self.output_message(f'{file_name} was successfully created and loaded.', 'green')

    def encode_message(self):
        if not self.encoder.encoding_table:
            self.output_message('No encoding table loaded!', 'red')
            return None

        message = self.message_entry.get()
        encoded_message = self.encoder.encode(message)

        self.output_result(encoded_message)

    def decode_message(self):
        if not self.decoder.decoding_table:
            self.output_message('No encoding table loaded!', 'red')
            return None

        message = self.message_entry.get()
        decoded_message = self.decoder.decode(message)

        self.output_result(decoded_message)

    def run(self):
        self.window.mainloop()
