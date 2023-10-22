import time
from obb import DataExtract

linkedin = DataExtract('https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0')
linkedin.ingresar_link()
linkedin.busqueda_id("job-search-bar-keywords").send_keys('Informatica')
linkedin.busqueda_id("job-search-bar-location").clear()
linkedin.busqueda_id("job-search-bar-location").send_keys('Colombia')
linkedin.busqueda_xpath("//*[@id='jobs-search-panel']/form/button").click()
time.sleep(1)
linkedin.scroll_down_smoothly()
linkedin.Obtener_perfiles('base-search-card__title','base-search-card__subtitle','job-search-card__location')
linkedin.Cerrar_drive()
#linkedin.Guardar_perfiles(f'/home/cscc/Documents/Proyects/Trabajo-de-grado/media/Resultados/Resultado_{hora}.csv')
json = linkedin.Guardar_perfiles()
print(json)