import urllib.request

def configure(context):
    context.config("departments", [44])
    context.config("air_pollution_year", 2021)

def execute(context):
    polluttants = {
        "SO2": "01",
        "NO": "02",
        "NO2": "03",
        "CO": "04",
        "O3": "08",
        "NOx": "12",
        "PM10": "24",
        "PM2.5": "39",
        "C6H6": "V4",
    }

    departments = list(map(str, context.config("departments")))
    air_pollution_year = context.config("air_pollution_year")

    start_date = str(air_pollution_year) + "-1-1"
    end_date = str(air_pollution_year + 1) + "-1-1"
    format = "csv"

    downloaded_files = {}

    for pollutant, code in polluttants.items():

        url = "https://data.airpl.org/api/v1/mesure/journaliere/?"
        url += "&code_configuration_de_mesure__code_point_de_prelevement__code_polluant=%s" % code
        url += "&date_heure_tu__range=%s,%s" % (start_date, end_date)
        url += "&code_configuration_de_mesure__code_point_de_prelevement__code_station__code_commune__code_departement__in=%s" % ','.join(departments)
        url += "&export=%s" % format
        
        local_filename, headers = urllib.request.urlretrieve(url, "%s/%s.%s" % (context.path(), pollutant, format))
        downloaded_files[pollutant] = "%s.%s" % (pollutant, format)
        print("downloading %s.%s from airpl.org" % (pollutant, format))
    
    return downloaded_files
