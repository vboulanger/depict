Welcome to depict's documentation!
==================================

Depict is built on the top of Bokeh. It aims at providing one-line access
to the most common types of graph by setting opinionated defaults and avoiding
boilerplate code. Graphs are aesthetic, efficiently rendered, interactive and
sharable.

It is made for data-{scientist, analyst, engineer, lead, etc} seeking to
create beautiful plots while reducing the graph-tweaking time.

Why Depict?
-----------

* **Made simple** – built-in defaults get you to common graph types fast.
* **Looking fresh** – attractive, shareable visual output by default.
* **Stay organized** – keep interactive HTML exports with contextual metadata.
* **Infinitely customizable** – extend any Depict figure with native Bokeh glyphs.

Getting started
---------------

Install the latest release from PyPI:

.. code-block:: bash

   pip install depict

Create your first plot in a single line:

.. code-block:: python

   import depict
   depict.line([3, 1, 4, 1, 5, 9])

Visit the :ref:`gallery <gallery>` for more examples or explore the individual
plot types below.

Contents
--------

.. toctree::
   :maxdepth: 2

   philosophy.rst
   gallery.rst
   line.rst
   point.rst
   histogram.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
