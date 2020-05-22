#Tener la ruta del archivo contenido en un variable

#convertir el pdf en txt

#Manipular el txt 

import requests 
import pdfplumber
import pandas as pd
def download_file(url):
    local_filename = url.split("/")[-1]
    
    with requests.get(url) as r:
        with open(local_filename, "wb") as f:
            f.write(r.content)
    
    return local_filename

ap_url = "https://www.tabs3.com/support/sample/apreports.pdf"

ap = download_file(ap_url)

with pdfplumber.open(ap) as pdf:
    page = pdf.pages[15]
    text = page.extract_text()
    
print(text)
