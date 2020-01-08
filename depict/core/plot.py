class Plot:
    def __init__(self, make_figure, steps):
        self.make_figure = make_figure
        self.steps = steps

    def __add__(self, other):
        return Plot(make_figure=self.make_figure, steps=self.steps + other.steps)
