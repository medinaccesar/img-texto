import re
from PIL import Image
import pytesseract

class ImgTexto():
    
    
    def extraer(self,imagen):        
        if not self.es_imagen(imagen):
            # Se trata de una ruta a la imagen, se abre
            imagen = Image.open(imagen)
        text = pytesseract.image_to_string(imagen)        
        return self.limpiar_texto(text)
    
    def extraer_parte(self,image_path, crop_rectangle):
        image = Image.open(image_path)
        cropped_image = image.crop(crop_rectangle)
        text = pytesseract.image_to_string(cropped_image)
        return self.limpiar_texto(text)
    
    def es_imagen(self,obj):
        return isinstance(obj, Image.Image)
    
    def limpiar_texto(self,text):        
        limpio = re.sub(r'[]', '', text)
        return limpio