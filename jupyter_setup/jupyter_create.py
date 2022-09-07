from jupyter_setup import * 
from terminal_subprocess import * 

def run_jupyter_create(link):

    # running local host on subprocess
    child_terminal = run_local_host(link)
    
    # starting the browser to link to localhost
    browser = selenium_setup()

    steg = stegan()


    start_jupyter(browser , steg)
    new_file(browser)
    switch_windows(browser)
    changing_name(browser , child_terminal)
    asking_user(browser , child_terminal)
    saving(browser)
    close(browser , child_terminal)

# change this for diff directory
run_jupyter_create('/Users/jackyboy/Desktop/Repertoire/shape_up/Abridged')

#/Users/jackyboy/Desktop/Repertoire/shape_up/Abridged
#/Users/jackyboy/Desktop/Repertoire/shape_up/Hyde