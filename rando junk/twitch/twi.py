import twitch_highlights

twitch_credentials = {
   "client_id": "1at6pyf0lvjk48san9j7fjak6hue2i",
   "client_secret": "5i2c7weuz1qmvtahrok6agi7nbqo7d"
}

acr_credentials = {
   "access_key": "m73k42t5v1jttq2h4h1r41v450lgqdpl",
   "secret_key": "1haPnq6StnU6S4FqoqzOvNAzLkapbaFeG7Pj945U",   
   "host": "identify-eu-west-1.acrcloud.com"  
}

TwitchHighlights(twitch_credentials=twitch_credentials, acr_credentials=acr_credentials)