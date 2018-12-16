from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.core.mail import send_mail
from .models import *
import numpy as np
from django.template.loader import get_template 
from PIL import Image
from PIL import ImageDraw
import imageio
import os
import copy

def hello(request):
	return render(request, 'sort/hello.html')
	
def mainpage(request):
	return render(request, 'sort/mainpage1.html')

def mainpage2(request):
	return render(request, 'sort/mainpage2.html')

def sendEmail(request):
	
	email = request.POST['email']

	start_list=request.POST['start_list']

	end_list=request.POST['end_list']

	sort_name = request.POST['sort_name']
	
	template = get_template('sort/email.html').render({'start_list': start_list,'end_list': end_list, 'sort_name': sort_name, 'full_path': request.get_host()})

	send_mail('Notification!', 'да', "Darina", [email] , fail_silently=False, html_message=template)

	return render(request, 'sort/mainpage2.html', {'end_list': end_list, 'sort_name': sort_name, 'start_list': eval(start_list)})
	
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
	lst = list(np.random.randint(-100, 100, 5))
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
	lst1 = list(np.random.randint(-100, 100, 5))
	lst2 = list(np.random.randint(-100, 100, 5))
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
	if len(lst)>1:
		lst2=eval(str(lst[len(lst)-2]))
	else:
		lst2=list(np.random.randint(-100, 100, 5))
	s=[lst1,lst2]
	c=doubleTrack(lst1,lst2)
	doubleTrackAnimation(lst1,lst2)
	return render(request, 'sort/mainpage2.html', {'end_list': c, 'sort_name': name, 'start_list': s})

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
	if len(lst)>1:
		lst2=eval(str(lst[len(lst)-2]))
	else:
		lst2=list(np.random.randint(-100, 100, 5))
	s=[lst1,lst2]
	c=abstract(lst1,lst2)
	abstractAnimation(lst1,lst2)
	return render(request, 'sort/mainpage2.html', {'end_list': c, 'sort_name': name, 'start_list': s})

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
	s=[lst]
	c=nish(lst)
	nishAnimation(lst)
	return render(request, 'sort/mainpage2.html', {'end_list': c, 'sort_name': name, 'start_list': s})

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
	s=[lst]
	c=vosh(copy.copy(lst))
	voshAnimation(copy.copy(lst))
	return render(request, 'sort/mainpage2.html', {'end_list': c, 'sort_name': name, 'start_list': s})

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
	s=[lst]
	c=ultrasort(lst)
	ultrasortAnimation(lst)
	return render(request, 'sort/mainpage2.html', {'end_list': c, 'sort_name': name, 'start_list': s})

def doubleTrackChanged1 (lst1,lst2):
	Achange=[]
	Bchange=[]
	Cchange=[[]]
	counter=[]
	def doubleTrackChanged (lst1,lst2):
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
	doubleTrackChanged (lst1,lst2)
	lst=[Achange, Bchange, Cchange,counter]
	return lst

def doubleTrackAnimation (lst1,lst2):
	fu=doubleTrackChanged1(lst1,lst2)
	Achange=fu[0]
	Bchange=fu[1]
	Cchange=fu[2]
	count=fu[3]
	print(Achange)
	print(Bchange)
	print(Cchange)
	print(count)
	if len(Achange)<len(Bchange):
		Achange.append([])
	if len(Bchange)<len(Achange):
		Bchange.append([])
	i=0
	j=0
	k=0
	index=1
	text1="Source data:"
	text4="Result: "
	color = (230, 230, 250)
	while k<len(Cchange):
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
		img.save("C:/Users/позитроника/Desktop/images/doubleTrack1/%d.png" % index)
		index = int(str(index)+"1")
		draw = ImageDraw.Draw(img)
		if k<len(count):
			count1=count[k]
			if count1==0:
				draw.ellipse([(10, 28), (30, 50)],fill=None, outline=128,width=2)
			else:
				draw.ellipse([(10, 46), (30, 70)],fill=None, outline=128,width=2)
			img.save("C:/Users/позитроника/Desktop/images/doubleTrack1/%d.png" % index)
			index= int(str(index)+"1")
		i=i+(1-count1)
		j=j+count1
		k=k+1
	path = 'C:/Users/позитроника/Desktop/images/doubleTrack1/'
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

def abstractChanged1(lst1,lst2):
	AUXchange=[]
	Cchange=[]
	counter=[]
	def abstractChanged (lst1,lst2):
		lst1=sorted(lst1)
		lst2=sorted(lst2)
		lst2.reverse()
		c=[]
		aux=lst1
		for i in lst2:
			aux.append(i)
		AUXchange.append(copy.copy(aux))
		while aux!=[]:
			i=0
			j=len(aux)-1
			if aux[i]<=aux[j]:
				c.append(aux[i])
				del aux[i]
				AUXchange.append(copy.copy(aux))
				Cchange.append(copy.copy(c))
				counter.append(0)
			else:
				c.append(aux[j])
				del aux[j]
				AUXchange.append(copy.copy(aux))
				Cchange.append(copy.copy(c))
				counter.append(1)
		return c
	abstractChanged (lst1,lst2)
	lst=[AUXchange, Cchange, counter]
	return lst

def abstractAnimation(lst1,lst2):
	fu=abstractChanged1(lst1,lst2)
	aux=fu[0]
	c=fu[1]
	count=fu[2]
	index=1
	text1="Source data:"
	text4="Result: "
	text2=str(lst1)
	text3=str(lst2)
	lst=[str([]),str(lst1), str(aux[0])]
	for text5 in lst:
	    color = (230, 230, 250)
	    img = Image.new('RGB', (300, 150), color) 
	    imgDrawer = ImageDraw.Draw(img) 
	    imgDrawer.text((10, 10), text1, (25, 25, 112))
	    imgDrawer.text((10, 30), text2, (25, 25, 112))
	    imgDrawer.text((10, 50), text3, (25, 25, 112))
	    imgDrawer.text((10, 70), text4, (25, 25, 112))
	    imgDrawer.text((10, 90), text5, (25, 25, 112))
	    img.save("C:/Users/позитроника/Desktop/images/abstract1/%d.png" % index)
	    index = int(str(index)+"1")
	i=0
	k=0
	while k<len(c):
	    text2=str(aux[i])
	    text5=str(c[k])
	    color = (230, 230, 250)
	    img = Image.new('RGB', (300, 150), color) 
	    imgDrawer = ImageDraw.Draw(img) 
	    imgDrawer.text((10, 10), text1, (25, 25, 112))
	    imgDrawer.text((10, 30), text2, (25, 25, 112))
	    imgDrawer.text((10, 70), text4, (25, 25, 112))
	    imgDrawer.text((10, 90), text5, (25, 25, 112))
	    img.save("C:/Users/позитроника/Desktop/images/abstract1/%d.png" % index)
	    index = int(str(index)+"1")
	    draw = ImageDraw.Draw(img)
	    if k<len(count):
	        count1=count[k]
	        if count1==0:
	            draw.ellipse([(10, 28), (30, 50)],fill=None, outline=128,width=2)
	        else:
	            f=len(aux[i])*16+1
	            draw.ellipse([(f, 28), (f+20, 50)],fill=None, outline=128,width=2)
	        img.save("C:/Users/позитроника/Desktop/images/abstract1/%d.png" % index)
	        index= int(str(index)+"1") 
	    i=i+1
	    k=k+1  
	path = 'C:/Users/позитроника/Desktop/images/abstract1/'
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

def nishChanged1(lst):
	Cchange=[lst]
	def nishChanged (lst):
		c=[]
		if len(lst)>1:
			n=(len(lst)+1)//2
			lst1=lst[0:n]
			lst2=lst[n:]
			nishChanged(lst1)
			nishChanged(lst2)
			c=abstract(lst1,lst2)
			Cchange.append(copy.copy(c))
		else:
			return
		return c
	nishChanged (lst)
	lst=Cchange
	return lst

def nishAnimation (lst):
	Cchange=nishChanged1(lst)
	index=1
	text1="Source data:"
	text2=str(lst)
	text4="Result: "
	for text in Cchange:
	    text5=str(text)
	    color = (230, 230, 250)
	    img = Image.new('RGB', (200, 150), color) 
	    imgDrawer = ImageDraw.Draw(img) 
	    imgDrawer.text((10, 10), text1, (25, 25, 112))
	    imgDrawer.text((10, 30), text2, (25, 25, 112))
	    imgDrawer.text((10, 70), text4, (25, 25, 112))
	    imgDrawer.text((10, 90), text5, (25, 25, 112))
	    img.save("C:/Users/позитроника/Desktop/images/nish1/%d.png" % index)
	    index = int(str(index)+"1")
	path = 'C:/Users/позитроника/Desktop/images/nish1/'
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

def voshChanged1(lst):
	Cchange=[[copy.copy(lst)]]
	def voshChanged(lst):
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
	        Cchange.append(copy.copy(c))
	        c=vosh(c)
	    else:
	       return lst[0]
	    return c
	voshChanged(lst)
	lst=Cchange
	return lst

def voshAnimation (lst):
	Cchange=voshChanged1(copy.copy(lst))
	index=1
	text1="Source data:"
	text2=str(lst)
	print(lst)
	text4="Result: "
	for text in Cchange:
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
	    img.save("C:/Users/позитроника/Desktop/images/vosh1/%d.png" % index)
	    index = int(str(index)+"1")
	path = 'C:/Users/позитроника/Desktop/images/vosh1/'
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


def ultrasortChanged1(a):
	Achange=[]
	Bchange=[]
	def ultrasortChanged(a):
		b=[]
		n=len(a)
		if n<=1:
			return a
		else:
			b.append(ultrasortChanged(a[0:n//2]))
			b.append(ultrasortChanged(a[n//2:]))
			Bchange.append(str(copy.copy(b[0]))+","+ str(copy.copy(b[1])))
			c=doubleTrack(b[0],b[1])
			Achange.append(copy.copy(c))
		return c
	ultrasortChanged(a)
	lst=[Achange, Bchange]
	return lst

def ultrasortAnimation (lst):
	fu=ultrasortChanged1(lst)
	Achange=fu[0]
	Bchange=fu[1]
	index=1
	text1="Source data:"
	text2=str(lst)
	text4="Result: "

	for i in list(range(len(Achange))):
	    text5="a: "+ str(Achange[i])
	    text6="b: "+ str(Bchange[i])
	    color = (230, 230, 250)
	    img = Image.new('RGB', (200, 150), color) 
	    imgDrawer = ImageDraw.Draw(img) 
	    imgDrawer.text((10, 10), text1, (25, 25, 112))
	    imgDrawer.text((10, 30), text2, (25, 25, 112))
	    imgDrawer.text((10, 70), text4, (25, 25, 112))
	    imgDrawer.text((10, 90), text6, (25, 25, 112))
	    img.save("C:/Users/позитроника/Desktop/images/ultra1/%d.png" % index)
	    index = int(str(index)+"1")
	    
	    text5="a: "+ str(Achange[i])
	    text6="b: "+ str(Bchange[i])
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

