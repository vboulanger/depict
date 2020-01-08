from bokeh.io import output_notebook

class Session:
    def __init__(self, width, height, jupyter_notebook,
                 background_color, grid_visible, show_plot):
        self.width = width
        self.height = height
        if jupyter_notebook:
            output_notebook()
        self.background_color = background_color
        self.grid_visible = grid_visible
        self.show_plot = show_plot
