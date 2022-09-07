import pandas as pd
import geopandas as gpd
from pathlib import Path

def configure(context):
    pass

def execute(context):
    output_path = context.path()

    pollutants_output_path = output_path + "/INPUT/ESPECES/"
    Path(pollutants_output_path).mkdir(parents=True, exist_ok=True)
    
    with open(pollutants_output_path + "Especes.dat", 'w') as f:
        f.writelines([
            "Id	Flag	Mmolaire	Vdepot	CoeffLessivage	DiamPart	RhoPart\n",
            "NO2	1	46.0	1.0	1.0	0.0	0.0\n",
            "NO	1	30.0	1.0	1.0	0.0	0.0\n",
            "O3	1	48.0	1.0	1.0	0.0	0.0\n",
            "PM	1	100.0	1.0	1.0	1.0E-5	1000.0\n",
            "PM25	0	100.0	1.0	1.0	2.5E-6	1000.0\n",
            "CO	0	28.0	1.0	1.0	0.0	0.0\n",
            "C6H6	0	78.0	1.0	0.0	0.0	0.0\n",
        ])
    with open(pollutants_output_path + "SrceGroup.dat", 'w') as f:
        f.writelines([
            "Id\n"
        ])


