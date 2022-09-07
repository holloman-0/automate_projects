from selenium_imports import *
from jupyter_format import *
from terminal_subprocess import shut_down_host 


def stegan():
    return "Gaming5"


def start_jupyter(browser , stegan):

    # inputing creds
    notebook = wait_to_load(browser , By.CLASS_NAME , "center-nav" , "Log-in Page")
    notebook.find_element(By.CLASS_NAME, "form-control").send_keys(stegan)
    notebook.find_element(By.ID, "login_submit").send_keys(Keys.RETURN)


def new_file(browser):

    # creating new jupyter file
    wait_to_load(browser , By.ID , "new-dropdown-button" , "Homepage").send_keys(Keys.RETURN)
    wait_to_load(browser , By.ID , "kernel-python3" , "Dropdown Menu").find_element(By.XPATH, "a").send_keys(Keys.RETURN)


def switch_windows(browser):

    # switching windows 
    wait_to_switch_window(browser , "Switched window")
    browser.switch_to.window(browser.window_handles[1])
    wait_to_read_title(browser, "New Window loaded")


def changing_name(browser , sub_process):

    user_name = input("\n\n\n*** --- Name of the new file? --- ***\n\n\n")

    if (user_name == "666"):
        close(browser , sub_process)
    
    else:
        notebook = wait_till_clickable(browser , By.XPATH , "/html/body/div[3]/div[1]/span[1]/span[1]" , "Notebook")
        notebook = wait_to_load(browser , By.XPATH , "/html/body/div[8]/div/div" , "Rename")
        notebook.find_element(By.XPATH, "div[2]/div/input").send_keys(user_name)
        notebook.find_element(By.XPATH, "div[3]/button[2]").send_keys(Keys.RETURN)


def asking_user(browser , sub_process):

    # creating formatting class
    formatter = Jupyter_Formatter(browser , sub_process)

    while True:

        user_wants = input("\n\n\n*** --- 1:[Title] , 2:[Unordered List] , 3:[Paragraphs] , 4:[Picture] , 5:[FINITO] --- ***\n\n\n")
        
        if( user_wants == "5"):
            break

        elif(user_wants == "1"):
            name = ask_user_name('Title')
            formatter.add_title(name)
        
        elif(user_wants == "2"):
            formatter.add_ul()
        
        elif(user_wants == "3"):
            how_many = ask_how_many('Paragraphs')
            formatter.add_paragraphs(how_many)


        elif(user_wants=="4"):
            picture_name = ask_user_name('Pictures')
            formatter.add_pictures(picture_name)
        
        elif(user_wants =="666"):
            close(browser , sub_process)


        else:
            print("\n\n\nIncorrect input, try again !\n\n\n")

def saving(browser):

    browser.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[2]/div/div/div[1]/button").click()
    print("Saved")


def close(browser , subprocess ) :

    while True:

        user_input = input("\n\n\n**** --- 0:[EXIT PROGRAM] --- ***\n\n\n")
        time.sleep(1)
        
        if (user_input == "0"):
            shut_down_host(subprocess)
            browser.close()
            quit()

        else:
            print("\n\n\nIncorrect input, try again !\n\n\n")
            


def ask_how_many(section):
    how_many = int(input('\n\n\nHow many {}?\n\n\n'.format(section)))
    return how_many


def ask_user_name(section):

    name = input("\n\n\nWhat is the name of the {}?\n\n\n".format(section))
    return name
