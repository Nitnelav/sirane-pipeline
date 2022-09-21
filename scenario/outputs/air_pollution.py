import pandas as pd
import geopandas as gpd
from pathlib import Path

def configure(context):
    context.stage("data.air_pollution.selected")
    context.config("pollutants", [])

def execute(context):
    output_path = context.path()
    required_pollutants = context.config("pollutants")

    df_air_pollution: pd.DataFrame = context.stage("data.air_pollution.selected")

    pollution_output_path = output_path + "/INPUT/FOND/"
    Path(pollution_output_path).mkdir(parents=True, exist_ok=True)

    # df_air_pollution = df_air_pollution[required_pollutants]
    df_air_pollution.to_csv(
        pollution_output_path + "Concentration_fond.dat", sep="\t",
        index_label="Date", date_format='%d/%m/%Y %H:%M'
    )

