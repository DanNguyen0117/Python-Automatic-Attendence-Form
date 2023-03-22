# Automatic Attendence Form
# First created on 1/26/2021 on ChromeDriver 86, program worked as of 2/24/2021 using ChromeDriver 86, current code 3/31/2021 on ChromeDriver 88 with some cleanup code to make it more readable
# Description: Program opens Chrome, signs in to Google and RapidIdentity account (my school used both), and autofills out google form sheet that had {firstname, lastname, studentID, classperiod, buttonyesIampresent}. 
# This program is definitely outdated and not really mass-producible, it's using chromedriver88 and solves a niche problem I had in my senior year of high school which can't really translate unless you massively change the code.

# So how this happened was when our school was starting under COVID, these Google attendence forms were their way of tracking attendence. It was a tedious process since you had to click the link, type in the same information, and do it again for however many classes you had.
# Basically I made this because I got tired of spending 3 minutes going through the attendence forms, so I made this program to do it in 30 seconds.
# Took me like a month to finish it tho. Uses Python Selenium, Python 2.7, Chromedriver 88. 
# Python 3 does not work for this, only 2.7

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# DO NOT USE VPN WHEN USING PROGRAM (google hates vpns and will break program)

#delay between filling in info, made this because program could fill in information before chrome could load in the url which would break the program
def sleep():
    time.sleep(1.3)

browser = webdriver.Chrome('/Users/dan/Downloads/chromedriver_88')

try:
    def google_sign_in():
        # specific gmail portal used for automation
        # main reason why this project took forever was because Google wasn't letting me sign in through automation fill-in, but this site was able to do so
        gmail_portal = 'https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F' \
                       '%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192' \
                       '.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow'

        # search gmail
        browser.get(gmail_portal)
        sleep()

        # gmail username sign in
        my_email = browser.find_element_by_xpath('//*[@id="identifierId"]')
        my_email.send_keys('xxxxx')
        my_email.send_keys('@stu.tempeunion.org')
        sleep()
        next_key = browser.find_element_by_class_name('VfPpkd-RLmnJb')
        next_key.click()
        time.sleep(3)

        # RapidIdentity username sign in
        rp_username = browser.find_element_by_xpath('//*[@id="identification"]')
        rp_username.send_keys('xxStudentIDxx')
        sleep()

        # RapidIdentity password sign in
        rp_password = browser.find_element_by_xpath('//*[@id="ember489"]')
        rp_password.send_keys('xxMyPasswordxx') # yes I hardcoded my password but for a single use project it got the job done 
        sleep()

        # RapidIdentity go button click
        go_button = browser.find_element_by_id('authn-go-button')
        go_button.click()
        time.sleep(3)

        # Submitting human confirmation
        actions = ActionChains(browser)
        tab_key = actions.send_keys(Keys.TAB)
        enter_key = actions.send_keys(Keys.ENTER)

        tab_key.perform()
        enter_key.perform()

        time.sleep(5)


    # storing values in the list. putting in placeholders but this was actually my first name, last name, etc
    firstName = 'xxFirstNamexx'
    lastName = 'xxLastNamexx'
    studentID = 'xxStudentIDxx'

    # the url of the google forms I had to fill out per class
    period_1 = 'https://docs.google.com/forms/d/e/1FAIpQLSdfEfcu9RveVqNcNySRgMCljKzyXXSsmgzR7Pw_xJ8p5zoI9w/viewform'
    period_2 = 'https://docs.google.com/forms/d/e/1FAIpQLSfqTPM4tCCYxPv4Hul0242p4_YHMeORwJbxOSi1mlekLOA5jg/viewform'
    period_3 = 'https://docs.google.com/forms/d/e/1FAIpQLScwG2Dj_lrPUFxqhyYP7guLr3tgkbjkLc6Hzwc17afb_Ox2oA/viewform'
    period_4 = 'https://docs.google.com/forms/d/e/1FAIpQLSepr1gLgXhnxcXLOMZJcUIDu6stLNh1XuaKOiL_I4RxuY8wwg/viewform'
    period_6 = 'https://docs.google.com/forms/d/e/1FAIpQLSeFjswPnl_LdeXJftK65kvag-m9s647cg0irxts9ui3Nb_8FA/viewform'
    period_7 = 'https://docs.google.com/forms/d/e/1FAIpQLSfDUspcSNLwfqev53-fdvefCL5eCYQgjHAW_K-aW316XJ120w/viewform'

    school_urls = [period_1, period_2, period_3, period_4, period_6, period_7]

    # run google sign in to sign into accounts to access school attendence forms
    google_sign_in()

    period = 1
    # goes through each class form url
    for url in school_urls:
        browser.get(url)
        sleep()

        # basically every form had a firstname, lastname, and studentID as textfields
        # radiobuttons for classperiod and a button that said that you were attending class
        # and finally there's a submit button
        
        # finds elements for google form (found class name using inspect and narrowing down the name)
        textboxes = browser.find_elements_by_class_name('quantumWizTextinputPaperinputInput')
        radioButtons = browser.find_elements_by_class_name('docssharedWizToggleLabeledLabelWrapper')
        submitButton = browser.find_element_by_class_name('appsMaterialWizButtonPaperbuttonContent')

        textboxes[0].send_keys(firstName)
        textboxes[1].send_keys(lastName)
        textboxes[2].send_keys(studentID)

        radioButtons[period].click()
        radioButtons[11].click()

        submitButton.click()

        period += 1

        # skips from period 4 to period 6 because period 5 was my lunch
        if period == 5:
            period += 1
            
    print('Program successfully run')

finally:
    sleep()
    browser.close()
