from .core.session import Session
from .core.line import line_base, _update_line_default_args
from .core.tools import show


_SESSION = None

line = line_base

def session(width=300, height=300, jupyter_notebook=False,
                background_color='aliceblue', grid_visible=True, show_plot=True):
    global _SESSION, line
    _SESSION = Session(width=width, height=height,
                       jupyter_notebook=jupyter_notebook,
                       background_color=background_color, grid_visible=grid_visible, show_plot=show_plot)
    line = _update_line_default_args(line=line, session=_SESSION)
