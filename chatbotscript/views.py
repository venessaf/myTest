# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from userresponses.models import UserResponses
from questionres.models import Questions, Responses
from account.models import Users
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json
import requests
import random
import time


@csrf_exempt
def event_handle(request):
    if request.method=='POST':
        data = request.body.decode('utf-8')
        event = json.loads(data)

        #Act according to event type
        if event['type'] == 'MESSAGE' or event['type'] == 'ADDED_TO_SPACE':
            message = newMessageCard( False)

        elif event['type'] == 'CARD_CLICKED':
            message = {}
            message['actionResponse'] = {}
            message['actionResponse']['type'] = "UPDATE_MESSAGE"
            message['cards'] =  [{"header":{"title":"Thank you. Your response has been recorded. "}}]
            storeResponse(event)

        else:
            return
        return JsonResponse(message)

    if request.method=='GET':
        return HttpResponse("Hey there you human! You just did a successful GET")


#Store the user response with their question ID
def storeResponse(event):
    #Get user information
    userEmail = event['user']['email']
    userObj = Users.objects.get(email__exact = userEmail)
    userId = userObj.uid

    #Get question info
    if event['action']['parameters'][0]['key'] == "questionId":
        qId = event['action']['parameters'][0]['value']

    #Save user response
    options_str = Questions.objects.get(qid=qId).options
    options_list = [raw.strip() for raw in options_str.split(',')]
    option_no = event['action']['actionMethodName']
    response_opt = options_list[int(option_no)]

    responseToSave = UserResponses(uid=Users.objects.get(pk=userId), qid=Questions.objects.get(pk=qId), uresponse=response_opt)
    responseToSave.save()

'''
Creates a new question message or tells user max tries are over
@param eent_name - the action card name
@param update - Update the existing message/card or post a new message
'''
def createMessage(event_name, update):
    bot_res = {}
    responseType = "UPDATE_MESSAGE" if update else "NEW_MESSAGE"
    bot_res['actionResponse'] = {}
    bot_res['actionResponse']['type'] = responseType

    if (event_name == 'good_rating'):
        bot_res['cards'] =  [{"header":{"title":"Thank you for your response."}}]
    elif (event_name == '0'):
        bot_res['cards'] =  [{"header":{"title":"Option1"}}]
    elif (event_name == '1'):
        bot_res['cards'] =  [{"header":{"title":"Option2"}}]
    elif (event_name == '2'):
        bot_res['cards'] =  [{"header":{"title":"Option3"}}]
    elif (event_name == '3'):
        bot_res['cards'] =  [{"header":{"title":"Option4"}}]
    elif (event_name == '4'):
        bot_res['cards'] =  [{"header":{"title":"Option5"}}]
    elif (event_name == 'bad_rating'):
        bot_res['cards'] =  [{"sections":[{"widgets":[{"textParagraph":{"text":"Oh oh, we will strive to betterment."}}]}]}]
    elif (event_name == 'new_message'):
        bot_res['cards'] = [{"header":{"title":"<b>Question: </b> How do you like the facilities provided?"},"sections":[{"widgets":[{"buttons":[{"textButton":{"text":"Good","onClick":{"openLink":{"url":"https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif"}}}},{"textButton":{"text":"Bad","onClick":{"openLink":{"url":"https://media.giphy.com/media/RWUqVYucDBD4A/giphy.gif"}}}}]},{"buttons":[{"textButton":{"text":"Okay","onClick":{"action":{"actionMethodName":"good_rating"}}}},{"textButton":{"text":"Satisfactory","onClick":{"action":{"actionMethodName":"bad_rating"}}}}]}]}]}]

    return bot_res

# create a  new card to post a new question to user, @param update has to be True
def newMessageCard(update):
    bot_res = {}
    responseType = "UPDATE_MESSAGE" if update else "NEW_MESSAGE"
    bot_res['actionResponse'] = {}
    bot_res['actionResponse']['type'] = responseType

    x = len(Questions.objects.all())
    random_num = random.randint(0,x)
    question_str = Questions.objects.get(qid=random_num).question
    bot_res['cards'] = []
    bot_res['cards'].insert(0, {"header":{"title":{}}})
    bot_res['cards'][0]['header']['title'] = question_str

    bot_res['cards'].insert(1,{"sections":[{"widgets":[]}]})
    bot_res['cards'][1]['sections'][0]['widgets']=[]
    options_str = Questions.objects.get(qid=random_num).options
    options_list = [raw.strip() for raw in options_str.split(',')]
    options_len = len(options_list)
    for i in range(0,options_len):
        bot_res['cards'][1]['sections'][0]['widgets'].insert(0,{"buttons":[{"textButton":{"onClick":{"action":{}}}}]})
        bot_res['cards'][1]['sections'][0]['widgets'][0]['buttons'][0]['textButton']['onClick']['action']['actionMethodName'] = str(i)
        bot_res['cards'][1]['sections'][0]['widgets'][0]['buttons'][0]['textButton']['onClick']['action']['parameters'] = []
        bot_res['cards'][1]['sections'][0]['widgets'][0]['buttons'][0]['textButton']['onClick']['action']['parameters'].insert(0,{"key":"questionId"})
        bot_res['cards'][1]['sections'][0]['widgets'][0]['buttons'][0]['textButton']['onClick']['action']['parameters'][0]['value'] = random_num
        #"actionMethodName":"good_rating"
        bot_res['cards'][1]['sections'][0]['widgets'][0]['buttons'][0]['textButton']['text'] = options_list[i] #+ "option" + str(i)

    return bot_res




