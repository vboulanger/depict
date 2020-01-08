from bokeh.plotting import show as show_bokeh

def show(plot):
    fig = plot.make_figure()
    for step in plot.steps:
        step(fig)
    show_bokeh(fig)
