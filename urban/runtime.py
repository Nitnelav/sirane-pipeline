import subprocess as sp
import shutil

def configure(context):
    context.config("urban_binary", "urban.exe")

def run(context, arguments = [], cwd = None, catch_output = False):
    """
        This function calls sirane.
    """
    # Make sure there is a dependency
    context.stage("urban.runtime")
    
    if cwd is None:
        cwd = context.path()

    command_line = [
        shutil.which(context.config("urban_binary"))
    ] + arguments

    if catch_output:
        return sp.check_output(command_line, cwd = cwd).decode("utf-8").strip()

    else:
        return_code = sp.check_call(command_line, cwd = cwd)

        if not return_code == 0:
            raise RuntimeError("return code: %d" % return_code)

def validate(context):
    if shutil.which(context.config("urban_binary")) == "":
        raise RuntimeError("Cannot find urban binary at: %s" % context.config("urban_binary"))

def execute(context):
    pass
