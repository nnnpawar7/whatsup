from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os  
from time import sleep
import json

driver = webdriver.Firefox(executable_path=r'C:\Users\nnnpa\OneDrive\Desktop\whatsapp\geckodriver-v0.29.0-win64\geckodriver.exe')
data = [
'913344556677',
'912233445566',
'911122334455',
driver.get('https://web.whatsapp.com/')
sleep(20)

for x in data:

    try:
        print('1-------------')
        messageLink = 'https://web.whatsapp.com/send?phone='+x+'&text=Hare%20Krishna,%0AThe%20*Bhagavad-Gita*,%20also%20called%20Gitopanishad,%20is%20the%20essence%20of%20all%20Vedic%20knowledge.%20%0A%0AIf%20one%20reads%20Bhagavad-gita%20very%20sincerely%20and%20with%20all%20seriousness,%20then%20by%20the%20grace%20of%20the%20Lord,%20the%20reactions%20of%20his%20past%20misdeeds%20will%20not%20act%20upon%20him.%20%0A%0AWe%20can%20find%20solutions%20to%20practically%20all%20our%20problems%20in%20Bhagavad%20Gita.%0A%0ATo%20understand%20the%20essence%20of%20Bhagavad-gita%20and%20its%20practical%20application%20in%20day-to-day%20life,%20join%20this%20FREE%20online%20workshop.%20Pls%20click%20on%20the%20below-mentioned%20link%20to%20register%0A%0A%F0%9F%97%93%EF%B8%8F%20:%2026-April%20to%2003-May-2020%20%0A%E2%8F%B0:%208%20pm%20onwards%0A%0A*For%20English:*%20https://bit.ly/jig21gen%0A%0A*%E0%A4%B9%E0%A4%BF%E0%A4%82%E0%A4%A6%E0%A5%80%20%E0%A4%95%E0%A5%87%20%E0%A4%B2%E0%A4%BF%E0%A4%8F:*%20bit.ly/jig21GenH%0A%0APlease%20register%20and%20help%20us%20in%20spreading%20the%20word.%0A%0ARegards%0AMayank'
        print('2-------------')
        driver.get(messageLink)
        print('3-------------')
        sleep(20)
        print('4-------------')
        attachbtn = driver.find_element_by_css_selector('.bDS3i > div:nth-child(1) > div:nth-child(1)')
        print('5-------------')
        sleep(1)
        print('6-------------')
        attachbtn.click()
        print('7-------------')
        attachbtn = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[1]')
        # attachbtn.click()
        attachImageAndVideoBtn = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input')
        attachImageAndVideoBtn.send_keys('C:\\WhatsApp.jpeg')
        sleep(5)
        elem = driver.find_element_by_css_selector('html.js.serviceworker.adownload.cssanimations.csstransitions.webp.webp-alpha.webp-animation.webp-lossless body.web div#app div._1rp8-._1f763.app-wrapper-web.os-win div._36Q2N.two div._3Bog7 div.i5ly3._2l_Ww span.WnX2e div._38iEl span._1TBWy div div._2BQrC.QWTBH.wx4c2._1mHgA.copyable-area div._1RHZR.b-lt8 span div._3ipVb')
        sleep(4)
        elem.click()
        sleep(5)
        print('Sent---------')

    except:
        print("Something went wrong")
    finally:
        print("The 'try except' is finished")
