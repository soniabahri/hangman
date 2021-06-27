class Player1:
    def __init__(self):
        self.mot = ""

    def joue(self):
        mot = input("entre un mot de 3 à 10 letters \n")
        while not(3 <= len(mot) <= 10):
            mot = input("entre un mot de 3 à 10 letters \n")

        self.mot = mot.upper()

    def get_mot(self):
        return self.mot


class Player2:
    def __init__(self, mot):
        self.guessed = "_"*len(mot)
        self.mot = mot

    def get_guessed(self):
        return self.guessed

    def set_guessed(self, mot):
        self.guessed = mot

    def joue(self):
        letter = input("Votre choix : ")
        while letter.isdigit() or len(letter) != 1:
            print("entre une lettre alphabétique svp ")
            letter = input("Votre choix : ")

        letter = letter.upper()

        if letter in self.mot:
            guessed = [i if letter != j else letter for i, j in zip(self.guessed, self.mot)]
            self.guessed = "".join(guessed)
            mot = [i if i != letter else "_" for i in self.mot]
            self.mot = "".join(mot)
            return True
        else:
            return False

    def over_or_not(self):
        if "_" in self.guessed:
            return False
        else:
            return True


class Game:
    drawing = (
        """
""",
        """
*




_|_
*
""",
        """
*


 |
 |
_|_
*
""",
        """
*
 --
 |
 |
 |
 |
_|_
*
""",
        """
*
 -----
 |   |   
 |
 |
 |
_|_
*
""",
        """
*
 -----
 |   |   
 |   O
 |
 |
_|_
*
""",
        """
*
 -----
 |   |   
 |   O
 |   | 
 |
_|_
*
""",
        """
*
 -----
 |   |   
 |   O
 |  /| 
 |
_|_
*
""",
        """
*
 -----
 |   |   
 |   O
 |  /|\\
 |
_|_
*
""",
        """
*
 -----
 |   |   
 |   O
 |  /|\\
 |  /   
_|_
*
""",
        """
*
 -----
 |   |   
 |   O
 |  /|\\
 |  / \\ 
_|_
*
""",
    )

    def start(self):
        player1 = Player1()
        player1.joue()
        mot = player1.get_mot()

        print("Le jeu commence...")
        print("\t\t"+"_"*len(mot))

        player2 = Player2(mot)
        i = 0
        while True:
            correct_guess = player2.joue()
            if not correct_guess:
                i += 1

            guessed = player2.get_guessed()
            print(self.drawing[i])
            if i < len(self.drawing) - 1:
                print("\t\t " + guessed)
                if player2.over_or_not():
                    print("Vous avez gagné !!!")
                    break
            else:
                print("\t\t Perdu !")
                print("Solution: " + mot)
                break


if __name__ == "__main__":
    game = Game()
    game.start()
