from django.shortcuts import render, render_to_response
from django.http import Http404
from django.template import Context

def search_index(request):
    return render(request, "search/index.html")

def exec_search(request):
    if request.method == "POST":
        if "kickasstorrents" in request.POST:
            engi = "kickasstorrents"
        elif "btdigg" in request.POST:
            engi = "btdigg"
        else:
            raise Http404

        query = request.POST[engi]
        #import engines.[engine]
        try:
            engine_module = __import__(".".join(("search.engines", engi)))
        except ImportError:
            #wrong engine? Impossible
            raise Http404
        engine_module = getattr(engine_module, "engines")
        #get low-level module
        engine_module = getattr(engine_module, engi)
        engine = getattr(engine_module, engi)()
        engine.search(query)
        
        #response
        context = Context({"results" : engine.get_results()} )
        return render(request, "search/query.html", context=context)
    #default is 404 as you should not access it without data
    else:
        raise Http404