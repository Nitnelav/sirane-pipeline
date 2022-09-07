import pandas as pd
import geopandas as gpd
from pathlib import Path

def configure(context):
    pass

def execute(context):
    output_path = context.path()

    stats_output_path = output_path + "/INPUT/STATISTIQUES/"
    Path(stats_output_path).mkdir(parents=True, exist_ok=True)
    
    with open(stats_output_path + "Criteres.dat", 'w') as f:
        f.writelines([
            "Espece	Calcul	Indices_Stat	QQ\n",
            "NO2	1	1	1\n",
            "PM	1	1	1\n"
        ])

    with open(stats_output_path + "Statistiques.dat", 'w') as f:
        f.writelines([
            "Type	Espece	Calcul	Grille	Recept	Recept_Mes	Rue	Valeur\n",
            "Moy	*	1	1	1	0	0	-9999\n",
            "Moy_Horaire	*	1	1	1	0	0	-9999\n",
            "Max	*	1	1	1	0	0	-9999\n",
            "Nb_Hr_Depass_Moy_Horaire	NO2	0	1	1	0	0	200\n",
            "Nb_Jr_Depass_Moy_Journaliere	PM	0	1	1	1	0	50\n",
            "Nb_Hr_Depass_Moy_Horaire	NO2	0	1	1	1	0	40\n",
            "Nb_Hr_Depass_Moy_Horaire	NO2	0	1	1	1	0	60\n",
            "Nb_Hr_Depass_Moy_Horaire_3Hr	O3	0	1	1	1	0	240\n",
            "Nb_Jr_Depass_Moy_8Hr	O3	0	1	1	1	0	120\n",
            "Centile	PM	1	0	1	1	0	98\n",
        ])


