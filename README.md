# Colabora videocursoscloud
 
 Permite generar un archivo markdown con los ultimos titulos de [humble bundles](https://www.humblebundle.com/)  
 
## Prerequisitos
 
Instale [WebDriver](https://www.selenium.dev/documentation/en/selenium_installation/installing_webdriver_binaries/) siguendo las instrucciones para su sistema operativo y no olvide configurar el [PATH](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/)

Tener instalado python 3.6 o superior


## Instalación
=====

Clone el repositorio en un directorio de su preferencia

## Ejecución
=====

Estando en el directorio de trabajo, active el entorno virtual de desarrollo

`.\Scripts\activate`

Navegue hacia la carpeta app

`cd app`

Instale las librerias necesarias con el siguiente comando:

`pip install -r requirements.txt`

Ejecute el programa con el siguiente comando:

`python app.py`

Debe generarse un archivo **colabora.md** con los nombres de los ultimos  humble bundles y el tiempo restante de promocion de los mismos.


