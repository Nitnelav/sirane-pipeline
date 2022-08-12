import pandas as pd
import numpy as np

def configure(context):
    air_pollution_source = context.config("air_pollution_source", "pdl")

    if air_pollution_source == "pdl":
        context.stage("data.air_pollution.pdl.cleaned", alias = "air_pollution")
    else:
        raise RuntimeError("Unknown air pollution source: %s" % air_pollution_source)

def execute(context):
    return context.stage("air_pollution")
