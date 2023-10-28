from PIL import Image
import pytesseract

class ImgTexto():
    
    
    def extraer(self,image_path):
        print(image_path)
        image = Image.open(image_path)
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    
    def extraer_parte(image_path, crop_rectangle):
        image = Image.open(image_path)
        cropped_image = image.crop(crop_rectangle)
        text = pytesseract.image_to_string(cropped_image)
        return text