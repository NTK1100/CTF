import hashlib
import base64
import tkinter as tk
from tkinter import messagebox
import sys

def check_debugger():
    if hasattr(sys, 'gettrace'):
        if sys.gettrace():
            sys.exit('Debugging detected! Exiting...')
            return None
        return None


def f1(n):
Unsupported opcode: BINARY_SLICE
    h = hashlib.md5(n.encode()).hexdigest()
# WARNING: Decompyle incomplete

encoded_flag = base64.b64encode(b'EnXp{C0rr3ct_P@$$w0rd123}').decode()

def f2():
    n = f3.get()
    p = f4.get()
    if len(p) != 12:
        messagebox.showerror('Error', 'Password must be exactly 12 characters long')
        return None
    cp = f1(n)
    if p == cp:
        decoded_flag = base64.b64decode(encoded_flag).decode()
        messagebox.showinfo('Success', f'''Login successful! Here\'s your flag: {decoded_flag}''')
        return None
    messagebox.showerror('Error', 'Incorrect password. Please try again.')

root = tk.Tk()
root.title('Login Window')
f5 = tk.Label(root, text = 'Enter your name:')
f5.pack(pady = 5)
f3 = tk.Entry(root)
f3.pack(pady = 5)
f6 = tk.Label(root, text = 'Enter your 12 char password:')
f6.pack(pady = 5)
f4 = tk.Entry(root)
f4.pack(pady = 5)
f7 = tk.Button(root, text = 'Login', command = f2)
f7.pack(pady = 10)
check_debugger()
root.mainloop()
