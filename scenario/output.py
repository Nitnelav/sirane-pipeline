import shutil 

def configure(context):
    context.stage("scenario.outputs.air_pollution")
    context.stage("scenario.outputs.meteo")
    context.stage("scenario.outputs.network")
    context.stage("scenario.outputs.pollutants")
    context.stage("scenario.outputs.receivers")
    context.stage("scenario.outputs.emissions")
    context.stage("scenario.outputs.statistics")
    context.stage("scenario.outputs.settings")
    context.stage("scenario.outputs.parameters")

    context.config("output_path")

def execute(context):
    output_path = context.config("output_path")

    shutil.copytree(context.path("scenario.outputs.air_pollution"), output_path, dirs_exist_ok=True)
    shutil.copytree(context.path("scenario.outputs.meteo"), output_path, dirs_exist_ok=True)
    shutil.copytree(context.path("scenario.outputs.network"), output_path, dirs_exist_ok=True)
    shutil.copytree(context.path("scenario.outputs.pollutants"), output_path, dirs_exist_ok=True)
    shutil.copytree(context.path("scenario.outputs.receivers"), output_path, dirs_exist_ok=True)
    shutil.copytree(context.path("scenario.outputs.emissions"), output_path, dirs_exist_ok=True)
    shutil.copytree(context.path("scenario.outputs.statistics"), output_path, dirs_exist_ok=True)
    shutil.copytree(context.path("scenario.outputs.settings"), output_path, dirs_exist_ok=True)
    shutil.copytree(context.path("scenario.outputs.parameters"), output_path, dirs_exist_ok=True)
