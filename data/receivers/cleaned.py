import pandas as pd
import geopandas as gpd

def configure(context):
    context.stage("data.receivers.raw")

def execute(context):
    gdf_recerivers = context.stage("data.receivers.raw")

    return gdf_recerivers