# set_window_geometry.py
import uimFuncs, os

from tkinter import *
root = Tk()

# Make window 300x150 and place at position (50,50)
root.geometry("300x400+50+50")
root.title("UI Migrate")

status = StringVar()
status.set("Status")

# Create a label as a child of root window
entries = [Label(root, text='Current Account'), Entry(root),
          Label(root, text='Target Account'), Entry(root),
          Label(root, text='Current Realm'), Entry(root),
          Label(root, text='Target Realm'), Entry(root),
          Label(root, text='Current Character'), Entry(root),
           Label(root, text='Target Character'), Entry(root),
           Label(root, textvariable=status)]

entries[1].insert(INSERT, 'acc')
entries[3].insert(INSERT, 'newacc')
entries[5].insert(INSERT, 'realm')
entries[7].insert(INSERT, 'newrealm')
entries[9].insert(INSERT, 'char')
entries[11].insert(INSERT, 'newchar')


for ent in entries:
    ent.pack()

def migrate():
    """Where the magic happens"""
    indata = []
    for ent in entries:
        if type(ent) == Entry and ent.get().strip() != '':
            indata.append(ent.get().strip())

    #print(indata)

    if len(indata) != 6:
        print("Error: Empty field(s)")
        status.set("Error: Empty field(s)")
        return

    oldPath = uimFuncs.getPaths(indata[0],indata[2], indata[4])
    newPath = uimFuncs.getPaths(indata[1],indata[3], indata[5])
    #print("oldPath: ", oldPath)
    #print("newPath: ", newPath)

    status.set("Migrating account...")
    uimFuncs.migrateAccount(oldPath, newPath)

    status.set("Done!")
    return



# Create a button that will print the contents of the entry
run_button = Button(root, text='Migrate', command=migrate)
run_button.pack()

# Create a button that will destroy the main window when clicked
exit_button = Button(root, text='Exit Program', command=root.destroy)
exit_button.pack()

root.mainloop()
