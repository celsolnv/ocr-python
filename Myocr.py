import pytesseract as ocr
import numpy as np
import cv2
from PIL import Image
class Myocr:
    def __init__(self,filenameimg):
        self.filenameimg = filenameimg
        self.filenametxt = filenameimg.split('.')[0] + ".txt"
    
    def comFormatacao(self):
        # Deixando a imagem em preto e branco para realçar as letras

        imagem = Image.open(self.filenameimg).convert('RGB')
        
        npimagem = np.asarray(imagem).astype(np.uint8)
        npimagem[:, :, 0] = 0 # zerando o canal R (RED)
        npimagem[:, :, 2] = 0 # zerando o canal B (BLUE)
        im = cv2.cvtColor(npimagem, cv2.COLOR_RGB2GRAY)
        ret, thresh = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        binimagem = Image.fromarray(thresh)
        phrase = ocr.image_to_string(binimagem, lang='por')

        # arquivo = open(self.filenametxt, 'w+')
        arquivo = open(self.filenametxt, 'w+')
        arquivo.writelines(phrase)

    
    def semFormatacao(self):
        frase = ocr.image_to_string(Image.open(self.filenameimg), lang='por')
        arquivo = open(self.filenametxt, 'w+')
        arquivo.writelines(frase)
    



