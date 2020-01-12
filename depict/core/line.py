from .plot import Plot
from .tools import show_base, save_base, is_color, format_color
from ..tools.color_palettes import palette_from_name_to_function

from bokeh.plotting import figure
from bokeh.models import ColorBar, LinearColorMapper
import numpy as np


def line_base(y, x, width, height, description, title, show_plot, color,
              colorbar_type, legend, grid_visible, session, save_path):
    """ One dimensional plot

    Args:
        x (array-like): X-axis data
        y (array-like): y-axis data
    """
    # We pre-process `x` and `y`
    if x is None:
        if isinstance(y[0], (list, np.ndarray, tuple)):
            x = [np.arange(len(y_i)) for y_i in y]
        else:
            x = [np.arange(len(y))]
            y = [y]
    elif np.ndim(x) == 1:
        if np.ndim(y) == 1:
            x = [x]
            y = [y]
        elif np.ndim(y) == 2:
            x = [x for _ in y]
    elif np.ndim(x) == 2:
        if np.ndim(y) == 1:  # Corner case
            y = [y for _ in x]

    # We pre-process `color`
    _color_bar_made = False
    if not color:
        nb_color_needed = len(y)
        color = palette_from_name_to_function[session.palette_name](
            nb_color_needed)
    # We pre-process `color`
    # Corner case: if color = [0.5, 0.6, 0.7] and len(y) == 3, we cannot say if
    # color means actually the color defined by [0.5, 0.6, 0.7] or if this
    # quantity should be converted into categorical colors (3 colors here cause
    # the 3 values are different). For that case we use the argument
    # `automatic_color_mapping` in from the session.
    elif (len(color) == 3) and isinstance(color[0], (
    float, int)) and session.automatic_color_mapping and (len(y) == 3):
        color = [color, color, color]
    else:
        # General case
        if is_color(color):
            color = [color for _ in y]
        elif isinstance(color, (list, np.ndarray, tuple)) and is_color(color[0]):
            if len(color) == len(y):
                pass  # Good case
            elif len(color) == 2:
                # TODO: Implement a linear set of color between the 2 given
                #  colors
                raise ValueError('Number of elements in `color` invalid')
            else:
                # TODO: Improve error message
                raise ValueError('Number of elements in `color` invalid')
        elif isinstance(color, (list, np.ndarray, tuple)) and isinstance(color[0], (float, int)):
            if len(color) != len(y):
                # TODO: Improve error message
                raise ValueError('Number of elements in `color` invalid')

            if not colorbar_type:
                colorbar_type = 'auto'
                _add_color_bar = False
            else:
                _add_color_bar = True

            if colorbar_type.lower() == 'auto':
                if ((len(np.unique(color)) / len(color)) <= 0.5) and (len(np.unique(color) < 9)):
                    # Data are considered categorical
                    colorbar_type = 'categorical'
                else:
                    colorbar_type = 'continuous'
            else:
                colorbar_type = colorbar_type.lower()

            if colorbar_type == 'categorical':
                if legend.lower() == 'auto':
                    legend = [str(c) for c in color]
                color_unique = sorted(list(np.unique(color)))
                nb_color_needed = len(color_unique)
                palette_colors = palette_from_name_to_function[
                    session.palette_name](nb_color_needed)
                color = [palette_colors[color_unique.index(c)] for c in color]
            elif colorbar_type == 'continuous':
                palette_colors = palette_from_name_to_function[
                    session.palette_name](256)
                color_mapper = LinearColorMapper(palette=palette_colors,
                                                 low=np.min(color),
                                                 high=np.max(color))
                color = np.array(color)
                col_indexes = (color - color.min()) / (
                            (color.max() - color.min()) / (256 - 1))
                color = [palette_colors[int(ci)] for ci in col_indexes]
                if _add_color_bar:
                    color_bar = ColorBar(color_mapper=color_mapper,
                                         location=(0, 0))
                    _color_bar_made = True

    color = [format_color(c) for c in color]

    # We pre-process `legend`
    add_legend = True
    if (legend is None) or (legend == 'auto'):
        add_legend = False
    elif isinstance(legend, str):
        legend = [legend for _ in y]
    elif isinstance(legend, (list, np.ndarray, tuple)) and isinstance(legend[0], str):
        if len(legend) != len(y):
            raise ValueError('The number of elements in `legend` is not '
                             'consistent with the data')

    if add_legend:
        steps = [
            (lambda f, x_copy=x_i, y_copy=y_i, col_c=col_i, leg_c=leg_i: f.line(
                x=x_copy,
                y=y_copy,
                color=col_c, legend_label=leg_c))
            for (x_i, y_i, col_i, leg_i) in zip(x, y, color, legend)]
    else:
        steps = [
            (lambda f, x_copy=x_i, y_copy=y_i, col_c=col_i: f.line(
                x=x_copy,
                y=y_copy,
                color=col_c))
            for (x_i, y_i, col_i) in zip(x, y, color)]

    def _make_fig():
        fig = figure(width=width, height=height, title=title,
                      background_fill_color=session.background_color)
        fig.title.align = 'center'
        fig.xgrid.grid_line_dash = [8, 3, 2, 3]
        fig.ygrid.grid_line_dash = [8, 3, 2, 3]
        fig.toolbar.autohide = True
        if _color_bar_made and _add_color_bar:
            fig.add_layout(color_bar, 'right')
        return fig

    plot = Plot(make_figure=_make_fig, steps=steps, description=description,
                figure=_make_fig(), width=width, grid_visible=grid_visible,
                width_session=session.width, session=session)

    if save_path:
        save_base(plot=plot, save_path=save_path,
                  file_exists_mode=session.file_exists_mode,
                  width_total_as_session=False, share_x=False, share_y=False)

    if show_plot:
        return show_base(plot) or plot
    else:
        return plot

def _update_line_default_args(line, session):
    def line_updated(y, x=None, width=session.width, height=session.height,
                     description=session.description, title=session.title,
                     show_plot=session.show_plot, color=None,
                     colorbar_type='auto', legend='auto',
                     save_path=session.save_path,
                     grid_visible=session.grid_visible):
        plot = line(y=y, x=x, width=width, height=height,
                    description=description, title=title, show_plot=show_plot,
                    color=color, colorbar_type=colorbar_type, legend=legend,
                    grid_visible=grid_visible, session=session,
                    save_path=save_path)
        return plot
    return line_updated
