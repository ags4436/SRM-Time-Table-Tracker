from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time
# Used to make Headless Browser.
options = Options()
options.headless = True

# add the path where you have installed the gecko driver with its name.
driver = webdriver.Firefox(options=options, executable_path=r'C:\Users\adity\Desktop\tt\geckodriver.exe')
wait = WebDriverWait(driver, 15)
driver.get('https://academia.srmist.edu.in/accounts/signin?_sh=false&hideidp=true&portal=10002227248&client_portal=true&dcc=true&servicename=ZohoCreator&service_language=en&serviceurl=https%3A%2F%2Facademia.srmist.edu.in%2F')
first_result = wait.until(presence_of_element_located((By.ID, 'Email')))
Username = driver.find_element_by_id("Email")
# add your registeration number.
Username.send_keys("Email Id")

Password = driver.find_element_by_id("Password")
# add your password number.
Password.send_keys("Passowrd")

driver.find_element_by_css_selector(".btn").click()
time.sleep(5)
driver.get('https://academia.srmist.edu.in/#Page:WELCOME')

second_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, ".highlight")))
soup = BeautifulSoup(driver.page_source,'html.parser')
link=soup.findAll('span',{"class": "highlight"})[1]
do = link.get_text()[-1]

driver.close()
driver.quit()

with open("index.html") as inf:
	txt = inf.read()
	soup = BeautifulSoup(txt,features="html.parser")
	for i in range(1,6):
		s="day"+str(i)
		soup.find("th", { "id" : s })['class']="cell100 column2"

	actstr="day"+do	
	soup.find("th", { "id" : actstr })['class']="cell100 column2 act"

with open("index.html", "w") as outf:
	outf.write(str(soup))
