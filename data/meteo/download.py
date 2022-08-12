# 
import urllib.request

def configure(context):
    context.config("meteo_year", "2021")

def execute(context):

    year = str(context.config("meteo_year"))

    downloaded_files = {}

    for m in range(1, 13):
        month = str(m).zfill(2)
        date = year + month

        url = "https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/synop.%s.csv.gz" % date

        local_filename, headers = urllib.request.urlretrieve(url, "%s/%s.csv.gz" % (context.path(), date))
        downloaded_files[date] = "%s.csv.gz" % (date) 

        print("downloading %s.csv.gz from meteofrance.fr" % date)

    stations_url = "https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/postesSynop.json"
    local_filename, headers = urllib.request.urlretrieve(stations_url, "%s/stations.geojson" % context.path())

    return downloaded_files, "stations.geojson"
