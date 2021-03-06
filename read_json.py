import json
from xml.dom import minidom
import xml.etree.ElementTree as gfg
import os

dir='/home/safehalo/Downloads/dlib-19.24/examples/'

root = gfg.Element('dataset')
images = gfg.Element('images')
root.append(images)
def create_xml(d,f):
    img = gfg.SubElement(images,'image')
    img.set('file',f)
    for i in range(len(d)):
        box = gfg.SubElement(img,'box')
        box.set('top',str(int(d[i]['top'])))
        box.set('left',str(int(d[i]['left'])))
        box.set('width',str(int(d[i]['width'])))
        box.set('height',str(int(d[i]['height'])))
        img.append(box)
    images.append(img)



file = open('captures_000.json')
data = json.load(file)
for i in range(len(data['captures'])):
    annotations = []
    for j in data['captures'][i]['annotations'][0]['values']:
        left = j['x']
        top = j['y']
        width = j['width']
        height = j['height']
        annotation={'left':left,'height':height,'width':width,'top':top}
        annotations.append(annotation)
        # print(data1)
    print(annotations)
    create_xml(annotations,dir+data['captures'][i]['filename'])
tree = gfg.ElementTree(root)
tree.write('example.xml')



