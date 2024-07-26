from tkinter import *
from tkinter import ttk
from threads import Threads

def calculate(*args):
    try:
      diameter = float(thread_diameter.get())
      tpi = int(thread_tpi.get())
      designation = thread_designation.get()
      t_calss = thread_class.get()
      thread = Threads(diameter, tpi, t_calss, designation)
      print(thread)
    except ValueError:
       pass

root = Tk()
root.title("UN Thread Calculator")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

thread_diameter = StringVar()
thread_diameter_entry = ttk.Entry(mainframe, width=7, textvariable=thread_diameter)
thread_diameter_entry.grid(column=2, row=1, sticky=(W, E))

thread_tpi = StringVar()
thread_tpi_entry = ttk.Entry(mainframe, width=7, textvariable=thread_tpi)
thread_tpi_entry.grid(column=2, row=2, sticky=(W, E))

thread_designation = StringVar()
thread_designation_entry = ttk.Entry(mainframe, width=7, textvariable=thread_designation)
thread_designation_entry.grid(column=2, row=3, sticky=(W, E))

thread_class = StringVar()
thread_class_entry = ttk.Entry(mainframe, width=7, textvariable=thread_class)
thread_class_entry.grid(column=2, row=4, sticky=(W, E))

ttk.Button(mainframe, text="Calculate Thread", command=calculate).grid(column=3, row=5, sticky=(W, E))

ttk.Label(mainframe, text="basic diameter").grid(column=1, row=1, sticky=(W))
ttk.Label(mainframe, text="in.").grid(column=3, row=1, sticky=(W))
ttk.Label(mainframe, text="threads per inch").grid(column=1, row=2, sticky=(W))
ttk.Label(mainframe, text="thread designation").grid(column=1, row=3, stick=(W))
ttk.Label(mainframe, text="thread class").grid(column=1, row=4, sticky=(W))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

thread_diameter_entry.focus()
