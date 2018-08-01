from bokeh.sampledata.autompg import autompg
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, LinearColorMapper, ColorBar
from bokeh.palettes import Viridis256
from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models.widgets import Dropdown

# data
autompg['brand'] = autompg.name.apply(lambda n: n.split(' ')[0])
source = ColumnDataSource(autompg)

# setup data
brand = 'ford'
source = ColumnDataSource(autompg.loc[autompg.brand == brand])
source.data = ColumnDataSource.from_df(autompg.loc[autompg.brand == brand])

# tooltips
tooltips = [('index', '@index'),
            ('Name', '@name'),
            ('Weight', '@weight'),
            ('Horsepower', '@hp'),
            ('Acceleration', '@accel')]

# figure
p = figure(plot_width = 800, plot_height = 500, tooltips = tooltips, title = 'car acceleration (in seconds)')

# color mapper
mapper = LinearColorMapper(palette = Viridis256, low = autompg.accel.min(), high = autompg.accel.max())

# color bar
color_bar = ColorBar(color_mapper = mapper, location = (0, 0))
p.add_layout(color_bar, 'right')

# data points
p.circle('weight', 'hp', size = 10, color = {'field': 'accel', 'transform': mapper}, alpha = 0.7, source = source)

# title
p.title.align = 'center'
p.title.text_color = Viridis256[50]
p.title.text_font = 'helvetica'
p.title.text_font_style = 'bold'
p.title.text_font_size = '16pt'

# x-axis
p.xaxis.axis_label = 'Weight'
p.xaxis.axis_label_text_color = Viridis256[150]

# y-axis
p.yaxis.axis_label = 'Horsepower'
p.yaxis.axis_label_text_color = Viridis256[150]

# setup widget
menu = [(b.capitalize(), b) for b in autompg.brand.unique()]
dropdown = Dropdown(label = 'Brand',  menu = menu)

# callback to widgets
def callback(attr, old, new):
    brand = dropdown.value
    source.data = ColumnDataSource.from_df(autompg.loc[autompg.brand == brand])
dropdown.on_change('value', callback)

# arrange plots and widgets in layouts
layout = column(dropdown, p)
curdoc().add_root(layout)
