import pandas as pd
import geopandas as gpd
import matsim

def configure(context):
    context.config("matsim_simulation_path")

def execute(context):
    matsim_path = context.config("matsim_simulation_path")
    
    net: matsim.Network.Network = matsim.read_network(matsim_path + '/output_network.xml.gz')

    gdf_roads: gpd.GeoDataFrame = net.as_geo(projection="EPSG:2154")

    return gdf_roads