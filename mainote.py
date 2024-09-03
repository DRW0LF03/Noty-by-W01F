from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile

root = Tk()
root.title("W01F Notepad")
root.config(bg='#242424')
root.geometry('700x500')
root.iconbitmap("icowlf.ico")


# Function to save file
def sss():
    new_file = asksaveasfile(mode='w', defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("Markdown files", "*.md"), ("All files", "*.*")])
    if new_file is None:
        return
    text = str(entry.get(1.0, END))
    new_file.write(text)
    new_file.close()

# Function to open file
def openf():
    file = askopenfile(mode='r', filetypes=[("Text files", "*.txt"), ("Markdown files", "*.md"), ("All files", "*.*")])
    if file is not None:
        content = file.read()
        entry.delete(1.0, END)  # Clear the current content in the text widget
        entry.insert(INSERT, content)

# Main frame for buttons
top1 = Frame(root)
top1.pack(padx=8, pady=5, anchor='nw')

# Open button
B1 = Button(root, text="Open", bg="#DAF7A6", command=openf)
B1.pack(in_=top1, side=LEFT)

# SaveAs button
B2 = Button(root, text="SaveAs", bg="#DAF7A6", command=sss)
B2.pack(in_=top1, side=LEFT)

# Text widget for writing content
entry = Text(root, bg="#e0d3af", font=("Drip October", 18))
entry.pack(padx=8, pady=8, expand=True, fill=BOTH)

root.mainloop()
