from Myocr import Myocr
import sys

filename = sys.argv[1]
ocr = Myocr(filename)
ocr.comFormatacao()
