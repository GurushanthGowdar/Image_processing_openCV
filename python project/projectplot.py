

from pythonproject import df 
from bokeh.plotting import figure,show,output_file
from bokeh.models import HoverTool,ColumnDataSource

df["start_String"]=df["START"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["END_STRING"]=df["END"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds=ColumnDataSource(df)

p=figure(x_axis_type='datetime',height=100,width=500,title="project plot graph")
#p.yaxis.minor_tick_line_color=None
#p.ygrid[0].ticker.desired_num_ticks=1

hover=HoverTool(tooltips=[("START","@start_String"),("END","@END_STRING")])
p.add_tools(hover)


q=p.quad(left="START",right="END",top=1,bottom=0,color="green",source=cds)

output_file("projectplot2.html")
show(p)























