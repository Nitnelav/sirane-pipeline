import pandas as pd
import geopandas as gpd

def configure(context):
    context.stage("data.matsim.facilities.raw")

def execute(context):
    df_receivers: pd.DataFrame = context.stage("data.matsim.facilities.raw")

    df_receivers = df_receivers.rename(columns={"id": "Id", "x": "X", "y": "Y"})
    df_receivers = df_receivers.drop(columns=["activity", "linkId"])
    df_receivers["Z"] = 4
    df_receivers["Type"] = 0

    return df_receivers