import ttkbootstrap as ttkb


class Setting(ttkb.Toplevel):
    """_summary_

    Args:
        ttkb (TopLevel): For setting and getting data from API
    """

    def __init__(
        self,
        parent,
        title: str = "Settings",
        start_size: tuple = (500, 300),
        user_credentials: dict = {
            "username": None,
            "secret": None,
            "tsgId": None,
        },
    ):
        super().__init__(parent)
        self.title(title)
        self.rootFrame = ttkb.Frame(master=self)
        self.rootFrame.pack(ipadx=5, ipady=5, fill="both", expand=True)
        userSettingFrame = ttkb.LabelFrame(
            master=self.rootFrame, text="User Credentials"
        )
        userSettingFrame.grid(padx=5, pady=5, ipadx=5, ipady=5, sticky="new")
        self.userCred = user_credentials

        username = ttkb.StringVar()
        secret = ttkb.StringVar()
        tsgId = ttkb.StringVar()

        ttkb.Label(master=userSettingFrame, text="User Name").grid(
            padx=5, pady=5, column=0, row=0, sticky="w"
        )
        self.nameField = ttkb.Entry(
            master=userSettingFrame, justify="left", textvariable=username, width=50
        )
        self.nameField.grid(padx=5, pady=5, row=0, column=1, sticky="e", columnspan=2)
        ttkb.Label(master=userSettingFrame, text="Secret").grid(
            padx=5, pady=5, column=0, row=1, sticky="w"
        )
        self.secretField = ttkb.Entry(
            master=userSettingFrame,
            justify="left",
            textvariable=secret,
            show="*",
            width=50,
        )
        self.secretField.grid(padx=5, pady=5, row=1, column=1, sticky="e", columnspan=2)
        ttkb.Label(master=userSettingFrame, text="TSG ID").grid(
            padx=5, pady=5, column=0, row=2, sticky="w"
        )
        self.tsgIdField = ttkb.Entry(
            master=userSettingFrame, justify="left", textvariable=tsgId, width=50
        )
        self.tsgIdField.grid(padx=5, pady=5, row=2, column=1, sticky="e", columnspan=2)
        ttkb.Button(
            master=userSettingFrame,
            command=lambda: print("Cancel"),
            bootstyle="danger",
            text="Cancel",
        ).grid(padx=5, pady=5, row=3, column=0, sticky="se")
        ttkb.Button(
            master=userSettingFrame,
            command=lambda: self.on_save(),
            bootstyle="success",
            text="Save",
        ).grid(padx=5, pady=5, row=3, column=1, sticky="se")
        ttkb.Button(
            master=userSettingFrame,
            command=lambda: self.test_connection(),
            bootstyle="info",
            text="Test Connection",
        ).grid(padx=5, pady=5, row=3, column=2, sticky="se")

        self.after(ms=10, func=self.__populate_entry)

    def __populate_entry(self):
        for key, value in self.userCred.items():
            if key == "username" and value is not None or "":
                self.nameField.delete(first=0, last=ttkb.END)
                self.nameField.insert(index=0, string=value)
            elif key == "secret" and value is not None or "":
                self.secretField.delete(first=0, last=ttkb.END)
                self.secretField.insert(index=0, string=value)
            elif key == "tsgId" and value is not None or "":
                self.tsgIdField.delete(first=0, last=ttkb.END)
                self.tsgIdField.insert(index=0, string=value)

    def on_save(self):
        self.userCred = {
            "username": self.nameField.get(),
            "secret": self.secretField.get(),
            "tsgId": self.tsgIdField.get(),
        }
        print(self.userCred)

    def test_connection(self):
        pass


def open_window(parent):
    print("Open Shazame")
    SW = Setting(
        parent=parent,
        user_credentials={
            "username": "NTT-API-Acc@1217317412.iam.panserviceaccount.com",
            "secret": "6ad0c141-5405-438a-b3f2-e6fd47cfb611",
            "tsgId": 1217317412,
        },
    )
    SW.grab_set()


if __name__ == "__main__":
    debug = ttkb.Window()
    ttkb.Button(debug, command=lambda: open_window(parent=debug), text="open").pack(
        expand=True
    )
    debug.geometry("200x200")
    debug.title("Debug Window")
    debug.mainloop()
