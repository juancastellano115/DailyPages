from PIL import Image, ImageDraw, ImageFont
from datetime import datetime



global day 
day = datetime.now().timetuple().tm_yday
W,H = (1000,1000)
msg= "Page "+str(day)+" of 366"


def crear_imagen():
    
    Imagen = Image.new('RGB', (W,H), color = 'white')

    fnt = ImageFont.truetype('Moon Flower.ttf', 145)


    Letra = ImageDraw.Draw(Imagen)
    w,h = fnt.getsize(msg)

    Letra.text(((W-w)/2,(H-h)/2), msg, font=fnt, fill='black')

    Imagen.save('day'+str(day)+'.png')



if __name__ == "__main__":
    crear_imagen()