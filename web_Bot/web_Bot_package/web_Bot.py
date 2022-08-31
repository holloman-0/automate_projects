# importing all the imports from import file7890p[]o0p[']\
from selenium_imports import *

### logging-in
email = "jackfeatherstone99@gmail.com"
password = "web_Bot1"

# defining our url's
address_dictionary = { 
"spareroom_url_Distirct": "https://www.spareroom.co.uk/flatshare/?search_id=1156762957&",
"spareroom_url_DLR" : "https://www.spareroom.co.uk/flatshare/?search_id=1156763253&",
"spareroom_url_Nothern" : "https://www.spareroom.co.uk/flatshare/?search_id=1156763519&",
"spareroom_url_central" :"https://www.spareroom.co.uk/flatshare/?search_id=1156763746&"
}


for x in address_dictionary.values():
    
    # creating the session for automated browsing
    s=Service('/Users/jackyboy/Desktop/projects/automater/chromedriver/chromedriver')
    browser = webdriver.Chrome(service=s)
    browser.get(x)

    # wait for homepage via the wait and except function
    homepage = wait_to_load( browser , By.ID ,'loginButtonNav' , 'Login form')

    # click login
    homepage.send_keys(Keys.RETURN)

    # wait for login form to appear
    input_un = wait_to_load(browser , By.ID , 'loginemail' ,'Input form')

    # as on the same page , once login email appears so will these 
    input_pass = browser.find_element(By.ID, "loginpass")
    sign_in = browser.find_element(By.ID, "sign-in-button")

    # do not have to update state as webpage did not change , click sign in
    input_un.send_keys(email)
    input_pass.send_keys(password)
    sign_in.send_keys(Keys.RETURN)
    ###

    ### getting each add in loop
    # wait for page to load
    each_add = wait_to_load_multiple(browser , By.CLASS_NAME , "listing-result " , "Listing results")
    no_of_posts = len(each_add)


    for x in range(no_of_posts):

        # getting the text of each ad before going into the ad
        each_post_text = each_add[x].text
        
        # check if each ad is early bird or contacted before we go into them
        if (each_post_text.find('Early Bird') != -1 or each_post_text.find('Contacted') != -1):
            print('Post {} Early Bird / Contacted'.format(x))
        
        else:
            # picking an add and clicking it
            individual_page = each_add[x].find_element(By.XPATH, "article/header/a").send_keys(Keys.RETURN)

            # wait for individual advert page to load
            # click email person
            email_button = wait_to_load( browser, By.CLASS_NAME , "emailadvertiser" , "Individual post")
            email_button.find_element(By.XPATH, 'a').send_keys(Keys.RETURN)

            # wait for email page to load
            # get advertiser details and sending email
            ads_name = wait_to_load(browser, By.CLASS_NAME , "advertiser-details__name", "Email page" )

            # if an early bird ad , ignore
            ads_name = ads_name.text.split()[1]
            input_text = browser.find_element( By.CLASS_NAME, "contact-form__text-area").send_keys(
            "Hi {}, \nThis room is just what I'm looking for, is it still available?\nI am looking to move in on the 1st of October. I am currently living in Ireland and would love to have a virtual interview / Video and put down a deposit straight away.\nKind regards, \nJack ".format(ads_name))

            submit= browser.find_element(By.CLASS_NAME, "contact-form__submit").find_element(By.XPATH, 'button').send_keys(Keys.RETURN)

            #back to individual ad
            back_advert = wait_to_load( browser, By.CLASS_NAME , "back_link" , "Back page")
            back_advert.send_keys(Keys.RETURN)

            # back to listing back
            individual_post = wait_to_load (browser , By.CLASS_NAME, "back_link" , "Individual Post")
            individual_post.send_keys(Keys.RETURN)

            # wait for listings to load 
            each_add = wait_to_load_multiple(browser , By.CLASS_NAME , "listing-result " , "Listing results")


    # # conditional if
    # if( browser.find_element(By.CLASS_NAME , "far fa-envelope" ).size() == 0 ):
    #     print("No new messages !")

    # no_of_messages = browser.find_element(By.ID , "messageNav")
    # no_new_messages = new_messages("You have" , no_of_messages)

    #After loop browser closes
    browser.close()
