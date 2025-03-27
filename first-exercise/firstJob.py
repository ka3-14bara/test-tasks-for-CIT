from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import pandas as pd
import time


def CreatePersons(contacts, fields) -> dict:
    rows = contacts.shape[0]
    columns = contacts.shape[1]
    people = dict()
    
    for i in range (rows):
        name = ('person_%s' % i)
        people[name] = { "FirstName" : '', "LastName" : '', "Company" : '', "Role" : '', "Address" : '', "Email" : '',"Phone" : ''}
        for j in range (columns):
            people[name][fields[j]] = str(contacts.iloc[i,j])
    return people
        
def FillForm(persons, fields) -> None:
    for person in persons:
        for i in range(len(fields)):
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[ng-reflect-name='label%s']" % fields[i])))
            element.send_keys(persons[person][fields[i]])
        submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Submit']")
        submit_button.click()

if __name__ == '__main__':

    driver = webdriver.Chrome()
    driver.get("https://www.rpachallenge.com/")

    downloadElement = driver.find_element(By.XPATH, '//*[text()=" Download Excel "]')

    url = downloadElement.get_attribute("href")
  
    response = requests.get(url)
    response.raise_for_status()

    with open('challenge.xlsx', 'wb') as file:
        file.write(response.content)
    
    data = pd.read_excel('./challenge.xlsx')
    fields = ["FirstName", "LastName", "CompanyName", "Role", "Address", "Email", "Phone"]
    persons = CreatePersons(data, fields)

    start_button = driver.find_element(By.XPATH, '//*[text()="Start"]')
    start_button.click()

    try:
        FillForm(persons, fields)
        time.sleep(5)
    finally:
        driver.quit()
