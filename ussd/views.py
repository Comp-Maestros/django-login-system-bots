from django.shortcuts import render

# Create your views here use africastalking to create ussd app i have the api key and username bulk_sms  and the short code 22384
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import africastalking



# Create your views here.
@csrf_exempt
def ussd_callback(request):
    # Parse the USSD parameters from the request
    sessionId = request.POST.get("sessionId", None)
    serviceCode = request.POST.get("serviceCode", None)
    phoneNumber = request.POST.get("phoneNumber", None)
    text = request.POST.get("text", None)

    # Implement your USSD logic here
    response = ""

    # Example USSD logic: Display a welcome message and menu options
    if text == "":
        response = "CON Welcome to My USSD App!\n"
        response += "1. Option 1\n"
        response += "2. Option 2\n"
        response += "3. Option 3"

    # Example USSD logic: Handle user responses to menu options
    elif text == "1":
        response = "CON You selected Option 1. Enter your name:"
    elif text == "2":
        response = "CON You selected Option 2. Enter your age:"
    elif text == "3":
        response = "END You selected Option 3. Thank you!"

    # Send the USSD response back to Africa's Talking
    return HttpResponse(response, content_type="text/plain")
 