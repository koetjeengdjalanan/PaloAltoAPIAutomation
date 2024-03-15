from mailbox import Message
import os
import ttkbootstrap as ttkb
from pprint import pprint
from dotenv import load_dotenv
from ttkbootstrap.dialogs import dialogs
from lib import FileHandler, Login, Download
from lib.api.auth import Profile


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
        user_name: str = None,
        secret_string: str = None,
        tsg_id: int = None,
        env_path: str = None,
    ):
        super().__init__(parent)
        self.title(title)
        self.rootFrame = ttkb.Frame(master=self)
        self.rootFrame.pack(ipadx=5, ipady=5, fill="both", expand=True)
        self.authRes = None

        ### ENV File Picker ###
        # envFilePicker = ttkb.LabelFrame(master=self.rootFrame, text="Environment File")
        # envFilePicker.grid(
        #     row=0, column=0, padx=5, pady=5, ipadx=5, ipady=5, sticky="new"
        # )
        # self.envFileEntry = ttkb.Entry(master=envFilePicker, justify="left", width=40)
        # self.envFileEntry.grid(padx=5, pady=5, row=0, column=0)
        # ttkb.Button(master=envFilePicker, image=PhotoImage(data=Icon.question)).grid(
        #     padx=5, pady=5, row=0, column=1
        # )
        # ttkb.Button(master=envFilePicker, image=PhotoImage(data=Icon.warning)).grid(
        #     padx=5, pady=5, row=0, column=2
        # )

        ### User Credentials ###
        userSettingFrame = ttkb.LabelFrame(
            master=self.rootFrame, text="User Credentials"
        )
        userSettingFrame.grid(
            row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5, sticky="sew"
        )
        self.userName = user_name
        self.secret = secret_string
        self.tsgId = tsg_id

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
        self.workingInfoLabel = ttkb.Label(master=userSettingFrame, justify="center")
        self.workingInfoLabel.grid(
            padx=2, pady=2, row=3, column=0, sticky="nsew", columnspan=3
        )
        ttkb.Button(
            master=userSettingFrame,
            command=lambda: self.destroy(),
            bootstyle="danger",
            text="Cancel",
        ).grid(padx=5, pady=5, row=4, column=0, sticky="se")
        ttkb.Button(
            master=userSettingFrame,
            command=lambda: self.on_save(),
            bootstyle="success",
            text="Save",
        ).grid(padx=5, pady=5, row=4, column=1, sticky="se")
        ttkb.Button(
            master=userSettingFrame,
            command=lambda: self.downloadList(),
            bootstyle="info",
            text="Download List",
        ).grid(padx=5, pady=5, row=4, column=2, sticky="se")

        self.after(ms=10, func=self.__populate_entry)

    def __populate_entry(self):
        if self.userName is not None or "":
            self.nameField.delete(first=0, last=ttkb.END)
            self.nameField.insert(index=0, string=self.userName)
        if self.secret is not None or "":
            self.secretField.delete(first=0, last=ttkb.END)
            self.secretField.insert(index=0, string=self.secret)
        if self.tsgId is not None or "":
            self.tsgIdField.delete(first=0, last=ttkb.END)
            self.tsgIdField.insert(index=0, string=self.tsgId)

    def on_save(self):
        self.workingInfoLabel.config(
            text="Logging In...", bootstyle="info", justify="center"
        )
        self.userName = self.nameField.get()
        self.secret = self.secretField.get()
        self.tsgId = self.tsgIdField.get()
        # print(self.userName, self.secret, self.tsgId, sep="\n")
        try:
            auth = Login(username=self.userName, secret=self.secret, tsg_id=self.tsgId)
            self.workingInfoLabel.config(
                text="Log in Success", bootstyle="success", justify="center"
            )
        except Exception as error:
            dialogs.Messagebox.show_error(
                Message=error, title="An Error Occurred", parent=self, alert=True
            )
        self.authRes = auth.request()
        print(self.authRes)
        try:
            profile = Profile(bearer_token=self.authRes["data"]["access_token"])
            self.workingInfoLabel.config(
                text="Get Profile Success", bootstyle="success", justify="center"
            )
        except Exception as error:
            dialogs.Messagebox.show_error(
                Message=error, title="An Error Occurred", parent=self, alert=True
            )
        self.profile = profile.request()
        print(self.profile)

    def downloadList(self):
        bearerToken = self.authRes["data"]["access_token"]
        download = Download(bearer_token=bearerToken)
        try:
            res = download.request()
            print(res)
            FH = FileHandler()
            FH.save_as_excel(data=res["data"]["items"])
        except Exception as error:
            dialogs.Messagebox.show_error(
                message=f"{error}", title="An Error Occurred", parent=self, alert=True
            )


def open_window(parent):
    print("Open Shazame")
    load_dotenv(dotenv_path="./.env")
    SW = Setting(
        parent=parent,
        user_name=os.getenv("USER_NAME"),
        secret_string=os.getenv("SECRET_STRING"),
        tsg_id=os.getenv("TSG_ID"),
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
