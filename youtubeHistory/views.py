from django.shortcuts import render,redirect
from .forms import HistoryEntryForm
from .models import HistoryEntry

def history(request):
    entries = HistoryEntry.objects.order_by('date_added')
   
    context = {'entries': entries}
    return render(request, 'youtubeHistory/index.html', context)


def add(request):
    if request.method == "POST":
        form = HistoryEntryForm(request.POST)
        
        if form.is_valid():
            new_entry = HistoryEntry(url=request.POST['url'],
                                     annotation=request.POST['annotation'])
        
            print(new_entry.url)
            if new_entry.url[0:4] != "http":
                new_entry.url = "https://" + new_entry.url
        
            if not new_entry.annotation:
                new_entry.annotation = "Video you added at {}".format(new_entry.date_added.strftime("%d/%b/%y"))

            new_entry.save()
            return redirect('history')
    else:
        form = HistoryEntryForm()
    
    context = {'form': form}
    return render(request, 'youtubeHistory/add.html', context)
