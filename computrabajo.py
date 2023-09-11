import pandas as pd
from obb import Data_extract, time

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
computrabajo.busqueda_xpath('/html/body/main/div[6]/div/div[1]/div[4]').click()
time.sleep(2)
computrabajo.busqueda_xpath('/html/body/main/div[6]/div/div[1]/div[4]/div/ul/li[3]').click()
time.sleep(2)

computrabajo.obtener_perfiles_paginados('js-o-link',3,'//*[@id="offersGridOfferContainer"]/div[8]/span[2]')
#pprint(computrabajo.text_list)

df = pd.DataFrame(computrabajo.text_list).T
with pd.option_context('display.max_rows', None, 'display.max_columns', None): 
    print(df)
