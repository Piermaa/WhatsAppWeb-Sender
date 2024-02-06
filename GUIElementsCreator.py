from ttkbootstrap import *
import ttkbootstrap as tb
from tkinter import Tk, ttk, filedialog

def create_button(new_root, button_text):
    new_button = tb.Button(new_root, text=button_text, bootstyle="danger, outline")  # style

    new_button.pack(padx=50, pady=5)

    return new_button


def create_window():
    root = tb.Window(themename="solar")
    root.title("WhatsApp Web Message Sender")
    # root.iconbitmap("images/codemy.ico")
    root.geometry("720x500")
    root.grid_anchor(anchor="center")

    return root



def create_file_button(new_root):
    file_entry = tb.Label(new_root, text="Select a file")
    file_entry.pack(padx=10, pady=10)

    select_button = ttk.Button(new_root, text="Select File")
    select_button.pack(pady=10)

    return file_entry, select_button

def create_window_label(new_root):
    script_title = tb.Label(new_root,text="WhatsApp message sender", font=("Helvetica", 28),
                            bootstyle="success, inverse")

    script_title.pack(pady=50)


def create_entry_boxes(new_root):
    message_label = tb.Label(new_root, text="Write your message:", font=("Helvetica", 10))
    message_label.pack(pady=10)

    message_entry = tb.Entry(new_root, style="TEntry", width=100)  # Entry box constructor
    message_entry.pack()


    return message_label, message_entry
