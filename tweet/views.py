from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from .models import Tweet, Comment
from .forms import TweetForm, CommentForm


# Create your views here.
def home(request):
    return render(request, 'index.html')


def Tweet_List(request):
    tweets = Tweet.objects.all().order_by('-date')
    comments = Comment.objects.filter().order_by('-date')
    # print(comments)
    return render(request, 'tweet_list.html', {'tweets': tweets, 'comments': comments})


@login_required
def Add_Tweet(request, parent_tweet_id=None):
    parent_tweet = None
    if parent_tweet_id:
        parent_tweet = Tweet.objects.get(id=parent_tweet_id)

    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            new_tweet = form.save(commit=False)
            new_tweet.user = request.user
            new_tweet.parent_tweet = parent_tweet
            new_tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()

    comments = Comment.objects.filter(tweet=parent_tweet) if parent_tweet else None

    return render(request, 'add_tweet.html', {'forms': form, 'parent_tweet': parent_tweet, 'comments': comments})


@login_required
def Add_Comment(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    comments = Comment.objects.filter(tweet=tweet)
    # print(comments)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.tweet = tweet
            new_comment.save()

            tweet.comment_count = comments.count()
            tweet.save()

            return redirect('tweet_list')
    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'tweet': tweet, 'comments': comments, 'form': form})


def LikeView(request, pk):
    tweet = get_object_or_404(Tweet, id=pk)
    tweet.likes.add(request.user)
    return HttpResponseRedirect('/')


def HashtagView(request, hashtag):
    tweets = Tweet.objects.filter(hashtag=hashtag)
    return render(request, 'hashtag.html', {'hashtag_tweets': tweets, 'hashtag': hashtag})

