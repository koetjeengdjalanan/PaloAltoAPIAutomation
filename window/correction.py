import ttkbootstrap as ttkb


class DataCorrection(ttkb.Toplevel):
    """
    Data Correction window to match api requirement to actual data
    """

    def __init__(
        self,
        parent,
        title: str = "Data Correction Windows",
        start_size: tuple = (500, 300),
    ):
        super().__init__(parent)
        self.geometry(f"{start_size[0]}x{start_size[1]}")
        self.title(title)
        ttkb.Button(self, command=self.destroy, text="close").pack(expand=True)

    pass
