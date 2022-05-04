from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from datetime import datetime
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.serializers import ProductSerializer

# Create your views here.

from . models import Product
# from . forms import ProductForm
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/Product-list/',
		'Detail View':'/Product-detail/<str:pk>/',
		'Create':'/Product-create/',
		'Update':'/Product-update/<str:pk>/',
		'Delete':'/Product-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = Product.objects.all().order_by('-id')
	serializer = ProductSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Product.objects.get(id=pk)
	serializer = ProductSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = ProductSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Product.objects.get(id=pk)
	serializer = ProductSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Product.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')




# def ShowAllProducts(request):
    
#     category = request.GET.get('category')

#     if category == None:
#         products = Product.objects.order_by('-price').filter(is_published=True)
#         page_num = request.GET.get("page")
#         # paginator = Paginator(products, 2)
#         # try:
#         #     products = paginator.page(page_num)
#         # except PageNotAnInteger:
#         #     products = paginator.page(1)
#         # except EmptyPage:
#         #     products = paginator.page(paginator.num_pages)             
#     else:
#         products = Product.objects.filter(category__name=category)
       
    
#     categories = Category.objects.all()
    
#     context = {
#         'products': products,
#         'categories': categories
#     }

#     return render(request, 'showProducts.html', context)




# def productDetail(request, pk):
#     eachProduct = Product.objects.get(id=pk)

#     num_comments = Comment.objects.filter(product=eachProduct).count()

#     context = {
#         'eachProduct': eachProduct,
#         'num_comments': num_comments,
#     }

#     return render(request, 'productDetail.html', context)




# def addProduct(request):
#     form = ProductForm()

#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('showProducts')
#     else:
#         form = ProductForm()

#     context = {
#         "form":form
#     }

#     return render(request, 'addProduct.html', context)



# def updateProduct(request,pk):
#     product = Product.objects.get(id=pk)

#     form = ProductForm(instance=product)

#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('showProducts')

#     context = {
#         "form":form
#     }

#     return render(request, 'updateProduct.html', context)




# def deleteProduct(request, pk):
#     product = Product.objects.get(id=pk)
#     product.delete()
#     return redirect('showProducts')




# def searchBar(request):
#     if request.method == 'GET':
#         query = request.GET.get('query')
#         if query:
#             products = Product.objects.filter(price__icontains=query) 
#             return render(request, 'searchbar.html', {'products':products})
#         else:
#             print("No information to show")
#             return render(request, 'searchbar.html', {})


# def add_comment(request, pk):
#     eachProduct = Product.objects.get(id=pk)

#     form = CommentForm(instance=eachProduct)

#     if request.method == 'POST':
#         form = CommentForm(request.POST, instance=eachProduct)
#         if form.is_valid():
#             name = request.user.username
#             body = form.cleaned_data['comment_body']
#             c = Comment(product=eachProduct, commenter_name=name, comment_body=body, date_added=datetime.now())
#             c.save()
#             return redirect('showProducts')
#         else:
#             print('form is invalid')    
#     else:
#         form = CommentForm()    


#     context = {
#         'form': form
#     }

#     return render(request, 'add_comment.html', context)


# def delete_comment(request, pk):
#     comment = Comment.objects.filter(product=pk).last()
#     product_id = comment.product.id
#     comment.delete()
#     return redirect(reverse('product', args=[product_id]))