import pandas as pd
import geopandas as gpd
from pathlib import Path
import shutil

def configure(context):
    context.config("output_path")
    context.config("zone_file", None)
    context.stage("data.spatial.departments")

def execute(context):
    urban_path = context.config("output_path") + "/URBAN"
    zone_path = urban_path + "/INPUT/ZONE"
    Path(zone_path).mkdir(parents=True, exist_ok=True)

    zone_file = context.config("zone_file")
    if (zone_file == None):
        gdf_departments: gpd.GeoDataFrame = context.stage("data.spatial.departments")
        gdf_zone = gdf_departments.dissolve()
        gdf_zone.to_file(zone_path + "/zone.shp")
    else:
        shutil.copy(zone_file, zone_path + "/zone.shp")

    return zone_path + "/zone.shp"