from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class AutoShare:

    def __init__(self):
        self.url = 'https://www.facebook.com'
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.maximize_window()
        self.driver.get(self.url)

    def auth(self,uname,passd):
        time.sleep(2)
        username = self.driver.find_element_by_id('email')
        password = self.driver.find_element_by_id('pass')
        username.send_keys(uname)
        password.send_keys(passd)
        password.send_keys(Keys.ENTER)

    def process(self,post_url, caption_text):
        groups = []
        groups = ['https://www.facebook.com/groups/bangalorestartupsnetwork/',
                  'https://www.facebook.com/groups/delhistartupnetwork/',
                  'https://www.facebook.com/groups/indianstartupnetwork']
        time.sleep(1)
        if not groups:
            try:
                number_of_groups = int(raw_input("How many groups:"))
                for j in range(0, number_of_groups):
                    app = raw_input("Enter group url(with https)" + str(j + 1) + ":")
                    groups.append(app)
                pass
            except:
                print "Error"

        else:
            pass

        for i in groups:
            try:
                self.driver.get(str(i))
                actions = ActionChains(self.driver)
                time.sleep(2)
                actions.send_keys('p').perform()
                time.sleep(1)

                actions2 = ActionChains(self.driver)
                actions2.send_keys(str(post_url) + " ").perform()
                time.sleep(3)


                actions4 = ActionChains(self.driver)

                for j in range(0, 15):
                    actions4.send_keys(Keys.BACK_SPACE).perform()

                caption = ActionChains(self.driver)
                caption.send_keys(caption_text).perform()

                click_post = self.driver.find_element_by_class_name("_332r")
                click_post.click()
                time.sleep(10)
                print "Successfully posted in " + str(i.split('https://www.facebook.com/groups/')[1].split('/')[0])
            except:
                print"Error posting in " + str(i.split('https://www.facebook.com/groups/')[1].split('/')[0])
        self.driver.close()

