import contextlib
from hashlib import sha256
import os


def wrap(id_, caption, label, directory):
    s = r'\begin{figure}[H]' + '\n\t'
    s += r'\centering' + '\n\t'
    s += r'\includegraphics[width=\textwidth]{' + \
        directory + id_+'.png}' + '\n\t'
    s += r'\caption{' + r'\href{run:./' + \
        'htmls/' + id_ + r'.html}{(View as HTML.)} '
    s += caption + r'}' + '\n\t'
    s += r'\label{fig:' + label + r'}' + '\n'
    s += r'\end{figure}'
    return s


def finish_fig(fig, caption=None, label=None):
    id_ = sha256(fig.to_json().encode()).hexdigest()
    if caption is None:
        caption = 'caption'
    if label is None:
        label = id_

    with contextlib.suppress(FileExistsError):
        os.mkdir('figures/' + id_+'/')
    directory = 'figures/' + id_ + '/'

    with open(f"{directory}{id_}.tex", 'w') as f:
        f.write(wrap(id_, caption, label, directory))

    fig.write_html(f"{'htmls/'}{id_}.html")
    fig.write_image(f"{directory}{id_}.png", width=1000, height=720)

if __name__ == '__main__':
    import plotly.express as px
    import pandas as pd
    import numpy as np
    import plotly.graph_objects as go
    """example"""
    df = px.data.tips()

    fig = px.density_heatmap(df, x="total_bill", y="tip")
    finish_fig(fig, caption = "This figure shows an example of a 2 dimensional histogram", label = None)
    fig.show()
