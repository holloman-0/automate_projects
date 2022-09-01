import subprocess

# A subprocess usually in python is a process python delegates to the o.s 
# This module allows us to run subprocesses directly from python 


# run 'runs' a command and waits for it to finish 
# shell=True invoking a shell before excecuting any subprocesses
# run local host so can access on google 

def run_local_host(path):
    return subprocess.Popen('jupyter notebook --no-browser', shell=True, cwd=path)

def shut_down_host(instance):
    print("Shutting down child terminal.")
    instance.terminate()
