questions = [
[
    "Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Saturn", 2
],

[
    "Who wrote 'Romeo and Juliet'?", "Charles Dickens", "J.K. Rowling", "William Shakespeare", "Mark Twain", 3
],
[
    "Which gas is most abundant in the Earth's atmosphere?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", 2
],

[
    "Who was the first President of the United States?", "George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams", 1
],

[
    "What is the capital of France?", "Berlin", "Madrid", "Rome", "Paris", 4
],

[
    "Which element has the chemical symbol 'O'?", "Osmium", "Oxygen", "Oganesson", "Oxide", 2
],

[
    "Which country is the largest by area?", "China", "USA", "Russia", "Canada", 3
],

[
    "Who painted the Mona Lisa?", "Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet", 2
],

[
    "What is the smallest prime number?", "1", "2", "3", "5", 2
],

[
    "Which organ is responsible for pumping blood throughout the human body?", "Lungs", "Brain", "Heart", "Liver", 3
],

[
    "Which ocean is the largest?", "Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Pacific Ocean", 4
],

[
    "Which country hosted the 2016 Summer Olympics?", "Brazil", "China", "UK", "Japan", 1
],

[
    "What is the hardest natural substance on Earth?", "Gold", "Iron", "Diamond", "Silver", 3
],

[
    "What is the currency of Japan?", "Dollar", "Yen", "Won", "Euro", 2
],

[
    "Which language is primarily spoken in Brazil?", "Spanish", "Portuguese", "English", "French", 2
]

]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,540000,660000,780000,900000,1000000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"Q){question[0]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 
print(f"You take {money}rs to your home.")
