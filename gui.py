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
      # allowance.set(round(thread.get_allowance(), 4))
      tolerance_major.set(round(thread.calculate_major_diameter_tolerance(), 4))
      tolerance_pitch.set(round(thread.calculate_pitch_diameter_tolerance(), 4))
      tolerance_minor.set(round(thread.calculate_minor_diameter_tolerance(), 4))
      length_of_engagement.set(thread._thread_engagement)
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
thread_designation_selection = ttk.Combobox(mainframe, width=7, textvariable=thread_designation)
thread_designation_selection['values'] = ("UN", "UNC", "UNF", "UNJ")
thread_designation_selection.state(["readonly"])
thread_designation_selection.grid(column=2, row=3, sticky=(W, E))

thread_class = StringVar()
thread_class_selection = ttk.Combobox(mainframe, width=7, textvariable=thread_class)
thread_class_selection['values'] = ("1A", "2A", "3A", "1B", "2B", "3B")
thread_class_selection.grid(column=2, row=4, sticky=(W, E))

ttk.Button(mainframe, text="Calculate Thread", command=calculate).grid(column=1, row=5, columnspan=3, sticky=(W, E))

ttk.Label(mainframe, text="basic diameter").grid(column=1, row=1, sticky=(W))
ttk.Label(mainframe, text="in.").grid(column=3, row=1, sticky=(W))
ttk.Label(mainframe, text="threads per inch").grid(column=1, row=2, sticky=(W))
ttk.Label(mainframe, text="thread designation").grid(column=1, row=3, stick=(W))
ttk.Label(mainframe, text="thread class").grid(column=1, row=4, sticky=(W))

# Tolerance Section
ttk.Label(mainframe, text="Tolerance").grid(column=1, row=10, stick=(W, E))
allowance = StringVar()
tolerance_major = StringVar()
tolerance_minor = StringVar()
tolerance_pitch = StringVar()
length_of_engagement = StringVar()
ttk.Label(mainframe, text=f"Allowance:").grid(column=1, row=11, sticky=(W))
ttk.Label(mainframe, textvariable=allowance).grid(column=2, row=11, sticky=(E))
ttk.Label(mainframe, text=f"Major Diameter:").grid(column=1, row=12, sticky=(W))
ttk.Label(mainframe, textvariable=tolerance_major).grid(column=2, row=12, sticky=(E))
ttk.Label(mainframe, text=f"Pitch Diameter:").grid(column=1, row=13, sticky=(W))
ttk.Label(mainframe, textvariable=tolerance_pitch).grid(column=2, row=13, sticky=(E))
ttk.Label(mainframe, text=f"Minor Diameter:").grid(column=1, row=14, sticky=(W))
ttk.Label(mainframe, textvariable=tolerance_minor).grid(column=2, row=14, sticky=(E))
ttk.Label(mainframe, text=f"Length of Engagement:").grid(column=1, row=15, sticky=(W))
ttk.Label(mainframe, textvariable=length_of_engagement).grid(column=2, row=15, sticky=(E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

thread_diameter_entry.focus()
root.bind("<Return>", calculate)
