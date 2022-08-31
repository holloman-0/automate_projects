from selenium_imports import *

# customization functions
#
#

class Formatter():

    def __init__(self , object  , cells  , constVariable = True , in_play = True , quotes = False , pictures = True , title = False , studies = False , facts_block = True):

        self.object = object
        self.cells = cells
        self.constVariable = constVariable
        self.in_play = in_play
        self.quotes = quotes
        self.pictures = pictures
        self.title = title
        self.studies = studies
        self.facts_block = facts_block


    def add_cells(self):

        notebook = wait_to_load(self.object , By.XPATH , "/html/body" , "Notebook")
        add_cell = notebook.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[2]/div/div/div[2]/button')

        for i in range(self.cells):
            add_cell.send_keys(Keys.ENTER)


# input_tabs = wait_to_load_multiple(notebook , By.CLASS_NAME , "input" , "input froms")
# def facts(object , x):

#     if x == True:

#         no_tabs = len(input_tabs)

#         for y in range(no_tabs):


#     else:
#         print("No Facts block in notepad.")




