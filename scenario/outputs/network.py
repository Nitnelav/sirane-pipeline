import pandas as pd
import geopandas as gpd
from shapely.geometry import LineString
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

    gdf_roads["NDDEB"] = gdf_roads["NDDEB"].astype(int)
    gdf_roads["NDFIN"] = gdf_roads["NDFIN"].astype(int)

    unique_deb = gdf_roads["NDDEB"].unique()
    # unique_deb.sort()
    replace_nodes = {}
    for i in range(len(unique_deb)):
        replace_nodes[unique_deb[i]] = i

    gdf_roads = gdf_roads.replace({"NDDEB": replace_nodes, "NDFIN": replace_nodes})

    gdf_roads = gdf_roads.reset_index(drop=True)
    gdf_roads.index = gdf_roads.index.rename("ID")

    # gdf_roads["points"] = gdf_roads["geometry"].apply(lambda g : nb_points(g))
    # gdf_roads["length"] = gdf_roads["geometry"].apply(lambda g : length(g))
    gdf_roads.to_file(network_output_path + "Reseau_rues-SIRANE.shp", index=True)


def nb_points(g: LineString):
    return len(g.coords)

def length(g: LineString):
    return g.length