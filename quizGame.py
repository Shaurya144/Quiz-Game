# in this program we need to randomly select 5 questions from a seperate file
# Automatically mark questions ( if incorrect show right answer ) 
# Add incorrect answer to seperate file with answer, time and date 
# this can be used by teachers to see if students are getting same questions wrong

import random
import time

questions = []
incorrectAnswers = []
score = 0

# Parse the data into a 2D list 
with open("CSQuestions&CorrectAnswers.txt","r") as file:

  for record in file:

    record = record.strip()
    # Delimiter is " -- " in the text file
    temp = record.split(" -- ")

    questions.append(temp)

# Ask 5 questions
for i in range(5):

  # Pick an index of one of the questions in the list 
  choice = random.randint(0,len(questions) - 1)

  # Ask the user the question (index zero) and convert to lower case so capitals don't matter
  answer = input(questions[choice][0]+ " ").lower()

  # Check if the answer (index 1) matches (convert to lower case so capitals don't matter)
  if answer == questions[choice][1].lower():
    print("Correct.")
    score += 1
  else:
    print("Incorrect. The answer was:",questions[choice][1])

    # Create a temporary list with the question, wrong answer, and timestamp and then append this to the master list
    incorrectAnswer = [questions[choice][0],answer,time.ctime()]
    incorrectAnswers.append(incorrectAnswer)

  # Delete the question from the list to prevent it being chosen again 
  del questions[choice]

print("Your final score was",score)

# Use the incorrectAnswers list to add any wrong answers to the 'Wrong Answers' text file
with open("WrongAnswers.csv","a") as file:
  
  for i in range(len(incorrectAnswers)):

    line = ",".join(incorrectAnswers[i]) + "\n"

    file.write(line)