from ttkbootstrap.constants import *  # noqa: F403
import ttkbootstrap as ttkb
from lib.filehandler import FileHandler


class App(ttkb.Window):
    def __init__(self, start_size, theme: str) -> None:
        super().__init__(themename=theme, iconphoto="assets/favicon.ico")
        self.title("Palo Alto Bulk Automation")
        self.geometry(f"{start_size[0]}x{start_size[1]}")

        self.frame = ttkb.Frame(self, bootstyle="default")
        self.frame.pack(expand=True, fill="both")

        SizeNotifier(
            self,
            {
                1200: self.create_Xlarge_layout,
                992: self.create_large_layout,
                768: self.create_medium_layout,
                576: self.create_small_layout,
                362: self.create_xsmall_layout,
            },
        )

        self.mainloop()

    def create_xsmall_layout(self):
        self.frame.pack_forget()
        self.frame = ttkb.Frame(self, bootstyle="default")
        self.frame.pack(expand=True, fill="both")
        print("Layout Change: XSMALL")

    def create_small_layout(self):
        self.frame.pack_forget()
        self.frame = ttkb.Frame(self, bootstyle="default")
        self.frame.pack(expand=True, fill="both")
        print("Layout Change: SMALL")

    def create_medium_layout(self):
        self.frame.pack_forget()
        self.frame = ttkb.Frame(self, bootstyle="default")
        self.frame.pack(expand=True, fill="both")
        print("Layout Change: MEDIUM")

    def create_large_layout(self):
        self.frame.pack_forget()
        self.frame = ttkb.Frame(self, bootstyle="default")
        self.frame.pack(expand=True, fill="both")

        def pick_source_file():
            FH = FileHandler()
            file = FH.select_file()
            if file != "":
                self.filePickerEntry.delete(0, ttkb.END)
                self.filePickerEntry.insert(0, file)

        self.filePickerFrame = ttkb.LabelFrame(self.frame, text="Source File")
        self.filePickerFrame.pack(fill="x", anchor="n", padx=10, pady=10)
        self.filePickerEntry = ttkb.Entry(
            self.filePickerFrame,
        )
        self.filePickerEntry.pack(pady=10, padx=10, side="left", fill="x", expand=True)
        ttkb.Button(
            self.filePickerFrame,
            text="Choose File",
            command=pick_source_file,
        ).pack(padx=10, pady=10, side="right", fill="none", expand=False)

        self.dataInfoFrame = ttkb.Frame(
            master=self.frame, width=int(self.winfo_width() / 12 * 3)
        )
        self.dataInfoFrame.pack(side="left", anchor="nw", fill="y", expand=False)
        self.dataInfoFrame.pack_propagate(False)
        self.dataInfoLabelFrame = ttkb.LabelFrame(
            self.dataInfoFrame, text="Data Information"
        )
        self.dataInfoLabelFrame.pack(padx=10, pady=(0, 10), fill="both", expand=True)
        ttkb.Label(master=self.dataInfoLabelFrame, text="File details goes here").pack(
            padx=10, pady=10
        )

        self.dataFrame = ttkb.LabelFrame(master=self.frame, text="Data Preview")
        self.dataFrame.pack(
            fill="both", anchor="center", padx=(0, 10), pady=(0, 10), expand=True
        )

        print("Layout Change: LARGE")

    def create_Xlarge_layout(self):
        self.frame.pack_forget()
        self.frame = ttkb.Frame(self, bootstyle="default")
        self.frame.pack(expand=True, fill="both")
        print("Layout Change: XLARGE")


class SizeNotifier:
    def __init__(self, window, size_dict) -> None:
        self.window = window
        self.size_dict = {key: value for key, value in sorted(size_dict.items())}
        self.current_min_size = None
        self.window.bind("<Configure>", self.check_size)

        self.window.update()

        min_height = self.window.winfo_height()
        min_width = list(self.size_dict)[0]
        self.window.minsize(min_width, min_height)

    def check_size(self, event) -> dict:
        if event.widget == self.window:
            window_width = event.width
            checked_size = None

            for min_size in self.size_dict:
                delta = window_width - min_size
                if delta >= 0:
                    checked_size = min_size

            if checked_size != self.current_min_size:
                self.current_min_size = checked_size
                self.size_dict[self.current_min_size]()
        # print({"width": event.width, "height": event.height})
        return {"width": event.width, "height": event.height}


app = App((992, 620), theme="darkly")
