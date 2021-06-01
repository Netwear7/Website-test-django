from django.shortcuts import render


# Create your views here.


def index(request):
    context = {'name': 'NL Julian'}
    # return HttpResponse(template.render(context, request))
    return render(request, 'first_app/index.html', context)
