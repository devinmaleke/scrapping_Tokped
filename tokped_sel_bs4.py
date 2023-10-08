import time
from selenium import webdriver
from bs4 import BeautifulSoup
from pandas import PeriodDtype


url = 'https://www.tokopedia.com/kalbeconsumer/product'

driver = webdriver.Chrome()
driver.get(url)

soup = BeautifulSoup(driver.page_source, "html.parser")
# print(soup)

for item in soup.findAll('div', class_='css-uwyh54'):
    nama_produk = item.find('div', class_='prd_link-product-name css-3um8ox').text
    
    tjl = item.find('div', class_='css-yaxhi2')
    if len (tjl) > 0:
        terjual = item.find ('span', class_='prd_label-integrity css-1sgek4h').text
        if item.find('span', class_='prd_rating-average-text css-t70v7i'):
            rating = item.find('span', class_='prd_rating-average-text css-t70v7i').text
        else:
            rating = ''    
    else:
        terjual = '' 
        rating = ''



    print(nama_produk)
    print(terjual)
    print(rating)
    print("==================\n")
    


#  tjl = item.findAll('div', class_='css-yaxhi2')
#     if len (tjl) > 0:
#         terjual = item.find ('span', class_='prd_label-integrity css-1sgek4h').text
#     else:
#         terjual = ''    
driver.close()

