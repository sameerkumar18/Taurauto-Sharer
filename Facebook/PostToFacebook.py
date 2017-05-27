'''
MIT License
Copyright (c) 2017 Sameer Kumar
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

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
        self.driver = webdriver.Chrome(chrome_options=chrome_options)#,'__path__' maybe required for Windows
        self.driver.get(self.url)

    def auth(self,uname,passd):
        time.sleep(2)
        username = self.driver.find_element_by_id('email')
        password = self.driver.find_element_by_id('pass')
        username.send_keys(uname)
        password.send_keys(passd)
        password.send_keys(Keys.ENTER)

    def process(self,caption_text):

        time.sleep(1)

        caption_text



        #self.driver.get("https://www.facebook.com")
        actions = ActionChains(self.driver)
        time.sleep(2)
        actions.send_keys('p').perform()
        time.sleep(1)

        caption = ActionChains(self.driver)
        caption.send_keys(caption_text).perform()


        click_post = self.driver.find_element_by_xpath('//div[2]/div[3]/div/div[2]/div/button')
        click_post.click()

        print "Successfully posted "
        self.driver.close()
#text = raw_input("Enter text to be posted - ")
caption_text = "Hey"
auto = AutoShare()

auto.auth(uname='', passd='')
auto.process(caption_text=caption_text)
