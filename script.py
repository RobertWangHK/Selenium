from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

def measure_cpu(url):
    """ Measure CPU consumption of the firefox-bin process"""
    print (url)
    os.system('echo %s >> ./cpu-usage' % url)
    cpu_list = []
    # Loop
    for i in range(90):
        cpu = os.popen("top -n 1 | grep /usr/lib/chromium/chrome | head -1 | awk '{print $8;}'").read().strip()
        time.sleep(1)
        cpu_list.append(cpu)
    os.system('echo %s >> ./cpu-usage' % cpu_list)
    # os.system("ps -eo pcpu,pid,user,args | grep 'firefox-bin' | sort -k1 -r -n | head -1 | awk '{print $1;}'")
    # os.system("ps -eo pcpu,pid,user,args | sort -k1 -r -n | head -1 | awk '{print $1;}'")

# weblist
# with open('weblist', 'r') as input:
#    sites = input.read().splitlines()
sites = ['http://lesbians4u.org/']

for site in sites:
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(site)
    measure_cpu(site)
    driver.quit()

exit()