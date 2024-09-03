import tkinter as tk
from tkinter import filedialog

def openf():
    # Function to open a file
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)  # Clear the current content of the Text widget
            text.insert(tk.END, file.read())  # Insert the content of the opened file

def sss():
    # Function to save the file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))  # Write the content of the Text widget to the file

root = tk.Tk()
root.title("W01F Notepad")
root.config(bg='#242424')
root.geometry('700x500')
root.iconbitmap("icowlf.ico")




top1 = tk.Frame(root)
top1.pack(side=tk.TOP, fill=tk.X)

# Text widget with vertical and horizontal scrollbars
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Vertical scrollbar
yscrollbar = tk.Scrollbar(frame)
yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Horizontal scrollbar
xscrollbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# Text widget
text = tk.Text(frame, wrap=tk.NONE,bg="#e0d3af", font=("Drip October", 15), yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)
text.pack(padx=2, pady=2,fill=tk.BOTH, expand=True)

# Configure the scrollbars to work with the Text widget
yscrollbar.config(command=text.yview)
xscrollbar.config(command=text.xview)

# Open button
B1 = tk.Button(top1, text="Open", bg="#DAF7A6", command=openf)
B1.pack(side=tk.LEFT)

# SaveAs button
B2 = tk.Button(top1, text="SaveAs", bg="#DAF7A6", command=sss)
B2.pack(side=tk.LEFT)

root.mainloop()
