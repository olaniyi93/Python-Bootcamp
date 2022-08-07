
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combine = (name1) + (name2)
add_both = combine.lower()

t = add_both.count('t')
r = add_both.count('r')
u = add_both.count('u')
e = add_both.count('e')
true = t + r + u + e

l = add_both.count('l')
o = add_both.count('o')
v = add_both.count('v')
e = add_both.count('e')
love = l + o + v + e
join_love = int(str(true) + str(love))

if (join_love < 10) or (join_love > 90):
  print(f"Your score is {join_love},you go together like coke and mentos. ")
if (join_love >= 40) and (join_love <= 50):
  print(f"Your score is {join_love}, you are alright together.")
else:
  print(f"Your score is {join_love}.")

