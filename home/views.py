from django.views import generic
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import View, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import UserForm
from .models import Product, Cart


class UserRegistration(View):
    form_class = UserForm
    template_name = 'home/registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home:homepage')
        return render(request, self.template_name, {'form': form})

class UserLogin(View):
    form_class = UserForm
    template_name = 'home/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request,self.template_name, {'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home:homepage')
        form = self.form_class(None)
        return render(request,self.template_name, {'form': form})

class HomepageView(generic.ListView):
    template_name = "home/Homepage.html"
    context_object_name = "all_products" # By default it is object_list
   
    def get_queryset(self):
        return Product.objects.all().order_by('genre')

class ProductCreate(CreateView):
    model = Product
    fields = ['title', 'description', 'genre', 'price', 'review_stars', 'sample_picture1',
              'sample_picture2', 'sample_picture3']

class ProductDetails(DetailView):
    model = Product
    template_name = 'home/Product_Details.html'
    # The name of the object used in the html will be product

def CartView(request):

    if request.user.is_authenticated:
        username = request.user.username
        cart_objects = Cart.objects.filter(Cart_owner = request.user)
        return render(request, "home/Cart_details.html", {'cart_objects': cart_objects, 'username': username})
    else:
        return redirect('home:login')

def AddToCart(request):
    if request.user.is_authenticated:
        existing_cart = Cart.objects.filter(Q(Cart_owner = request.user) & 
                                            Q(Cart_content = request.POST["product_id"]))
        if existing_cart:
            existing_cart[0].Number_of_products = existing_cart[0].Number_of_products + 1
            existing_cart[0].save()
        else:
            new_cart = Cart()
            new_cart.Cart_owner = request.user
            new_cart.Cart_content = get_object_or_404(Product, id = request.POST["product_id"])
            new_cart.save()
        return redirect('home:Cart_details')
    else:
        return redirect('home:login')

class RemoveFromCart(DeleteView):
    model = Cart
    success_url = reverse_lazy('home:Cart_details')

def UserLogout(request):
    logout(request)
    form = UserForm(None)
    return redirect('home:login')

def SearchView(request):
    query = request.GET.get('q')
    query_splitted = query.split()
    search_querry = '-'.join(query_splitted)
    if query:
        searched_product = Product.objects.filter(Q(title__icontains = query) | 
                                                  Q(description__icontains = query))
        if searched_product:
            return render(request, 'home/search_details.html', {'searched_product': searched_product})
        else:
            for query in query_splitted:
                searched_product = Product.objects.filter(Q(title__icontains = query) | 
                                                          Q(description__icontains = query))
                if searched_product:
                    return render(request, 'home/search_details.html', {'searched_product': searched_product})

def filter(request):
    if request.method == "GET":
        return render(request,'home/filter_form.html')
    else:
        try:
            max_price = int(request.POST.get('max_price'))
            min_price = int(request.POST.get('min_price'))
            category = request.POST.get('category')
        except:
            return render(request,'home/filter_form.html')
        else:   
            
            if max_price is None or min_price is None or category is None:
                return render(request, 'home/filter_form.html')
            else:
                searched_category = Product.objects.filter(genre__icontains = category)
                if not searched_category:
                    splitted_category = category.split()
                    for words in splitted_category:
                        searched_category = Product.objects.filter(genre__icontains = words)
                        if searched_category:
                            break
                    
                searched_product = []
                for product in searched_category:
                    if product.price >= min_price and product.price <= max_price:
                        searched_product.append(product)
                return render(request, 'home/search_details.html', {'searched_product': searched_product})



