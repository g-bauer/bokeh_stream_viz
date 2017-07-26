# Continuously visualizing data from a file in the browser.

This is a toy example of a live visualization in the browser using bokeh.
Data is gathered from a (continuously growing) file.

The ipython notebook implementation uses a loop that fetches entries from the file one after another.
[This SO answer](https://stackoverflow.com/questions/43101497/how-do-stream-data-to-a-bokeh-plot-in-jupyter-with-a-high-refresh-rate) greatly helped with the notebook implementation.

The "browser" version relies on the `bokeh server` and uses a callback function.
It would be nice to trigger callbacks once the observed file changes.

## Prerequesites

- [bokeh](http://bokeh.pydata.org/en/latest/)
- numpy

## Usage

Assume that you start a program that writes to the file `running_avg.dat`.
To visualize the data (or a computation with said data), simply type:

### Browser

```terminal
bokeh serve --show bokeh_stream_viz.py
```

### Ipython notebook

Simply execute the cell within the notebook.
