import pandas as pd
import geopandas as gpd
from pathlib import Path

def configure(context):
    pass

def execute(context):
    output_path = context.path()

    settings_output_path = output_path + "/SETTINGS/"
    Path(settings_output_path).mkdir(parents=True, exist_ok=True)

    with open(settings_output_path + "Don_Defaut_FR.dat", 'w', encoding='utf-8') as f:
        f.write("""/******************************************************************************/
/*                                                                            */
/* Modele SIRANE version 2.1 - LMFA/ECL 2017                                  */
/*                                                                            */
/* Don_Defaut_FR.dat --> Definition des donnees par defaut                    */
/*                                                                            */
/******************************************************************************/
/*                                                                            */
/*                    ATTENTION ! DONNEES PAR DEFAUT                          */
/*                      NE PAS MODIFIER CE FICHIER                            */
/*                           SANS PRECAUTIONS                                 */
/*                                                                            */
/******************************************************************************/
/ SYNTAXE
/ MOT-CLE ; Description ; OBL ou OPT ; Valeur par D�faut ; Min ; Max
/
FICH_DIR_INPUT ; Repertoire des donnees d'entree ; OPT ; cchar ; . ; ;
/------------------------------------------------------------------------------/
/ Periode                                                                      /
/------------------------------------------------------------------------------/
DATE_DEB ; Date de debut ; OBL ; date ; 01/01/2004 00:00:00 ; 01/01/2004 00:00:00 ; 01/01/2005 23:00:00
DATE_FIN ; Date de fin ; OBL ; date ; 31/12/2004 23:00:00 ; 31/12/2004 23:00:00 ; 31/12/2005 23:00:00
/------------------------------------------------------------------------------/
/ Polluants                                                                    /
/------------------------------------------------------------------------------/
FICH_ESPECES ; Fichier des especes ; OBL ; cchar ; ; ;
FICH_SRCE_GROUP ; Fichier de groupes de sources ; OBL ; cchar ; ; ;
B_CHEM_NO_NO2_O3 ; Activation du modele chimique NO-NO2-O3 [0/1/2] ; OPT ; integer ; 0 ; 0 ; 2
B_EMIS_NOEQNO2 ; Emissions de NO en equivalent NO2 [0/1] ; OPT ; integer ; 0 ; 0 ; 1
B_AGE_CALC ; Calcul de l'age des polluants [0/1] ; OPT ; integer ; 0 ; 0 ; 1
B_AGE_WRITE ; Ecriture de l'age des polluants [0/1] ; OPT ; integer ; 0 ; 0 ; 1
PCC_AGE_SPECIES ; Espece pour le calcul de l'age des polluants ; OPT ; cchar ; ; ;
/------------------------------------------------------------------------------/
/ Emissions                                                                    /
/------------------------------------------------------------------------------/
FICH_SOURCES_PONCT ; Fichier de sources ponctuelles ; OBL ; cchar ; ; ;
FICH_SOURCES_SURF ; Fichier de sources surfaciques ; OBL ; cchar ; ; ;
FICH_SOURCES_LIN ; Fichier de sources lineiques ; OBL ; cchar ; ; ;
I_N_MOD_LIN ; Nombre de modulations lineiques ; OBL ; integer ; 1 ; 1 ; 10
B_BACKGROUND_CONC_2D ; Concentration de fond 2D [0/1] ; OPT ; integer ; 0 ; 0 ; 1
FICH_POLL_FOND ; Fichier de pollution de fond ; OBL ; cchar ; ; ;
/------------------------------------------------------------------------------/
/ Caracteristiques du milieu urbain                                            /
/------------------------------------------------------------------------------/
TYPE_FICH_RESEAU ; Type de fichier de reseau [0/1/2] ; OPT ; integer ; 2 ; 0 ; 2  
FICH_RUE ; Fichier de rue ; OPT ; cchar ; ; ;   
FICH_NOEUD ; Fichier de noeud ; OPT ; cchar ; ; ;
FICH_RESEAU ; Fichier de reseau ; OPT ; cchar ; ; ;   
FICH_SITE_DISP ; Fichier de site de dispersion ; OBL ; cchar ; ; ;
Z0D_BAT ; Rugosite aerodynamique des batiments [m] ; OPT ; double ; 0.05 ; 0.0 ; 1.0
H_R ; Hauteur de reflexion des bouffees [m] ; OPT ; double ; 20.0 ; 0.0 ; 100.0
/------------------------------------------------------------------------------/
/ Conditions meteorologiques                                                   /
/------------------------------------------------------------------------------/
TYPE_METEO ; Conditions meteorologiques [0/1/2/3] ; OPT ; integer ; 0 ; 0 ; 3
/ Donnees meteorologiques fournies [0/1/2] :
/ 0 --> U / Couverture nuageuse
/ 1 --> U / Rayonnement solaire
/ 2 --> U_star / Inverse L_MO
INPUT_METEO ; Donnees meteorologiques fournies [0/1/2] ; OPT ; integer ; 0 ; 0 ; 2
FICH_METEO ; Fichier meteo ; OBL ; cchar ; ; ;
FICH_SITE_METEO ; Fichier de site de mesures meteorologiques ; OBL ; cchar ; ; ;
U_MIN ; Vitesse du vent minimale [m/s] ; OPT ; double ; 1.0 ; 0.0 ; 5.0
SIGMA_V_MIN ; Ecart-type de vitesse sigmav minimal [m/s] ; OPT ; double ; 0.5 ; 0.0 ; 2.0
SIGMA_W_MIN ; Ecart-type de vitesse sigmaw minimal [m/s] ; OPT ; double ; 0.3 ; 0.0 ; 2.0
/------------------------------------------------------------------------------/
/ Turbulence                                                                   /
/------------------------------------------------------------------------------/
TYPE_DISP ; Modele de diffusion [0/1/2] ; OPT ; integer ; 2 ; 0 ; 2
KY ; Diffusivite turbulente horizontale [m2/s] ; OPT ; double ; 10.0 ; 0.0 ; 100.0
KZ ; Diffusivite turbulente verticale [m2/s] ; OPT ; double ; 10.0 ; 0.0 ; 100.0
/------------------------------------------------------------------------------/
/ Grilles                                                                      /
/------------------------------------------------------------------------------/
FICH_GRD_MET ; Fichier de description de la grille meteo ; OBL ; cchar ; ; ;
FICH_GRD_SORTIE ; Fichier de description de la grille de sortie ; OBL ; cchar ; ; ;
/------------------------------------------------------------------------------/
/ Calcul SIRANE                                                                /
/------------------------------------------------------------------------------/
AFFICH ; Niveau d'affichage [0/1/2] ; OPT ; integer ; 0 ; 0 ; 2
N_MAX_THREADS ; Nombre maximum de threads utilises ; OPT ; integer ; 1000 ; 1 ; 1000
/------------------------------------------------------------------------------/
/ Sortie des resultats                                                         /
/------------------------------------------------------------------------------/
FICH_DIR_RESUL ; Repertoire d'ecriture des resultats ; OBL ; cchar ; ; ;
FICH_RECEPT ; Fichier de position des recepteurs ponctuels ; OBL ; cchar ; ; ;
B_SIGMA_Y_Z ; Ecriture des caracteristiques du panache [0/1] ; OPT ; integer ; 0 ; 0 ; 1
FICH_COLORMAP_ESPECES ; Fichier de colormap des especes ; OPT ; cchar ; ; ;
/------------------------------------------------------------------------------/
/ Champs de concentration                                                      /
/------------------------------------------------------------------------------/
CALC_GRID ; Calcul sur la grille [0/1] ; OBL ; integer ; 0 ; 0 ; 1
FORMAT_CHP_SORTIE ; Format du fichier de champ de concentration [0/1/2/3/4] ; OBL ; integer ; 0 ; 0 ; 4
FORMAT_IMAGE_SORTIE ; Ecriture du champ de concentration au format image [0/1/2] ; OPT ; integer ; 0 ; 0 ; 2
B_GRID_BLANKED ; Filtrage des points masques [0/1] ; OPT ; integer ; 0 ; 0 ; 1
FICH_MASQUE_SORTIE ; Fichier de masque de la grille de sortie ; OPT ; cchar ; ; ;
/------------------------------------------------------------------------------/
/ Parametres statistiques                                                      /
/------------------------------------------------------------------------------/
B_CALC_STAT ; Calcul des statistiques [0/1] ; OBL ; integer ; 1 ; 0 ; 1
FICH_STATS ; Fichier des statistiques ; OBL ; cchar ; ; ;
B_CALC_CRITERES ; Comparaison modele-mesures [0/1] ; OBL ; integer ; 1 ; 0 ; 1
FICH_CRITERES ; Fichier des criteres de comparaison ; OBL ; cchar ; ; ;
FICH_COLORMAP_NB ; Fichier de colormap des depassements ; OPT ; cchar ; ; ;
/------------------------------------------------------------------------------/
/ Depot                                                                        /
/------------------------------------------------------------------------------/
B_ECRIRE_DEPOT ; Ecriture du depot [0/1] ; OPT ; integer ; 0 ; 0 ; 1
FICH_DEPOT ; Fichier du depot ; OBL ; cchar ; ; ;
/------------------------------------------------------------------------------/
/ Rues                                                                         /
/------------------------------------------------------------------------------/
CALC_RUES ; Ecriture des resultats sur les rues [0/1] ; OPT ; integer ; 0 ; 0 ; 1
ECRIRE_RESEAU ; Ecriture du fichier de reseau de rues [0/1] ; OPT ; integer ; 1 ; 0 ; 1
FORMAT_RUES_SORTIE ; Format du fichier de rues [0/1] ; OPT ; integer ; 0 ; 0 ; 1
/------------------------------------------------------------------------------/
/ Parametres de calcul                                                         /
/------------------------------------------------------------------------------/
B_BOUFFEES ; Prise en compte des bouffees [0/1] ; OPT ; integer ; 1 ; 0 ; 1
B_SRCE_PCT ; Prise en compte des sources ponctuelles [0/1] ; OPT ; integer ; 1 ; 0 ; 1
B_RETRO ; Prise en compte des retrotrajectoires [0/1] ; OPT ; integer ; 1 ; 0 ; 1
B_PANACHE ; Prise en compte des rues-panaches [0/1] ; OPT ; integer ; 1 ; 0 ; 1
B_FOND ; Prise en compte de la pollution de fond [0/1] ; OPT ; integer ; 1 ; 0 ; 1
SEUIL_GAUSS ; Seuil sur sigma pour negliger une bouffee ; OPT ; double ; 4.0 ; 0 ; 100000
SEUIL_DEBIT ; Seuil sur le debit d'emission des bouffees ; OPT ; double ; 0.000001 ; 0 ; 10000
SEUIL_PONCT ; Seuil L/Sigma pour considerer une source comme ponctuelle ; OPT ; double ; 0.14 ; 0 ; 10000
RATIO_GRILLE ; Ratio entre pas meteo et pas retrotrajectoires ; OPT ; integer ; 3 ; 1 ; 6
RATIO_BOUFFEE ; Ratio du sous pas de temps pour le modele a bouffees ; OPT ; integer ; 6 ; 1 ; 60
RETRO_BUFF ; Zone tampon en cellules pour le calcul des retrotrajectoires ; OPT; integer ; 5 ; 0 ; 10
SRCEPCT_BUFF ; Zone tampon en cellules pour le calcul des sources ponctuelles ; OPT; integer ; 6 ; 0 ; 1000
B_RUE_DECOUP ; Decoupage des rues sur la grille retrotrajectoires [0/1] ; OPT ; integer ; 1 ; 0 ; 1
/------------------------------------------------------------------------------/""")

    with open(settings_output_path + "Site_Defaut_FR.dat", 'w', encoding='utf-8') as f:
        f.write("""/******************************************************************************/
/*                                                                            */
/* Modele SIRANE version 2.1 - LMFA/ECL 2017                                  */
/*                                                                            */
/* Site_Defaut_FR.dat --> Definition des donnees de site par defaut           */
/*                                                                            */
/******************************************************************************/
/*                                                                            */
/*                    ATTENTION ! DONNEES PAR DEFAUT                          */
/*                      NE PAS MODIFIER CE FICHIER                            */
/*                           SANS PRECAUTIONS                                 */
/*                                                                            */
/******************************************************************************/
/ SYNTAXE
/ MOT-CLE ; Description ; OBL ou OPT ; Valeur par D�faut ; Min ; Max
/
/------------------------------------------------------------------------------/
/ Caracteristiques du site                                                     /
/------------------------------------------------------------------------------/
LATITUDE ; Latitude [deg] ; OPT ; double ; 45.0 ; -90.0 ; 90.0
ALTITUDE ; Hauteur par rapport au sol [m] ; OPT ; double ; 10.0 ; 0.0 ; 90.0
Z0D ; Rugosite aerodynamique [m] ; OBL ; double ; 0.05 ; 0.0 ; 3.0
ZDISPL ; Epaisseur de deplacement [m] ; OBL ; double ; 0.0 ; 0.0 ; 50.0
ALBEDO ; Albedo ; OBL ; double ; 0.2 ; 0.0 ; 1.0
EMISSIVITE ; Emissivite ; OPT ; double ; 0.88 ; 0.0 ; 1.0
PRIESTLEY_TAYLOR ; Coefficient de Priestley-Taylor ; OPT ; double ; 0.5 ; 0.0 ; 1.0
/------------------------------------------------------------------------------/""")


