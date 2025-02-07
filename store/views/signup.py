from calendar import error
from itertools import product
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.template.defaultfilters import first
from store.model.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validations
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)

            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None;
        if (not customer.first_name):
            error_message = "First Name required"
        elif len(customer.first_name) < 4:
            error_message = "First name must be 4 or more characters"
        elif (not customer.last_name):
            error_message = "Last Name required"
        elif len(customer.last_name) < 4:
            error_message = "First name must be 4 or more characters"
        elif (not customer.phone):
            error_message = "Phone required"
        elif len(customer.phone) < 10:
            error_message = "Phone number must be 10 no. long"
        elif (not customer.password):
            error_message = "password mush be required"
        elif len(customer.password) < 6:
            error_message = "password must be 6 char long"
        elif (not customer.email):
            error_message = "email is required"
        elif customer.isExists():
            error_message = 'Email address already exit'

        # saving
        return error_message
