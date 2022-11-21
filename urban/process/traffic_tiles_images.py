import urban.runtime as urban

def configure(context):
    context.stage("urban.runtime")
    context.stage("urban.process.buildings_tiles_image")
    context.config("output_path")

def execute(context):
    urban_path = context.config("output_path") + "/URBAN"
    
    urban.run(context, [
        "Traffic_Tiles_Images", "./"
    ], catch_output=False, cwd=urban_path)