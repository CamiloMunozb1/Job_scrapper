# Job Scraper - Python Jobs en Nueva Zelanda

Este proyecto es una automatización simple para obtener ofertas de trabajo relacionadas con Python en Nueva Zelanda desde la página [Seek](https://www.seek.co.nz/). Utiliza **requests** para hacer la solicitud HTTP y **BeautifulSoup** para extraer la información relevante del HTML.

## Características
- Extrae los títulos de los primeros 10 empleos encontrados.
- Obtiene los enlaces directos a las ofertas.
- El código es minimalista y fácil de entender.

## Requisitos
Asegúrate de tener Python instalado y las siguientes librerías:
```sh
pip install requests beautifulsoup4
```

## Uso
Ejecuta el script y verás en consola los nombres de los trabajos junto con sus enlaces correspondientes.

## Notas
- Este proyecto está diseñado para ser lo más simple posible.
- La estructura del HTML de la página puede cambiar, lo que podría afectar la extracción de datos.
- Recuerda revisar los términos de uso del sitio web antes de hacer scraping.

## Contribución
Si tienes ideas para mejorar el código manteniendo su simplicidad, siéntete libre de contribuir.

## Licencia
Este proyecto esta bajo una licencia MIT.

