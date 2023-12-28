from string import ascii_letters, digits, punctuation
import random


class Encoder:
    def __init__(self):
        self.encoding_table = {}

    @staticmethod
    def create_encoding_table() -> dict:
        encoding_table = {}
        cyrillic_letters = 'абвгдежзийклмнопрстуфхцчшщъьюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЮЯ'
        all_chars_keys = ascii_letters + digits + punctuation + ' ' + '\n' + cyrillic_letters
        all_chars_values = all_chars_keys

        for ch in all_chars_keys:
            new_char = random.choice(all_chars_values)
            all_chars_values = all_chars_values.replace(new_char, '')
            encoding_table[ch] = new_char

        return encoding_table

    def encode(self, message: str) -> str:
        if not self.encoding_table:
            return 'There is no encoding table!'

        for ch in message:
            if ch not in self.encoding_table:
                continue
            message = message.replace(ch, self.encoding_table[ch])

        return message
