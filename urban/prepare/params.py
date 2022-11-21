import pandas as pd
import geopandas as gpd
from pathlib import Path

def configure(context):
    context.config("output_path")

def execute(context):
    urban_path = context.config("output_path") + "/URBAN"
    Path(urban_path).mkdir(parents=True, exist_ok=True)

    data = f"""###########################################################
##                                                       ##
##          URBAN - version 1.2 - LMFA/ECL 2022          ##
##  Universal Recognition of Buildings Area and Network  ##
##                                                       ##
##                      Param File                       ##
##                                                       ##
###########################################################
#======================================
sFiles:
#======================================
#   Dossier de résultats
    pcInputFolder: "INPUT"
#   Dossier de résultats
    pcResultFolder: "RESULT"
#--------------------------------------
#   Fichier de bâtiments (shp/dat)
    pcBuildingsFile: "buildings.shp"
#   Fichier de traffic (shp/dat)    
    pcTrafficFile: "traffic.shp"
#   Fichier de Zone (shp)
    pcTilesZone: "zone.shp"
#   Fichier de dallage
    pcTilesFile: "Dallage.dat"
#======================================
sOptions:
#======================================
#   Niveau d'affichage du listing
    iMessage_Level: 2
#   Création des images à partir d'un Shapefile
    sSHP_to_Images:
        bActive: Yes
#--------------------------------------
#   URBAN_Canyon
    sURBAN_Canyon:
        bActive: Yes
#--------------------------------------
#   URBAN_Wake
    sURBAN_Wake:
        bActive: No
        dDirection_Min: 0.0
        dDirection_Max: 20.0
        dDirection_Step: 10.0
#======================================"""

    with open(urban_path + "/Param.yaml", 'w', encoding='utf-8') as f:
        f.write(data)