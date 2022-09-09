from swiftclient import client
import traceback
import Tkinter as tk
from Tkinter import Text
import tkFileDialog
import os

def list_apps():
    for widget in frame.winfo_children():
        widget.destroy()
    conn = client.Connection("http://127.0.0.1:8080/auth/v1.0/", "myaccount:me", "1234")
    header,objects = conn.get_container(container = "mycontainer")
    global label
    label = tk.Listbox(frame)
    print type(label)
    for i in range(len(objects)):
        label.insert(i,objects[i]["name"])
    label.pack()
    conn.close

def download_apps():
    select=label.get(label.curselection())
    wdir = tkFileDialog.askdirectory(initialdir = "/home/mahir")
    objname = wdir+"/"+select
    conn = client.Connection("http://127.0.0.1:8080/auth/v1.0/", "myaccount:me", "1234")
    header,o = conn.get_object(container = "mycontainer",obj=select)
    with open(objname, 'w') as local:
        local.write(objname)
    conn.close()

def upload_apps():
    pathn = tkFileDialog.askopenfilename(initialdir = "/home/mahir")
    filen = str(pathn).split("/")[::-1]
    filen = filen[0]
    conn = conn = client.Connection("http://127.0.0.1:8080/auth/v1.0/", "myaccount:me", "1234")
    with open(pathn, 'r') as local:
        conn.put_object(
            container = "mycontainer",
            obj=filen,
            contents=local,
        )
    conn.close()

try:
    label = None
    root = tk.Tk()
    canvasmain = tk.Canvas(root, bg = "grey", height = 700, width = 700)
    canvasmain.pack()
    frame = tk.Frame(canvasmain, bg="white")
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    ups = tk.Button(root,text= "upload", padx = 50, pady =50, bg = "grey", fg = "black",command = (lambda: upload_apps()))
    listc = tk.Button(root,text= "list container", padx = 50, pady =50, bg = "grey", fg = "black",command = (lambda: list_apps()))
    dps = tk.Button(root,text= "download", padx = 50, pady =50, bg = "grey", fg = "black", command = (lambda: download_apps()))
    ups.pack()
    listc.pack()
    dps.pack()
    root.mainloop()
except Exception:
    traceback.print_exc()