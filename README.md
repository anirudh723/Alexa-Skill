# Alexa-Skill - 'CSWiki'

Project Description:
    Created my first Alexa Skill. It is called CSWiki. It is a simple skill that provides simple and helpful
    definitions for general terms in the field of Computer Science. I thought this would be helpful for curious learners
    who are just diving into the subject. Much of the common syntax that is used while coding can be a bit hard to
    grasp at first. With the help of Alexa, you can ask simply ask her the meaning of a specific keyword, and she'll
    provide you a brief, easy-to-understand definition. Now, you don't have to go on Google every single time and try
    to find an easy way to learn the word you're looking to get help on.

How it works:
    If you have an Alexa-enabled device, all you need to say is "Alexa, open CSWiki". Once she opens the skill, you can
    ask her for a definition. For example, you can say "what is the definition of an interface?". She will then provide
    you with a simple easy-to-understand meaning of an interface.

General notes on the design/development:
    I used Python to write the program. On the other side, I utilized the Amazon Web Services' (AWS) Lambda tool to
    upload my function, so that it can interact with the Alexa Skills Kit (ASK) on the Amazon Developer Console. As the
    user makes a request to open a skill, Alexa will invoke the custom skill. Then, a certain request can be made using
    specific utterances. In the case of an intent request (ex: for a definition), the ASK will trigger an event to
    invoke the Lambda function, where some piece of the code will execute. The response is then sent back to the Alexa
    platform, which is then sent back to the user, through voice and the Alexa app. The ASK and AWS Lambda tool will
    work back and forth until the conversation is terminated.

Author:
    Anirudh Singh - Northeastern University.
    Contact me: anirudh.s723@gmail.com