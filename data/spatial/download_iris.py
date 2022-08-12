# ftp://Contours_IRIS_ext:ao6Phu5ohJ4jaeji@ftp3.ign.fr/CONTOURS-IRIS_2-1__SHP__FRA_2020-01-01.7z

import os
import urllib.request
import py7zr
import re

def configure(context):
    pass

def execute(context):
    year = 2021

    url = "ftp://Contours_IRIS_ext:ao6Phu5ohJ4jaeji@ftp3.ign.fr/CONTOURS-IRIS_2-1__SHP__FRA_%s-01-01.7z" % year

    zip_file, headers = urllib.request.urlretrieve(url, "%s/CONTOURS-IRIS_2-1__SHP__FRA_%s-01-01.7z" % (context.path(), year))
    to_extract = []
    
    with py7zr.SevenZipFile(zip_file) as zip:
        allfiles_in_zip = zip.getnames()
        filter_pattern = re.compile(r'.*/.*/1_DONNEES_.*/.*SHP_LAMB93_FXX.*/CONTOURS-IRIS\..*')
        for file_in_zip in allfiles_in_zip:
            if filter_pattern.match(file_in_zip):
                to_extract.append(file_in_zip)
        zip.extract(context.path(), targets=to_extract)

    for file in to_extract:
        os.rename("%s/%s" % (context.path(), file), "%s/%s" % (context.path(), file.split("/")[-1]))

    
    return "CONTOURS-IRIS.shp"
