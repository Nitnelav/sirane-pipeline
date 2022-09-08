import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon
from shapely import ops

LEFT = 1
RIGHT = -1
DISTANCE_STEPS = 10
DISTANCE_MAX = 30

TYPE_CANYON = 0
TYPE_OPEN = 1

def configure(context):
    context.stage("data.bdtopo.cleaned")
    context.stage("data.matsim.roads.cleaned")

def execute(context):

    gdf_buildings: gpd.GeoDataFrame = context.stage("data.bdtopo.cleaned")
    gdf_roads: gpd.GeoDataFrame = context.stage("data.matsim.roads.cleaned")

    # algo :
    #  buffer left
    #  find first buffer dist where there are intersections.
    #  same on right
    #  union left & right ; width = left dist + right dist / 2
    #  intersection buildings
    #  get mean height of intersecting buildings : H

    gdf_roads["TYPE"] = TYPE_OPEN
    gdf_roads["BUFFERED"] = None
    gdf_roads["WG"] = 0.0
    gdf_roads["WD"] = 0.0
    gdf_roads["HG"] = 0.0
    gdf_roads["HD"] = 0.0
    gdf_roads["WG"] = gdf_roads["WG"].astype(float)
    gdf_roads["WD"] = gdf_roads["WD"].astype(float)
    gdf_roads["HG"] = gdf_roads["HG"].astype(float)
    gdf_roads["HD"] = gdf_roads["HD"].astype(float)
    gdf_roads["NDDEB"] = gdf_roads["from_node"]
    gdf_roads["NDFIN"] = gdf_roads["to_node"]
    gdf_roads["MODUL_EMIS"] = 0
    gdf_roads["MODUL_EMIS"] = gdf_roads["MODUL_EMIS"].astype(int)

    count = 0

    with context.progress(total = len(gdf_roads), label = "Processing roads types ...") as progress:
        for index, road in gdf_roads.iterrows():
            progress.update()

            # count += 1
            # if count >= 100:
            #     print("ok")
            #     break

            buffered_geom: Polygon = None
            has_bat = False
            has_both_sides = 0
            total_sum_volume = 0
            total_sum_surface = 0

            road_geom: Polygon = road['geometry']
            gdf_buildings_filtered = gdf_buildings.loc[gdf_buildings.intersects(road_geom.buffer(DISTANCE_MAX, cap_style=2))]

            if len(gdf_buildings_filtered) == 0:
                continue

            height_left = 0.0
            height_right = 0.0
            width_left = 0.0
            width_right = 0.0

            for orientation in [LEFT, RIGHT]:
                for buffer_distance in range(DISTANCE_STEPS, DISTANCE_MAX + DISTANCE_STEPS, DISTANCE_STEPS):
                    sum_volume = 0
                    sum_surface = 0

                    half_buffered_geom: Polygon = road_geom.buffer(buffer_distance * orientation, cap_style=2, single_sided=True)
                    half_buffered_geom = ops.transform(lambda *args: args[:2], half_buffered_geom) # remove z, force 2D

                    intersect_bat: gpd.GeoDataFrame = gdf_buildings_filtered.loc[gdf_buildings_filtered.intersects(half_buffered_geom)]
                    # remove bat if height < width / 3
                    intersect_bat = intersect_bat[intersect_bat["HAUTEUR"] >= (buffer_distance * 2 / 3)]

                    if (len(intersect_bat) == 0):
                        continue

                    has_bat = True
                    has_both_sides += orientation

                    for bat in intersect_bat.itertuples():
                        bat_geom: Polygon = ops.transform(lambda *args: args[:2], bat.geometry)
                        intersection = bat_geom.intersection(half_buffered_geom)
                        sum_surface += intersection.area
                        sum_volume += intersection.area * bat.HAUTEUR
                        half_buffered_geom = half_buffered_geom.difference(bat_geom)

                    if orientation == LEFT:
                        width_left = buffer_distance
                        height_left = sum_volume / sum_surface
                    elif orientation == RIGHT:
                        width_right = buffer_distance
                        height_right = sum_volume / sum_surface

                    total_sum_surface += sum_surface
                    total_sum_volume += sum_volume

                    if buffered_geom is None:
                        buffered_geom = half_buffered_geom
                    else:
                        buffered_geom = ops.unary_union([buffered_geom, half_buffered_geom])
                    break

            if has_bat and has_both_sides == 0:
                gdf_roads.at[index, "TYPE"] = TYPE_CANYON
                gdf_roads.at[index, "BUFFERED"] = buffered_geom
                gdf_roads.at[index, "HEIGHT"] = total_sum_volume / total_sum_surface
                gdf_roads.at[index, "WIDTH"] = width_left + width_right
                gdf_roads.at[index, "HG"] = height_left
                gdf_roads.at[index, "HD"] = height_right
                gdf_roads.at[index, "WG"] = width_left
                gdf_roads.at[index, "WD"] = width_right

    gdf_roads = gdf_roads[["TYPE", "NDDEB", "NDFIN", "WG", "WD", "HG", "HD", "MODUL_EMIS", "geometry"]]

    return gdf_roads