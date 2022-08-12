import pandas as pd
import geopandas as gpd

def configure(context):
    context.stage("data.spatial.departments")
    context.stage("data.meteo.raw")

def execute(context):

    df_data: pd.DataFrame
    gdf_stations: gpd.GeoDataFrame
    gdf_departments = context.stage("data.spatial.departments")
    df_data, gdf_stations = context.stage("data.meteo.raw")

    gdf_stations = gdf_stations.loc[gdf_stations.intersects(gdf_departments.dissolve().iloc[0].geometry)]
    df_data = df_data.rename(columns={"ff": "wind_spd", "dd": "wind_dir", "t": "temp", "n": "cloud", "rr3": "precip"})
    df_data = df_data[["numer_sta", "date", "temp", "wind_spd", "wind_dir", "cloud", "precip"]]

    df_data = df_data.loc[df_data["numer_sta"].isin(gdf_stations["ID"].astype(int).unique())]

    df_data["wind_spd"] = df_data["wind_spd"].astype(float).round(decimals = 2)
    
    df_data["cloud"] = df_data["cloud"].replace('mq', '0').astype(int)
    df_data["cloud"] = df_data["cloud"] * 8 // 100 

    df_data["temp"] = df_data["temp"].astype(float) - 273.15
    df_data["temp"] = df_data["temp"].round(decimals = 2)

    df_data["precip"] = df_data["precip"].replace('mq', '0').astype(float) / 3 # divide precipitations in the last 3 hours by 3 to get mm/h
    df_data["precip"] = df_data["precip"].round(decimals = 2)
    
    df_data["date"] = pd.to_datetime(df_data["date"], format='%Y%m%d%H%M%S', errors='coerce')
    df_data = df_data.set_index("date")
    df_data = df_data.resample("1h").ffill()

    return df_data