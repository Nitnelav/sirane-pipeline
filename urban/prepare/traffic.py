import pandas as pd
import geopandas as gpd
from pathlib import Path

def configure(context):
    context.config("output_path")
    context.stage("data.matsim.roads.cleaned")

def execute(context):
    urban_path = context.config("output_path") + "/URBAN"
    traffic_path = urban_path + "/INPUT/TRAFFIC"
    Path(traffic_path).mkdir(parents=True, exist_ok=True)

    gdf_traffic: gpd.GeoDataFrame = context.stage("data.matsim.roads.cleaned")
    gdf_traffic.drop(columns=["detailed_geometry"], inplace=True)
    gdf_traffic.to_file(traffic_path + "/traffic.shp")

    return traffic_path + "/traffic.shp"