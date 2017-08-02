
USERNAME = "vivaperu47"
PASSWORD = "cortoCanaNoInverno00"
follow = False

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.proxy import *
import sys

driver = None




def unfollow(user, count):

    try:
        driver.get("https://www.instagram.com/<USER>/")
    except:
        #
        driver.execute_script("window.stop();")
        print ("TIMED OUT")

    time.sleep(1)
    driver.find_elements_by_xpath("//span[contains(text(), 'following')]")[0].click()
    count = 0
    while count < 700:
        try:
            for x in range(0,100):
                count += 1
                driver.find_elements_by_xpath("//button[contains(text(), 'Following')]")[0].click()
                time.sleep(3)
            time.sleep(5)
        except:

            time.sleep(10)


def likeItAll():
    global driver
    #try:
    #    for x in range(0,20):
    #        time.sleep(1)
    #        driver.find_elements_by_xpath("//a[@class='_oidfu']")[0].click()
    #except:
    #    pass
    #oidfu
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(8)
    liked = []
    likedCnt = 0
    print ( "liking")
    while(True):
        try:
            posts = driver.find_elements_by_xpath("//a[contains(@href, 'tagged')]")
            for x in posts:
                if x.get_attribute("href") in liked:
                    print ("liked already")
                    continue
                liked.append(x.get_attribute("href"))

                x.click()
                likedCnt += 1
                print ("liked" + str(likedCnt))
                time.sleep(4)
                try:
                    driver.find_elements_by_xpath("//span[contains(@class, 'HeartOpen')]")[0].click()
                except:

                    print("heart not found")
                    pass
                time.sleep(1)
                if follow:
                    try:  #to follow
                        driver.find_elements_by_xpath("//button[contains(@class, '_jvpff')]")[0].click()
                    except:
                        pass
                time.sleep(1)
                driver.find_elements_by_xpath("//button[contains(@class, '3eajp')]")[0].click()
                driver.find_elements_by_xpath("//body")[0].send_keys(webdriver.common.keys.Keys.ESCAPE)
            time.sleep(1)
            driver.find_elements_by_xpath("//a[@class='_oidfu']")[0].click()
            time.sleep(5)
        except:
            pass

main()



#driver.find_elements_by_xpath("//a[contains(@data-reactid, 'topPosts')]")[0].click()

#driver.find_elements_by_xpath("//a[contains(@class, 'HeartOpen')]")[0].click()
