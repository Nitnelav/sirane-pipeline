import pandas as pd
import geopandas as gpd

def configure(context):
    context.config("matsim_simulation_path")

def execute(context):
    emissions_file = "%s/%s" % (context.config("matsim_simulation_path"), "/emissions_network.shp")

    gdf_emissions = gpd.read_file(emissions_file)

    return gdf_emissions