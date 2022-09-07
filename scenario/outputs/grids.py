import pandas as pd
import geopandas as gpd
from pathlib import Path

def configure(context):
    context.stage("scenario.grids")

def execute(context):
    output_path = context.path()

    grids_output_path = output_path + "/INPUT/GRILLES/"
    Path(grids_output_path).mkdir(parents=True, exist_ok=True)

    df_grids: pd.DataFrame = context.stage("scenario.grids")
    pd.DataFrame(df_grids.loc["sortie"]).T.to_csv(
        grids_output_path + "info-grid-sortie.dat", sep="\t", index=False
    ) 
    pd.DataFrame(df_grids.loc["meteo"]).T.to_csv(
        grids_output_path + "info-grid-meteo.dat", sep="\t", index=False
    )

