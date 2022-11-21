import pandas as pd
import geopandas as gpd
from shapely import wkb

def configure(context):
    context.stage("data.bdtopo.raw")

def execute(context):
    gdf_buildings = context.stage("data.bdtopo.raw")
    drop_z = lambda geom: wkb.loads(wkb.dumps(geom, output_dimension=2))
    gdf_buildings["geometry"] = gdf_buildings["geometry"].transform(drop_z)
    return gdf_buildings