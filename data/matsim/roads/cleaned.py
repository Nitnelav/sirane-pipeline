import pandas as pd
import geopandas as gpd
import numpy as np
import re

def configure(context):
    context.stage("data.matsim.roads.raw")
    context.config("matsim_detailed_link_path", None)

def execute(context):
    gdf_roads: gpd.GeoDataFrame = context.stage("data.matsim.roads.raw")

    matsim_detailed_link_path = context.config("matsim_detailed_link_path")

    if matsim_detailed_link_path != None:
        df_details = pd.read_csv(matsim_detailed_link_path, sep=',')
        df_details = df_details.rename(columns={"LinkId": "link_id", "Geometry": "detailed_geometry"})
        df_details["link_id"] = df_details["link_id"].astype(str)
        gdf_roads["link_id"] = gdf_roads["link_id"].astype(str)
        gdf_roads = pd.merge(gdf_roads, df_details, on="link_id", how="left")
        gdf_roads["detailed_geometry"] = gdf_roads["detailed_geometry"].apply(lambda g: fix_wtk(g))
        gdf_roads["detailed_geometry"] = gdf_roads["detailed_geometry"].fillna(gdf_roads["geometry"].to_wkt())
        gdf_roads["geometry"] = gpd.GeoSeries.from_wkt(gdf_roads["detailed_geometry"])

    gdf_roads = gdf_roads.loc[gdf_roads["modes"].str.contains("car")]

    return gdf_roads

def fix_wtk(geom):
    if geom is np.nan:
        return geom
    if re.match(r"LINESTRING\(\d+\.?\d+ \d+\.?\d+\)", geom):
        return np.nan
    return geom