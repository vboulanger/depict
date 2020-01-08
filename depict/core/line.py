from .plot import Plot

from bokeh.plotting import figure
from bokeh.io import show
import numpy as np


def line_base(y, x=None, width=300, height=300, background_color='aliceblue', grid_visible=True):
    """ One dimensional plot

    Args:
        x (array-like): X-axis data
        y (array-like): y-axis data
    """
    if x is None:
        x = np.arange(len(y))
    fig = figure(width=width, height=height, background_fill_color=background_color)
    if not grid_visible:
        fig.xgrid.visible = False
        fig.ygrid.visible = False
    fig.line(x=x, y=y)
    def _make_fig():
        return figure(width=width, height=height, background_fill_color=background_color)
    steps = [lambda f: f.line(x=x, y=y)]
    plot = Plot(make_figure=_make_fig, steps=steps)
    return show(fig) or plot

def _update_line_default_args(line, session):
    def line_updated(y, x=None, width=session.width, height=session.height,
                     background_color=session.background_color,
                     grid_visible=session.grid_visible):
        plot = line(y=y, x=x, width=width, height=height,
                    background_color=background_color,
                    grid_visible=grid_visible)
        return plot
    return line_updated
