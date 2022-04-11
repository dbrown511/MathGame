import random  #Lets me have random things

Travel = [
    "Dear Mom: I've decided to quit my job as OCC1 to pursue my real passion for NOUNS as a OCC2 in COUNTRY",
    [["Suggest an occupation: ", "OCC1"], ["A second occupation: ", "OCC2"],
     ["A plural noun: ", "NOUNS"], ["A country: ", "COUNTRY"]]
]  #A Story

SillySale = [
    "Oh hey there, are you wanting a NOUN1? Well simply buy 24 NOUNS and get NOUN1 for free! Just finance the purchase through our in store METAL card and pay no interest for NUM years!!!",
    [["Suggest a metal: ", "METAL"], ["A single noun: ", "NOUN1"],
     ["A plural noun: ", "NOUNS"], ["A number between 42 and 69: ", "NUM"]]
]  #Also a story

ShowTell = [
    "Did I ever show you my favourite NOUN? It's so cool, no other brand of NOUN can VERB as well! It's also by far the ADJECTIVE in the whole NOUN2 product category",
    [["Suggest a noun: ", "NOUN"], ["A verb: ", "VERB"],
     ["An adjective: ", "ADJECTIVE"], ["Another noun: ", "NOUN2"]]
]  #also also a story

stories = [Travel, SillySale, ShowTell]

Selection = int(input("Pick a number from 0 to 2: "))
PickedStory = stories[Selection]
prose = PickedStory[0]
swaps = PickedStory[1]

for prompt, placeholder in swaps:
    userinput = input(prompt)
    prose = prose.replace(placeholder, userinput)

print(prose)
