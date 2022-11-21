import pandas as pd
import geopandas as gpd
from pathlib import Path

def configure(context):
    context.config("output_path")
    context.stage("data.bdtopo.cleaned")

def execute(context):
    urban_path = context.config("output_path") + "/URBAN"
    buildings_path = urban_path + "/INPUT/BUILDINGS"
    Path(buildings_path).mkdir(parents=True, exist_ok=True)

    gdf_bdtopo: gpd.GeoDataFrame = context.stage("data.bdtopo.cleaned")

    gdf_bdtopo.to_file(buildings_path + "/buildings.shp")

    return buildings_path + "/buildings.shp"