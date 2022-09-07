import pandas as pd
import geopandas as gpd

def configure(context):
    context.stage("data.receivers.selected")
    context.stage("data.spatial.departments")

    context.config("sirane_output_grid_dist", 10)
    context.config("sirane_meteo_grid_dist", 300)

def execute(context):
    grids = {}

    output_dist = context.config("sirane_output_grid_dist")
    meteo_dist = context.config("sirane_meteo_grid_dist")

    df_receivers: pd.DataFrame = context.stage("data.receivers.selected")
    gdf_receivers = gpd.GeoDataFrame(
        df_receivers, geometry=gpd.points_from_xy(df_receivers.X, df_receivers.Y)
    )

    x1, y1, x2, y2 = tuple(gdf_receivers.total_bounds)
    grids.update({
        "sortie": [(x2 - x1) // output_dist + 1, (y2 - y1) // output_dist + 1, x1, x2, y1, y2]
    })

    gdf_departments: gpd.GeoDataFrame = context.stage("data.spatial.departments")
    x1, y1, x2, y2 = tuple(gdf_departments.total_bounds)
    grids.update({
        "meteo": [(x2 - x1) // meteo_dist + 1, (y2 - y1) // meteo_dist + 1, x1, x2, y1, y2]
    })

    df_grids = pd.DataFrame.from_dict(
        grids, orient='index', columns=['Nx', 'Ny', 'xmin', 'xmax', 'ymin', 'ymax']
    )

    return df_grids
    