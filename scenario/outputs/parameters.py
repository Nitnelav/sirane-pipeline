import pandas as pd
import geopandas as gpd
from pathlib import Path

def configure(context):
    context.config("air_pollution_year", 2021)

def execute(context):
    output_path = context.path()
    air_pollution_year = context.config("air_pollution_year")

    parameters = {
        "input": "INPUT",
        "start": "01/01/%d 00:00:00" % air_pollution_year,
        "stop": "31/01/%d 00:00:00" % air_pollution_year,
        "dispersion": "RESEAU/Site_Disp.dat",
        "network": "RESEAU/Reseau_rues-SIRANE",
        "fond": "FOND/Concentration_fond.dat",
        "meteo": "METEO/meteo.txt",
        "meteo_site": "METEO/Site_Meteo.dat",
        "meteo_grid": "GRILLES/info-grid-meteo.dat",
        "especes": "ESPECES/Especes.dat",
        "srcegroup": "ESPECES/SrceGroup.dat"
    }

    data = f"""/******************************************************************************/
/**                   Donnees pour l'utilisation de SIRANE                   **/
/******************************************************************************/
Repertoire des donnees d'entree = {parameters["input"]}
/-----------------------------------------------------------------------------------------------------/
/ Periode                                                                                             /
/-----------------------------------------------------------------------------------------------------/
Date de debut = {parameters["start"]}
Date de fin = {parameters["stop"]}
/-----------------------------------------------------------------------------------------------------/
/ Zone d etude                                                                                        /
/-----------------------------------------------------------------------------------------------------/
Fichier de site de dispersion = {parameters["dispersion"]}
Fichier de reseau = {parameters["network"]}
Concentration de fond 2D [0/1] = 0
Fichier de pollution de fond = {parameters["fond"]}
/-----------------------------------------------------------------------------------------------------/
/ Meteorologie                                                                                        /
/-----------------------------------------------------------------------------------------------------/
Donnees meteorologiques fournies [0/1/2] = 0
/ Description du parametre Donnees meteorologiques fournies
/ La valeur 0 correspond à la fourniture des données meteo : U / DIR / Temp / Couverture nuageuse 
/ La valeur 1 correspond a la fourniture des données meteo : U / DIR / Temp / Rayonnement solaire
/ La valeur 2 correspond a la fourniture des données meteo : U_star / DIR / Temp / Inverse L_MO
Fichier meteo = {parameters["meteo"]}
Fichier de site de mesures meteorologiques = {parameters["meteo_site"]}
Fichier de description de la grille meteo = {parameters["meteo_grid"]}
Vitesse du vent minimale [m/s] = 1.0
/-----------------------------------------------------------------------------------------------------/
/ Polluants                                                                                           /
/-----------------------------------------------------------------------------------------------------/
Fichier des especes = {parameters["especes"]}
Fichier de groupes de sources = {parameters["srcegroup"]}
Emissions de NO en equivalent NO2 [0/1] = 1
Activation du modele chimique NO-NO2-O3 [0/1/2] = 2
/ Description du parametre Activation du modele chimique NO-NO2-O3
/ La valeur 0 correspond a : pas de modele chimique active
/ La valeur 1 correspond a : activation du modele photostationnaire
/ La valeur 2 correspond a : activation du nouveau modele chimie
Calcul de l'age des polluants [0/1] = 1
Ecriture de l'age des polluants [0/1] = 0
Espece pour le calcul de l'age des polluants = NO2
/-----------------------------------------------------------------------------------------------------/
/ Emissions                                                                                           /
/-----------------------------------------------------------------------------------------------------/
Fichier de sources ponctuelles = EMISSIONS/EMIS_PONCT/Sources_Ponct.dat
Fichier de sources surfaciques = EMISSIONS/EMIS_SURF/Sources_Surf.dat
Fichier de sources lineiques = EMISSIONS/EMIS_LIN/Sources_Lin.dat
Nombre de modulations lineiques = 1
/-----------------------------------------------------------------------------------------------------/
/ Statistiques                                                                                        /
/-----------------------------------------------------------------------------------------------------/
Calcul des statistiques [0/1] = 1
Fichier des statistiques = STATISTIQUES/Statistiques.dat
Comparaison modele-mesures [0/1] = 0
Fichier des criteres de comparaison = STATISTIQUES/Criteres.dat
/-----------------------------------------------------------------------------------------------------/
/ Sortie des resultats                                                                                /
/-----------------------------------------------------------------------------------------------------/
Repertoire d'ecriture des resultats = RESULT_URBAN_ZONE
/ 1- Recepteurs              /
/---------------------------/
Fichier de position des recepteurs ponctuels = RECEPTEURS/Recepteurs.dat
/ 2- Champs de concentration /
/---------------------------/
Fichier de description de la grille de sortie = GRILLES/info-grid-sortie.dat
Calcul sur la grille [0/1] = 1
Format du fichier de champ de concentration [0/1/2/3/4] = 3
/ 3- Depot                   /
/---------------------------/
Ecriture du depot [0/1] = 0
Fichier du depot = DEPOT/Depot.dat
/-----------------------------------------------------------------------------------------------------/
/ Options de simulation                                                                               /
/-----------------------------------------------------------------------------------------------------/
Nombre maximum de threads utilises = 6
Ratio entre pas meteo et pas retrotrajectoires = 2
Zone tampon en cellules pour le calcul des retrotrajectoires = 3"""

    with open(output_path + "/Donnees.dat", 'w', encoding='utf-8') as f:
        f.write(data)