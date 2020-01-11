# Depict
**Business grade plots in seconds.**

Depict is built on the top of Bokeh. It aims at providing one-line access 
to the most common types of graph by avoiding boilerplate code. Graphs are
esthetic, efficiently rendered, interactive and sharable.

It is made for data {scientist, analyst, engineer, lead, etc} seeking to 
create beautiful plots while reducing the graph-tweaking time.

# Guiding principles
* **Made simple**

While Bokeh, Matplotlib, Dash and many others provide a tremendous flexibility,
Depict will get you faster to the classical graphs by making choices for you.
Scatter plots, histograms and other heat-maps are accessible in one line.
* **Looking fresh is not more expensive**

Graphs should be ready to share and pleasant to look at, for technical and 
 non technical audience. Depict takes care of the freshness of your graphs
 to let you focus on the maths. 
* **Stay organized**

Depict helps you save you graphs in html with textual metadata and share them
around. Your plots are kept interactive, contextualized and readable in the
browser.

* **Infinitely customizable with Bokeh**

You want to personalized you graph further? You can use Bokeh glyphs to 
interact with depict figure and get access to a fine level of granularity.

# Install


* Install depict from PyPI (recommended):

    `pip install depict`

* Install depict from GitHub sources:
    
    Clone the git repository
     
    `git clone https://github.com/vboulanger/depict.git`
   
    Inside the depict folder, install the package
    
  ```
  cd depict  
  sudo python setup.py install
  ```

# Get started
### Hello world

```
import depict

depict.line([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
```

### Key features





