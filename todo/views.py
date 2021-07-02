from django.shortcuts import render, redirect, loader, HttpResponse
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from django.core.paginator import Paginator, Page, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse, request
from django.urls import reverse
from .forms import TodoingForm, RawTodoForm
from .models import Todoing
import itertools
from datetime import datetime, date

# Create your views here.
def home_view(request):
    print(request.user)
    my_form = RawTodoForm()
    if request.method == "POST":
        my_form = RawTodoForm(request.POST)
        if my_form.is_valid():
            # now the data is good
            print(my_form.cleaned_data)
            Todoing.objects.create(**my_form.cleaned_data)
            my_form = RawTodoForm()
        else:
            print(my_form.errors)
    context = {
        'form': my_form
    }
    return render(request, 'home.html', context)

def saved_view(request):
    my_form = Todoing.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(my_form, 5)
    try:
        todolist = paginator.page(page)
    except PageNotAnInteger:
        todolist = paginator.page(1)
    except EmptyPage:
        todolist = paginator.page(paginator.num_pages)

    return render(request, "saved_view.html", {'todolist': todolist})


# class SearchResults(ListView):
#     model = Todoing
#     template_name = 'search_results.html'
#     context_object_name = 'todo'
#     paginate_by = 5
#
#     def get_queryset(self):
#         query = self.request.GET.get('t')
#         object_list = Todoing.objects.filter(Q(subject__icontains=query) | Q(task__icontains=query) | Q(date__icontains=query))
#         return object_list


class SearchResults(ListView):
    model = Todoing
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('t')
        object_list = Todoing.objects.filter(Q(subject__icontains=query) | Q(task__icontains=query) | Q(date__icontains=query))
        return object_list

    # my_form = object_list.all()
    # page = request.GET.get('page', 1)
    #
    # paginator = Paginator(my_form, 5)
    # try:
    #     todolist = paginator.page(page)
    # except PageNotAnInteger:
    #     todolist = paginator.page(1)
    # except EmptyPage:
    #     todolist = paginator.page(paginator.num_pages)
    # return render(request, "search_results.html", {'todolist': todolist})


class Leo(ListView):
    model = Todoing
    template_name = 'search_date.html'

    def get_queryset(self):
        query = self.request.GET.get('v')
        object_list = Todoing.objects.filter(Q(subject__icontains=query) | Q(task__icontains=query) | Q(date__icontains=query))
        return object_list

class SearchResultsView(ListView):
    model = Todoing
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Todoing.objects.filter(Q(subject__icontains=query) | Q(task__icontains=query) | Q(date__icontains=query))
        return object_list

def destroy(request, id):
    records = Todoing.objects.get(id=id)
    records.delete()
    return redirect("/saved")

def edit(request, id):
    records = Todoing.objects.get(id=id)
    return render(request, "edit.html",{'todo':records})

def update(request, id):
    records = Todoing.objects.get(id=id)
    form = TodoingForm(request.POST, instance = records)
    if form.is_valid():
        form.save()
        return redirect("/saved")
    else:
        print(form.errors)
    return render(request, "edit.html",{'todo':records})
