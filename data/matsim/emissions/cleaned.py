import pandas as pd
import geopandas as gpd
import numpy as np

import datetime

def configure(context):
    context.stage("data.matsim.emissions.raw")
    context.config("pollutants", [])

    # context.config("air_pollution_year")

def execute(context):

    # air_pollution_year = context.config("air_pollution_year")

    # timestamp_string = "01/01/%s 00:00:00" % air_pollution_year
    # timestamp_element = datetime.datetime.strptime(timestamp_string,"%d/%m/%Y %H:%M:%S")
    # timestamp_offset = datetime.datetime.timestamp(timestamp_element)

    required_pollutants = context.config("pollutants")

    gdf_emissions: gpd.GeoDataFrame = context.stage("data.matsim.emissions.raw")

    df_emissions = pd.DataFrame(gdf_emissions)
    df_emissions = df_emissions.drop(columns=["geometry"])

    # fix pollutants column names
    df_emissions =  df_emissions.rename(columns={"PM": "PM10"})

    # for poll in required_pollutants:
    #     if poll not in df_emissions:
    #         df_emissions[poll] = 0.0

    min_time = df_emissions["time"].min()
    # remove everything beyond min time of the next day
    df_emissions = df_emissions.loc[df_emissions["time"] < (min_time + 86400)]
    # move second day data at the beginning of the first one
    df_emissions["time"] = df_emissions["time"] % 86400

    df_emissions = df_emissions.sort_values(by=['link', 'time'])

    time_index = np.arange(0, 86400, 3600)
    df_emissions = (
        df_emissions.groupby(["link"], )
        .apply(lambda group: group.set_index("time").reindex(time_index, fill_value=0))
        .drop(columns=["link"])
        .reset_index()
    )

    # df_emissions["timestamp"] = df_emissions["time"] + timestamp_offset + 3600
    # df_emissions["date"] = pd.to_datetime(df_emissions["timestamp"], errors='coerce', unit='s')

    return df_emissions