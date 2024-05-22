#Love_Score

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

comb_name = name1 + name2
low_name = comb_name.lower()
t = low_name.count("t")
r = low_name.count("r")
u = low_name.count("u")
e = low_name.count("e")
f_digit = t + r + u + e

l = low_name.count("l")
o = low_name.count("o")
v = low_name.count("v")
e = low_name.count("e")
s_digit = l + o + v + e

score = int(str(f_digit) + str(s_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
