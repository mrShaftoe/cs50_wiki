from django.shortcuts import render

from . import util
import random


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

def random_page(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return render(request, "encyclopedia/entry.html", {
        "name": random_entry,
        "entry": util.convert_entry(util.get_entry(random_entry))
    })