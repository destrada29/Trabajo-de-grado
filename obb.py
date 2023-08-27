from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import matplotlib.pyplot as plt
import re
import numpy as np



class Data_extract():
    def __init__(self,link):
        self.link= link
        self.servicio= Service(executable_path="trabajo_selenium\chromedriver.exe")
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

    def Obtener_perfiles(self,dato):
        self.text_list = [element.text for element in self.driver.find_elements(By.CLASS_NAME,dato)]

    def Cerrar_drive(self):
        self.driver.close()
    
    def obtener_perfiles_paginados(self,dato,num,xpath):
        self.text_list = [[element.text for element in self.driver.find_elements(By.CLASS_NAME,dato)]]
        for i in range(num):
            self.busqueda_xpath(xpath).click()
            time.sleep(4)
            self.text_list.append([element.text for element in self.driver.find_elements(By.CLASS_NAME,dato)])


         











