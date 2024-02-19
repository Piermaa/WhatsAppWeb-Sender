from ttkbootstrap import *
import ttkbootstrap as tb
from tkinter import Tk, ttk, filedialog

def create_button(new_root, button_text, side):
    new_button = tb.Button(new_root, text=button_text, bootstyle="danger, outline")  # style

    new_button.pack(padx=20, side="left")

    return new_button


def create_window():
    root = tb.Window(themename="solar")
    root.title("WhatsApp Web Message Sender")
    # root.iconbitmap("images/codemy.ico")
    root.geometry("720x500")
    root.grid_anchor(anchor="center")

    return root



def create_file_button(new_root, label_text):
    file_entry_label = tb.Label(new_root, text=label_text)
    file_entry_label.pack(padx=10, pady=1)

    select_button = ttk.Button(new_root, text="Select File")
    select_button.pack(pady=1)

    return file_entry_label, select_button

def create_window_label(new_root):
    script_title = tb.Label(new_root,text="WhatsApp message sender", font=("Helvetica", 28),
                            bootstyle="success, inverse")

    script_title.pack(pady=30)


def create_entry_boxes(new_root):
    message_label = tb.Label(new_root, text="Write your message:", font=("Helvetica", 10))
    message_label.pack(pady=1)

    message_entry = tb.Entry(new_root, style="TEntry", width=100)  # Entry box constructor
    message_entry.pack()


    return message_label, message_entry
