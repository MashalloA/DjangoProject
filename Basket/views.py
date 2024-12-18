from django.shortcuts import render,redirect,get_object_or_404
from Basket.models import BasketModel
from Basket.forms import BasketForm
from django.views import generic

#creat
class CreateBasketView(generic.CreateView):
    template_name = 'basket/create_basket.html'
    form_class = BasketForm
    success_url = '/basket_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBasketView, self).form_valid(form)

# def creat_basket_view(request):
#     if request.method == 'POST':
#         form = BasketForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('BasketList')
#
#     else:
#         form = BasketForm()
#     return render(request, 'basket/create_basket.html', context={'form': form})


#read
class BasketListView(generic.ListView):
    template_name = 'basket/basket_list.html'
    context_object_name = 'basket_list'
    model = BasketModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

# def basket_list_view(request):
#     if request.method == 'GET':
#         basket_list = BasketModel.objects.all().order_by('-id')
#         context = {'basket_list': basket_list}
#         return render(request, template_name='basket/basket_list.html', context=context)


#detail
class BasketDetailView(generic.DetailView):
    template_name = 'basket/basket_detail.html'
    context_object_name = 'basket_id'

    def get_object(self, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(BasketModel, id=basket_id)

# def basket_detail_view(request, id):
#     if request.method == 'GET':
#         basket_id = get_object_or_404(BasketModel, id=id)
#         context = {'basket_id': basket_id}
#         return render(request, template_name='basket/basket_detail.html', context=context)

#update
class UpdateBasketView(generic.UpdateView):
    template_name = 'basket/update_basket.html'
    form_class = BasketForm
    success_url = '/basket_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateBasketView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(BasketModel, id=basket_id)

# def update_basket_view(request, id):
#     basket_id = get_object_or_404(BasketModel, id=id)
#     if request.method == 'POST':
#         form = BasketForm(request.POST, instance=basket_id)
#         if form.is_valid():
#             form.save()
#             return redirect('BasketList')
#
#     else:
#         form = BasketForm(instance=basket_id)
#     return render(request, template_name='basket/update_basket.html',
#                   context={'basket_id': basket_id, 'form': form})

#delet
class DeleteBasketView(generic.DeleteView):
    template_name = 'basket/delete_basket.html'
    success_url = '/basket_list/'

    def get_object(self, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(BasketModel, id=basket_id)

# def delete_basket_view(request, id):
#     basket_id = get_object_or_404(BasketModel, id=id)
#     basket_id.delete()
#     return redirect('BasketList')

class ListOfOrdersView(generic.ListView):
    template_name = 'basket/List_of_orders.html'
    context_object_name = 'list_of_orders'
    model = BasketModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

# def list_of_orders_view(request):
#     if request.method == 'GET':
#         list_of_orders = BasketModel.objects.all().order_by('-id')
#         context = {'list_of_orders': list_of_orders}
#         return render(request, template_name='basket/List_of_orders.html', context=context)