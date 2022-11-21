import urban.runtime as urban

def configure(context):
    context.stage("urban.process.merge")
    context.config("output_path")

def execute(context):
    urban_path = context.config("output_path") + "/URBAN"
    