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

        username = ttkb.StringVar(value=user_credentials["username"])
        secret = ttkb.StringVar(value=user_credentials["secret"])
        tsgId = ttkb.StringVar(value=user_credentials["tsgId"])

        ttkb.Label(master=userSettingFrame, text="User Name").grid(
            padx=5, pady=5, column=0, row=0, sticky="w"
        )
        nameField = ttkb.Entry(
            master=userSettingFrame, justify="left", textvariable=username, width=50
        )
        nameField.grid(padx=5, pady=5, row=0, column=1, sticky="e", columnspan=2)
        ttkb.Label(master=userSettingFrame, text="Secret").grid(
            padx=5, pady=5, column=0, row=1, sticky="w"
        )
        secretField = ttkb.Entry(
            master=userSettingFrame,
            justify="left",
            textvariable=secret,
            show="*",
            width=50,
        )
        secretField.grid(padx=5, pady=5, row=1, column=1, sticky="e", columnspan=2)
        ttkb.Label(master=userSettingFrame, text="TSG ID").grid(
            padx=5, pady=5, column=0, row=2, sticky="w"
        )
        tsgIdField = ttkb.Entry(
            master=userSettingFrame, justify="left", textvariable=tsgId, width=50
        )
        tsgIdField.grid(padx=5, pady=5, row=2, column=1, sticky="e", columnspan=2)
        ttkb.Button(
            master=userSettingFrame,
            command=lambda: print("Cancel"),
            bootstyle="danger",
            text="Cancel",
        ).grid(padx=5, pady=5, row=3, column=0, sticky="se")
        ttkb.Button(
            master=userSettingFrame,
            command=lambda: print("Save"),
            bootstyle="success",
            text="Save",
        ).grid(padx=5, pady=5, row=3, column=1, sticky="se")
        ttkb.Button(
            master=userSettingFrame,
            command=lambda: print("Test Connection"),
            bootstyle="info",
            text="Test Connection",
        ).grid(padx=5, pady=5, row=3, column=2, sticky="se")


def open_window(parent):
    print("Open Shazame")
    SW = Setting(parent=parent)
    SW.grab_set()


if __name__ == "__main__":
    debug = ttkb.Window()
    ttkb.Button(debug, command=lambda: open_window(parent=debug), text="open").pack(
        expand=True
    )
    debug.geometry("200x200")
    debug.title("Debug Window")
    debug.mainloop()
