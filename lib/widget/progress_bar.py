from tkinter import DoubleVar, IntVar, Misc
from typing import Literal
from ttkbootstrap import Progressbar


class ProgressBar(Progressbar):
    """
    Progress Bar Widget Controller
    """

    def __init__(
        self,
        master: Misc | None = None,
        *,
        class_: str = ...,
        cursor: (
            str
            | tuple[str]
            | tuple[str, str]
            | tuple[str, str, str]
            | tuple[str, str, str, str]
        ) = ...,
        length: str | float = ...,
        maximum: float = ...,
        mode: Literal["determinate"] | Literal["indeterminate"] = ...,
        name: str = ...,
        orient: Literal["horizontal"] | Literal["vertical"] = ...,
        phase: int = ...,
        style: str = ...,
        value: float = ...,
        variable: IntVar | DoubleVar = ...
    ) -> None:
        super().__init__(
            master,
            class_=class_,
            cursor=cursor,
            length=length,
            maximum=maximum,
            mode=mode,
            name=name,
            orient=orient,
            phase=phase,
            style=style,
            value=value,
            variable=variable,
        )
