import random


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

try:

    while True:
        try:
            r_p_s = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors.\n"))
            r_p_s_computer = random.randint(1, 3)

          
            if r_p_s == 1 or r_p_s == 2 or r_p_s == 3:

                if r_p_s == 1:
                    print(rock)
                elif r_p_s == 2:
                    print(paper)
                elif r_p_s == 3:
                    print(scissors)
                else:
                    print("Please choose from given numbers. Enter 1 for Rock, 2 for Paper, 3 for Scissors.\n")

                if r_p_s_computer == 1:
                    print(rock)
                if r_p_s_computer == 2:
                    print(paper)
                if r_p_s_computer == 3:
                    print(scissors)
                else:
                    pass

                if r_p_s == r_p_s_computer:
                    print("Match Draw.\n")
                elif r_p_s == 2 and r_p_s_computer == 1:
                    print("You win!\n")
                elif r_p_s == 2 and r_s_computer == 3:
                    print("You win!\n")
                elif r_p_s == 3 and r_s_computer == 0:
                    print("You win!\n")
                else:
                    print("You lose!\nTry again!")
            else:
                print("Please enter correct input")
        except ValueError:
            print("Please enter between the numbers given bellow.")
            

except KeyboardInterrupt:
    print("\n\nInturrepted by User\n\n")
