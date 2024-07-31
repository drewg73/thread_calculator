from tkinter import *
from tkinter import ttk
from threads import *

class GUI():
    def __init__(self, master):
        self.frame_thread_builder = ttk.LabelFrame(
            master,
            text="Thread Builder"
        )
        self.frame_thread_builder.pack()

        ttk.Label(
            self.frame_thread_builder,
            text="Basic Diameter:"
          ).grid(column=0, row=0, sticky=(E))
        diameter_entry = ttk.Entry(
            self.frame_thread_builder,
        )
        diameter_entry.grid(column=1, columnspan=2, row=0)
        ttk.Label(
            self.frame_thread_builder,
            text="TPI:"
        ).grid(column=0, row=1, sticky=(E))
        tpi_entry = ttk.Entry(
            self.frame_thread_builder,
        )
        tpi_entry.grid(column=1, columnspan=2, row=1)
        ttk.Label(
            self.frame_thread_builder,
            text="Series:"
        ).grid(column=0, row=2, sticky=(E))
        series_entry = ttk.Combobox(
            self.frame_thread_builder,
            values=["UN", "UNC", "UNF", "UNR"],
            state="readonly",
        )
        series_entry.set("UNC")
        series_entry.grid(column=1, columnspan=2, row=2)
        ttk.Label(
            self.frame_thread_builder,
            text="Class:"
        ).grid(column=0, row=3, stick=(E))
        class_entry = ttk.Combobox(
            self.frame_thread_builder,
            values=["1A", "2A", "3A", "1B", "2B", "3B"],
            state="readonly",
        )
        class_entry.set("2A")
        class_entry.grid(column=1, columnspan=2, row=3, sticky=(E))
        button = ttk.Button(
            self.frame_thread_builder,
            text="Calcualte"
        )
        button.grid(column=0, columnspan=3, row=4, sticky=(W, E))

        self.frame_thread_data = ttk.LabelFrame(
            master,
            text="Thread Data"
        )
        self.frame_thread_data.pack()
        ttk.Label(self.frame_thread_data, text="Definition:").pack()
        ttk.Label(self.frame_thread_data, text="Major Diameters:").pack()
        ttk.Label(self.frame_thread_data, text="Pitch Diameter:").pack()
        ttk.Label(self.frame_thread_data, text="Minor Diameter:").pack()
