from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def main(uid,passd, tag,n):
    url = 'https://www.instagram.com'
    driver = webdriver.Chrome()
    driver.get(url)

    #driver.maximize_window()


    assert "Instagram" in driver.title

    elem = driver.find_element_by_class_name('_fcn8k')
    elem.click()

    time.sleep(5)

    username = driver.find_element_by_name('username')
    username.send_keys(str(uid))


    password = driver.find_element_by_name('password')
    password.send_keys(str(passd))


    password.send_keys(Keys.ENTER)

    time.sleep(2)

    driver.get('https://www.instagram.com/explore/tags/'+str(tag))
    actions = ActionChains(driver)

    time.sleep(2)

    for x in range(1,2):
        x=2

        for i in range(1,int(n)):
            if i>12:
                time.sleep(0.5)

            for j in range(1,3):

                path = '//*[@id="react-root"]/section/main/article/div['+str(x)+']/div/div[' + str(i) +']/a[' + str(j) + ']/div/div[2]'

                try:
                        actions.send_keys(Keys.ESCAPE).perform()

                        time.sleep(1)


                        posts = driver.find_element_by_xpath(str(path)).click()

                        time.sleep(1)

                        like = driver.find_element_by_class_name('coreSpriteHeartOpen').click()

                        actions.send_keys(Keys.ESCAPE).perform()
                        print str("Successfully Liked at  x="+str(x)+" i="+str(i)+" j="+str(j))
                        try:
                            scroller(driver,2)
                        except:
                            pass



                except:
                        print str("Error at  x="+str(x)+" i="+str(i)+" j="+str(j))
            time.sleep(2)




    driver.close()


def scroller(driver,x):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(x)
