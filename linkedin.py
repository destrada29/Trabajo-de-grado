from obb import Data_extract
import time
from pprint import pprint


linkedin=Data_extract('https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0')
linkedin.ingresar_link()
time.sleep(2)
linkedin.busqueda_id("job-search-bar-keywords").send_keys('Informatica')
time.sleep(2)
linkedin.busqueda_id("job-search-bar-location").clear()
time.sleep(2)
linkedin.busqueda_id("job-search-bar-location").send_keys('Perímetro Urbano Medellín, Antioquia, Colombia')

time.sleep(2)
linkedin.busqueda_xpath("//*[@id='jobs-search-panel']/form/button").click()
time.sleep(2)
linkedin.busqueda_xpath("//*[@id='jserp-filters']/ul/li[6]/div/div/button").click()
time.sleep(2)
linkedin.busqueda_id('f_E-1').click()
time.sleep(2)
linkedin.busqueda_id('f_E-3').click()

time.sleep(2)
linkedin.busqueda_xpath("//*[@id='jserp-filters']/ul/li[6]/div/div/div/button").click()
time.sleep(2)
linkedin.scroll_down(10,'/html')
linkedin.Obtener_perfiles('sr-only')
pprint(linkedin.text_list)
