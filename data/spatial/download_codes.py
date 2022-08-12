# https://www.insee.fr/fr/statistiques/fichier/2017499/reference_IRIS_geo2021.zip

import urllib.request
import zipfile

def configure(context):
    pass

def execute(context):
    year = 2021

    url = "https://www.insee.fr/fr/statistiques/fichier/2017499/reference_IRIS_geo%s.zip" % year
    zip_file, headers = urllib.request.urlretrieve(url, "%s/reference_IRIS_geo%s.zip" % (context.path(), year))

    with zipfile.ZipFile(zip_file) as zip:
        zip.extract("reference_IRIS_geo%s.xlsx" % year, context.path())

    return "reference_IRIS_geo%s.xlsx" % year
