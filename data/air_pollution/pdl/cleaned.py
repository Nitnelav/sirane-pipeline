import pandas as pd
import geopandas as gpd

def configure(context):
    context.stage("data.air_pollution.pdl.raw")

def execute(context):

    # TODO : add zero pollution for absent poluttants

    df_data: pd.DataFrame = context.stage("data.air_pollution.pdl.raw")
    df_data["influence"] = df_data["influence"].astype("category")

    df_data = df_data.loc[df_data["influence"] == "background"]
    df_data = df_data.loc[df_data["statut_valid"] == True]
    df_data = df_data.loc[df_data["code_station (ue)"] == "FR23188"]

    df_data["date"] = pd.to_datetime(df_data["date_debut"])

    pollutants = df_data['nom_poll'].astype(str).unique()
    for poll in pollutants:
        df_data[poll] = None

    for i, row in df_data.iterrows():
        df_data.at[i, row["nom_poll"]] = row["valeur"]

    df_data = df_data[["date"] + list(pollutants)]
    # df = df[["date", 'nom_station'] + list(pollutants)]


    df_data = df_data.groupby(["date"]).mean().reset_index()

    df_data = df_data.set_index("date")
    df_data = df_data.sort_index()

    df_data = df_data.resample("1h").ffill()

    return df_data