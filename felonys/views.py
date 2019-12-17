from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from bootstrap_datepicker_plus import DatePickerInput

from .models import Felony
from prisoners.models import Prisoner

class FelonysListView(ListView):
    model = Felony
    ordering = ['prisoner', 'title']
    template_name = 'felonys/list.html'

    def dispatch(self, request, *args, **kwargs):
        """
        Overridden to ensure that the passed primary key does exist
        """
        self.prisoner = get_object_or_404(Prisoner, pk=kwargs['prisoner_pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        """
        Return only the felonies for the passed prisoner
        """
        return Felony.objects.filter(
            prisoner=self.prisoner).order_by('title')

class FelonysDetailView(DetailView):
    model = Felony
    template_name = 'felonys/detail.html'

class FelonysUpdateView(UpdateView):
    model = Felony
    fields = ('title', 'description', 'start_date', 'end_date', 'fine_charged')
    template_name = 'felonys/edit.html'

class FelonysCreateView(CreateView):
    model = Felony
    fields = ('prisoner', 'title', 'description', 'start_date', 'end_date', 'fine_charged')
    template_name = 'felonys/new.html'

    def dispatch(self, request, *args, **kwargs):
        """
        Overridden to ensure that the passed primary key does exist
        """
        self.prisoner = get_object_or_404(Prisoner, pk=kwargs['prisoner_pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view
        """
        initial = super(FelonysCreateView, self).get_initial()
        initial['prisoner'] = self.prisoner
        return initial

    def get_form(self):
        """
        Overridden to change the DateFields from text boxes to
        DatePicker widgets
        """
        form = super(FelonysCreateView, self).get_form()
        form.fields['start_date'].widget = DatePickerInput().start_of('duration')
        form.fields['end_date'].widget = DatePickerInput().end_of('duration')
        return form
