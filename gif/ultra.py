from PIL import Image
from PIL import ImageDraw
import imageio
import os
import copy
a=[7,6,3,2,4,1,8,2]
Bdisision=[]
Adisision=[]

def doubleTrack (lst1,lst2):
    lst1=sorted(lst1)
    lst2=sorted(lst2)
    c=[]
    while lst1!=[] or lst2!=[]:
        if lst1==[] or lst2==[]:
            for i in max(lst1,lst2,key=len):
                c.append(i)
            break
        else:
            if lst1[0]<=lst2[0]:
                c.append(lst1[0])
                del lst1[0]
            else:
                c.append(lst2[0])
                del lst2[0]
    return c

def ultrasort(a):
    b=[]
    n=len(a)
    if n<=1:
        return a
    else:
        b.append(ultrasort(a[0:n//2]))
        b.append(ultrasort(a[n//2:]))
        Bdisision.append(str(copy.copy(b[0]))+","+ str(copy.copy(b[1])))
        c=doubleTrack(b[0],b[1])
        Adisision.append(copy.copy(c))
    return c

ultrasort(a)
print(a)
print(len(Adisision))
print(len(Bdisision))

index=1
text1="Source data:"
text2=str(a)
text4="Result: "

for i in list(range(len(Adisision))):
    text5="a: "+ str(Adisision[i])
    text6="b: "+ str(Bdisision[i])
    color = (230, 230, 250)
    img = Image.new('RGB', (200, 150), color) 
    imgDrawer = ImageDraw.Draw(img) 
    imgDrawer.text((10, 10), text1, (25, 25, 112))
    imgDrawer.text((10, 30), text2, (25, 25, 112))
    imgDrawer.text((10, 70), text4, (25, 25, 112))
    imgDrawer.text((10, 90), text6, (25, 25, 112))
    img.save("%d.png" % index)
    index = int(str(index)+"1")
    
    text5="a: "+ str(Adisision[i])
    text6="b: "+ str(Bdisision[i])
    color = (230, 230, 250)
    img = Image.new('RGB', (200, 150), color) 
    imgDrawer = ImageDraw.Draw(img) 
    imgDrawer.text((10, 10), text1, (25, 25, 112))
    imgDrawer.text((10, 30), text2, (25, 25, 112))
    imgDrawer.text((10, 70), text4, (25, 25, 112))
    imgDrawer.text((10, 90), text6, (25, 25, 112))
    imgDrawer.text((10, 110), text5, (25, 25, 112))
    img.save("%d.png" % index)
    index = int(str(index)+"1")


path = 'C:/Users/позитроника/Desktop/images/ultra/'
image_folder = os.fsencode(path)
filenames = []

for file in os.listdir(image_folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.jpeg', '.png') ):
        filenames.append(filename)

filenames.sort()

images = list(map(lambda filename: imageio.imread(path+filename), filenames))

imageio.mimsave(os.path.join(path+'gif_for_ultra.gif'), images, duration = 0.7)


