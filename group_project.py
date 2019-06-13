
#graphing
from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd



df = pd.read_excel("GISdata.xlsx",sheet_name = "cancercases")




Cancer = go.Bar(x=df["CancerType"],y=df["Number"],
                
                marker = {"color": df["Number"], "colorscale":  "YlGnBu"}
                 )

plot([Cancer])

titles = go.Layout(
                    title = "Cancer Cases in Women",
                    
                    xaxis=go.layout.XAxis(
                            title=go.layout.xaxis.Title(
                                    text="Cancer Type",
                                    )
                            ),
                    
                    yaxis=go.layout.YAxis(
                            title=go.layout.yaxis.Title(
                                    text="Number of Occurances"
                                    )
                                )
                    
                    
                    )
                            
fig = go.Figure(data=[Cancer],layout = titles)

plot(fig)
