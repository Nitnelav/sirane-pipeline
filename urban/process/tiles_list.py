import urban.runtime as urban

def configure(context):
    context.stage("urban.runtime")
    context.stage("urban.prepare.buildings")
    context.stage("urban.prepare.traffic")
    context.stage("urban.prepare.zone")
    context.stage("urban.prepare.params")
    context.config("output_path")

def execute(context):
    urban_path = context.config("output_path") + "/URBAN"
    
    urban.run(context, [
        "Tiles_List", "./"
    ], catch_output=False, cwd=urban_path)