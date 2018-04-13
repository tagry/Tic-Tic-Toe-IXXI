# coding: utf-8
import sys
import math

# Remplissage de case
ME = 0
OPPONENT = 1
EMPTY = -1


class Case(object):
    def __init__(self):
        self.owner = EMPTY


class Grille(object):
    """
    Une grille de morpion 3x3, vide
    """
    def __init__(self):
        self.grille = [[Case() for _ in xrange(3)] for _ in xrange(3)]
        self.owner = EMPTY

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

    def copy(self):
        # TODO
        pass

    def __str__(self):
        #TODO
        pass


# game loop
while True:
    opponent_row, opponent_col = [int(i) for i in input().split()]
    valid_action_count = int(input())
    for i in range(valid_action_count):
        row, col = [int(j) for j in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print("0 0")