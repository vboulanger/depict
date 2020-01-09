from .plot import Plot
from .tools import show

from bokeh.plotting import figure
from bokeh.io import output_file
from bokeh.layouts import column
from bokeh.models.widgets import Div
import numpy as np


def line_base(y, x, width, height, description, background_color,
              grid_visible, width_session):
    """ One dimensional plot

    Args:
        x (array-like): X-axis data
        y (array-like): y-axis data
    """
    if x is None:
        x = np.arange(len(y))
    def _make_fig():
        return figure(width=width, height=height,
                      background_fill_color=background_color)
    steps = [lambda f: f.line(x=x, y=y)]
    plot = Plot(make_figure=_make_fig, steps=steps, description=description,
                width=width, grid_visible=grid_visible,
                width_session=width_session)
    return show(plot) or plot

def _update_line_default_args(line, session):
    def line_updated(y, x=None, width=session.width, height=session.height,
                     description=session.description,
                     background_color=session.background_color,
                     grid_visible=session.grid_visible):
        plot = line(y=y, x=x, width=width, height=height,
                    description=description,
                    background_color=background_color,
                    grid_visible=grid_visible,
                    width_session=session.width)
        return plot
    return line_updated
