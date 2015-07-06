from django.shortcuts import render, render_to_response
from django.http import Http404
from django.template import Context

def index(request):
    return render(request, "search/index.html")

def exec_search(request):
    if request.method == "POST":
        for engi, query in request.POST.items():
            if not query or query == "\\":
                continue
            #import engines.[engine]
            try:
                engine_module = __import__(".".join(("search.engines", engi)))
            except ImportError:
                continue
            engine_module = getattr(engine_module, "engines")
            #get low-level module
            engine_module = getattr(engine_module, engi)
            engine = getattr(engine_module, engi)()
            try:
                engine.search(query)
            except:
                continue
        
            #response
            context = Context({"results" : engine.get_results()} )
            render(request, "search/query.html", context=context)
    #default is 404 as you should not access it without data
    else:
        raise Http404