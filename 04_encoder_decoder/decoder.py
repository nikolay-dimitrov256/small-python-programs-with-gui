class Decoder:
    def __init__(self):
        self.decoding_table = {}

    def create_decoding_table(self, encoding_table: dict) -> None:
        self.decoding_table = {v: k for k, v in encoding_table.items()}

    def decode(self, message: str) -> str:
        if not self.decoding_table:
            return 'There is no decoding table!'

        for ch in message:
            message = message.replace(ch, self.decoding_table[ch])

        return message
