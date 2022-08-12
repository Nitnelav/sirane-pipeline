import pandas as pd
import geopandas as gpd
import gzip

def configure(context):
    context.stage("data.meteo.download")

def execute(context):

    downloaded_files, stations_file = context.stage("data.meteo.download")
    
    df_data = pd.DataFrame()
    for date, file in downloaded_files.items():
        with gzip.open("%s/%s" % (context.path("data.meteo.download"), file)) as f:
            df_data = pd.concat([df_data, pd.read_csv(f, sep=";")])
    
    df_stations: gpd.GeoDataFrame = gpd.read_file("%s/%s" % (context.path("data.meteo.download"), stations_file))
    df_stations = df_stations.to_crs(2154)
    
    return df_data, df_stations