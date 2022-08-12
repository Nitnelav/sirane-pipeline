import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon, Point
from pathlib import Path

def configure(context):
    context.stage("scenario.roads.processed")
    context.stage("data.meteo.cleaned")
    context.stage("data.air_pollution.selected")
    context.stage("data.spatial.departments")

    context.config("output_path")

def execute(context):

    output_path = context.config("output_path")
    
    df_meteo: pd.DataFrame = context.stage("data.meteo.cleaned")
    
    meteo_output_path = output_path + "/INPUT/METEO/"
    Path(meteo_output_path).mkdir(parents=True, exist_ok=True)

    df_meteo[
        ["wind_spd", "wind_dir", "temp", "cloud", "precip"]
    ].to_csv(
        meteo_output_path + "meteo.txt", sep="\t",
        header=["U", "Dir", "Temp", "Cld", "Precip"],
        index_label="Date", date_format='%d/%m/%Y %H:%M'
    )
    
    with open(meteo_output_path + "/Site_Meteo.dat", 'w') as f:
        f.writelines([
            "/ Caracteristiques du site meteo :\n",
            "/---------------------------------\n",
            "Hauteur par rapport au sol [m] = 10.0\n",
            "Rugosite aerodynamique [m] = 0.1\n",
            "Epaisseur de deplacement [m] = 0.0\n",
            "Albedo = 0.1873\n",
            "Emissivite = 0.88\n",
            "Coefficient de Priestley-Taylor = 0.5"
        ])

    df_air_pollution: pd.DataFrame = context.stage("data.air_pollution.selected")
    
    pollution_output_path = output_path + "/INPUT/FOND/"
    Path(pollution_output_path).mkdir(parents=True, exist_ok=True)

    df_air_pollution.to_csv(
        pollution_output_path + "Concentration_fond.dat", sep="\t",
        index_label="Date", date_format='%d/%m/%Y %H:%M'
    )

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
            "Coefficient de Priestley-Taylor = 0.5"
        ])

    gdf_roads: gpd.GeoDataFrame = context.stage("scenario.roads.processed")
    gdf_roads.to_file(network_output_path + "Reseau_rues-SIRANE-UTM31.shp")

    return
