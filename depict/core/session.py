from bokeh.io import output_notebook

class Session:
    def __init__(self, width=300, height=300, jupyter_notebook=False):
        self.width = width
        self.height = height
        if jupyter_notebook:
            output_notebook()
