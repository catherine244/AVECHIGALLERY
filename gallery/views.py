from django.shortcuts import render

# Create your views here.
# Create your views here.
def welcome(request):
    all_images = Image.objects.all()
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    return render(request,'index.html', {'all_images':all_images,'location_results':location_results,'category_results':category_results})