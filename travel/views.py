from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Travel
# Create your views here.

def myView(request):
    all_travel_items = Travel.objects.all()
    return render(request, 'index.html', {'all_items': all_travel_items})

def addTravel(request):
    new_item = Travel(content = request.POST['content'])
    new_item.save()

    return HttpResponseRedirect('/travel/')

def deleteTravel(request, travel_id):
    item_to_delete = Travel.objects.get(id=travel_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/travel/')

# class Assets(View):
#
#     def get(self, _request, filename):
#         path = os.path.join(os.path.dirname(__file__), 'dist', filename)
#
#         if os.path.isfile(path):
#             with open(path, 'rb') as file:
#                 return HttpResponse(file.read(), content_type='application/javascript')
#         else:
#             return HttpResponseNotFound()
