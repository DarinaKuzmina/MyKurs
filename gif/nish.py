from PIL import Image
from PIL import ImageDraw
import imageio
import os
a=[5, 77, 74, 92, 3]
Adisision=[]
Bdisision=[]
Cdisision=[a]
counter=[]
import copy

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

def nish (lst):
    c=[]
    if len(lst)>1:
        n=(len(lst)+1)//2
        lst1=lst[0:n]
        lst2=lst[n:]
        nish(lst1)
        nish(lst2)
        Bdisision.append(str(copy.copy(lst1))+","+ str(copy.copy(lst2)))
        c=abstract(lst1,lst2)
        Cdisision.append(copy.copy(c))
        print(c)
    else:
        return
    return c


nish(a)

print(Cdisision)

index=1
text1="Source data:"
text2=str(a)
text4="Result: "



for text in Cdisision:
    text5=str(text)

    color = (230, 230, 250)
    img = Image.new('RGB', (200, 150), color) 
    imgDrawer = ImageDraw.Draw(img) 
    imgDrawer.text((10, 10), text1, (25, 25, 112))
    imgDrawer.text((10, 30), text2, (25, 25, 112))
    imgDrawer.text((10, 70), text4, (25, 25, 112))
    imgDrawer.text((10, 90), text5, (25, 25, 112))
    img.save("%d.png" % index)
    index = int(str(index)+"1")



path = 'C:/Users/позитроника/Desktop/images/nish/'
image_folder = os.fsencode(path)
filenames = []

for file in os.listdir(image_folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.jpeg', '.png') ):
        filenames.append(filename)

filenames.sort()

images = list(map(lambda filename: imageio.imread(path+filename), filenames))

imageio.mimsave(os.path.join(path+'gif_for_nish.gif'), images, duration = 1.2)
