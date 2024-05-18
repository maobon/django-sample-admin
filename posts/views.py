from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .form import CreatePost
from .models import Person


# Create your views here.
def posts_list(request):
    persons = Person.objects.all().order_by('-created_time')
    context = {
        'list': persons
    }
    return render(request, 'posts/posts_list.html', context)


# param 传递的参数名称要严格对应
def post_page(request, param):
    # use slug as key to get the person instance
    person = Person.objects.all().get(slug=param)

    context = {
        'person': person
    }
    return render(request, 'posts/post_page.html', context)


@login_required(login_url="/users/login/")
def post_new(request):
    if request.method == 'POST':
        new_form = CreatePost(request.POST, request.FILES)

        if new_form.is_valid():
            print("valid form. go ahead ...")
            # form.save() is wrong ... must not commit. to generate id
            # first step save not commit, because user id is null
            form_instance = new_form.save(commit=False)
            # manually set user get from request.user
            form_instance.author = request.user
            form_instance.save()
            print("form_instance saved ...")
            return redirect("posts:list")
        else:
            print("invalid form. sorry ...")

    else:
        new_form = CreatePost()
        print("this request is not POST request. create a blank form ...")

    return render(request, 'posts/post_new.html', {'form': new_form})
