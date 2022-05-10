import contextlib
import plotly.express as px
import pandas as pd
import numpy as np
from hashlib import sha256
import os
import plotly.graph_objects as go


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


if True:
    df = pd.read_csv('_deg89_100G.data')
    fig = px.density_heatmap(df, x="orgx", y="orgy",
                             marginal_x="histogram", marginal_y="histogram")
    # set x and y scale same
    fig.update_layout(xaxis_range=[-5, 5], yaxis_range=[-5, 5])
    finish_fig(fig, 'XY-distribution', 'None')

else:
    fig = go.Figure(data=[
        go.Mesh3d(

            # 8 vertices of a cube
            x=[-1, -1, -1, 1, 1, 1, 1, -1],
            y=[-1, -1, 1, -1, -1, 1, 1, 1],
            z=[-1, 1, -1, -1, 1, -1, 1, 1],

            opacity=0.6,
            color='#DC143C',
            flatshading=True
        )
    ])
    fig.show()
