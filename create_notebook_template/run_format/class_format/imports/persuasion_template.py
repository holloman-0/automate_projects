from ast import Pass
from lib2to3.pgen2 import driver
from selenium_imports import *
from terminal_subprocess import *
from Formatter import *

child_terminal = run_local_host('/Users/jackyboy/Desktop/Repertoire/shape_up/Pen')

# def create_template(name):
## function parameters after finished
# name , 

name = "Forgiven Quickly"
cells_added = 9
facts_block = True
constVariable = True
in_play = True
quotes = False
pictures = True

# connecting to the terminal subprocess
x = "http://localhost:8888"
password = "Gaming5"
s=Service('/Users/jackyboy/Desktop/projects/automater/chromedriver/chromedriver')
browser = webdriver.Chrome(service=s)
browser.get(x)

# inputing creds
notebook = wait_to_load(browser , By.CLASS_NAME , "center-nav" , "Log-in Page")
notebook.find_element(By.CLASS_NAME, "form-control").send_keys(password)
notebook.find_element(By.ID, "login_submit").send_keys(Keys.RETURN)

# creating new jupyter file
notebook = wait_to_load(browser , By.ID , "new-dropdown-button" , "Homepage").send_keys(Keys.RETURN)
notebook = wait_to_load(browser , By.ID , "kernel-python3" , "Dropdown Menu")
notebook.find_element(By.XPATH, "a").send_keys(Keys.RETURN)


# switching windows 
wait_to_switch_window(browser , "Switched window")
browser.switch_to.window(browser.window_handles[1])
wait_to_read_title(browser, "New Window loaded")

# changing name
notebook = wait_till_clickable(browser , By.XPATH , "/html/body/div[3]/div[1]/span[1]/span[1]" , "Notebook")
notebook = wait_to_load(browser , By.XPATH , "/html/body/div[8]/div/div" , "Rename")
notebook.find_element(By.XPATH, "div[2]/div/input").send_keys(name)
notebook.find_element(By.XPATH, "div[3]/button[2]").send_keys(Keys.RETURN)

# adding all the layout 
#
#
formatter = Formatter(browser , cells_added)
formatter.add_cells()


# adding fact block
#facts( input_tabs , facts_block )

# notebook = wait_to_load(browser , By.XPATH , "div[2]/div/input" , "Rename")


# notebook.find_element(By.CLASS_NAME,'btn btn-default btn-sm btn-primary')
# notebook.send_keys(Keys.RETURN)

#notebook = wait_to_load(browser , By.CLASS_NAME , "form-control" , "Rename Form").click()




# changing name on jupyter file 
# notebook = wait_to_load(browser , By.CLASS_NAME , "output_wrapper" , "Notebook")

#notebook = wait_to_load(browser , By.ID , "notebook_name" , "Notebook")


#notebook = wait_to_load(browser , By.XPATH, "a" , "Dropdown button")
#notebook.send_keys(Keys.RETURN)

#notebook = wait_to_load(browser , By.CLASS_NAME , "center-nav" , "Log-in Page")
#shut_down_host(child_terminal)
# creating new notepad file

# new_template_name = "Forgiven quickly"
# create_template(new_template_name)


