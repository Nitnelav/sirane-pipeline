import pandas as pd
import geopandas as gpd

def configure(context):
    context.stage("data.bdtopo.raw")

def execute(context):
    gdf_buildings = context.stage("data.bdtopo.raw")

    return gdf_buildings