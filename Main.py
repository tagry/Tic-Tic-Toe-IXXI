# coding: utf-8
import sys
import math
import random

# Remplissage de case
ME = 0
OPPONENT = 1
EMPTY = -1


class Case(object):
    def __init__(self):
        self.owner = EMPTY

    def copy(self):
        c = self.__class__()
        c.owner = self.owner
        return c

    def __str__(self):
        if self.owner == ME:
            return "X"
        elif self.owner == OPPONENT:
            return "O"
        else:
            return "."


class Move(object):
    def __init__(self, i, j):
        self.i = i
        self.j = j


class Grille(object):
    """
    Une grille de morpion 3x3, vide
    """

    def __init__(self, class_case=Case):
        self.grille = [[class_case() for _ in range(3)] for _ in range(3)]
        self.owner = EMPTY
        self.class_case = class_case

    def set_case(self, i, j, o):
        """
        Mets la marque dans la case, calcul si victoire
        :param i: abs, entre 0 et 3
        :param j: ord, entre 0 et 3
        :param o: owner : ME ou OPPONENT
        :return: rien
        """
        self.grille[i][j].owner = o
        self.calc_owner(i, j)

    def calc_owner(self, i, j):
        """
        Calcul si gagnant, renseigne self.owner
        :param i, j : dernier coup joué
        :return: rien
        """
        if self.owner == EMPTY:
            g = self.grille
            # horiz:
            if g[i][0].owner == g[i][1].owner and g[i][0].owner == g[i][2].owner:
                self.owner = g[i][0].owner
            # vert:
            elif g[0][j].owner == g[1][j].owner and g[0][j].owner == g[2][j].owner:
                self.owner = g[0][j].owner
            # diag \:
            elif i == j and g[0][0].owner == g[1][1].owner and g[0][0].owner == g[2][2].owner:
                self.owner = g[1][1].owner
            # diag /:
            elif i + j == 2 and g[0][2].owner == g[1][1].owner and g[0][2].owner == g[2][0].owner:
                self.owner = g[1][1].owner

    def coups_possibles(self):
        """
        :return: renvoie une liste de Move, coups possibles
        """
        result = []
        for i in range(3):
            for j in range(3):
                if self.grille[i][j].owner == EMPTY:
                    result.append(Move(i, j))
        return result

    def copy(self):
        # TODO
        pass

    def __str__(self):
        s = ""
        for i in range(3):
            for j in range(3):
                s += str(self.grille[i][j])
            s += "|\n"
        return s + "----"


class RandomBrain(object):
    def __init__(self, grid):
        self.grille = grid
        self.possible = None

    def init_turn(self, moves):
        self.possible = moves

    def play(self):
        return random.choice(self.possible)


class MinMaxBrain(RandomBrain):
    def play(self):
        # TODO
        return random.choice(self.possible)

g = Grille()
b = RandomBrain(g)

# game loop
while True:
    opponent_row, opponent_col = [int(i) for i in input().split()]
    if opponent_row >= 0:
        g.set_case(opponent_row, opponent_col, OPPONENT)
    valid_action_count = int(input())
    moves = []
    for i in range(valid_action_count):
        row, col = [int(j) for j in input().split()]
        moves.append(Move(row, col))

    b.init_turn(moves)

    m = b.play()
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print(str(g), file=sys.stderr)

    g.set_case(m.i, m.j, ME)
    print(str(g.owner), file=sys.stderr)

    print("{i} {j}".format(**m.__dict__))