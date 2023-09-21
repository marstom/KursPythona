import tkinter as tk


# Function to retrieve text from the text area
def save_text(text_area):
    text = text_area.get("1.0", "end-1c")  # Get text from the beginning (1.0) to the end (end-1c)
    print("Text in the text area:", text)

def undo(text_area):
    text = text_area.setvar()
    text_area.delete("1.0", "end")  # Clear the current text
    text_area.insert("1.0", "New text here undo to impoelemn")  # Insert the new text


# Function to get the cursor position
def get_cursor_position(text_area):
    cursor_position = text_area.index(tk.INSERT)
    print("Cursor Position:", cursor_position)

# Function to set the cursor position
def set_cursor_position(text_area, line, column):
    position = f"{line}.{column}"
    text_area.mark_set(tk.INSERT, position)
    print("Set cursor positon!")


# def set_text(new_text):
def main():


    # Create the main window
    root = tk.Tk()
    root.title("Text Area Example")

    # Create a Text widget for the text area
    text_area = tk.Text(root, height=10, width=30)
    text_area.pack()

    # Create a button to retrieve the text
    save_text_button = tk.Button(root, text="Save Text", command=lambda: save_text(text_area))
    save_text_button.pack()

    undo_button = tk.Button(root, text="Undo", command=lambda: undo(text_area))
    undo_button.pack()

    # Start the Tkinter main loop
    root.mainloop()


if __name__ == '__main__':
    main()