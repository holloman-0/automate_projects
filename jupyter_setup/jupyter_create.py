from jupyter_setup import * 
from terminal_subprocess import * 

def run_jupyter_create():

    # running local host on subprocess
    child_terminal = run_local_host('/Users/jackyboy/Desktop/Repertoire/shape_up/Pen')
    
    # starting the browser to link to localhost
    browser = selenium_setup()

    steg = stegan()


    start_jupyter(browser , steg)
    new_file(browser)
    switch_windows(browser)
    changing_name(browser)
    asking_user(browser)
    close(browser , child_terminal)

run_jupyter_create()


