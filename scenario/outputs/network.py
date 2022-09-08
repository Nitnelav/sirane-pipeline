import pandas as pd
import geopandas as gpd
from pathlib import Path

def configure(context):
    context.stage("data.spatial.departments")
    context.stage("scenario.roads.processed")

def execute(context):
    output_path = context.path()

    network_output_path = output_path + "/INPUT/RESEAU/"
    Path(network_output_path).mkdir(parents=True, exist_ok=True)

    gdf_departments: gpd.GeoDataFrame = context.stage("data.spatial.departments")
    latitude = gdf_departments.to_crs("EPSG:4326").dissolve().iloc[0].geometry.centroid.y

    with open(network_output_path + "Site_Disp.dat", 'w') as f:
        f.writelines([
            "/ Caracteristiques du quartier :\n",
            "/-------------------------------\n",
            "Latitude [deg] = %f\n" % latitude,
            "Rugosite aerodynamique [m] = 0.9\n",
            "Epaisseur de deplacement [m] = 13.0\n",
            "Albedo = 0.1873\n",
            "Emissivite = 0.88\n",
            "Coefficient de Priestley-Taylor = 0.5\n"
        ])

    gdf_roads: gpd.GeoDataFrame = context.stage("scenario.roads.processed")
    gdf_roads.index.names = ['ID']
    gdf_roads.to_file(network_output_path + "Reseau_rues-SIRANE.shp", index=True)



