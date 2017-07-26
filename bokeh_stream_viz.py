import numpy as np
from bokeh.models.sources import ColumnDataSource
from bokeh.plotting import figure, curdoc
from functools import partial
from collections import deque

# data sources
em = ColumnDataSource(data=dict(x=[0], y=[0]))
ec = ColumnDataSource(data=dict(x=[0], y=[0]))

# figures
ec_fig = figure(plot_width=800, plot_height=250)
ec_fig.line("x", "y", source=ec, line_color='red', legend='EC')

new_data_ec = dict(x=[0], y=[0])
# data buffer
y = deque()
x = deque()

step = 0 # step counter
n_show = 25 # number of points to keep and show

# open file
f = open('data/running_avg.dat', 'r')
# jump to the end of the file
f.seek(0,2)
doc = curdoc()

def update(data):
    ec.stream(data, n_show) # only show the last `n_show` data points

def read_data():
    global step
    # read current line
    newline = f.readline()
    # if there is no new line since last read cycle, do nothing
    # else:
    if newline:
        a0 = list(map(np.float, newline.split()))
        x.append(step)
        y.append(a0[1])
        # limit x and y to size
        # we cannot reassign global variables, hence we modify
        if len(x) > n_show:
            x.popleft()
            y.popleft()
        new_data_ec['x'] = x
        new_data_ec['y'] = y
        doc.add_next_tick_callback(partial(update, new_data_ec))
        step += 1

doc.add_root(ec_fig)
doc.add_periodic_callback(read_data, 100) # call ever 100'th ms
