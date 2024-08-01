from tkinter import *
from tkinter import ttk
from threads import *

class GUI():
    def __init__(self, master):
        self.frame_thread_builder = ttk.LabelFrame(
            master,
            text="Thread Builder"
        )
        self.frame_thread_builder.columnconfigure(0, )
        self.frame_thread_builder.pack(fill=BOTH)
        self.diameter = StringVar()
        self.tpi = StringVar()
        self.series = StringVar()
        self.class_ = StringVar()
        ttk.Label(
            self.frame_thread_builder,
            text="Basic Diameter:",
            padding=[5, 0]
          ).grid(column=0, row=0, sticky=(E))
        diameter_entry = ttk.Entry(
            self.frame_thread_builder,
            textvariable=self.diameter,
        )
        diameter_entry.grid(column=1, columnspan=2, row=0, sticky=(W, E))
        ttk.Label(
            self.frame_thread_builder,
            text="TPI:",
            padding=[5, 0],
        ).grid(column=0, row=1, sticky=(E))
        tpi_entry = ttk.Entry(
            self.frame_thread_builder,
            textvariable=self.tpi,
        )
        tpi_entry.grid(column=1, columnspan=2, row=1, sticky=(W, E))
        ttk.Label(
            self.frame_thread_builder,
            text="Series:",
            padding=[5, 0]
        ).grid(column=0, row=2, sticky=(E))
        series_entry = ttk.Combobox(
            self.frame_thread_builder,
            values=["UN", "UNC", "UNF", "UNR"],
            state="readonly",
            textvariable=self.series,
        )
        self.series.set("UNC")
        series_entry.grid(column=1, columnspan=2, row=2)
        ttk.Label(
            self.frame_thread_builder,
            text="Class:",
            padding=[5, 0]
        ).grid(column=0, row=3, stick=(E))
        class_entry = ttk.Combobox(
            self.frame_thread_builder,
            values=["1A", "2A", "3A", "1B", "2B", "3B"],
            state="readonly",
            textvariable=self.class_,
        )
        class_entry.set("2A")
        class_entry.grid(column=1, columnspan=2, row=3)
        button = ttk.Button(
            self.frame_thread_builder,
            text="Calcualte",
            command=self.on_click,
        )
        button.grid(column=0, columnspan=3, row=4, sticky=(W, E))

        self.frame_thread_data = ttk.LabelFrame(
            master,
            text="Thread Data"
        )
        self.frame_thread_data.pack(fill=BOTH)
        self.thread_definition = StringVar()
        self.major_diameter = StringVar()
        self.pitch_diameter = StringVar()
        self.minor_diameter = StringVar()
        ttk.Label(self.frame_thread_data, text="Definition:").grid(column=0, row=0, sticky=(E))
        ttk.Label(self.frame_thread_data, textvariable=self.thread_definition, padding=[5, 0]).grid(column=1, row=0, sticky=(W))
        ttk.Label(self.frame_thread_data, text="Major Diameters:").grid(column=0, row=1, sticky=(E))
        ttk.Label(self.frame_thread_data, textvariable=self.major_diameter, padding=[5, 0]).grid(column=1, row=1, sticky=(W))
        ttk.Label(self.frame_thread_data, text="Pitch Diameter:").grid(column=0, row=2, sticky=(E))
        ttk.Label(self.frame_thread_data, textvariable=self.pitch_diameter, padding=[5, 0]).grid(column=1, row=2, sticky=(W))
        ttk.Label(self.frame_thread_data, text="Minor Diameter:").grid(column=0, row=3, sticky=(E))
        ttk.Label(self.frame_thread_data, textvariable=self.minor_diameter, padding=[5, 0]).grid(column=1, row=3, sticky=(W))

    def on_click(self):
      try:
         thread = United_National(float(self.diameter.get()), int(self.tpi.get()), self.series.get(), self.class_.get())
         self.thread_definition.set(thread)
         major, pitch, minor = thread.calc_basic_dimensions()
         self.major_diameter.set(major)
         self.pitch_diameter.set(pitch)
         self.minor_diameter.set(minor)
      except ValueError:
         pass
