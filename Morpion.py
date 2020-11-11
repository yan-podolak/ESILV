class State:
    empty_array = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]

    def __init__(self, array=empty_array):
        self.array = array;

    def print(self):
        for i in range(len(self.array)):
            for j in range(len(self.array[i])):
                if self.array[i][j] == 1:
                    print("O", end=" ")
                if self.array[i][j] == -1:
                    print("X", end=" ")
                if self.array[i][j] == 0:
                    print("-", end=" ")
            print()


def Actions(state, joueur):
    liste_action = []
    liste_action_state = []
    state_array = state.array
    for i in range(3):
        for j in range(3):
            if state.array[i][j] == 0:
                array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                for l in range(3):
                    for m in range(3):
                        array[l][m] = state_array[l][m]
                array[i][j] = joueur
                liste_action.append(array)
    for i in range(len(liste_action)):
        liste_action_state.append(State(liste_action[i]))
    return liste_action_state


def Result(state, a):
    for i in range(3):
        for j in range(3):
            state.array[i][j] = a.array[i][j]
    return state;


def Terminal_Test(state):
    # print(state)
    var = 0
    for i in range(3):
        for j in range(3):
            if state.array[i][j] == 0:
                var = var + 1
    if var == 0:
        # print("Rempli")
        return True

    if state.array[0][0] == state.array[1][1] and state.array[0][0] == state.array[2][2] and state.array[0][0] != 0:
        # print("Desc")
        return True
    else:
        if state.array[2][0] == state.array[1][1] and state.array[2][0] == state.array[0][2] and state.array[2][0] != 0:
            # print("Asc")
            return True
        else:
            for i in range(len(state.array)):
                if state.array[i][0] == state.array[i][1] and state.array[i][0] == state.array[i][2] and state.array[i][
                    0] != 0:
                    # print("Ligne")
                    return True

            for j in range(len(state.array)):
                if state.array[0][j] == state.array[1][j] and state.array[2][j] == state.array[0][j] and state.array[0][
                    j] != 0:
                    # print("Colonne")
                    return True
            return False


def Utility(state):
    if state.array[0][0] == state.array[1][1] and state.array[0][0] == state.array[2][2] and state.array[0][0] != 0:
        # print("Desc")
        return state.array[0][0]
    else:
        if state.array[2][0] == state.array[1][1] and state.array[2][0] == state.array[0][2] and state.array[2][0] != 0:
            # print("Asc")
            return state.array[2][0]
        else:
            for i in range(len(state.array)):
                if state.array[i][0] == state.array[i][1] and state.array[i][0] == state.array[i][2] and state.array[i][
                    0] != 0:
                    # print("Ligne")
                    return state.array[i][0]

            for j in range(len(state.array)):
                if state.array[0][j] == state.array[1][j] and state.array[0][j] == state.array[2][j] and state.array[0][
                    j] != 0:
                    # print("Colonne")
                    return state.array[0][j]
            return 0


def minmax(state, joueur):
    if Terminal_Test(state):
        return Utility(state)
    if joueur == False:
        maxi = -1000
        liste_action = Actions(state, 1)
        for i in range(len(liste_action)):
            val = minmax(liste_action[i], True)
            maxi = max(val, maxi)
        return maxi
    else:
        mini = 1000
        liste_action = Actions(state, -1)
        for i in range(len(liste_action)):
            val = minmax(liste_action[i], False)
            mini = min(mini, val)
        return mini


def alphabeta(state, joueur, alpha, beta):
    if Terminal_Test(state):
        return Utility(state)
    if joueur == False:
        maxi = -1000
        liste_action = Actions(state, 1)
        for i in range(len(liste_action)):
            maxi = max(maxi, alphabeta(liste_action[i], True, alpha, beta))
            if maxi >= beta:
                return maxi
            alpha = max(alpha, maxi)
        return maxi
    else:
        mini = 1000
        liste_action = Actions(state, -1)
        for i in range(len(liste_action)):
            mini = min(beta, alphabeta(liste_action[i], False, alpha, beta))
            if alpha >= mini:
                return mini
            beta = min(beta, mini)
        return mini


def Jeu():
    state = State()
    joueur = -1
    while Terminal_Test(state) == False:
        if joueur == -1:
            print(" A vous de jouer, voici la grille : ")
            state.print()
            print("")
            print("")
            jeu = Actions(state, -1)
            for i in range(len(jeu)):
                print("Choix", i, ":")
                jeu[i].print()
            i = -1
            while (i < 0 or i > 8):
                i = int(input("Selectionnez votre choix :"))
            state = Result(state, jeu[i])
            joueur = 1
        else:
            score = -100
            liste_action = Actions(state, 1)
            index = 0
            for i in range(len(liste_action)):
                val = minmax(liste_action[i],True)
                #val = alphabeta(liste_action[i], True, -10000, 10000)
                if val > score:
                    score = val
                    index = i
            state = Result(state, liste_action[index])
            joueur = -1
            print("")
            print("")

    if Utility(state) == -1:
        print("Vous avez gagné ! Bravo !")
    if Utility(state) == 1:
        print("Vous avez perdu ! Dommage !")
    if Utility(state) == 0:
        print("Egalité")
    state.print()

def AI():
    state = State()
    joueur = -1
    while Terminal_Test(state) == False:
        print("Etat")
        state.print()
        if joueur == -1:
            score = 100
            liste_action = Actions(state, -1)
            index = 0
            for i in range(len(liste_action)):
                # val = minmax(liste_action[i],True)
                val = minmax(liste_action[i], False)
                if val < score:
                    score = val
                    index = i
            state = Result(state, liste_action[index])
            joueur = 1
            print("")
            print("")
        else:
            score = -100
            liste_action = Actions(state, 1)
            index = 0
            for i in range(len(liste_action)):
                # val = minmax(liste_action[i],True)
                val = alphabeta(liste_action[i], True, -10000, 10000)
                if val > score:
                    score = val
                    index = i
            state = Result(state, liste_action[index])
            joueur = -1
            print("")
            print("")

    if Utility(state) == -1:
        print("Vous avez gagné ! Bravo !")
    if Utility(state) == 1:
        print("Vous avez perdu ! Dommage !")
    if Utility(state) == 0:
        print("Egalité")
    state.print()

if __name__ == '__main__':
    # Initialisation du morpion
    #AI()
    Jeu()