import pandas as pd
import geopandas as gpd
from pathlib import Path

def configure(context):
    context.config("pollutants", [])

def execute(context):
    output_path = context.path()
    required_pollutants = context.config("pollutants")

    stats_output_path = output_path + "/INPUT/STATISTIQUES/"
    Path(stats_output_path).mkdir(parents=True, exist_ok=True)

    with open(stats_output_path + "Criteres.dat", 'w') as f:
        lines = ["Espece	Calcul	Indices_Stat	QQ\n"]
        for pollutant in required_pollutants:
            lines.append("%s	1	1	1\n" % pollutant)
        f.writelines(lines)

    with open(stats_output_path + "Statistiques.dat", 'w') as f:
        f.writelines([
            "Type	Espece	Calcul	Grille	Recept	Recept_Mes	Rue	Valeur\n",
            "Moy	*	1	1	1	0	0	-9999"
        ])


