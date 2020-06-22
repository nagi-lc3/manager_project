from django.views.generic import ListView

from .models import *  # noqa


class WorkerListView(ListView):
    model = Worker  # noqa
    template_name = 'worker_list.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        workers = Worker.objects.all()  # noqa
        context['workers'] = workers

        return context


index = WorkerListView.as_view()
