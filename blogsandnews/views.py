from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login

def index(request):

    user = request.user
    if user.is_superuser:
        return redirect("/admin")
            
    if user.is_authenticated:
        return redirect("/user/home")

    return render(request, 'nonlogin/index.html', {})

@never_cache
def user_login(request):
    if request.method == "GET":
        user = request.user
        if user.is_superuser:
            return redirect("/admin")
        
        if user.is_authenticated:
            return redirect("/user/home")

        return render(request, 'nonlogin/user_login.html', {})

    elif request.method == "POST":
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)  
            return redirect("/user/home")
        else:
            return render(request, 'nonlogin/user_login.html', {'error_message': True})


@never_cache
def admin_login(request):
    if request.method == "GET":
        user = request.user
        if user.is_superuser:
            return redirect("/admin")
        
        if user.is_authenticated:
            return redirect("/user/home")

        return render(request, 'nonlogin/admin_login.html', {})

    elif request.method == "POST":
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            return redirect("/user/home")
        else:
            return render(request, 'nonlogin/admin_login.html', {'error_message': True})


# import requests

    # url = "https://newsapi.org/v2/everything?q=apple&from=2023-11-06&to=2023-11-06&sortBy=popularity&apiKey=74923f7f3cf044dabea89d371ccd5f84"

    # data = requests.get(url).json()
    # articles = data['articles']

    # blogs = []
    # for article in articles:
    #     blog = {
    #         'author': article['author'],
    #         'title': article['title'],
    #         'image': article['urlToImage'],
    #         'description': article['description']
    #     }
    #     blogs.append(blog)

    # return render(request, 'index.html', {"blogs": blogs[0:50]})

    # <div class="container">
    #     <div class="row">
    #         {% for blog in blogs %}
    #             <div class="col-10 offset-1 mt-5">
    #                 <div class="card">
    #                     <div class="card-title mt-2">
    #                         <h3 style="font-family: 'Times New Roman', Times, serif;">{{ blog.title }}</h3> 
    #                     </div>
    #                     <div class="card-img">
    #                         <img src="{{ blog.image }}" class="img-fluid" alt="Blog Image">
    #                     </div>
    #                     <div class="card-body text-muted">
    #                         <p>{{ blog.description}} </p>
    #                     </div>
    #                     <div class="card-footer text-end">
    #                         {{ blog.author }}
    #                     </div>
    #                 </div>
    #             </div>
    #         {% endfor %}
    #     </div>
    # </div>

