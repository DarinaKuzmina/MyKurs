from PIL import Image
from PIL import ImageDraw
import imageio
import os
a=[1,3,5,7,9]
b=[2,4,6]
AUXdisision=[]
Cdisision=[[]]
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
    AUXdisision.append(copy.copy(aux))
    while aux!=[]:
        i=0
        j=len(aux)-1
        if aux[i]<=aux[j]:
            c.append(aux[i])
            del aux[i]
            AUXdisision.append(copy.copy(aux))
            Cdisision.append(copy.copy(c))
            counter.append(0)
        else:
            c.append(aux[j])
            del aux[j]
            AUXdisision.append(copy.copy(aux))
            Cdisision.append(copy.copy(c))
            counter.append(1)
    return c

abstract (a,b)
print(AUXdisision, "да",Cdisision,"да", counter )

aux=AUXdisision
c=Cdisision
count=counter
index=1
text1="Source data:"
text4="Result: "
text2=str(a)
text3=str(b)
lst=[str([]),str(a), str(aux[0])]
for text5 in lst:
    color = (230, 230, 250)
    img = Image.new('RGB', (200, 150), color) 
    imgDrawer = ImageDraw.Draw(img) 
    imgDrawer.text((10, 10), text1, (25, 25, 112))
    imgDrawer.text((10, 30), text2, (25, 25, 112))
    imgDrawer.text((10, 50), text3, (25, 25, 112))
    imgDrawer.text((10, 70), text4, (25, 25, 112))
    imgDrawer.text((10, 90), text5, (25, 25, 112))
    img.save("%d.png" % index)
    index = int(str(index)+"1")


i=0
k=0
while k<len(c):
    text2=str(aux[i])
    text5=str(c[k])
    color = (230, 230, 250)
    img = Image.new('RGB', (200, 150), color) 
    imgDrawer = ImageDraw.Draw(img) 
    imgDrawer.text((10, 10), text1, (25, 25, 112))
    imgDrawer.text((10, 30), text2, (25, 25, 112))
    imgDrawer.text((10, 70), text4, (25, 25, 112))
    imgDrawer.text((10, 90), text5, (25, 25, 112))
    img.save("%d.png" % index)
    index = int(str(index)+"1")
    draw = ImageDraw.Draw(img)
    if k<len(count):
        count1=count[k]
        if count1==0:
            draw.ellipse([(10, 28), (30, 50)],fill=None, outline=128,width=2)
        else:
            f=len(aux[i])*16+1
            draw.ellipse([(f, 28), (f+20, 50)],fill=None, outline=128,width=2)
        img.save("%d.png" % index)
        index= int(str(index)+"1")




    
    i=i+1
    k=k+1

        
path = 'C:/Users/позитроника/Desktop/images/abstract/'
image_folder = os.fsencode(path)
filenames = []

for file in os.listdir(image_folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.jpeg', '.png') ):
        filenames.append(filename)

filenames.sort()

images = list(map(lambda filename: imageio.imread(path+filename), filenames))

imageio.mimsave(os.path.join(path+'gif_for_abstract.gif'), images, duration = 0.9)


