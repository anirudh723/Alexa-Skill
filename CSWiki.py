# Program Entry
def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event, context)
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event, context)


# Launch
def on_launch(event, context):
    return statement("Greetings", "Welcome to the CS Wiki!")


# Intent Routing
def on_intent(event, context):
    intent = event['request']['intent']['name']
    if intent == "AskDefinitionIntent":
        return ask_definition_intent(event, context)
    if intent == "AMAZON.CancelIntent":
        return cancel_intent()
    if intent == "AMAZON.HelpIntent":
        return help_intent()
    if intent == "AMAZON.StopIntent":
        return stop_intent()
    else:
        return statement("Please try again", "I could not recognize a request for a definition. Please ask again.")


# Responses
def statement(title, body):
    speechlet = {}
    speechlet['outputSpeech'] = build_plain_speech(body)
    speechlet['card'] = build_simple_card(title, body)
    if title in ("Stop", "Cancel"):
        speechlet['shouldEndSession'] = True
    else:
        speechlet['shouldEndSession'] = False
    return build_response(speechlet)


# Built-in Intents
def cancel_intent():
    return statement("Cancel", "CSWiki will now stop. Thank you!")


def help_intent():
    return statement("Help", "You are seeking for help")


def stop_intent():
    return statement("Stop", "CSWiki will now stop. Thank you!")
