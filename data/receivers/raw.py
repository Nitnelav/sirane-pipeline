import pandas as pd
import geopandas as gpd

def configure(context):
    context.config("receivers_file")

def execute(context):

    gdf_receivers = gpd.read_file(context.config("receivers_file"))

    return gdf_receivers 