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
        send_messages(messages, excel_filepath)


def select_file():
    new_file_path = filedialog.askopenfilename(title="Select a file")
    if new_file_path:
        message_file_label.config(text="File selected: " + str(new_file_path))
        current_file.file_path = new_file_path

def select_excel_file():
    new_file_path = filedialog.askopenfilename(title="Select the .xls or .xlsx file")
    if new_file_path:
        excel_file_label.config(text="File selected: " + str(new_file_path))
        global excel_filepath
        excel_filepath = new_file_path
# ===================================================================================

#############
##VARIABLES##
#############

messages = []
current_file = MyFile("")
excel_filepath = ""

root = create_window()

#############
#####GUI#####
#############

create_window_label(root)
# Create Excel file
excel_file_label, excel_file_button = create_file_button(root, "Select .xls or .xlsx")

ttk.Frame(root, width=10).pack(pady=20)

# Message creation
message_label, message_entry = create_entry_boxes(root)

ttk.Frame(root, width=10).pack(pady=10)

message_file_label, message_file_button = create_file_button(root, "Select file to attach")
message_file_button.config(command=select_file)

ttk.Frame(root, width=10).pack(pady=5)

#Buttons creation

ttk.Frame(root, width=10).pack(padx=108,side="left")
create_button(root,"Add","left").config(command=add_message)
create_button(root,"Start","left").config(command=start_script)
create_button(root,"Quit","right").config(command=root.quit)


root.mainloop()
