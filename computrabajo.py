import time
import pprint
import datetime
import pandas as pd
from obb import Data_extract

hora = str(datetime.datetime.now())

computrabajo=Data_extract('https://co.computrabajo.com/')
computrabajo.ingresar_link()
time.sleep(2)
computrabajo.busqueda_id("prof-cat-search-input").send_keys('Informatica')
time.sleep(2)
computrabajo.busqueda_id("place-search-input").send_keys('Colombia')
time.sleep(2)
computrabajo.busqueda_id("search-button").click()
time.sleep(2)
computrabajo.busqueda_xpath('//*[@id="pop-up-webpush-sub"]/div[2]/div/button[1]').click()
time.sleep(2)

"""
#Filtro de experiencia
computrabajo.busqueda_xpath('/html/body/main/div[6]/div/div[1]/div[4]').click()
time.sleep(2)
computrabajo.busqueda_xpath('/html/body/main/div[6]/div/div[1]/div[4]/div/ul/li[3]').click()
time.sleep(2)
"""

js-o-link fc_base

linkedin.Obtener_perfiles('base-search-card__title','base-search-card__subtitle','job-search-card__location')


computrabajo.obtener_perfiles_paginados('js-o-link',3,'//*[@id="offersGridOfferContainer"]/div[8]/span[2]')
computrabajo.Guardar_df(f'Trabajo-de-grado/Resultados/Resultado_{hora}.csv')



#pprint(computrabajo.text_list)


"""
computrabajo.Cerrar_drive()
time.sleep(2)
computrabajo.Guardar_df(f'Trabajo-de-grado/Resultados/Resultado_{hora}.csv')
"""


"""
df = pd.DataFrame(computrabajo.text_list).T
with pd.option_context('display.max_rows', None, 'display.max_columns', None): 
    print(df)
"""
