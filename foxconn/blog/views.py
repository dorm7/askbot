# -*- coding: utf-8 -*-

import requests

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page

from askbot.conf import settings as askbot_settings
from settings import TUMBLR_CONSUMER_KEY
from settings import TUMBLR_SITE

@cache_page(60*15)
def index(request):
    limit = request.GET.get('limit', '5')
    offset = request.GET.get('offset', '0')
    key = TUMBLR_CONSUMER_KEY
    tumber_site = TUMBLR_SITE
    tumblr_api = 'http://api.tumblr.com/v2/blog/{tumber_site}/posts/text?api_key={key}&limit={limit}&offset={offset}'.format(**locals())
    r = requests.get(tumblr_api)
    response = r.json()['response']

    posts = response['posts']
    total_posts = int(response['total_posts'])
    next_url = ''
    prev_url = ''
    if int(offset)+int(limit) < total_posts:
        next_url = '/?offset={offset}&limit={limit}'.format(offset=str(int(offset)+int(limit)), limit=limit)
    if int(offset)-int(limit) >= 0:
        prev_url = '/?offset={offset}&limit={limit}'.format(offset=str(int(offset)-int(limit)), limit=limit)

    return render_to_response(
        'blog_detail.html',
        {'settings': askbot_settings, 'posts': posts, 'prev_url': prev_url, 'next_url': next_url},
        context_instance=RequestContext(request))
