from script import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource 

#converted datetime values to string, to be used in hover 
df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H-%M-%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H-%M-%S")

#data source
cds=ColumnDataSource(df)

#figure initialization
p=figure(x_axis_type='datetime',height=100,width=500,title="Motion Graph",sizing_mode='scale_width')

#remove ticks
p.yaxis.minor_tick_line_color=None   
p.ygrid[0].ticker.desired_num_ticks=1

#hover tool addition
hover=HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
p.add_tools(hover)

#green rectangles addition
q=p.quad(left="Start", right="End", bottom=0, top=1, color="green", source=cds)

output_file("Graph.html")
show(p)