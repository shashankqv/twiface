from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext

from pprint import pprint
from social_auth.models import UserSocialAuth

import requests
import json
from PIL import Image
from random import choice

def get_twitter_username(user):
    return user.social_auth.get(provider='twitter').extra_data['screen_name']

def get_twitter_followers_list(request):

    API_URL = 'http://api.twitter.com/1/statuses/followers.json?screen_name=%s&cursor=-1'

    try:
        instance = UserSocialAuth.objects.filter(provider='twitter').get()
    except ObjectDoesNotExist:
        return redirect(getattr(settings,'LOGIN_URL','/login/twitter/'))

    oauth_access_token=(instance.tokens).get('oauth_token')
    oauth_access_secret=(instance.tokens).get('oauth_token_secret')

    username = get_twitter_username(request.user)
    url = API_URL%username
    req = requests.get(url)

    return render_to_response("customize.html",
            context_instance=RequestContext(request))

def create_image_grid():
    """
    (c) 2012 Vipin Nair <swvist@gmail.com>
    - https://gist.github.com/2692786
    (c) 2012 Madzen
    - https://gist.github.com/2705927
    """
    # Set the appropriate image properties for PIL
    img_type = "RGBA"
    img_columns = 30
    img_rows = 25
    img_width = 50
    img_height = 50

    #Create the initial Image Canvas
    img_canvas = Image.new(img_type, (img_width * img_columns, img_height * img_rows))

    for x in range(img_rows):
        for y in range(img_columns):
            img_canvas.paste(choice(followers_images), (y * img_width, x * img_height))
