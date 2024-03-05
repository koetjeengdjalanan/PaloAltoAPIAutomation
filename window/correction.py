import pprint
import icecream as ic
import ttkbootstrap as ttkb
from ttkbootstrap.scrolled import ScrolledFrame


class DataCorrection(ttkb.Toplevel):
    """
    Data Correction window to match api requirement to actual data
    """

    def __init__(
        self,
        parent,
        title: str = "Data Correction",
        start_size: tuple = (500, 300),
        required: dict = {},
        provided: list = [],
    ):
        super().__init__(parent)
        # self.geometry(f"{start_size[0]}x{start_size[1]}")
        self.title(title)
        self.configure()
        self.rootFrame = ScrolledFrame(master=self)
        # self.rootFrame.grid_columnconfigure(0, weight=1)
        self.rootFrame.pack(ipadx=5, ipady=5, fill="both", expand=True)

        ### Main Content ###
        self.content(provided=provided, required=required)

    def content(self, provided, required):
        contentCount: int = 0
        for key, value in required.items():
            l1Frame = ttkb.LabelFrame(master=self.rootFrame, text=key)
            l1Frame.grid(
                ipadx=5,
                ipady=5,
                padx=5,
                pady=5,
                column=0,
                row=contentCount,
                sticky="nsew",
            )
            # print(key, value, sep=" : ")
            if value["value"] is not None:
                iContent = 0
                for iKey, iValue in value["value"].items():
                    # print(iKey, iValue["req"], sep=" : ")
                    self.__internalContent(
                        master=l1Frame,
                        textVariable=provided,
                        label=str(iKey),
                        req=bool(iValue["req"]) or False,
                        rowNumber=iContent,
                    )
                    iContent += 1
            # print("\n")
            self.__internalContent(
                master=l1Frame,
                textVariable=provided,
                label=str(key),
                req=bool(value["req"]) or False,
            )
            contentCount += 1

        ttkb.Button(master=self.rootFrame, command=self.destroy, text="close").grid(
            padx=5, pady=5, sticky="se"
        )

    def __internalContent(
        self, master, textVariable, label: str, req: bool = False, rowNumber: int = 0
    ):
        ttkb.Label(
            master=master, text=label, bootstyle="danger" if req else "default"
        ).grid(padx=5, pady=5, column=0, row=rowNumber, sticky="w")
        ttkb.Combobox(master=master, textvariable=textVariable).grid(
            padx=5, pady=5, column=1, row=rowNumber, sticky="e"
        )


def open_window():
    try:
        DC = DataCorrection(
            parent=debug,
            start_size=(768, 300),
            required=[],
            provided=[],
        )
        DC.grab_set()
    except Exception as error:
        ic(error)


if __name__ == "__main__":
    debug = ttkb.Window()
    ttkb.Button(debug, command=open_window, text="open").pack(expand=True)
    debug.geometry("200x200")
    debug.title("Debug Window")
    debug.mainloop()
