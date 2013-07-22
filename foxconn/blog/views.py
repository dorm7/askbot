# -*- coding: utf-8 -*-

import requests

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page

from askbot.conf import settings as askbot_settings


@cache_page(60*15)
def index(request):
    TUMBLR_CONSUMER_KEY = '1jckdvdQGTd0PUTXf8IlEu3dw4xZ8odqO3jDTxJf7dXfIA3RhA'
    limit = '10'
    tumblr_api = 'http://api.tumblr.com/v2/blog/blog.krdai.info/posts/text?api_key={key}&limit={limit}'.format(key=TUMBLR_CONSUMER_KEY, limit=limit)
    r = requests.get(tumblr_api)
    response = r.json()['response']
    posts = response['posts']
    return render_to_response(
        'blog_detail.html',
        {'settings': askbot_settings, 'posts': posts},
        context_instance=RequestContext(request))
