from PIL import Image
from PIL import ImageDraw
import imageio
import os
a=[7,6,3,2,4,1,8,2]
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
        Cdisision.append(copy.copy(lst1))
        Cdisision.append(copy.copy(lst2))
        nish(lst1)
        nish(lst2)
        c=abstract(lst1,lst2)
        Cdisision.append(copy.copy(c))
        print(c)
    else:
        return
    return c

print(a)
nish(a)
print(Adisision, "да",Bdisision, "да",Cdisision,"да", counter )
print(len(Cdisision))
lst=[]
i=1
while i<=len(a):
    f=[]
    for j in Cdisision:
        if len(j)==i:
            f.append(j)
    lst.append(f)
    i=i*2
for i in lst:
    print(i)
index=1
text1="Source data:"
text2=str(a)
text4="Result: "
n=len(lst)
text5=str([7, 6, 3, 2, 4, 1, 8, 2])

color = (230, 230, 250)
img = Image.new('RGB', (250, 150), color) 
imgDrawer = ImageDraw.Draw(img) 
imgDrawer.text((10, 10), text1, (25, 25, 112))
imgDrawer.text((10, 30), text2, (25, 25, 112))
imgDrawer.text((10, 70), text4, (25, 25, 112))
imgDrawer.text((10, 90), text5, (25, 25, 112))
img.save("%d.png" % index)
index = int(str(index)+"1")

text5="[7, 6, 3, 2], [4, 1, 8, 2]"

color = (230, 230, 250)
img = Image.new('RGB', (250, 150), color) 
imgDrawer = ImageDraw.Draw(img) 
imgDrawer.text((10, 10), text1, (25, 25, 112))
imgDrawer.text((10, 30), text2, (25, 25, 112))
imgDrawer.text((10, 70), text4, (25, 25, 112))
imgDrawer.text((10, 90), text5, (25, 25, 112))
img.save("%d.png" % index)
index = int(str(index)+"1")

text5="[7, 6], [3, 2], [4, 1], [8, 2]"
    
color = (230, 230, 250)
img = Image.new('RGB', (250, 150), color) 
imgDrawer = ImageDraw.Draw(img) 
imgDrawer.text((10, 10), text1, (25, 25, 112))
imgDrawer.text((10, 30), text2, (25, 25, 112))
imgDrawer.text((10, 70), text4, (25, 25, 112))
imgDrawer.text((10, 90), text5, (25, 25, 112))
img.save("%d.png" % index)
index = int(str(index)+"1")


text5="[7], [6], [3], [2], [4], [1], [8], [2]"
                       
color = (230, 230, 250)
img = Image.new('RGB', (250, 150), color) 
imgDrawer = ImageDraw.Draw(img) 
imgDrawer.text((10, 10), text1, (25, 25, 112))
imgDrawer.text((10, 30), text2, (25, 25, 112))
imgDrawer.text((10, 70), text4, (25, 25, 112))
imgDrawer.text((10, 90), text5, (25, 25, 112))
img.save("%d.png" % index)
index = int(str(index)+"1")

text5="[6, 7], [2, 3], [1, 4], [2, 8]"

color = (230, 230, 250)
img = Image.new('RGB', (250, 150), color) 
imgDrawer = ImageDraw.Draw(img) 
imgDrawer.text((10, 10), text1, (25, 25, 112))
imgDrawer.text((10, 30), text2, (25, 25, 112))
imgDrawer.text((10, 70), text4, (25, 25, 112))
imgDrawer.text((10, 90), text5, (25, 25, 112))
img.save("%d.png" % index)
index = int(str(index)+"1")

text5="[2, 3, 6, 7], [1, 2, 4, 8]"

color = (230, 230, 250)
img = Image.new('RGB', (250, 150), color) 
imgDrawer = ImageDraw.Draw(img) 
imgDrawer.text((10, 10), text1, (25, 25, 112))
imgDrawer.text((10, 30), text2, (25, 25, 112))
imgDrawer.text((10, 70), text4, (25, 25, 112))
imgDrawer.text((10, 90), text5, (25, 25, 112))
img.save("%d.png" % index)
index = int(str(index)+"1")

text5="[1, 2, 2, 3, 4, 6, 7, 8]"

color = (230, 230, 250)
img = Image.new('RGB', (250, 150), color) 
imgDrawer = ImageDraw.Draw(img) 
imgDrawer.text((10, 10), text1, (25, 25, 112))
imgDrawer.text((10, 30), text2, (25, 25, 112))
imgDrawer.text((10, 70), text4, (25, 25, 112))
imgDrawer.text((10, 90), text5, (25, 25, 112))
img.save("%d.png" % index)
index = int(str(index)+"1")

path = 'C:/Users/позитроника/Desktop/images/Новая папка/'
image_folder = os.fsencode(path)
filenames = []

for file in os.listdir(image_folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.jpeg', '.png') ):
        filenames.append(filename)

filenames.sort()

images = list(map(lambda filename: imageio.imread(path+filename), filenames))

imageio.mimsave(os.path.join(path+'gif_for_nish.gif'), images, duration = 0.9)
