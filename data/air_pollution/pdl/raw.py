import pandas as pd

def configure(context):
    context.stage("data.air_pollution.pdl.download")

def execute(context):

    downloaded_files: dict[str, str] = context.stage("data.air_pollution.pdl.download")
    
    df = pd.DataFrame()
    for pollutant, file in downloaded_files.items():
        df = pd.concat([df, pd.read_csv("%s/%s" % (context.path("data.air_pollution.pdl.download"), file), sep=";")])
    
    return df.reset_index()