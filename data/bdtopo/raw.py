import pandas as pd
import geopandas as gpd


def configure(context):
    context.stage("data.bdtopo.download")
    context.stage("data.spatial.departments")
    context.config("zone_file", None)

def execute(context):
    building_file =  context.stage("data.bdtopo.download")

    gdf_departments: gpd.GeoDataFrame = context.stage("data.spatial.departments")
    bounding_box = gdf_departments.dissolve().iloc[0].geometry

    gdf_buildings: gpd.GeoDataFrame = gpd.read_file(
        "%s/%s" % (context.path("data.bdtopo.download"), building_file),
        mask=bounding_box,
    )
    
    gdf_buildings = gdf_buildings[["HAUTEUR", "geometry"]]
    
    zone_file = context.config("zone_file")
    if zone_file != None:
        zone = gpd.read_file(zone_file)
        gdf_buildings = gdf_buildings.loc[gdf_buildings.intersects(zone.iloc[0].geometry)]

    return gdf_buildings