from selenium import webdriver
from selenium.webdriver.common import keys
import time
import sys
import re
import json
from colorama import Fore
print(Fore.YELLOW + '''  
 _   _     _                           _         _        
| | | | __| | ___ _ __ ___  _   _     / \  _   _| |_ ___  
| | | |/ _` |/ _ \ '_ ` _ \| | | |   / _ \| | | | __/ _ \ 
| |_| | (_| |  __/ | | | | | |_| |  / ___ \ |_| | || (_) |
 \___/ \__,_|\___|_| |_| |_|\__, | /_/   \_\__,_|\__\___/ 
                            |___/                         
 _____                 _ _           
| ____|_ __  _ __ ___ | | | ___ _ __ 
|  _| | '_ \| '__/ _ \| | |/ _ \ '__|
| |___| | | | | | (_) | | |  __/ |   
|_____|_| |_|_|  \___/|_|_|\___|_|   
                                     
                                      
     ''')
with open('acc.json') as f:
    data = json.loads(f.read())
    emailid=data['email']
    passwordd=data['password']
browser = webdriver.Chrome()


def login():
    browser.get('https://www.udemy.com/join/login-popup/')
    time.sleep(5)
    mail=browser.find_elements_by_css_selector('#email--1')
    mail[0].send_keys(emailid)
    passs=browser.find_elements_by_css_selector('#id_password')
    passs[0].send_keys(passwordd)
    klik=browser.find_elements_by_css_selector('#submit-id-submit')
    klik[0].click()
    print(Fore.GREEN + 'Login Sucess, Enrolling Now\n')  

def Enroll():    
    with open('courses.txt','r')as courses:
        for line in courses:
            if re.search("https://www.udemy.com/", line):
                browser.get(line)
                time.sleep(5)
                try:
                    firsEnrol=browser.find_element_by_css_selector('.generic-purchase-section--free-course--JmRjJ > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)')
                    text=firsEnrol.text
                    print(text)
                    if text!='Enroll now':
                        print(Fore.RED +'The Course is not free or coupan is expired!\n')
                    else:
                        firsEnrol=browser.find_element_by_css_selector('.generic-purchase-section--free-course--JmRjJ > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)')
                        firsEnrol.click()
                        time.sleep(2)
                        secondEnrol=browser.find_element_by_css_selector('.styles--checkout-pane-outer--1syWc > div:nth-child(1) > div:nth-child(4) > button:nth-child(2)')
                        secondEnrol.click()
                        print(Fore.GREEN+f'Sucessfully Enrolled: {line}\n')
                        time.sleep(2)
                except:
                    print('Looks like it is already enrolled, Check Link once again and try again\n')        

            else:
                print(Fore.RED+'Invalid Course Link\n')        
login()
Enroll()
browser.quit()
