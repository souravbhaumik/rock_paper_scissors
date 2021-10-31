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

game_images = [rock, paper, scissors]
try:

    while True:
        try:
            r_p_s = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
            r_p_s_computer = random.randint(0, 2)

          
            if r_p_s == 0 or r_p_s == 1 or r_p_s == 2:

                
                print(game_images[r_p_s])

                
                print(game_images[r_p_s_computer])

                if r_p_s == r_p_s_computer:
                    print("Match Draw.\n")
                elif r_p_s == 1 and r_p_s_computer == 0:
                    print("You win!\n")
                elif r_p_s == 1 and r_p_s_computer == 2:
                    print("You win!\n")
                elif r_p_s == 2 and r_p_s_computer == 0:
                    print("You win!\n")
                else:
                    print("You lose!\nTry again!")
            else:
                print("Please enter correct input")
        except ValueError:
            print("Please enter between the numbers given bellow.")
        except IndexError:
            print("Please enter between the numbers given bellow.")
            

except KeyboardInterrupt:
    print("\n\nInturrepted by User\n\n")
