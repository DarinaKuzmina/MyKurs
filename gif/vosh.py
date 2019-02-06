from PIL import Image
from PIL import ImageDraw
import imageio
import os
import copy
a=[7,6,3,2,4,1,8,2]
a1=copy.copy(a)
Cdisision=[[a1]]

def abstract (lst1,lst2):
    lst1=sorted(lst1)
    lst2=sorted(lst2)
    lst2.reverse()
    c=[]
    aux=lst1
    for i in lst2:
        aux.append(i)
    while aux!=[]:
        i=0
        j=len(aux)-1
        if aux[i]<=aux[j]:
            c.append(aux[i])
            del aux[i]
        else:
            c.append(aux[j])
            del aux[j]
    return c

def vosh(a):
    c=[]
    n=len(a)
    if n>1:
        for i in list(range(0, n)):
            if type(a[i]) == int:
                a[i]=[a[i]]
        for i in list(range(0, n-1, 2)):
            c.append(abstract(a[i],a[i+1]))
        if n%2 == 1:
            c.append(a[-1])
        Cdisision.append(copy.copy(c))
        c=vosh(c)
    else:
       return a[0]
    return c

vosh(a)
print(Cdisision)

index=1
text1="Source data:"
text2=str(a1)
text4="Result: "


for text in Cdisision:
    text5=""
    for t in text:
        text5=text5 + str(t) +"  "

    color = (230, 230, 250)
    img = Image.new('RGB', (200, 150), color) 
    imgDrawer = ImageDraw.Draw(img) 
    imgDrawer.text((10, 10), text1, (25, 25, 112))
    imgDrawer.text((10, 30), text2, (25, 25, 112))
    imgDrawer.text((10, 70), text4, (25, 25, 112))
    imgDrawer.text((10, 90), text5, (25, 25, 112))
    img.save("%d.png" % index)
    index = int(str(index)+"1")



path = 'C:/Users/позитроника/Desktop/images/vosh/'
image_folder = os.fsencode(path)
filenames = []

for file in os.listdir(image_folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.jpeg', '.png') ):
        filenames.append(filename)

filenames.sort()

images = list(map(lambda filename: imageio.imread(path+filename), filenames))

imageio.mimsave(os.path.join(path+'gif_for_vosh.gif'), images, duration = 1.2)











