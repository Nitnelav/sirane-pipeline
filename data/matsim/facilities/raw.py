import pandas as pd
import geopandas as gpd
import gzip

def configure(context):
    context.config("matsim_simulation_path")

def execute(context):
    facilities_gz_file = "%s/%s" % (context.config("matsim_simulation_path"), "/output_facilities.xml.gz")

    with gzip.open(facilities_gz_file) as f:
        df_receivers = pd.read_xml(f, parser='etree')

    return df_receivers 