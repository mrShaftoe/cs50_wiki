from django.shortcuts import render

from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, name):
    entry = util.get_entry(name)

    if entry:
        return render(request, "encyclopedia/entry.html", {
            "name": name,
            "entry": util.convert_entry(name)
    })

    return render(request, "encyclopedia/404.html", {
        "name": name
    })

