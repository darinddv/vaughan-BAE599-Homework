import shapely.geometry as shp

# Needed for working with arrays and plotting

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as io

def polygon():
    # Create points
    # These can stand for markers in a field
    point1 = shp.Point(1.25,2.3)
    point2 = shp.Point(0.25,2)

    # Create polygon
    # These coordinates specify the boundaries as
    # (x,y) points
    poly1coord1 = (0,5)
    poly1coord2 = (1,1)
    poly1coord3 = (3,0)

    poly2coord1 = (1,2)
    poly2coord2 = (2,0)
    poly2coord3 = (0,0)

    # Bunch the coordinates into a list make things tidy
    # Not necessary since the points may be typed into Polygon
    # directly, but more complicated polygons will look cluttered
    coordinates1 = [poly1coord1,poly1coord2,poly1coord3]
    coordinates2 = [poly2coord1,poly2coord2,poly2coord3]
    # Supply a list of coordinates as the argument
    # Note, if you do not use a list to bunch 
    # coordinates beforehand, you must use [] 
    # in the Polygon method call: Polygon([(0,5), ..., etc])
    polygon1 = shp.Polygon(coordinates1)
    polygon2 = shp.Polygon(coordinates2)    

    # Now extract the coordinate arrays
    # There are two: one for x, one for y
    x1 = polygon1.exterior.coords.xy[0].tolist()
    y1 = polygon1.exterior.coords.xy[1].tolist()

    x2 = polygon2.exterior.coords.xy[0].tolist()
    y2 = polygon2.exterior.coords.xy[1].tolist()

    # Initialize an empty Figure object
    fig = go.Figure()
    
    # Fill Figure object with plots
    fig.add_scatter(x=x1, y=y1,fill="toself", line=dict(color='mediumpurple'))
    fig.add_scatter(x=[0,1,2,0], y=[0,2,0,0], fill="toself",line=dict(color='yellowgreen'))    
    fig.add_scatter(x=[point1.x, point2.x], y=[point1.y, point2.y], mode="markers", line=dict(color='red'))

    plot_div = io.to_html(fig, full_html=True)

    return plot_div



if (__name__ == '__main__'):
    polygon()