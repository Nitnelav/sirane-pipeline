# ftp://BDTOPO_V3_ext:Aish3ho8!!!@ftp3.ign.fr/BDTOPO_3-0_2021-03-15/BDTOPO_3-0_TOUSTHEMES_GPKG_LAMB93_D001_2021-03-15.7z

import urllib.request
import py7zr
import re
import os
def configure(context):
    context.stage("data.spatial.codes")

def execute(context):
    df_codes = context.stage("data.spatial.codes")
    region = str(df_codes["region_id"].unique()[0])

    url = "ftp://BDTOPO_V3_ext:Aish3ho8!!!@ftp3.ign.fr/BDTOPO_3-0_2021-12-15/BDTOPO_3-0_TOUSTHEMES_SHP_LAMB93_R%s_2021-12-15.7z" % region.zfill(2)
    zip_file, headers = urllib.request.urlretrieve(url, "%s/BDTOPO.7z" % context.path())
    
    to_extract = []
    
    with py7zr.SevenZipFile(zip_file) as zip:
        allfiles_in_zip = zip.getnames()
        filter_bati = re.compile(r'.*/.*/1_DONNEES_.*/.*SHP_LAMB93_.*/BATI/BATIMENT\..*')
        for file_in_zip in allfiles_in_zip:
            if filter_bati.match(file_in_zip):
                to_extract.append(file_in_zip)
        zip.extract(context.path(), targets=to_extract)

    for file in to_extract:
        os.rename("%s/%s" % (context.path(), file), "%s/%s" % (context.path(), file.split("/")[-1]))

    return "BATIMENT.shp"
