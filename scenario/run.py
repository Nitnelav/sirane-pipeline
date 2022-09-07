import sirane.runtime as sirane

def configure(context):
    context.stage("scenario.output")
    context.stage("sirane.runtime")
    context.config("output_path")

def execute(context):
    sirane.run(context, [
        "Donnees.dat"
    ], catch_output=False, cwd=context.config("output_path"))