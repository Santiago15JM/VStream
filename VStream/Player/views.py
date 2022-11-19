from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Video, Comment
from django.db.models import Q
from django.urls import reverse

# Create your views here.


def home(req):
    videos = Video.objects.all()
    context = {'videos': videos}
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, req))


def player(req, vid):
    videos = Video.objects.filter(~Q(id=vid))
    currentVideo = Video.objects.get(id=vid)
    comments = Comment.objects.filter(video=currentVideo)
    context = {'videos': videos,
               'currentVideo': currentVideo,
               'uploader': currentVideo.uploader.username,
               'comments': comments}
    template = loader.get_template('player.html')
    return HttpResponse(template.render(context, req))


def addComment(req, vid):
    videos = Video.objects.filter(~Q(id=vid))
    currentVideo = Video.objects.get(id=vid)
    comments = Comment.objects.filter(video=currentVideo)
    context = {'videos': videos,
               'currentVideo': currentVideo,
               'uploader': currentVideo.uploader.username,
               'comments': comments}
    template = loader.get_template('addcomment.html')
    return HttpResponse(template.render(context, req))


def saveComment(req, vid):
    x = req.POST['comment']
    comment = Comment(comment=x, user=req.user,
                      video=Video.objects.get(id=vid))
    comment.save()
    return HttpResponseRedirect(f'/player/{vid}')


def search(req):
    terms = req.GET['search']
    s = terms.split()
    results = Video.objects.filter(
        Q(title__icontains=terms) | Q(uploader__username__in=s))

    context = {
        'search': terms,
        'results': results}
    template = loader.get_template('searchresults.html')
    return HttpResponse(template.render(context, req))
