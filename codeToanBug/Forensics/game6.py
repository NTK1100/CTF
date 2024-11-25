#Steganographic Image Embedding Challenge
from PIL import Image
import random

class SteganographyChallenge:
    def __init__(self):
        self.flag = "CTB{fake_flag!}"
        self.image_path = "stego_image.png"
        self.embed_flag()

    def embed_flag(self):
        img = Image.new('RGB', (100, 100), "blue")
        pixels = img.load()
        binary_flag = ''.join(format(ord(c), '08b') for c in self.flag)

        i = 0
        for y in range(100):
            for x in range(100):
                if i < len(binary_flag):
                    bit = int(binary_flag[i])
                    r, g, b = pixels[x, y]
                    r = (r & ~1) | bit
                    pixels[x, y] = (r, g, b)
                    i += 1

        img.save(self.image_path)
        print(f"Flag embedded in image '{self.image_path}'.")

    def print_intro(self):
        print("=" * 60)
        print("🖼️ Steganographic Image Embedding Challenge")
        print("Extract the hidden flag from the image.")
        print("=" * 60)

    def play(self):
        self.print_intro()
        print(f"The image has been saved at '{self.image_path}'")

# Start the game
game = SteganographyChallenge()
game.play()
