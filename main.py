import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# DO NOT USE VPN WHEN USING PROGRAM (google hates vpns and will break program)

def sleep():
    time.sleep(1.3)

browser = webdriver.Chrome('/Users/dan/Downloads/chromedriver_88')

try:
    def google_sign_in():
        # specific gmail portal used for automation
        gmail_portal = 'https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F' \
                       '%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192' \
                       '.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow'

        # search gmail
        browser.get(gmail_portal)
        sleep()

        # gmail username sign in
        my_email = browser.find_element_by_xpath('//*[@id="identifierId"]')
        my_email.send_keys('s21600529')
        my_email.send_keys('@stu.tempeunion.org')
        sleep()
        next_key = browser.find_element_by_class_name('VfPpkd-RLmnJb')
        next_key.click()
        time.sleep(3)

        # RapidIdentity username sign in
        rp_username = browser.find_element_by_xpath('//*[@id="identification"]')
        rp_username.send_keys('s21600529')
        sleep()

        # RapidIdentity password sign in
        rp_password = browser.find_element_by_xpath('//*[@id="ember489"]')
        rp_password.send_keys('Huud@no3Huud@no3')
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

        # # gmail password sign in
        # my_password = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        # my_password.send_keys('Huud@no3Huud@no3')
        # sleep()
        # s_next_key = browser.find_element_by_class_name('VfPpkd-RLmnJb')
        # s_next_key.click()

        time.sleep(5)


    # storing values in the list
    firstName = 'Dan'
    lastName = 'Nguyen'
    studentID = '21600529'
    test_urls = ['https://docs.google.com/forms/d/e/1FAIpQLScplbnlSpxms7HNJJ_0V3o01jbkoyz9LX4xRyydibARRrRQ0A'
                 '/viewform?vc=0&c=0&w=1&flr=0 ', 'https://docs.google.com/forms/d/e'
                 '/1FAIpQLSc3a47akkLSAlvcKa2CVDQdE7zhCJHSze2bHyvWvB3XAp954w'
                 '/viewform?vc=0&c=0&w=1&flr=0 ', 'https://docs.google.com/forms/d/e'
                 '/1FAIpQLSeC3Jy2NklYxdgTVr60TLZWXUJjnr3Z1lRm6dUM4HeXuzERdw/viewform',
                 'https://docs.google.com/forms/d/e'
                 '/1FAIpQLSfIOE1iucr5VdJA8cYmi6am5MrcWVUW5WrL2IqeM6XoDFntGw/viewform']

    period_1 = 'https://docs.google.com/forms/d/e/1FAIpQLSdfEfcu9RveVqNcNySRgMCljKzyXXSsmgzR7Pw_xJ8p5zoI9w/viewform'
    period_2 = 'https://docs.google.com/forms/d/e/1FAIpQLSfqTPM4tCCYxPv4Hul0242p4_YHMeORwJbxOSi1mlekLOA5jg/viewform'
    period_3 = 'https://docs.google.com/forms/d/e/1FAIpQLScwG2Dj_lrPUFxqhyYP7guLr3tgkbjkLc6Hzwc17afb_Ox2oA/viewform'
    period_4 = 'https://docs.google.com/forms/d/e/1FAIpQLSepr1gLgXhnxcXLOMZJcUIDu6stLNh1XuaKOiL_I4RxuY8wwg/viewform'
    period_6 = 'https://docs.google.com/forms/d/e/1FAIpQLSeFjswPnl_LdeXJftK65kvag-m9s647cg0irxts9ui3Nb_8FA/viewform'
    period_7 = 'https://docs.google.com/forms/d/e/1FAIpQLSfDUspcSNLwfqev53-fdvefCL5eCYQgjHAW_K-aW316XJ120w/viewform'

    school_urls = [period_1, period_2, period_3, period_4, period_6, period_7]

    # run google sign in
    google_sign_in()

    period = 1
    for url in school_urls:
        browser.get(url)
        sleep()

        # finds elements for google form
        textboxes = browser.find_elements_by_class_name('quantumWizTextinputPaperinputInput')
        radioButtons = browser.find_elements_by_class_name('docssharedWizToggleLabeledLabelWrapper')
        submitButton = browser.find_element_by_class_name('appsMaterialWizButtonPaperbuttonContent')

        textboxes[0].send_keys(firstName)
        textboxes[1].send_keys(lastName)
        textboxes[2].send_keys(studentID)

        radioButtons[period].click()
        radioButtons[11].click()

        submitButton.click()
        
        # alert_obj = browser.switch_to.alert
        # alert_obj.accept()

        period += 1

        # skips from period 4 to period 6
        if period == 5:
            period += 1
    print('Program successfully run')

finally:
    sleep()
    browser.close()