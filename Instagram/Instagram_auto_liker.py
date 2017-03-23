from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def main(uid,passd,n):
    try:
        url = 'https://www.instagram.com'
        driver = webdriver.Chrome()
        driver.get(url)

        assert "Instagram" in driver.title

        elem = driver.find_element_by_class_name('_fcn8k')
        elem.click()


        username = driver.find_element_by_name('username')
        username.send_keys(uid)

        password = driver.find_element_by_name('password')
        password.send_keys(passd)

        password.send_keys(Keys.ENTER)

        time.sleep(2)


        like = driver.find_elements_by_link_text('Like')

        for i in range(0,n):

            try:
                like = driver.find_element_by_class_name('coreSpriteHeartOpen').click()


                print str("Successfully Liked at  i="+ str(i))
                if i%10==0:
                    try:
                        scroller(driver,2)
                    except:
                            pass

            except:
                        print str("Error at  i="+ str(i))
            time.sleep(1)




        driver.close()
    except:
        print "error"

def scroller(driver, x):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(x)

#known bug - It starts unliking pictures back again once-> the scrolling taken > time.sleep()
#basically user should close the browser, once this starts happening

