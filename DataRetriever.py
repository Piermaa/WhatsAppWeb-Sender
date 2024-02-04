import ttkbootstrap as tb


class DataRetriever:

    message_entry = tb.Entry()
    value_entry = tb.Entry()

    def __init__(self, p_message_entry, p_values_entry):
        self.message_entry = p_message_entry
        self.value_entry = p_values_entry

    def retrieve_data(self):
        return self.message_entry.get(), self.value_entry.get()
