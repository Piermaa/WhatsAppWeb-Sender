from FileImport import send_messages
from GUIElementsCreator import *
from ttkbootstrap import *
import ttkbootstrap as tb


def checker():
    print("botontocheckiau")


def start_script():
    message = None
    values = None


    if message_entry.get() == '':
       # message_entry.config(bootsyle="danger")
        message_label.config(bootstyle="primary")
        print("Message null")
    else:
        message = message_entry.get()

    if values_entry.get() == '':
        print("Value null")
        values_label.config(bootstyle="primary")
    else:
        values = values_entry.get()

        try:
            values = int(values)
        except:
            print("Value is not an integer")
            values_label.config(bootstyle="warning")



    if message is not None and values is not None:
        send_messages(message, values)



# </editor-fold>
root = create_window()
create_window_label(root)
message_label, values_label, message_entry, values_entry = create_entry_boxes(root)
create_start_button(root).config(command=start_script)
create_quit_button(root)

# <editor-fold desc="Checks">

#message_is_file = BooleanVar()
#check = tb.Checkbutton(root, bootstyle="info, square-toggle",
#                           text="Yes",
#                           variable=message_is_file,
#                           onvalue=True,
#                           offvalue=False,
#                           command=checker)
#check.pack(pady=10, padx=20)

# </editor-fold>

root.mainloop()
