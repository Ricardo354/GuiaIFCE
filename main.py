import pandas as pd
import selenium
import json
from bs4 import BeautifulSoup


URL = 'https://ifce.edu.br/crato/cursosemcrato/tecnicos/integrados/informatica/matriz'

#POR ENQUANTO TENTAR SÓ COM INFORMÁTICA E AGRO


driver = webdriver.Firefox()
driver.get(URL)
source = driver.page_source

soup = BeautifulSoup(page_source,'html.parser')

#iterate through tags
