from django.shortcuts import render
from django.views.generic import TemplateView,ListView
# Create your views here.
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import PhotoPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import PhotoPost
class  IndexView(ListView):
    template_name='index.html'
    queryset  = PhotoPost.objects.order_by('-posted_at')
    pagination_by = 9

@method_decorator(login_required,name='dispatch')
class CreatePhotoView(CreateView):
    form_class = PhotoPostForm
    template_name = 'post_photo.html'
    success_url = reverse_lazy('photo:post_done')

    def form_valid(self,form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)
    

class PostSuccessView(TemplateView):
    template_name = 'post_success.html'

class CategoryView(ListView):
    template_name = 'index.html'
    paginate_by = 9

    def get_queryset(self):
        category_id = self.kwargs['category']
        categories=PhotoPost.objects.filter(category=category_id).order_by('-posted_at')
        return categories
