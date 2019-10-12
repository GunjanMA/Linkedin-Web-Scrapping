from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import parameters
from parsel import Selector


driver=webdriver.Chrome('C:/Users/gunjan/Desktop/Web_Scraping/chromedriver')
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
#sleep(0.5)
uname=driver.find_element_by_id('username')
uname.send_keys('9955867077')
#sleep(0.5)
passwd=driver.find_element_by_id('password')
passwd.send_keys('Aadi@123')
#sleep(0.5)
sign_in_btn=driver.find_element_by_xpath('//*[@type="submit"]')
sign_in_btn.click()
#sleep(5)


driver.get('https://www.google.com')
search_q=driver.find_element_by_name('q')
#sleep(0.5)
search_q.send_keys('site:linkedin.com/in/ AND "full stack developer" AND "Chennai"')
#sleep(2)
search_q.send_keys(Keys.RETURN)
#sleep(5)
linkedin_urls=driver.find_elements_by_tag_name('cite')
len(linkedin_urls)
linkedin_urls=[url.text for url in linkedin_urls]
linkedin_urls


for linkedin_url in linkedin_urls:
    driver.get(linkedin_url)
    sleep(5)

    sel=Selector(text=driver.page_source)
    
