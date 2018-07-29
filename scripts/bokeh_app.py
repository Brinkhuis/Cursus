# imports
from bokeh.io import curdoc
from bokeh.plotting import figure, output_file, show, reset_output
from bokeh.models import ColumnDataSource
from bokeh.layouts import widgetbox, row, column
from bokeh.models.widgets import Select, Dropdown
from bokeh.sampledata.iris import flowers # load data

# setup data
species = 'setosa'
source = ColumnDataSource(flowers.loc[flowers.species == species])
source.data = ColumnDataSource.from_df(flowers.loc[flowers.species == species])

# setup tooltips
tooltips = [('index', '@index'),
            ('Sepal Length', '@sepal_length'),
            ('Sepal Width', '@sepal_width'),
            ('Species', '@species')]

# setup plot
p = figure(plot_width = 400, plot_height = 400, tooltips = tooltips)
p.circle('sepal_length', 'sepal_width', size = 10, color = 'blue', alpha = 0.5, source = source)

# setup widget
menu = [(s.capitalize(), s) for s in flowers.species.unique()]
dropdown = Dropdown(label = 'Species',  menu = menu)

# callback to widgets
def callback(attr, old, new):
    species = dropdown.value
    source.data = ColumnDataSource.from_df(flowers.loc[flowers.species == species])
dropdown.on_change('value', callback)

# arrange plots and widgets in layouts
layout = column(dropdown, p)
curdoc().add_root(layout)