import pytesseract as ocr
import numpy as np
import cv2
from PIL import Image

def comFormatacao(filenameimg,filenametxt):
    # Deixando a imagem em preto e branco para realçar as letras
    imagem = Image.open(filenameimg).convert('RGB')
    
    npimagem = np.asarray(imagem).astype(np.uint8)
    npimagem[:, :, 0] = 0 # zerando o canal R (RED)
    npimagem[:, :, 2] = 0 # zerando o canal B (BLUE)
    im = cv2.cvtColor(npimagem, cv2.COLOR_RGB2GRAY)
    ret, thresh = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    binimagem = Image.fromarray(thresh)
    phrase = ocr.image_to_string(binimagem, lang='por')

    arquivo = open(filenametxt, 'w+')
    arquivo.writelines(phrase)

def semFormatacao(filenameimg,filenametxt):
    frase = ocr.image_to_string(Image.open(filenameimg), lang='por')
    arquivo = open(filenametxt, 'w+')
    arquivo.writelines(frase)

def executarDemo():
    diretorioImg = "./demo-img/img0"
    diretorioTxt = "./demo-txt/img0"
    for i in range(1,6):
        pathImg = diretorioImg + str(i) + ".jpg"
        pathTxt = diretorioTxt + str(i) + ".txt"

        comFormatacao(pathImg,pathTxt)
        # semFormatacao(pathImg,pathTxt)

executarDemo()