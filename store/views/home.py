from calendar import error
from itertools import product
from urllib import request
from django.shortcuts import render , redirect
from store.model.Product import Product
from store.model.category import Category
from django.views import View


class Index(View):

    def post(self, request ):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        print(product)
        return redirect('homepage')



    def get(self, request):
        prds = None
        category=Category.get_all_categories()
        categoryid = request.GET.get( 'category')
        if categoryid:
            products=Product.get_all_products_by_categoryid(categoryid)
        else:
            products=Product.get_all_products()
        data = {'products': products, 'category': category}
        return render(request,'index.html' ,data)






