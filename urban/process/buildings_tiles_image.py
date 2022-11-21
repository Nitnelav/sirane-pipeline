import urban.runtime as urban

def configure(context):
    context.stage("urban.runtime")
    context.stage("urban.process.tiles_list")
    context.config("output_path")

def execute(context):
    urban_path = context.config("output_path") + "/URBAN"
    
    urban.run(context, [
        "Buildings_Tiles_Images", "./"
    ], catch_output=False, cwd=urban_path)