from django.shortcuts import render

# Create your views here.
# Create your views here.
def welcome(request):
    all_images = Image.objects.all()
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    return render(request,'index.html', {'all_images':all_images,'location_results':location_results,'category_results':category_results})

def search_results(request):
    
    if 'searchItem' in request.GET and request.GET["searchItem"]:
        search_term = request.GET.get("searchItem")
        searched_image = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'index.html',{"message":message,"all_images": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'index.html',{"message":message})
    
def get_category(request,category):
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    category_result = Image.objects.filter(image_category__cat_name = category)
    return render(request,'index.html',{'all_images':category_result,'category_results':category_results,'location_results':location_results})
    