import pandas as pd
import geopandas as gpd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path

def configure(context):
    context.stage("data.matsim.emissions.cleaned")
    context.stage("scenario.roads.processed")
    context.config("air_pollution_year")
    context.config("pollutants", [])

def execute(context):
    output_path = context.path()
    air_pollution_year = context.config("air_pollution_year")
    required_pollutants = context.config("pollutants")

    emissions_output_path = output_path + "/INPUT/EMISSIONS/"
    Path(emissions_output_path).mkdir(parents=True, exist_ok=True)

    emissions_lin_output_path = output_path + "/INPUT/EMISSIONS/EMIS_LIN/"
    Path(emissions_lin_output_path).mkdir(parents=True, exist_ok=True)

    gdf_roads: gpd.GeoDataFrame = context.stage("scenario.roads.processed")

    df_emissions: pd.DataFrame = context.stage("data.matsim.emissions.cleaned")

    df_emissions = df_emissions.sort_values(by="link").rename(columns={"link": "Id"})

    time_list = np.arange(0, 86400, 3600)

    for time in time_list:
        time_string = "%dh" % (time // 3600)
        df = df_emissions.loc[df_emissions["time"] == time]
        df = df.drop(columns=["time"])
        df = df.set_index("Id")
        df.index = df.index.astype(int)
        df = df.reindex(gdf_roads.index.rename("Id"), fill_value=0.0)
        df = df.reset_index(drop=True)
        df.index = df.index.rename("Id")

        df = df[required_pollutants]
        df.to_csv(emissions_lin_output_path + "emis_rues_%s.dat" % time_string, sep="\t", float_format='%.6f', index=True)

    emis_trafic = []
    mod_trafic = []
    date_time = datetime(air_pollution_year, 1, 1, 0, 0, 0)
    while date_time.year == air_pollution_year:
        emis_trafic.append({
            "Date": date_time.strftime('%d/%m/%Y %H:%M'),
            "Fich_Emis": "EMISSIONS/EMIS_LIN/emis_rues_%dh.dat" % date_time.hour,
        })
        mod_trafic.append({
            "Date": date_time.strftime('%d/%m/%Y %H:%M'),
            "Coeff_Modul": "1.0",
        })
        date_time += timedelta(hours=1)

    df_emis_trafic = pd.DataFrame.from_dict(emis_trafic)
    df_emis_trafic.to_csv(emissions_lin_output_path + "Evol_Emis_Trafic.dat", sep="\t", index=False)

    df_mod_trafic = pd.DataFrame.from_dict(mod_trafic)
    df_mod_trafic.to_csv(emissions_lin_output_path + "Mod_Temp_Trafic.dat", sep="\t", index=False)

    with open(emissions_lin_output_path + "Sources_Lin.dat", 'w') as f:
        f.writelines([
            "Fich_Evol_Emis\tFich_Modul\n",
            "EMISSIONS/EMIS_LIN/Evol_Emis_Trafic.dat\tEMISSIONS/EMIS_LIN/Mod_Trafic.dat\n"
        ])

    with open(emissions_lin_output_path + "Mod_Trafic.dat", 'w') as f:
        f.writelines([
            "Espece	Type_Emis	Type_Modul	Fich_Modul_Temp	Fich_Modul_Heure	Fich_Modul_Jour	Fich_Modul_Mois\n"
            "*	0	0	EMISSIONS/EMIS_LIN/Mod_Temp_Trafic.dat	NULL	NULL	NULL"
        ])

    Path(emissions_output_path + "EMIS_PONCT/").mkdir(parents=True, exist_ok=True)
    with open(emissions_output_path + "EMIS_PONCT/Sources_Ponct.dat", 'w') as f:
        f.writelines([
            "Id	X	Y	Z	D	Ux	Uy	Uz	T	Fichier\n"
        ])

    Path(emissions_output_path + "EMIS_SURF/").mkdir(parents=True, exist_ok=True)
    with open(emissions_output_path + "EMIS_SURF/Sources_Surf.dat", 'w') as f:
        f.writelines([
            "Id	Fich_Grille	Fich_Evol_Emis	Fich_Modul\n"
        ])