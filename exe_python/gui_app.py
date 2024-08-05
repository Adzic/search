import tkinter as tk
from tkinter import ttk

# Sample data
data = [
    ("123-45-6789", "1990-01-01", 1000),
    ("987-65-4321", "1985-05-15", 1500),
    ("456-78-9012", "1992-07-23", 1200)
]

# Column names
columns = ("SSN_NBR", "DOB", "PTCPN_DPST")

def search_ssn(event):
    query = ssn_var.get().lower()
    for row in tree.get_children():
        tree.delete(row)
    for item in data:
        if query in str(item[0]).lower():
            tree.insert("", tk.END, values=item)

def search_dob(event):
    query = dob_var.get().lower()
    for row in tree.get_children():
        tree.delete(row)
    for item in data:
        if query in str(item[1]).lower():
            tree.insert("", tk.END, values=item)

def search_ptcpn(event):
    query = ptcpn_var.get().lower()
    for row in tree.get_children():
        tree.delete(row)
    for item in data:
        if query in str(item[2]).lower():
            tree.insert("", tk.END, values=item)

app = tk.Tk()
app.title("Searchable Table Viewer")

# Create a frame for the search bars and treeview
frame = tk.Frame(app)
frame.pack(pady=20)

# Create search bars and labels for each column
ssn_frame = tk.Frame(frame)
ssn_frame.pack(side=tk.LEFT, padx=10)
ssn_label = tk.Label(ssn_frame, text="SSN_NBR")
ssn_label.pack()
ssn_var = tk.StringVar()
ssn_entry = ttk.Entry(ssn_frame, textvariable=ssn_var)
ssn_entry.pack()
ssn_entry.bind("<KeyRelease>", search_ssn)

dob_frame = tk.Frame(frame)
dob_frame.pack(side=tk.LEFT, padx=10)
dob_label = tk.Label(dob_frame, text="DOB")
dob_label.pack()
dob_var = tk.StringVar()
dob_entry = ttk.Entry(dob_frame, textvariable=dob_var)
dob_entry.pack()
dob_entry.bind("<KeyRelease>", search_dob)

ptcpn_frame = tk.Frame(frame)
ptcpn_frame.pack(side=tk.LEFT, padx=10)
ptcpn_label = tk.Label(ptcpn_frame, text="PTCPN_DPST")
ptcpn_label.pack()
ptcpn_var = tk.StringVar()
ptcpn_entry = ttk.Entry(ptcpn_frame, textvariable=ptcpn_var)
ptcpn_entry.pack()
ptcpn_entry.bind("<KeyRelease>", search_ptcpn)

# Create the Treeview
tree = ttk.Treeview(app, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)

# Insert the data into the Treeview
for item in data:
    tree.insert("", tk.END, values=item)

tree.pack(pady=20)

app.geometry("500x300")
app.mainloop()