import pandas as pd
import geopandas as gpd

def configure(context):
    receivers_source = context.config("receivers_source", "file") 

    if receivers_source == "file":
        context.stage("data.receivers.cleaned", alias = "receivers")
    elif receivers_source == "matsim":
        context.stage("data.matsim.facilities.cleaned", alias = "receivers")
    else:
        raise RuntimeError("Unknown receivers source (file|matsim): %s" % receivers_source)

def execute(context):
    return context.stage("receivers")