from decoder import Decoder
from encoder import Encoder
from encoding_decoding_app import EncodingDecodingApp

encoder_ = Encoder()
decoder_ = Decoder()
enigma = EncodingDecodingApp('Enigma', encoder_, decoder_)
enigma.run()
