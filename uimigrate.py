# set_window_geometry.py
from tkinter import Tk, Label, Button, Entry, INSERT
root = Tk()

# Make window 300x150 and place at position (50,50)
root.geometry("300x400+50+50")
root.title("UI Migrate")

# Create a label as a child of root window
entries = [Label(root, text='Current Realm'), Entry(root),
          Label(root, text='Target Realm'), Entry(root),
          Label(root, text='Current Account'), Entry(root),
          Label(root, text='Target Account'), Entry(root),
          Label(root, text='Current Character'), Entry(root),
          Label(root, text='Target Character'), Entry(root)]

for ent in entries:
    if type(ent) == Entry:
        ent.insert(INSERT, "Hello, world!")
    ent.pack()

# Print the contents of entry widget to console
def print_content():
    for ent in entries:
         if type(ent) == Entry:
             print(ent.get())

# Create a button that will print the contents of the entry
run_button = Button(root, text='Migrate', command=print_content)
run_button.pack()

# Create a button that will destroy the main window when clicked
exit_button = Button(root, text='Exit Program', command=root.destroy)
exit_button.pack()

root.mainloop()
