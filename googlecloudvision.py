import argparse, random, io, re, os
from PIL import Image, ImageDraw, ImageFont
from google.cloud import vision

coords = []

def localize_objects(path):
   
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
        r = lambda: random.randint(0,255)
        draw.line(box + [box[0]], width=5, fill='#%02X%02X%02X' % (r(),r(),r()))
        draw.text((20, 70), "something123", font=ImageFont.truetype("~/Library/Fonts/MuseoSansCyrl-100.ttf"))

    im.save(path+"_output.png")
            
if __name__ == '__main__':
    localize_objects("tGdkZ3F2vKE.jpg")