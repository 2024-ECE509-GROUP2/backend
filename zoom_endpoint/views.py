import json
import os
from urllib import response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from backend.settings import ZOOM_CLIENT_KEY, ZOOM_CLIENT_SECRET, ZOOM_ACCOUNT_ID, ZOOM_BASE_URL, ZOOM_MEETING_CLIENT_KEY, ZOOM_MEETING_CLIENT_SECRET
import jwt
import base64
import requests as fakePostman

# Create your views here.
# Generate Token For API
def get_token():

    key = '%s:%s' %(ZOOM_CLIENT_KEY, ZOOM_CLIENT_SECRET)
    encoded_key = base64.b64encode(key.encode()) 

    request_header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic %s"  %encoded_key.decode()
    }

    response = fakePostman.post(
        'https://zoom.us/oauth/token', 
        data={
            "grant_type": "account_credentials",
            "account_id": ZOOM_ACCOUNT_ID
        },
        headers=request_header
    )

    return response.json()

def get_zakToken(access_token):

    # Add generated acces token
    request_header = {
        "Authorization": "Bearer %s"  %access_token
    }

    response = fakePostman.get(
        ZOOM_BASE_URL+'/users/me/zak', 
        headers=request_header
    )

    return response.json()

@csrf_exempt
def generate_signature(meetingNumber, role=0):
    
    # const iat = Math.round(new Date().getTime() / 1000) - 30
    # get time in epoch form (seconds)
    iat = round(datetime.timestamp(datetime.now())) # iat = 'issued at'
    exp = iat + 60 * 60 * 2     # expiration time is 2 hours  

    # const oHeader = { alg: 'HS256', typ: 'JWT' } 
    header = { "alg" : 'HS256', "typ": 'JWT'}

    key = ZOOM_MEETING_CLIENT_KEY               #   client key from environment
    secret= ZOOM_MEETING_CLIENT_SECRET          #   client secret from environment

    oPayload = {
        "sdkKey": key,
        "appKey": key,
        "mn": meetingNumber,
        "role": role,
        "iat": iat,
        "exp": exp,
        "tokenExp": exp
    }

    # const sdkJWT = KJUR.jws.JWS.sign('HS256', sHeader, sPayload, secret)
    signature = jwt.encode(oPayload, secret, algorithm="HS256", headers=header)

    return signature

@csrf_exempt
def join_meeting(request):

    data = JSONParser().parse(request)

    meetingNumber = data['meeting'] 

    response = {}

    response['signature'] = generate_signature(meetingNumber, 0)
    response['sdkKey'] = ZOOM_MEETING_CLIENT_KEY

    # return sdkJWT
    return JsonResponse(response, status=200, safe=False)

@csrf_exempt
def start_meeting(request):

    data = JSONParser().parse(request)

    meetingNumber = data['meeting'] 

    token_response = get_token()
    access_token = token_response['access_token']

    response = get_zakToken(access_token) # the user zak token to start meeting

    response['signature'] = generate_signature(meetingNumber, 1) # 1 is for meeting host 
    response['sdkKey'] = ZOOM_MEETING_CLIENT_KEY

    # return sdkJWT
    return JsonResponse(response, status=200, safe=False)

@csrf_exempt
def  create_meeting(request):

    data = JSONParser().parse(request)

    print(data)

    # course_cycle = data['course']

    token = get_token()
    access_token = token['access_token']

    # Add generated acces token
    headers = {
        "Authorization": "Bearer %s"  %access_token
    }

    response = fakePostman.post(
        ZOOM_BASE_URL+'/users/me/meetings', 
        json= data,
        headers=headers
    )

    print(response.text)

    # return sdkJWT
    return JsonResponse(response.json(), status=200, safe=False)

@csrf_exempt
def  get_meetings(request):

    # data = JSONParser().parse(request)

    # course_cycle = data['course']

    token = get_token()
    access_token = token['access_token']

    # Add generated acces token
    headers = {
        "Authorization": "Bearer %s"  %access_token
    }

    response = fakePostman.get(
        ZOOM_BASE_URL+'/users/me/meetings', 
        headers=headers
    )

    # return sdkJWT
    return JsonResponse(response, status=200, safe=False)