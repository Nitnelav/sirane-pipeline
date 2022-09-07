import pandas as pd
import geopandas as gpd
from pathlib import Path

def configure(context):
    context.stage("data.meteo.cleaned")

def execute(context):
    output_path = context.path()

    df_meteo: pd.DataFrame = context.stage("data.meteo.cleaned")
    
    meteo_output_path = output_path + "/INPUT/METEO/"
    Path(meteo_output_path).mkdir(parents=True, exist_ok=True)

    df_meteo[
        ["wind_spd", "wind_dir", "temp", "cloud", "precip"]
    ].to_csv(
        meteo_output_path + "meteo.txt", sep="\t",
        header=["U", "Dir", "Temp", "Cld", "Precip"],
        index_label="Date", date_format='%d/%m/%Y %H:%M'
    )
    
    with open(meteo_output_path + "/Site_Meteo.dat", 'w') as f:
        f.writelines([
            "/ Caracteristiques du site meteo :\n",
            "/---------------------------------\n",
            "Hauteur par rapport au sol [m] = 10.0\n",
            "Rugosite aerodynamique [m] = 0.1\n",
            "Epaisseur de deplacement [m] = 0.0\n",
            "Albedo = 0.1873\n",
            "Emissivite = 0.88\n",
            "Coefficient de Priestley-Taylor = 0.5\n"
        ])

    return