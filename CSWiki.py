# Program Entry
def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return on_launch()
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event)


# Launch
def on_launch():
    return statement("Greetings", "Welcome to the CS Wiki!")


# Intent Routing
def on_intent(event):
    intent = event['request']['intent']['name']
    if intent == "AskDefinitionIntent":
        return ask_definition_intent(event)
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
    speechlet = {'outputSpeech': build_plain_speech(body), 'card': build_simple_card(title, body)}
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


# Custom Intents
def ask_definition_intent(event):
    class_def = "Classes are templates used in object-oriented programming to create objects, which are instances" \
                " of that class.  All classes may contain variable definitions and methods."
    method_def = "A method is a procedure or function associated with a class. As part of a class, a method defines a" \
                 " particular behavior of a class instance. A class can have more than one method."
    var_def = "Variables are used to store information to be referenced and manipulated in a computer" \
              " program. It is helpful to think of variables as containers that hold information."
    static_def = "A static member is a member of a class that isn’t associated with an instance of a class. Instead," \
                 " the member belongs to the class itself.  As a result, you can access the static member without" \
                 " creating a class instance."
    interface_def = "An interface is essentially a class with no implementation that is intended to be subclassed so" \
                    " that a related set of classes all share a common set of methods. In other words, interfaces" \
                    " specify what a class must do and not how. It is the blueprint of the class. This concept is" \
                    "very useful as it prevents code redundancy and helps increase security."
    private_def = "Private is a keyword that specifies access level and provides programmers with some control over" \
                  " which variables and methods are hidden in a class. Variables and methods defined with the" \
                  " private keyword may be accessed only by other methods within the class and cannot be" \
                  " accessed by derived classes."
    this_def = "Within an instance method or a constructor, this is a reference to the current object — the object" \
               " whose method or constructor is being called. You can refer to any member of the current object from" \
               " within an instance method or a constructor by using this."
    abstract_class_def = "Abstraction is a process of hiding the implementation details and showing only " \
                         "functionality to the user. A class which is declared as abstract is known as an abstract" \
                         " class. It can have abstract and non-abstract" \
                         " methods. It needs to be extended and its method implemented. It cannot be instantiated."
    super_def = "The super keyword is used inside a sub-class method definition to call a method defined in the super" \
                " class, which is the class it extends from."
    for_loop_def = "A for loop is a control flow statement which is used to check for certain conditions and then" \
                   " repeatedly executes a block of code as long as those conditions are met. It distinguishes itself" \
                   " from other kinds of iterative statements as" \
                   " it allows the body of the loop to know the exact sequencing of each iteration."
    while_loop_def = "A while loop is a control flow statement which executes a block of code an unknown number of" \
                     " times, until a certain condition is not met."
    for_each_loop_def = "A for each loop is a control flow statement that is used to access each successive value in" \
                        " a collection of values. It is sometimes called the enhanced for loop."

    facts = {"class": class_def, "class az": class_def, "method": method_def, "variable": var_def, "verbal": var_def,
             "harry revel": var_def, "static": static_def, "interface": interface_def, "this": this_def,
             "abstract class": abstract_class_def, "abstract class az": abstract_class_def, "private": private_def,
             "private variable": private_def, "private method": private_def, "super": super_def,
             "for loop": for_loop_def, "while loop": while_loop_def, "for each loop": for_each_loop_def}
    asked_word = event['request']['intent']['slots']['word']['value']
    if asked_word in facts:
        return statement("Definition of word", facts.get(asked_word))
    else:
        return statement("Definition not found", "I could not find a definition for this word")


# Builders
def build_plain_speech(body):
    speech = {'type': 'PlainText', 'text': body}
    return speech


def build_simple_card(title, body):
    card = {'type': 'Simple', 'title': title, 'content': body}
    return card


def build_response(message, session_attributes={}):
    response = {'version': '1.0', 'sessionAttributes': session_attributes, 'response': message}
    return response
