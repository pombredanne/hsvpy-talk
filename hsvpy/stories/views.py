from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Story, Paragraph
from .forms import ParagraphForm, StoryForm

def index(request):
    stories = Story.objects.all()

    return render(request, 'stories/index.html', locals())

def show_story(request, story_id):
    story = get_object_or_404(Story, pk=int(story_id))

    return render(request, 'stories/story.html', locals())

@login_required
def add_story(request):
    story = Story(created_by=request.user)

    form = StoryForm(request.POST or None, instance=story)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("add-paragraph", kwargs={"story_id": story.id,}))

    return render(request, 'stories/add-story.html', locals())

@login_required
def edit_story(request, story_id):
    story = get_object_or_404(Story, pk=int(story_id))

    form = StoryForm(request.POST or None, instance=story)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("show-story", kwargs={"story_id": story.id,}))

    return render(request, 'stories/edit-story.html', locals())

@login_required
def edit_paragraph(request, story_id, para_id=None):
    story = get_object_or_404(Story, pk=int(story_id))

    if para_id:
        paragraph = get_object_or_404(Paragraph, pk=int(para_id), story=story)
        template = 'stories/edit-paragraph.html'
    else:
        paragraph = Paragraph(story=story, written_by=request.user)
        template = 'stories/add-paragraph.html'

    form = ParagraphForm(request.POST or None, instance=paragraph)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("show-story", kwargs={"story_id": story.id,}))

    return render(request, template, locals())
