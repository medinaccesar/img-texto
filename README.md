# img-texto
Extractor simple del texto de una imagen. Cuando se ejecuta en modo consola extrae el texto a un archivo. Próximamente: si se ejecuta en modo gráfico se extrae el texto de toda la imagen o de la parte seleccionada a un cuadro de texto, pudiéndose, asimismo, exportar a un archivo.

# Requisitos
 Python 3.
 
 Si se quiere usar la interfaz gráfica se requiere «tkinter».    
 En linux se puede instalar con apt-get o el gestor de paquetes correspondiente, por ejemplo:
```
 sudo apt-get install python3-tk
 ```
En «windows» está incluido a partir de python 3.

# Instalación de dependencias
Se instalan las dependencias establecidas en el setup:
```
 pip install .    
```
# Uso
```
Uso: img_texto.py [-h] [-e ARCHIVO | -g] [--version]

img-texto 1.0.0

argumentos opcionales:
  -h, --help            muestra este mensaje de ayuda y sale
  -e ARCHIVO, --extraer ARCHIVO  Extrae el texto de la imagen
  -g, --gui             Se ejecuta el entorno gráfico
  --version             Muestra la versión del programa

```
Por ejemplo:
```
## Extraer todo el texto de un archivo de imagen
python  img_texto.py -e ./rec/prueba.png
Se ejecuta en modo consola
```
