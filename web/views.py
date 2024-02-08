from django.contrib.auth.decorators import login_required
from django.shortcuts import *
from web.forms import *
from django.contrib.auth import *

User = get_user_model()


def main_view(request):
    posts = Post.objects.prefetch_related()
    return render(request, 'web/main.html', {
        'posts': posts
    })


def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            is_success = True
    return render(request, 'web/registration.html', {
        'form': form,
        'is_success': is_success
    })


def auth_view(request):
    form = AuthForm()
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, 'Неверный логин или пароль')
            else:
                login(request, user)
                return redirect('main')
    return render(request, 'web/auth.html', {
        'form': form
    })


@login_required()
def logout_view(request):
    logout(request)
    return redirect('main')


def blog_view(request):
    posts = Post.objects.prefetch_related().filter(user=request.user)
    return render(request, 'web/blog.html', {
        'posts': posts
    })


def post_view(request, id=None):
    post = get_object_or_404(Post, id=id)
    is_author = post.user == request.user
    return render(request, 'web/post.html', {
        'post': post, 'is_author': is_author
    })


@login_required
def create_post_view(request):
    form = PostForm()
    cars = Car.objects.select_related().filter(owner=request.user)
    if request.method == 'POST':
        car = Car(id=request.POST['car'])
        form = PostForm(data=request.POST, initial={'user': request.user, 'car': car})
        if form.is_valid():
            form.save()
            return redirect('blog')
    return render(request, 'web/createPost.html', {
        'form': form, 'cars': cars
    })


@login_required
def edit_post_view(request, id=None):
    post = Post.objects.get(id=id)
    form = PostForm(instance=post)
    cars = Car.objects.select_related().filter(owner=request.user)
    selected_car = post.car
    if request.method == 'POST':
        car = Car(id=request.POST['car'])
        form = PostForm(data=request.POST, instance=post, initial={'user': request.user, 'car': car})
        if form.is_valid():
            form.save()
            return redirect('blog')
    return render(request, 'web/editPost.html', {
        'form': form, 'cars': cars, 'selected_car': selected_car
    })


@login_required
def delete_post_view(request, id=None):
    post = get_object_or_404(Post, user=request.user, id=id)
    post.delete()
    return redirect('blog')


def cars_view(request):
    cars = Car.objects.select_related().filter(owner=request.user)
    return render(request, 'web/cars.html', {
        'cars': cars
    })


def car_view(request, id=None):
    car = get_object_or_404(Car, id=id)
    is_owner = car.owner == request.user
    return render(request, 'web/car.html', {
        'car': car, 'is_owner': is_owner
    })


@login_required
def add_car_view(request):
    form = CarForm()
    if request.method == 'POST':
        form = CarForm(data=request.POST, files=request.FILES, initial={'user': request.user})
        if form.is_valid():
            form.save()
            return redirect('cars')
    return render(request, 'web/addCar.html', {
        'form': form
    })


@login_required
def edit_car_view(request, id=None):
    car = Car.objects.select_related().get(id=id)
    form = CarForm(instance=car)
    if request.method == 'POST' and car.owner == request.user:
        form = CarForm(data=request.POST, files=request.FILES, instance=car, initial={'user': request.user})
        if form.is_valid():
            form.save()
            return redirect('cars')
    return render(request, 'web/editCar.html', {
        'form': form
    })


@login_required
def delete_car_view(request, id=None):
    car = get_object_or_404(Car, owner=request.user, id=id)
    car.delete()
    return redirect('cars')
