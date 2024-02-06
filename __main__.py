from tkinter import messagebox
from tkinter import Tk, ttk, filedialog
from FileImport import send_messages
from GUIElementsCreator import *
import WhatsAppMessage
from ttkbootstrap import *
import ttkbootstrap as tb


class MyFile:
    def __init__(self, new_file_path):
        self.file_path = new_file_path


def add_message():
    print("Added")
    if message_entry.get() == '':
        message_label.config(bootstyle="warning")
        print("Message null")
    else:
        new_message = WhatsAppMessage.WhatsAppMessage(message_entry.get(), current_file.file_path)
        messages.append(new_message)


def start_script():
    print("Starting script" + str(len(messages)))
    if len(messages) > 0:
        send_messages(messages)


def select_file():
    new_file_path = filedialog.askopenfilename(title="Select a file")
    if new_file_path:
        file_label.config(text="File selected: " + str(new_file_path))
        current_file.file_path = new_file_path

# ===================================================================================

#############
##VARIABLES##
#############

messages = []
current_file = MyFile("")


root = create_window()

#############
#####GUI#####
#############

create_window_label(root)
message_label, message_entry = create_entry_boxes(root)
file_label, file_button = create_file_button(root)
file_button.config(command=select_file)
create_button(root,"Add").config(command=add_message)
create_button(root,"Start").config(command=start_script)
create_button(root,"Quit").config(command=root.quit)


root.mainloop()
