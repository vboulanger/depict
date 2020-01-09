class Plot:
    def __init__(self, make_figure, steps, description, width, grid_visible, width_session):
        self.make_figure = make_figure
        self.steps = steps
        self.description = description
        self.width = width
        self.grid_visible = grid_visible
        self.width_session = width_session

    def __add__(self, other):
        new_description = self.description + '<br>' + other.description
        return Plot(make_figure=self.make_figure,
                    steps=self.steps + other.steps, description=new_description,
                    width=self.width, grid_visible=self.grid_visible,
                    width_session=self.width_session)
