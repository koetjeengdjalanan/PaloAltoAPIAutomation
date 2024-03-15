import threading
import time
import datetime
import ttkbootstrap as ttkb
import tkinter as tk
import os
from lib.api.siteconfig import Update as SCAPIUpdate
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.scrolled import ScrolledText
from ttkbootstrap.constants import *  # noqa: F403
from tkinter.messagebox import showerror
from dotenv import load_dotenv
from lib.filehandler import FileHandler
from window import DataCorrection, Setting


class App(ttkb.Window):
    def __init__(self, start_size: tuple, theme: str) -> None:
        super().__init__(themename=theme, iconphoto="assets/favicon.ico")
        self.title("Palo Alto Network Bulk Automation")
        self.geometry(f"{start_size[0]}x{start_size[1]}")
        self.resizable(False, False)

        self.frame = ttkb.Frame(self, bootstyle="default")
        self.frame.pack(expand=True, fill="both")
        self.dataPreviewDetails = {"Data Count": "", "nullValue": ""}
        load_dotenv(dotenv_path="./.env")

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

    def pick_source_file(self) -> None:
        self.progress_bar(loop=True)
        FH = FileHandler()
        file = FH.select_file()
        self.insert_log(text=f"Source File: {file}")
        self.dataPreview = FH.sourcedata
        self.dataPreviewDetails = {
            "Data Count": len(self.dataPreview),
            "nullValue": self.dataPreview[
                self.dataPreview.isin(["-", None]).any(axis=1)
            ].shape[0],
        }

        self.insert_log(text="Preparing Table View")
        self.show_data_table()

        threading.Thread(target=self.show_data_preview_details()).start()
        threading.Thread(target=self.find_data_error()).start()

        if file != "":
            self.filePickerEntry.delete(0, ttkb.END)
            self.filePickerEntry.insert(0, file)
        self.progress_bar(reset=True)

    def find_data_error(self) -> None:
        self.insert_log(text="Start Filtering Error")
        for count in range(self.dataPreviewDetails["Data Count"]):
            data = self.dataPreview.loc[count, :]
            if data.isnull().any() or data.isin(["-", None]).any():
                self.insert_log(
                    f"Validation Failed for {self.previewTable.get_row(index=count).iid} : {data.tolist()}"
                )
                self.previewTable.view.item(
                    item=self.previewTable.get_row(index=count).iid, tags="error"
                )

    def show_data_table(self) -> None:
        startTime = time.monotonic()
        self.previewTable.build_table_data(
            coldata=list(self.dataPreview.columns.values),
            rowdata=self.dataPreview.to_numpy().tolist(),
        )
        self.insert_log(
            f"Table View Completed for {datetime.timedelta(seconds=(time.monotonic() - startTime))}"
        )

    # def show_data_preview(self) -> None:
    #     self.previewTable = ttkb.Treeview(
    #         master=self.dataFrame,
    #         columns=list(self.dataPreview.columns.values),
    #         show="headings",
    #         style="info.treeview",
    #     )
    #     for heading in list(self.dataPreview.columns):
    #         self.previewTable.heading(column=heading, text=heading)
    #     self.previewTableYScroll = ttkb.Scrollbar(
    #         master=self.dataFrame, orient="vertical", command=self.previewTable.yview
    #     )
    #     self.previewTableXScroll = ttkb.Scrollbar(
    #         master=self.dataFrame, orient="horizontal", command=self.previewTable.xview
    #     )
    #     self.previewTable.configure(
    #         xscrollcommand=self.previewTableXScroll.set,
    #         yscrollcommand=self.previewTableYScroll.set,
    #     )
    #     self.previewTable.grid(row=0, column=0, sticky="nsew")
    #     self.previewTableYScroll.grid(row=0, column=1, sticky="ns")
    #     self.previewTableXScroll.grid(row=1, column=0, sticky="ew")
    #     self.dataFrame.grid_columnconfigure(index=0, weight=1)
    #     self.dataFrame.grid_rowconfigure(index=0, weight=1)
    #     self.previewTable.tag_configure(tagname="error", background="lightcoral")
    #     for count in range(self.dataPreviewDetails["Data Count"]):
    #         data = self.dataPreview.loc[count, :]
    #         value = data.values.flatten().tolist()
    #         if data.isnull().any() or data.isin(["-", None]).any():
    #             self.previewTable.insert(
    #                 parent="", index=ttkb.END, values=value, tags=("error",)
    #             )
    #         else:
    #             self.previewTable.insert(
    #                 parent="",
    #                 index=ttkb.END,
    #                 values=value,
    #             )

    def show_data_preview_details(self) -> None:
        for heading in list(self.dataPreviewDetails.keys()):
            self.dataInfoDetails.heading(column=heading, text=heading)
        for col in list(self.dataPreviewDetails.keys()):
            self.dataInfoDetails.column(
                column=col, minwidth=1, width=50, stretch=True, anchor="center"
            )
        self.dataInfoDetails.insert(
            "", ttkb.END, values=list(self.dataPreviewDetails.values())
        )
        self.dataPreviewDetails.update()

    def data_correction(self) -> None:
        try:
            DC = DataCorrection(
                parent=self,
                start_size=(768, 300),
                required=SCAPIUpdate().body,
                provided=list(self.dataPreview.columns.values),
            )
            DC.grab_set()
        except AttributeError as error:
            showerror(
                title="No Data Found!",
                message=f"No data found! please (re)select the data or contact support! \n\n {error}",
            )

    def insert_log(self, text: str):
        self.logWindow.text.configure(state="normal")
        self.logWindow.text.insert(ttkb.INSERT, f"{self.get_now()} \t {text}\n")
        self.logWindow.text.configure(state="disabled")

    def progress_bar(
        self, reset: bool = False, mode: str = "determinate", loop: float = False
    ):
        if reset:
            self.progressBar.stop()
            self.progressBar.configure(
                maximum=100,
                orient="horizontal",
                value=0,
                mode="determinate",
                bootstyle="default",
            )
        if loop:
            self.progressBar.configure(
                mode="determinate", bootstyle="striped", maximum=100
            )
            self.progressBar.start(interval=10)
        pass

    def get_now(self) -> str:
        return datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    def open_setting(self) -> None:
        settingWindow = Setting(
            parent=self,
            user_name=os.getenv("USER_NAME") or "",
            secret_string=os.getenv("SECRET_STRING") or "",
            tsg_id=int(os.getenv("TSG_ID")) or "",
        )
        settingWindow.grab_set()

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
        self.frame = ttkb.Frame(self, bootstyle="default", name="rootFrame")
        self.frame.pack(expand=True, fill="both")

        ### Source File ###
        self.filePickerFrame = ttkb.LabelFrame(self.frame, text="Source File")
        self.filePickerFrame.pack(fill="x", anchor="n", padx=10, pady=10)
        self.filePickerEntry = ttkb.Entry(
            self.filePickerFrame,
        )
        self.filePickerEntry.pack(pady=10, padx=10, side="left", fill="x", expand=True)
        ttkb.Button(
            master=self.filePickerFrame,
            text="Setting",
            command=lambda: self.open_setting(),
        ).pack(padx=10, pady=10, side="right", fill="none", expand=False)
        ttkb.Separator(master=self.filePickerEntry, orient="vertical").pack(
            side="right"
        )
        ttkb.Button(
            master=self.filePickerFrame,
            text="Choose File",
            command=lambda: threading.Thread(target=self.pick_source_file).start(),
        ).pack(padx=10, pady=10, side="right", fill="none", expand=False)

        contentFrame = tk.Frame(master=self.frame, background="red")
        contentFrame.pack(fill="both", expand=True)

        ### Data Info Frame ###
        self.dataInfoFrame = ttkb.Frame(
            master=contentFrame, width=int(self.winfo_width() / 12 * 3)
        )
        self.dataInfoFrame.pack(side="left", anchor="nw", fill="y", expand=False)
        self.dataInfoFrame.pack_propagate(False)
        self.dataInfoLabelFrame = ttkb.LabelFrame(
            self.dataInfoFrame, text="Data Information"
        )
        self.dataInfoLabelFrame.pack(padx=10, pady=(0, 10), fill="both", expand=True)
        self.dataInfoDetails = ttkb.Treeview(
            self.dataInfoLabelFrame,
            columns=list(self.dataPreviewDetails.keys()),
            show="headings",
            style="primary.Treeview",
            height=1,
            selectmode="none",
        )
        self.dataInfoDetails.pack(
            side="top", anchor="nw", fill="y", expand=False, padx=10, pady=10
        )
        ttkb.Button(
            master=self.dataInfoLabelFrame,
            command=self.data_correction,
            text="Match Data",
        ).pack(side="left", padx=10, pady=(0, 10))
        ttkb.Button(
            master=self.dataInfoLabelFrame,
            command=lambda: self.progress_bar(loop=True),
            text="Go",
        ).pack(side="right", padx=10, pady=(0, 10))

        ### Preview Table ###
        self.dataFrame = ttkb.LabelFrame(master=contentFrame, text="Data Preview")
        self.dataFrame.pack(
            fill="both",
            anchor="center",
            padx=(0, 10),
            pady=(0, 10),
            expand=True,
        )
        self.previewTable = Tableview(
            master=self.dataFrame,
            paginated=False,
            searchable=True,
            autofit=True,
            stripecolor=("gray22", None),
        )
        self.previewTable.view.tag_configure(tagname="error", background="lightcoral")
        self.previewTable.pack(padx=10, pady=10, expand=True, fill="y", side="top")
        # self.previewTable.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        ttkb.Separator(master=self.frame, orient="horizontal").pack(fill="x", padx=10)

        self.logWindow = ScrolledText(
            master=self.frame, padding=5, height=5, autohide=True, bootstyle="dark"
        )
        self.logWindow.text.configure(state="disabled")
        self.logWindow.pack(fill="x", expand=False, padx=10)
        self.progressBar = ttkb.Progressbar(
            master=self.frame, maximum=100, orient="horizontal"
        )
        self.progressBar.pack(fill="x", padx=10, expand=False, pady=(0, 10))

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


app = App((1190, 620), theme="darkly")
