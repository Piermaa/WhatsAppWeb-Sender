def replace_values(base_messages, row):
    for base_message in base_messages:
        while '[' in base_message.base_text and ']' in base_message.base_text:
            # Find the first occurrence of '[' and ']'
            start_index = base_message.base_text.find('[')
            end_index = base_message.base_text.find(']')

            # Extract the substring within the square brackets
            placeholder = base_message.base_text[start_index + 1:end_index]

            # Check if the placeholder is a column in the Excel file
            if placeholder in row:
                # Get the value from the Excel file
                value = row[placeholder]

                # Replace the placeholder in the message with the value
                base_message.base_text = (base_message.base_text[:start_index] + str(value) +
                                          base_message.base_text[end_index + 1:])
            else:
                print(f"Column '{placeholder}' not found in the Excel file.")

    return base_messages