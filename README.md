A document that contains figures or plots can sometimes make it difficult for the reader to read and identify the data points correctly. Especially plots of a terrain or other multidimensional data sets are difficult to recognize and follow in this way. The python library [plotly](https://plotly.com/) has beautiful ways to visualize data interactively, but only a fraction of this representation is brought to the end reader. There is a workaround for this problem, which is to link to the original plot in the document using python and [LaTeX](https://www.latex-project.org/) 







Example usage:
``` python
from plotly_latex import finish_fig 
import  plotly.express as px

# load example data
df = px.data.tips() 
fig = px.density_heatmap(df, x="total_bill", y="tip")
caption = "<caption>"
label = "<label>"
finish_fig(fig, caption = caption, label = label) 
```
If you do not provide a label, a hash is casted on the figure object and is used as a label
output code: ```<label>.tex```
```latex
\begin{figure}[H]
	\centering
	\includegraphics[width=\textwidth]{figures/<label>.png}
	\caption{\href{run:./htmls/<label>.html}{(View source) <caption>}}
	\label{fig:<label>}
\end{figure}'
```


Beside the output LaTeX code, two additional files are created: 
```
. 
├── figures
│    └── <label> 
│          └── <label>.png
│          └── <label>.tex
├── htmls
      └── <label>.html 
```

All that’s left to do, is a simple input flag in your LaTeX code. Make sure, that the main LaTeX file is in the same directory as the folders „htmls“ and „figures“:
```latex
\input{figures/<label>.tex}
```
If you hand the compiled PDF document to someone, also make sure that the reader opens the PDF in the same directory as the folder „htmls“.


