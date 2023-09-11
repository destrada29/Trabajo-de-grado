import time
import platform
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

class Data_extract():
    
    def __init__(self,link):
        self.link= link
        if platform.system() == "Windows":
            self.servicio = Service(executable_path = "trabajo_selenium\chromedriver.exe")
        else:
            self.servicio = Service(executable_path = "/usr/local/bin/chromedriver")

        self.driver = webdriver.Chrome(service=self.servicio)
    
    def ingresar_link(self):
        return self.driver.get(self.link)
    
    def busqueda_xpath(self,dato):
        return self.driver.find_element(By.XPATH,dato)
    
    def busqueda_id(self,dato):
        return self.driver.find_element(By.ID,dato)
    
    def scroll_down(self,num,dato):
        for i in range(num):
            self.driver.find_element(By.XPATH,dato).send_keys(Keys.END)
            time.sleep(2)

    def Obtener_perfiles(self,title,company,location):
        self.title = [element.text for element in self.driver.find_elements(By.CLASS_NAME,title)]
        self.location = [element.text for element in self.driver.find_elements(By.CLASS_NAME,location)]
        self.company = [element.text for element in self.driver.find_elements(By.CLASS_NAME,company)]

    def Guardar_df(self,name):
        df_jobs = pd.DataFrame({'Title' : self.title, 'Location' : self.location, 'Company' : self.company})
        df_jobs.to_csv(name, index=False)
    
    def Cerrar_drive(self):
        self.driver.close()
    
    def obtener_perfiles_paginados(self,dato,num,xpath):
        self.title = [[element.text for element in self.driver.find_elements(By.CLASS_NAME,dato)]]
        for i in range(num):
            self.busqueda_xpath(xpath).click()
            time.sleep(4)
            self.title.append([element.text for element in self.driver.find_elements(By.CLASS_NAME,dato)])