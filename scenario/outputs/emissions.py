import pandas as pd
import geopandas as gpd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path

def configure(context):
    context.stage("data.matsim.emissions.cleaned")
    context.config("air_pollution_year")

def execute(context):
    output_path = context.path()
    air_pollution_year = context.config("air_pollution_year")

    emissions_output_path = output_path + "/INPUT/EMISSIONS/"
    Path(emissions_output_path).mkdir(parents=True, exist_ok=True)

    emissions_lin_output_path = output_path + "/INPUT/EMISSIONS/EMIS_LIN/"
    Path(emissions_lin_output_path).mkdir(parents=True, exist_ok=True)

    df_emissions: pd.DataFrame = context.stage("data.matsim.emissions.cleaned")
    df_emissions = df_emissions.sort_values(by="link").rename(columns={"link": "Id"})

    time_list = np.arange(0, 86400, 3600)

    for time in time_list:
        time_string = "%dh" % (time // 3600)
        df = df_emissions.loc[df_emissions["time"] == time]
        df.drop(columns=["time"])
        df.to_csv(emissions_lin_output_path + "emis_rues_%s.dat" % time_string, sep="\t", index=False)

    emis_trafic = []
    date_time = datetime(air_pollution_year, 1, 1, 0, 0, 0)
    while date_time.year == air_pollution_year:
        emis_trafic.append({
            "Date": date_time.strftime('%d/%m/%Y %H:%M'),
            "Fich_Emis": "EMISSIONS/EMIS_LIN/emis_rues_%dh.dat" % date_time.hour,
        })
        date_time += timedelta(hours=1)

    df_emis_trafic = pd.DataFrame.from_dict(emis_trafic)
    df_emis_trafic.to_csv(emissions_lin_output_path + "Evol_Emis_Trafic.dat", sep="\t", index=False)


    with open(emissions_lin_output_path + "Sources_Lin.dat", 'w') as f:
        f.writelines([
            "Fich_Evol_Emis\tFich_Modul\n",
            "EMISSIONS/EMIS_LIN/Evol_Emis_Trafic.dat\tNULL\n"
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