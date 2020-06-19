from bootstrap_datepicker_plus import DatePickerInput
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from birthday_manager.models import Person


class Index(generic.ListView):
    template_name = "index.html"
    context_object_name = 'contacts_list'

    def get_queryset(self):
        month = timezone.now().month
        day = timezone.now().day
        return Person.objects.filter(birthday__month=month, birthday__day=day)


class Contacts(generic.ListView):
    paginate_by = 7
    template_name = "contacts.html"
    context_object_name = "contacts_list"

    def get_queryset(self):
        return Person.objects.order_by("birthday")


# ADD CONTACT
# form
# Maybe import CreateView // Rename it. PersonCreate
class CreateView(generic.edit.CreateView):
    model = Person
    template_name = 'add.html'
    fields = ['name', 'birthday']

    def get_form(self, **kwargs):
        form = super().get_form()
        form.fields['birthday'].widget = DatePickerInput()
        return form

    def get_success_url(self):
        return reverse('success', kwargs={'pk': self.object.pk})


# success page
class SuccessAdding(generic.DetailView): # Django Messages
    model = Person
    template_name = 'success_adding.html'


# SEARCH
# form
# TODO: Instead of CreateView, inherit from FormView
class SearchView(generic.edit.CreateView):
    model = Person
    template_name = 'search.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('found', kwargs={'name': self.object.name})


# success page
class SuccessSearching(generic.ListView):
    model = Person
    template_name = 'success_searching.html'
    context_object_name = "contacts_list"

    def get_queryset(self):
        people = Person.objects.all()
        for name in self.request.GET.get('name', "").split():
            people = people.filter(name__icontains=name)
        return people
