from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.core.mail import send_mail
from .models import *
import numpy as np

def hello(request):
	return render(request, 'sort/hello.html')
	
def mainpage(request):
	return render(request, 'sort/mainpage1.html')



def add_list_end(lst):
	c=Lists(lists=str(lst))
	c.save()

def add_funcs(func):
	funcs=func
	count=funcs.find(",")
	func1=funcs[0:count]
	func2=funcs[count+1:]
	c=eval('[' + func1 +' for x in range(' + func2 + ')]')
	return c

def add_list(request):
	a=str(request.POST['list'])
	lst=modern_list(a)
	add_list_end(lst)
	return HttpResponseRedirect(reverse('sort:mainpage'))

def modern_list(a):
	b=list(map(lambda it: int(it),a.split(',')))
	return b

def add_list_func(request):
	c=add_funcs(request.POST['func'])
	add_list_end(c)
	return HttpResponseRedirect(reverse('sort:mainpage'))

def add_list_random(request):
	lst = list(np.random.randint(-100, 100, 20))
	add_list_end(lst)
	return HttpResponseRedirect(reverse('sort:mainpage'))

def add_lists(request):
	lst=str(request.POST['list1'])
	lst=modern_list(lst)
	add_list_end(lst)
	lst=str(request.POST['list2'])
	lst=modern_list(lst)
	add_list_end(lst)
	return HttpResponseRedirect(reverse('sort:mainpage'))

def add_lists_func(request):
	c=add_funcs(request.POST['func1'])
	add_list_end(c)
	c=add_funcs(request.POST['func2'])
	add_list_end(c)
	return HttpResponseRedirect(reverse('sort:mainpage'))

def add_lists_random(request):
	lst1 = list(np.random.randint(-100, 100, 20))
	lst2 = list(np.random.randint(-100, 100, 20))
	add_list_end(lst1)
	add_list_end(lst2)
	return HttpResponseRedirect(reverse('sort:mainpage'))

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

def doubleTrackShow (request):
	name='Двухпутевое слияние'
	lst=Lists.objects.all()
	lst1=eval(str(lst[len(lst)-1]))
	lst2=eval(str(lst[len(lst)-2]))
	c=doubleTrack(lst1,lst2)
	return render(request, 'sort/mainpage2.html', {'end_list': c, 'sort_name': name})

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

def abstractShow (request):
	name='Абстрактное обменное слияние'
	lst=Lists.objects.all()
	lst1=eval(str(lst[len(lst)-1]))
	lst2=eval(str(lst[len(lst)-2]))
	c=abstract(lst1,lst2)
	return render(request, 'sort/mainpage2.html', {'end_list': c, 'sort_name': name})

def nish (lst):
	c=[]
	if len(lst)>1:
		n=(len(lst)+1)//2
		lst1=lst[0:n]
		lst2=lst[n:]
		nish(lst1)
		nish(lst2)
		c=abstract(lst1,lst2)
	else:
		return
	return c

def nishShow (request):
	name='Нисходящая сортировка слиянием'
	lstt=Lists.objects.all()
	lst=eval(str(lstt[len(lstt)-1]))
	c=nish(lst)
	return render(request, 'sort/mainpage2.html', {'end_list': c, 'sort_name': name})


def vosh(lst):
    c=[]
    n=len(lst)
    if n>1:
        for i in list(range(0, n)):
            if type(lst[i]) == int:
                lst[i]=[lst[i]]
        for i in list(range(0, n-1, 2)):
            c.append(abstract(lst[i],lst[i+1]))
        if n%2 == 1:
            c.append(lst[-1])
        c=vosh(c)
    else:
       return lst[0]
    return c

def voshShow (request):
	name='Восходящая сортировка слиянием'
	lstt=Lists.objects.all()
	lst=eval(str(lstt[len(lstt)-1]))
	c=vosh(lst)
	return render(request, 'sort/mainpage2.html', {'end_list': c, 'sort_name': name})

def ultrasort(lst1):
    lst2=[]
    n=len(lst1)
    if n<=1:
        return lst1
    else:
        lst2.append(ultrasort(lst1[0:n//2]))
        lst2.append(ultrasort(lst1[n//2:]))
        c=doubleTrack(lst2[0],lst2[1])
    return c

def ultrasortShow (request):
	name='Усовершенствованный базовый алгоритм'
	lstt=Lists.objects.all()
	lst=eval(str(lstt[len(lstt)-1]))
	c=ultrasort(lst)
	ultrasortAnimation(lst)
	return render(request, 'sort/mainpage2.html', {'end_list': c, 'sort_name': name })




from PIL import Image
from PIL import ImageDraw
import imageio
import os
import copy

def ultrasortChanged1(a):
	Adisision=[]
	Bdisision=[]
	def ultrasortChanged(a):
		b=[]
		n=len(a)
		if n<=1:
			return a
		else:
			b.append(ultrasortChanged(a[0:n//2]))
			b.append(ultrasortChanged(a[n//2:]))
			Bdisision.append(str(copy.copy(b[0]))+","+ str(copy.copy(b[1])))
			c=doubleTrack(b[0],b[1])
			Adisision.append(copy.copy(c))
		return c
	ultrasortChanged(a)
	lst=[Adisision, Bdisision]
	return lst

def ultrasortAnimation (lst):
	fu=ultrasortChanged1(lst)
	Adisision=fu[0]
	Bdisision=fu[1]
	print("сделано")
	print(Adisision,Bdisision)
	index=1
	text1="Source data:"
	text2=str(lst)
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
	    img.save("C:/Users/позитроника/Desktop/images/ultra1/%d.png" % index)
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
	    img.save("C:/Users/позитроника/Desktop/images/ultra1/%d.png" % index)
	    index = int(str(index)+"1")
	path = 'C:/Users/позитроника/Desktop/images/ultra1/'
	image_folder = os.fsencode(path)
	filenames = []

	for file in os.listdir(image_folder):
	    filename = os.fsdecode(file)
	    if filename.endswith( ('.jpeg', '.png') ):
	        filenames.append(filename)

	filenames.sort()

	images = list(map(lambda filename: imageio.imread(path+filename), filenames))
	path1='img1/1.gif'

	imageio.mimsave(os.path.join('C:/Users/позитроника/Desktop/MyKurs/sort/static/'+path1), images, duration = 0.7)
	return 

