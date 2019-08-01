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
