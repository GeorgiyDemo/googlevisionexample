import argparse, random, io, re, os, time, requests
from PIL import Image, ImageDraw, ImageFont
from google.cloud import vision

def localize_objects(path):
    try:
        coords = []
        allcoords = []
           
        im = Image.open(path)
        draw = ImageDraw.Draw(im)
        client = vision.ImageAnnotatorClient()
        with open(path, 'rb') as image_file:
            content = image_file.read()
            image = vision.types.Image(content=content)

        objects = client.object_localization(image=image).localized_object_annotations

        print('Number of objects found: {}'.format(len(objects)))
        for object_ in objects:
            print('\n{} (confidence: {})'.format(object_.name, object_.score))
                    
            box = [(vertex.x*im.width, vertex.y*im.height) for vertex in object_.bounding_poly.normalized_vertices]
                
            if box not in allcoords:
                allcoords.append(box)
                print(box)
                r = lambda: random.randint(0,255)
                draw.line(box + [box[0]], width=5, fill='#%02X%02X%02X' % (r(),r(),r()))
                draw.text(box[0], object_.name+" "+str(object_.score), font=ImageFont.truetype("~/Library/Fonts/MuseoSansCyrl-300.ttf",30))
        image_file.close()
        im.save("output"+path+".png")
    except:
        print("РИП БРАТ")
        time.sleep(30)
            

if __name__ == '__main__':
    allfileslist = []
    for root, dirs, files in os.walk("."):  
        for filename in files:
            if filename[-3:] == "jpg":
                allfileslist.append(filename)
    allfileslist.sort()
    print(allfileslist)
    for this_image in allfileslist:
        localize_objects(this_image)