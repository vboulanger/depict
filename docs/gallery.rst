Gallery
=======

.. image:: _static/example_gallery_1.png

::

    import depict
    import numpy as np
    import scipy

    p_all = []
    for i in range(1, 5):
        x = np.random.rand(i)
        y = np.random.rand(i)
        pol = scipy.interpolate.lagrange(x, y)
        p = depict.point(x, y, show_plot=False, color='Red',
                         title='Lagrange - {}'.format(i))
        p += depict.line(x=np.linspace(0, 1, 1000),
                         y=scipy.polyval(pol, np.linspace(0, 1, 1000)),
                         show_plot=False)
        p_all.append(p)
    depict.show(np.reshape(p_all, (2, 2)))
