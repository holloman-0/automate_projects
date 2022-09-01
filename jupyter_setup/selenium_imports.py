import time
from multiprocessing.connection import wait
# wait for an element located on the page
from selenium.webdriver.support.ui import WebDriverWait

# predefined conditions to work with webdriverwait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# installing the driver for chrome (enables this device to communicate with chrome)
from selenium import webdriver

# provides keys in the keyboard like RETURN, F1, ALT etc
from selenium.webdriver.common.keys import Keys

# used to locate elements within a document.
from selenium.webdriver.common.by import By

# class introduced to start a webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver import ActionChains


def selenium_setup():

    # making the chrome tab invisible
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    
    # connecting to the terminal subprocess
    x = "http://localhost:8888"
    s=Service('/Users/jackyboy/Desktop/projects/automater/chromedriver/chromedriver')
    browser = webdriver.Chrome(service=s)
    browser.get(x)
    return browser


# delay to wait for pages to load (seconds)
delay = 10

def error_message(about):
    print("{} taken too long!".format(about))

def successful_message(about):
    print("{} ready!".format(about))

# gets the first occuracnce of the locator
def wait_to_load( browser , locator , locator_name , mssge):

    try:
        feature = WebDriverWait(browser,delay).until(EC.presence_of_element_located(( locator , locator_name)))
        return feature

    except TimeoutException:
        error_message(mssge)

def wait_till_clickable(browser , locator ,path , mssge):

    try:
        WebDriverWait(browser,delay).until(EC.element_to_be_clickable((locator,path))).click()
    
    except TimeoutError:
        error_message(mssge)

def wait_to_switch_window(browser , mssge):

    try:
        WebDriverWait(browser, delay).until(lambda d : len(d.window_handles) == 2)
    
    except TimeoutError:
        error_message(mssge)

def wait_to_read_title(browser , mssge):

    try:
        WebDriverWait(browser, delay).until(lambda d : len(d.title) != "")
    
    except TimeoutError:
        error_message(mssge)

def new_messages(string , html_attribute):

    if string not in html_attribute.get_attribute('outerHTML'):
        return 0

    else:
        index_of_string = html_attribute.get_attribute('outerHTML').find(string)
        no_messages = index_of_string + len(string) + 1
        return html_attribute.get_attribute('outerHTML')[no_messages]
        
# gets multiple cases of the locator
def wait_to_load_multiple( browser , locator , locator_name , mssge):

    try:
        feature = WebDriverWait(browser,delay).until(EC.presence_of_all_elements_located(( locator , locator_name)))
        return feature

    except TimeoutException:
        error_message(mssge)


def input_on_highlight( object , identicator , identicator_name , text):

    wait_till_clickable(object , identicator , identicator_name , text)
    object.find_element(identicator , identicator_name).click()
    
    # get active element highlighted
    active = object.switch_to.active_element
    active.send_keys(text)
    active.send_keys(Keys.ESCAPE)


