from PIL import Image
from PIL import ImageDraw
import imageio
import os
a=[1, 4, 3]
b=[6, 2, 9]


import copy

Achange=[]
Bchange=[]
Cchange=[[]]
counter=[]

def doubleTrack (lst1,lst2):
    lst1=sorted(lst1)
    lst2=sorted(lst2)
    Achange.append(copy.copy(lst1))
    Bchange.append(copy.copy(lst2))
    c=[]
    while lst1!=[] or lst2!=[]:
        if lst1==[] or lst2==[]:
            if lst1==[]:
                for i in lst2:
                    c.append(i)
                counter.append(1)
                Bchange.append(copy.copy(lst1))
            if lst2==[]:
                for i in lst1:
                    c.append(i)
                counter.append(0)
                Achange.append(copy.copy(lst2))
            Cchange.append(copy.copy(c))
            break
        else:
            if lst1[0]<=lst2[0]:
                c.append(lst1[0])
                del lst1[0]
                Achange.append(copy.copy(lst1))
                Cchange.append(copy.copy(c))
                counter.append(0)
            else:
                c.append(lst2[0])
                del lst2[0]
                Bchange.append(copy.copy(lst2))
                Cchange.append(copy.copy(c))
                counter.append(1)
    return c




doubleTrack (a,b)

a=Achange
b=Bchange
c=Cchange
count=counter
if len(a)<len(b):
    a.append([])
if len(b)<len(a):
    b.append([])
print(a,b)


i=0
j=0
k=0
index=1
text1="Source data:"
text4="Result: "
color = (230, 230, 250)
while k<len(c):
    text2=str(Achange[i])
    text3=str(Bchange[j])
    text5=str(Cchange[k])
    img = Image.new('RGB', (200, 150), color) 
    imgDrawer = ImageDraw.Draw(img) 
    imgDrawer.text((10, 10), text1, (25, 25, 112))
    imgDrawer.text((10, 30), text2, (25, 25, 112))
    imgDrawer.text((10, 50), text3, (25, 25, 112))
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
            draw.ellipse([(10, 46), (30, 70)],fill=None, outline=128,width=2)
        img.save("%d.png" % index)
        index= int(str(index)+"1")
    i=i+(1-count1)
    j=j+count1
    k=k+1

        
path = 'C:/Users/позитроника/Desktop/images/doubleTrack/'
image_folder = os.fsencode(path)
filenames = []

for file in os.listdir(image_folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.jpeg', '.png') ):
        filenames.append(filename)

filenames.sort()

images = list(map(lambda filename: imageio.imread(path+filename), filenames))

imageio.mimsave(os.path.join(path+'gif_for_doubleTrack.gif'),images, duration = 0.7)




















