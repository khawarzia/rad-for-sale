from django.shortcuts import render,redirect
import requests,json
from proud_forest_23287.settings import HUBSPOT_API_KEY

def newsletter_signup(request):
    template = 'newsletter_app/signup.html'
    context = {}
    if request.method == 'POST':
        endpoint = 'https://api.hubapi.com/contacts/v1/contact/?hapikey='+HUBSPOT_API_KEY        
        headers = {}
        headers["Content-Type"]="application/json"
        data = json.dumps({
            "properties":[
                {"property":"email","value":request.POST['email']}
            ]
        })
        r = requests.post(url=endpoint,data=data,headers=headers)
        return redirect('/newsletter-signup-complete')
    return render(request,template,context)

def signup_complete(request):
    template = 'newsletter_app/complete.html'
    context = {}
    return render(request,template,context)