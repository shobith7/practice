import language_check
tool = language_check.LanguageTool('en-US')
#text = u'A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'
#text = u'My motter is a doctor. my father is a enginer. I had  gun.'
text = """We 11Signals Technologies a Bengaluru based startup founded in latter 2015. 
The company focuses on building next generation education products for
    teachers and students. Our latest product qurae.com is an assessment tool targeted to provide
    solutions to colleges, schools, corporates to ease and enhance learning and teaching.
    Using our vast experience, we simply education system with the integration of AI, ML and NLP technologies."""


matches = tool.check(text)

print (len(matches))
for i in matches:  print (i)
