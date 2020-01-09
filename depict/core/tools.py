from .plot import Plot

from bokeh.layouts import column, row
from bokeh.models.widgets import Div
from bokeh.plotting import show as show_bokeh
import numpy as np


def show(plot, width_total_as_session=False):
    # TODO: Check the shape first, the types etc
    def build_plot(plot, width=None):
        fig = plot.make_figure()
        if width:
            fig.width = width
        if not plot.grid_visible:
            fig.xgrid.visible = False
            fig.ygrid.visible = False
        for step in plot.steps:
            step(fig)
        if width:
            div = Div(text=plot.description, width=width, height=None)
        else:
            div = Div(text=plot.description, width=plot.width, height=None)
        return column(fig, div)

    if isinstance(plot, Plot):
        if width_total_as_session:
            show_bokeh(build_plot(plot=plot, width=plot.width_session))
        else:
            show_bokeh(build_plot(plot))
    elif isinstance(plot, (list, np.ndarray)):
        row_all = []
        for p_1 in plot:
            if isinstance(p_1, Plot):
                if width_total_as_session:
                    row_all.append(build_plot(p_1, width=p_1.width_session))
                else:
                    row_all.append(build_plot(p_1))
            elif isinstance(p_1, (list, np.ndarray)):
                if width_total_as_session:
                    fig_width = int(p_1[0].width_session / len(p_1))
                    row_all.append(
                        row([build_plot(pp, width=fig_width) for pp in p_1]))
                else:
                    row_all.append(row([build_plot(pp) for pp in p_1]))
        show_bokeh(column(row_all))
