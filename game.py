questions = [
  [1,2],
  [5,5],
  [7,8],
  [1,3],
  [4,5],
  [3,7],
  [9,1],
]
score = 0
Qanswered = 0
for a, b in questions:
  response = int(input("What's the value of " + str(a) + " + " + str(b) + "?: "))
  Qanswered += 1
  if  response == (a + b):
    score += 1
    print("Good Job! your score so far is: " + str(score) + " out of " + str(Qanswered))
  else:
    print("whoops! your score so far is: " + str(score) + " out of " + str(Qanswered))

scorepct = int(score / 5 * 100)

print("You got " + str(scorepct) + "% correct!")
if scorepct == 100:
  print("you are a math genius!")
  
elif scorepct >= 80 and scorepct != 100:
  print("Not too shabby!")
elif scorepct < 80:
  print("Better study up, champ!")
