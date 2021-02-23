from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os  
from time import sleep
import json

driver = webdriver.Firefox(executable_path=r'C:\Users\nnnpa\OneDrive\Desktop\whatsapp\geckodriver-v0.29.0-win64\geckodriver.exe')
data = [

{'no':1122334455,	'name':'name1'},
{'no':9988776655,	'name':'name2'}, 

]

driver.get('https://web.whatsapp.com/')
sleep(20)

for x in data:
  if(len(str((x['no'])))==10):
      try:
          no=str(x["no"])
          uname=x["name"]
          messageLink = 'https://web.whatsapp.com/send?phone=91'+no+'&text=*Hare%20Krishna%20'+uname+'*,%20have%20you%20registered%20for%20Jigyasa?%0APlease%20register%20if%20you%20haven%27t.%0A%0AAbout%20Jigyasa:%20It%20is%20a%20foundational%20course%20on%20Bhagavad%20Gita.%20It%20focuses%20on%20scientific%20understanding%20and%20practical%20applications%20in%20life.%0A%0ATopics:%0A1.%20Who%20am%20I%0A2.%20Incredible%20Vedas%201%0A3.%20Real%20Yoga%0A4.%20Laws%20of%20Karma%0A5.%20Demystifying%20world%20religions%0A6.%20Art%20of%20happiness%0A7.%20Principles%20of%20freedom%0A%0A%F0%9F%93%86:%2027th%20Feb%20to%206th%20March%0A%0A%F0%9F%95%97:%208%20pm%20-%209%20pm%0A%0ALearn%20more:%20https://youtu.be/55N50cjrdnA%0A%0ARegistration%20link%0AFor%20English:%20http://bit.ly/jig21mad%0A%E0%A4%B9%E0%A4%BF%E0%A4%82%E0%A4%A6%E0%A5%80%20%E0%A4%95%E0%A5%87%20%E0%A4%B2%E0%A4%BF%E0%A4%8F:%20%20http://bit.ly/Jig21madh%0A%0ARegards%0AHKM%20Mumbai'
          driver.get(messageLink)
          sleep(20)
          elem = driver.find_element_by_css_selector('html.js.serviceworker.adownload.cssanimations.csstransitions.webp.webp-alpha.webp-animation.webp-lossless body.web div#app div._1rp8-._1f763.app-wrapper-web.os-win div._36Q2N.two div.i5ly3._2l_Ww div#main._2AuNk footer._2ig1U div._3SvgF._1mHgA.copyable-area div._3qpzV button._2Ujuu')
          elem.click()
      except:
          print("Something went wrong")
      finally:
          print("The 'try except' is finished")
