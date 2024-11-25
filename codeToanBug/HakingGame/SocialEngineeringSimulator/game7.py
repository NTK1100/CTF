#Hidden Key Decryption
class HiddenKeyDecryption:
    def __init__(self):
        self.flag = "CTB{fake_flag}"
        self.encryption_key = 35  # Hidden key for XOR decryption
        self.encrypted_flag = self.encrypt_flag(self.flag)

    def encrypt_flag(self, flag):
        return ''.join(chr(ord(char) ^ self.encryption_key) for char in flag)

    def print_intro(self):
        print("=" * 60)
        print("Welcome to Hidden Key Decryption!")
        print("You must uncover the hidden key to reveal the flag.")
        print("=" * 60)

    def attempt_decryption(self):
        attempt = input("Enter decryption key: ")
        try:
            attempt_key = int(attempt)
            decrypted_flag = ''.join(chr(ord(char) ^ attempt_key) for char in self.encrypted_flag)
            if decrypted_flag.startswith("FLAG"):
                print(f"Success! FLAG: {decrypted_flag}")
            else:
                print("Incorrect key. Try again.")
        except ValueError:
            print("Invalid input. Enter a numerical key.")

    def play(self):
        self.print_intro()
        print("Hint: The key may be hidden somewhere in the code.")
        for _ in range(3):
            self.attempt_decryption()

# Start game
game = HiddenKeyDecryption()
game.play()
