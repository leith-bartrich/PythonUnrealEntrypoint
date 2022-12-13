import pkg_resources
import unreal
import traceback


def run_entrypoints():
    unreal.log("Running any 'init_unreal' entrypoints, if registered.")
    # get all registered entrypoints to 'init_unreal'.
    # loop through them
    for entry_point in pkg_resources.iter_entry_points('init_unreal'):
        # To make sure faulty entrypoints don't pre-empt functional ones, we do a catch-all for exceptions.
        # Usually this is a very bad thing.  But since this is top level, embedded, main-loop initialization; it actually makes sense.
        try:
            #run the entrypoint
            unreal.log("Running an 'init_unreal' entrypoint: {} {} {}".format(entry_point.name,entry_point.value,entry_point.group))
            entry_point.load()
        except:
            #if we've thrown for any reason, we log loudly to the unreal console and print the kind of stack trace one would expect from a repl
            unreal.log_error("An 'init_unreal' entrypoint threw an exception: {} {} {}".format(entry_point.name,entry_point.value,entry_point.group))
            for line in traceback.format_exc():
                unreal.log_error(line)


#run the function when this script is run (by unreal).
run_entrypoints()


