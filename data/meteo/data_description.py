# Descriptif", "Mnémonique", "Type *", "Unité"
data_desc = {
    "numer_sta": ("indicatif OMM station", "numer_sta", "car", "a"),
    "date": ("date (UTC)", "date", "car", "AAAAMMDDHHMISS"),
    "pmer": ("pression au niveau mer", "pmer", "int", "Pa"),
    "tend": ("variation de pression en 3 heures", "tend", "int", "Pa"),
    "cod_tend": ("type de tendance barométrique", "cod_tend", "int", "code (0200)"),
    "dd": ("direction du vent moyen 10mn", "dd", "int", "degré"),
    "ff": ("vitesse du vent moyen 10mn", "ff", "réel", "m/s"),
    "t": ("température", "t", "réel", "K"),
    "td": ("point de rosée", "td", "réel", "K"),
    "u": ("humidité", "u", "int", "%"),
    "vv": ("visibilité horizontale", "vv", "réel", "mètre"),
    "ww": ("temps présent", "ww", "int", "code (4677)"),
    "w1": ("temps passé 1", "w1", "int", "code (4561)"),
    "w2": ("temps passé 2", "w2", "int", "code (4561)"),
    "n": ("nébulosité totale", "n", "réel", "%"),
    "nbas": ("nébulosité des nuages de l’étage inférieur", "nbas", "int", "octa"),
    "hbas": ("hauteur de la base des nuages de l’étage inférieur", "hbas", "int", "mètre"),
    "cl": ("type des nuages de l’étage inférieur", "cl", "int", "code (0513)"),
    "cm": ("type des nuages de l’étage moyen", "cm", "int", "code (0515)"),
    "ch": ("type des nuages de l’étage supérieur", "ch", "int", "code (0509)"),
    "pres": ("pression station", "pres", "int", "Pa"),
    "niv_bar": ("niveau barométrique", "niv_bar", "int", "Pa"),
    "geop": ("géopotentiel", "geop", "int", "m²/s²"),
    "tend24": ("variation de pression en 24 heures", "tend24", "int", "Pa"),
    "tnN": ("température minimale sur N heures", "tnN", "réel", "K"),
    "txN": ("température maximale sur N heures", "txN", "réel", "K"),
    "tminsol": ("température minimale du sol sur 12 heures", "tminsol", "réel", "K"),
    "sw": ("méthode mesure tw", "sw", "int", "code (3855)"),
    "tw": ("température du thermomètre mouillé", "tw", "réel", "K"),
    "raf10": ("rafales sur les 10 dernières minutes", "raf10", "réel", "m/s"),
    "rafper": ("rafales sur une période", "rafper", "réel", "m/s"),
    "per": ("période de mesure de la rafale", "per", "réel", "minute"),
    "etat_sol": ("état du sol", "etat_sol", "int", "code (0901)"),
    "ht_neige": ("hauteur totale de la couche de neige, glace, autre, au sol", "ht_neige", "réel", "mètre"),
    "ssfrai": ("hauteur de la neige fraîche", "ssfrai", "réel", "mètre"),
    "perssfrai": ("Période de mesure de la neige fraîche", "perssfrai", "réel", "1/10 heure"),
    "rrN": ("Précipitations dans les N dernières heures", "rrN", "réel", "mm"),
    "phenspeN": ("Phénomène spécial", "phenspeN", "réel", "code (3778)"),
    "nnuageN": ("Nébulosité couche nuageuse N", "nnuageN", "int", "octa"),
    "ctypeN": ("Type de nuage N", "ctypeN", "int", "code (0500)"),
    "hnuageN": ("Hauteur de base de nuage N", "hnuageN", "int", "mètre")
}
