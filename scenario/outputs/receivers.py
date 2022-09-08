import pandas as pd
import geopandas as gpd
from pathlib import Path

def configure(context):
    context.stage("data.receivers.selected")

def execute(context):
    output_path = context.path()

    receivers_output_path = output_path + "/INPUT/RECEPTEURS/"
    Path(receivers_output_path).mkdir(parents=True, exist_ok=True)

    gdf_receivers: gpd.GeoDataFrame = context.stage("data.receivers.selected")
    gdf_receivers["Fichier"] = "_"
    gdf_receivers.to_csv(
        receivers_output_path + "Recepteurs.dat", sep="\t", index=False
    )

