import subprocess as sp
import shutil

def configure(context):
    context.config("sirane_binary", "sirane.exe")

def run(context, arguments = [], cwd = None, catch_output = False):
    """
        This function calls sirane.
    """
    # Make sure there is a dependency
    context.stage("sirane.runtime")
    
    if cwd is None:
        cwd = context.path()

    command_line = [
        shutil.which(context.config("sirane_binary"))
    ] + arguments

    if catch_output:
        return sp.check_output(command_line, cwd = cwd).decode("utf-8").strip()

    else:
        return_code = sp.check_call(command_line, cwd = cwd)

        if not return_code == 0:
            raise RuntimeError("Git return code: %d" % return_code)

def validate(context):
    if shutil.which(context.config("sirane_binary")) == "":
        raise RuntimeError("Cannot find sirane binary at: %s" % context.config("sirane_binary"))

def execute(context):
    pass
