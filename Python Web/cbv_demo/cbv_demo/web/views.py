from django import views
from django.views import generic as views
from django.http import HttpResponse
from django.shortcuts import render

from cbv_demo.web.models import Employee


class IndexView(views.View):
    def get(self, request):
        context = {
            'title': 'Class Base View',
        }
        return render(request, 'index.html', context)


class IndexViewWithTemplate(views.TemplateView):
    template_name = 'index.html'
    extra_context = {
        'title': 'Template View',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        return context


class IndexViewWithListView(views.ListView):
    model = Employee
    template_name = 'index.html'
    context_object_name = 'employees'
    extra_context = {
        'title': 'List View',
    }

    def get_queryset(self):
        query_set = super().get_queryset()

        pattern = self.__get_pattern()

        if pattern:
            query_set = query_set.filter(first_name__icontains=pattern.lower())

        return query_set

    def __get_pattern(self):
        return self.request.GET.get('pattern', None)


class EmployeeDetailsView(views.DetailView):
    model = Employee
    template_name = 'employees/details.html'


class EmployeeCreateView(views.CreateView):
    model = Employee
    template_name = 'employees/create.html'
    fields = '__all__'
    success_url = '/'


class EmployeeUpdateView(views.UpdateView):
    model = Employee
    template_name = 'employees/create.html'
    fields = 'all'
