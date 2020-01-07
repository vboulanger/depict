from bokeh.plotting import figure
from bokeh.io import show


def line(y, x=None):
    """ One dimensional plot

    Args:
        x (array-like): X-axis data
        y (array-like): y-axis data
    """
    if x is None:
        y = np.arange(len(y))
    plot = figure()
    plot.line(x=x, y=y)
    show(plot)