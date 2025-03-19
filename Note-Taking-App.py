# import modules
import tkinter as tk
from tkinter import messagebox
import requests
# Creating a function for Note app
class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note App")
        self.title_label = tk.Label(root, text="Title:")
        self.title_label.pack()
        self.title_entry = tk.Entry(root)
        self.title_entry.pack()
        self.content_label = tk.Label(root, text="Content:")
        self.content_label.pack()
        self.content_entry = tk.Text(root)
        self.content_entry.pack()
        self.save_button = tk.Button(root, text="Save", command=self.save_note)
        self.save_button.pack()
    def save_note(self):
        title = self.title_entry.get()
        content = self.content_entry.get("1.0", "end-1c")
        response = requests.post('http://localhost:5000/notes', json={'title': title, 'content': content})
# Conditional statements
        if response.status_code == 201:
            messagebox.showinfo("Success", "Note saved successfully")
        else:
            messagebox.showerror("Error", "Failed to save note")
# Main function
if __name__ == '__main__':
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()

