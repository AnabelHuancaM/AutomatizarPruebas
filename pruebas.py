#automatizar pruebas, descargar primero con pip install selenium y el driver de chrome
import unittest
from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#pagina a usar
website = 'https://www.google.com/'
#ruta de donde se encuentra el driver de chrome
path = 'C:\Program Files (x86)\chromedriver' 

class usando_chrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=path)

    def tearDown(self): #se cierra la clase
        self.driver.close()

    def test_buscar_por_nombre(self): #buscar por el nombre en el buscador
        driver = self.driver
        driver.get(website)
        time.sleep(2)
        buscar_por_nombre = driver.find_element(By.NAME, 'q')
        buscar_por_nombre.send_keys("Como Aprobar el curso", Keys.ARROW_DOWN)
        boton_busqueda = driver.find_element(By.NAME, "btnK")
        time.sleep(3)
        boton_busqueda.click()
        time.sleep(10)

if __name__ == '__main__':
    unittest.main()