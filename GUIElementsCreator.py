from ttkbootstrap import *
import ttkbootstrap as tb


def create_quit_button(new_root):
    close_button = tb.Button(new_root,text="Close", bootstyle="danger, outline",
                             command=new_root.quit)  # style

    close_button.pack(padx=50, pady=10)


def create_start_button(new_root):
    begin_button = tb.Button(new_root, text="Start", bootstyle="danger, outline")  # style

    begin_button.pack(padx=50, pady=20)

    return begin_button


def create_window():
    root = tb.Window(themename="solar")
    root.title("WhatsApp Web Message Sender")
    # root.iconbitmap("images/codemy.ico")
    root.geometry("720x500")
    root.grid_anchor(anchor="center")

    return root


def create_window_label(new_root):
    script_title = tb.Label(new_root,text="WhatsApp message sender", font=("Helvetica", 28),
                            bootstyle="success, inverse")

    script_title.pack(pady=50)


def create_entry_boxes(new_root):
    message_label = tb.Label(new_root, text="Write your message:", font=("Helvetica", 10))
    message_label.pack(pady=10)

    message_entry = tb.Entry(new_root, style="TEntry", width=100)  # Entry box constructor
    message_entry.pack()


    return message_label,  message_entry
