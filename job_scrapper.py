# Importamos las librerías necesarias
import requests  # Para hacer solicitudes HTTP
from bs4 import BeautifulSoup  # Para analizar el contenido HTML

# Definimos la URL de la página web de empleos de Python en Nueva Zelanda
url = "https://www.seek.co.nz/python-jobs"

# Realizamos una solicitud GET para obtener el contenido de la página
respuesta = requests.get(url)

# Convertimos el contenido de la respuesta en un objeto BeautifulSoup para su análisis
peticion = BeautifulSoup(respuesta.text, "html.parser")

# Buscamos todas las etiquetas <h3> en la página, que probablemente contengan los títulos de los trabajos
trabajos = peticion.find_all("h3")

# Iteramos sobre los primeros 10 resultados encontrados
for i, trabajos in enumerate(trabajos[:10], start=1):
    
    # Concatenamos la URL base con el valor del atributo "href" del enlace dentro de cada trabajo
    joblink = "https://www.seek.co.nz" + trabajos.find("a").get("href")
    
    # Extraemos y mostramos el texto dentro de cada etiqueta <h3>, eliminando espacios innecesarios
    # También mostramos el enlace de la oferta de trabajo
    print(f"{i}. {trabajos.get_text(strip=True)}: {joblink}")
