
from selenium_imports import * 

# customization functions
#
#

class Jupyter_Formatter():

    def __init__(self , object  , constVariable = True , in_play = True , quotes = False  , title = False , studies = False , facts_block = [1]):

        self.object = object
        self.constVariable = constVariable
        self.in_play = in_play
        self.quotes = quotes
        self.title = title
        self.studies = studies
        self.facts_block = facts_block
        self.used_cells = 1


    def add_pictures(self , picture_name):

        input_on_highlight( self.object , By.XPATH , '/html/body/div[4]/div/div/div[1]/div[1]/div[{}]/div[1]/div[2]/div[2]/div/div[6]/div[1]/div/div/div/div[5]'.format(self.used_cells) ,  "from IPython.display import Image\nImage(filename='jpeg/{}.jpeg')".format(picture_name))
        
        # adding one used cell
        self.used_cells += 1

        # no formatting needed
        self.format_text(False)


    def add_title(self,title):

        input_on_highlight(self.object , By.XPATH ,'/html/body/div[4]/div/div/div[1]/div[1]/div[{}]/div[1]/div[2]/div[2]/div/div[6]/div[1]/div/div/div/div[5]'.format(self.used_cells) , "<h1><i>{}</i></h1>".format(title))   

        # adding one used cell
        self.used_cells += 1

        # formatting needed
        self.format_text(True)
   

    def add_ul(self):

        input_on_highlight(self.object , By.XPATH , '/html/body/div[4]/div/div/div[1]/div[1]/div[{}]/div[1]/div[2]/div[2]/div/div[6]/div[1]/div/div/div/div[5]'.format(self.used_cells) , "<ul>\n<li></li>\n<li></li>\n<li></li>\n<li></li>\n<li></li>\n</ul>")
        
        # adding one used cell
        self.used_cells += 1

        self.format_text(True)
    
    
    def add_paragraphs(self , num_para):

        input_on_highlight(self.object , By.XPATH , '/html/body/div[4]/div/div/div[1]/div[1]/div[{}]/div[1]/div[2]/div[2]/div/div[6]/div[1]/div/div/div/div[5]'.format(self.used_cells) , ("<p>\n....<br>\n</p>\n" * num_para))

        # adding one used cell
        self.used_cells += 1

        self.format_text(True)


    def format_text(self , code):
        
        actions = ActionChains(self.object)

        # if not code have to change cell type 
        if code == True:
            actions.send_keys('m').perform
            actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).perform()
            actions.reset_actions()

        else:
            actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).perform()
            actions.reset_actions()




