import pandas as pd
import geopandas as gpd
from pathlib import Path

def configure(context):
    context.stage("data.air_pollution.selected")

def execute(context):
    output_path = context.path()

    df_air_pollution: pd.DataFrame = context.stage("data.air_pollution.selected")
    
    pollution_output_path = output_path + "/INPUT/FOND/"
    Path(pollution_output_path).mkdir(parents=True, exist_ok=True)

    df_air_pollution.to_csv(
        pollution_output_path + "Concentration_fond.dat", sep="\t",
        index_label="Date", date_format='%d/%m/%Y %H:%M'
    )

