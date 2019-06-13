
#plotly
import pandas
import plotly
dir(plotly)

studentlist = [["Steve",32,"male"],["Lia",28,"female"],["Vin",45,"male"],["Katie",38,"female"]]
studentlistdf = pandas.DataFrame(studentlist,columns=["Name","Age","Gender"],index=["1","2","3","4"])
print(studentlistdf)


#graphing
from plotly.offline import plot
import plotly.graph_objs as go

agename = go.Bar(x=studentlistdf["Name"], y=studentlistdf["Age"])

plot([agename])


#getting data
import pandas as pd

df = pd.read_excel("GISdata.xlsx",sheet_name = "womenOccupation")

#plotting data on bar graphs
womenoccupation = go.Bar(x=df["occupation"],y=df["women"],
                
                marker = {"color": df["women"], "colorscale":  "Jet"}
                 )
plot([womenoccupation])

titles = go.Layout(
                    title = "Percentage of Women Employed by Occupation",
                    
                    xaxis=go.layout.XAxis(
                            title=go.layout.xaxis.Title(
                            text="Occupation",
                        )
                    ),
                    
                    yaxis=go.layout.YAxis(
                            title=go.layout.yaxis.Title(
                            text="Percentage"
                            )
                        )
                    )
                            
fig = go.Figure(data=[womenoccupation],layout = titles)

plot(fig)
