from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
import os
from PIL import Image, ImageTk

hunians = []
hunians.append(Apartemen("Nelly Joy", 3, 3))
hunians.append(Rumah("Sekar MK", 5, 2))
hunians.append(Indekos("Bp. Romi", "Cahya"))
hunians.append(Rumah("Satria", 1, 4))

root = Tk()
root.withdraw()
# root.title("Praktikum DPBO Python")
def open_main_window():
    landing_page.destroy()
    root.deiconify()

def get_total_kamar():
    total_kamar = 0
    for hunian in hunians:
        total_kamar += hunian.get_jml_kamar()
    return total_kamar

landing_page = Toplevel()
landing_page.title("Landing Page")

welcome_label = Label(landing_page, text="GUI python mantav")
welcome_label.pack(pady=10)


script_dir = os.path.dirname(os.path.abspath(__file__))

image_path = os.path.join(script_dir, 'b.png')

image = PhotoImage(file=image_path)

image_label = Label(landing_page, image=image)
image_label.pack(pady=10)


enter_button = Button(landing_page, text="Enter", command=open_main_window)
enter_button.pack(pady=10)


def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    # d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w").grid(row=0, column=0, sticky="w")
    d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail() + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT).grid(row=0, column=0, sticky="w")


    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=10, pady=10)
    b_close = Button(btn, text="Close", command=top.destroy)
    b_close.grid(row=0, column=0)


frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
frame.pack(padx=10, pady=10)

opts = LabelFrame(root, padx=10, pady=10)
opts.pack(padx=10, pady=10)

b_add = Button(opts, text="Add Data", state="disabled")
b_add.grid(row=0, column=0)

b_exit = Button(opts, text="Exit", command=root.quit)
b_exit.grid(row=0, column=1)




for index, h in enumerate(hunians):
    idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
    idx.grid(row=index, column=0)

    type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
    type.grid(row=index, column=1)

    if h.get_jenis() != "Indekos": 
        name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)
    else:
        name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)

    b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
    b_detail.grid(row=index, column=3)

total_kamar_label = Label(frame, text="Total Kamar = " + str(get_total_kamar()), anchor="w", justify=LEFT)
total_kamar_label.grid(row=len(hunians)+1, column=0, sticky="w")

root.withdraw()  # Hide the main window initially
landing_page.mainloop()
root.mainloop()






