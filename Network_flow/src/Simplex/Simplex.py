"""
Date: 11/26/2019
The class which implements the functions in simplex algorithm
"""


from src.Simplex.SlackForm import SlackForm
from src.Simplex.StandardForm import StandardForm
import numpy as np


class Simplex:
    def __init__(self):
        pass

    """
    The entrance of the algorithm
    """
    def simplex(self, standard_form: StandardForm):
        # first call the initialize_simplex procedure
        result = self.initialize_simplex(standard_form)
        # if initialize_simplex returns "infeasible", return.
        if result == "infeasible":
            print("infeasible")
            return
        else:
            # then call the simplex_main procedure, which takes as input a slack form
            res = self.simplex_main(result)
            # if the slack form is unbounded, prints out "unbounded"
            if res is None:
                print("unbounded")
                return
            else:
                assert isinstance(res, SlackForm)
                res_arr, final_form = self.simplex_get_result(res)
                # remove x0
                res_arr = np.delete(res_arr, 0)
                v = final_form.get_v()
                if type(v) == np.ndarray:
                    v = v[0]
                v = round(v, 6)
                print("max flow: ", v)
                print("basic solution: ")
                np.set_printoptions(formatter={'float': '{: 0.6f}'.format})
                print(res_arr)
                print("final slack form: ")
                self.print_slack_form(final_form)
                return

    """
    The initialize procedure
    """
    def initialize_simplex(self, standard_form: StandardForm):
        b = standard_form.get_b()
        min_value, min_index = self.get_min_index_and_value_in_b(standard_form)
        A = standard_form.get_A()
        c = standard_form.get_c()
        N = []
        for i in range(len(c)):
            N.append(i + 1)
        B = []
        for i in range(len(b)):
            B.append(i + len(c) + 1)
        # if all variables in b are greater than 0, returns the slack form of this standard form
        if min_value >= 0:
            v = 0
            slack_form = SlackForm(N, B, A, b, c, v)
            return slack_form
        # otherwise an aux LP is needed
        new_v = 0
        N.append(0)
        new_c = np.zeros(len(c) + 1)
        new_c[len(new_c) - 1] = -1
        new_A = np.zeros((len(B), len(N)))
        for i in range(len(B)):
            for j in range(len(N)):
                if j != len(N) - 1:
                    new_A[i][j] = A[i][j]
                else:
                    new_A[i][j] = -1
        new_slack_form = SlackForm(N, B, new_A, b, new_c, new_v)
        leaving = new_slack_form.get_B()[min_index]
        entering = 0
        # eliminate the negative value in array b
        new_slack_form = self.pivot(new_slack_form, leaving, entering)
        # get the optimal solution of the new slack form
        new_slack_form = self.simplex_main(new_slack_form)
        basic_solution, new_slack_form = self.simplex_get_result(new_slack_form)
        # if x0 is not zero
        if basic_solution[0] != 0:
            return "infeasible"
        else:
            final_B = new_slack_form.get_B()
            # if x0 is a basic variable
            if 0 in final_B:
                deg_A = new_slack_form.get_A()
                index_0_in_B = self.get_index(final_B, 0)
                for index in range(len(deg_A[index_0_in_B])):
                    if deg_A[index_0_in_B][index] != 0:
                        deg_entering = new_slack_form.get_N()[index]
                        # make x0 non-basic
                        new_slack_form = self.pivot(new_slack_form, 0, deg_entering)
                        break
            # remove x0
            new_N = []
            old_N = new_slack_form.get_N()
            # old_B is also new_B
            old_B = new_slack_form.get_B()
            old_A = new_slack_form.get_A()
            # old_b is also new_b
            old_b = new_slack_form.get_b()
            # construct the new N
            for item in old_N:
                if item != 0:
                    new_N.append(item)

            # the new A
            new_A = np.zeros((len(old_B), len(old_N) - 1))
            # calculate the co in new A
            for index in range(len(new_N)):
                item = new_N[index]
                old_index = self.get_index(old_N, item)
                for index2 in range(len(old_B)):
                    new_A[index2][index] = old_A[index2][old_index]

            # update the objective function
            new_v = 0
            new_c = np.zeros(len(new_N))
            for var_index in range(1, len(c) + 1):
                if var_index in old_B:
                    old_co = c[var_index - 1]
                    index_in_b = self.get_index(old_b, var_index)
                    var_b = old_b[index_in_b]
                    # update the z value
                    new_v = new_v + old_co * var_b
                    # update the value in c
                    for index in range(len(new_N)):
                        # if the variable is in old c
                        if new_N[index] in range(1, len(c) + 1):
                            new_c[index] = c[new_N[index]-1] + (-1.0) * new_A[index_in_b][index] * old_co
                        else:
                            new_c[index] = (-1.0) * new_A[index_in_b][index] * old_co
            final_slack_form = SlackForm(new_N, old_B, new_A, old_b, new_c, new_v)
        return final_slack_form

    """
    The pivot procedure
    """
    def pivot(self, slack_form: SlackForm, l: int, e: int) -> SlackForm:
        old_A = slack_form.get_A()
        old_B = slack_form.get_B()
        old_N = slack_form.get_N()
        old_b = slack_form.get_b()
        old_c = slack_form.get_c()

        # compute new sets of basic and nonbasic variables
        new_N = []
        for item in old_N:
            if item != e:
                new_N.append(item)
        new_N.append(l)

        new_B = []
        for item in old_B:
            if item != l:
                new_B.append(item)
        new_B.append(e)

        # the new matrix A, initialize with all 0
        new_A = np.zeros((len(old_B), len(old_N)))

        # the new small b, initialize with all 0
        new_b = np.zeros(len(old_b))

        # the new c, initialize with all 0
        new_c = np.zeros(len(old_c))

        index_e = self.get_index(old_N, e)
        index_l = self.get_index(old_B, l)
        new_index_e = self.get_index(new_B, e)
        new_index_l = self.get_index(new_N, l)

        b_e = old_b[index_l] / old_A[index_l][index_e]
        new_b[new_index_e] = b_e

        # compute the coefficients of the equation for new basic variable Xe
        for item in range(len(old_N)):
            item_index_new = self.get_index(new_N, old_N[item])
            if new_N[item_index_new] != l:
                new_A[new_index_e][item_index_new] = old_A[index_l][item] / old_A[index_l][index_e]
        new_A[new_index_e][new_index_l] = 1.0 / old_A[index_l][index_e]

        # compute the coefficients of the remaining constraints
        for item in range(len(old_B)):
            item_index_new = self.get_index(new_B, old_B[item])
            if new_B[item_index_new] != e:
                new_b[item_index_new] = old_b[item] - old_A[item][index_e] * b_e
                for item2 in range(len(old_N)):
                    item2_index_new = self.get_index(new_N, old_N[item2])
                    if new_N[item2_index_new] != l:
                        new_A[item_index_new][item2_index_new] \
                            = old_A[item][item2] - old_A[item][index_e] * new_A[new_index_e][item2_index_new]
                new_A[item_index_new][new_index_l] = (-1.0) * old_A[item][index_e] * new_A[new_index_e][new_index_l]

        # compute the objective function
        new_v = slack_form.get_v() + old_c[index_e] * b_e
        for item in range(len(old_N)):
            item_index_new = self.get_index(new_N, old_N[item])
            if new_N[item_index_new] != l:
                new_c[item_index_new] = old_c[item] - old_c[index_e] * new_A[new_index_e][item_index_new]
        new_c[new_index_l] = (-1.0) * old_c[index_e] * new_A[new_index_e][new_index_l]
        new_slack_form = SlackForm(new_N, new_B, new_A, new_b, new_c, new_v)
        return new_slack_form

    """
    The main procedure(pseudo code from line 3 to line 12)
    """
    def simplex_main(self, slack_form: SlackForm):
        # let delta be a new vector of length m, initialize with infinity
        delta = np.full(len(slack_form.get_B()), float('inf'))
        while self.is_slack_form_c_has_positive(slack_form):
            slack_form_A = slack_form.get_A()
            slack_form_B = slack_form.get_B()
            slack_form_b = slack_form.get_b()
            max_idx = self.get_largest_positive_in_c(slack_form)
            for item_index in range(len(slack_form_B)):
                if slack_form_A[item_index][max_idx] > 0:
                    delta[item_index] = slack_form_b[item_index] / slack_form_A[item_index][max_idx]
                else:
                    delta[item_index] = float('inf')
            min_delta_index = 0
            min_delta = float('inf')
            for index in range(len(delta)):
                if delta[index] < min_delta:
                    min_delta = delta[index]
                    min_delta_index = index
            # unbounded
            if min_delta == float('Inf'):
                return None
            else:
                e_value = int(slack_form.get_N()[max_idx])
                l_value = int(slack_form_B[min_delta_index])
                slack_form = self.pivot(slack_form, l_value, e_value)
        return slack_form

    """
    The main procedure(pseudo code from line 13 to line 17)
    """
    def simplex_get_result(self, slack_form: SlackForm):
        resultArr = np.zeros(len(slack_form.get_N()) + len(slack_form.get_B()) + 1)
        for index in range(0, len(resultArr)):
            if index in slack_form.get_B():
                b_index = self.get_index(slack_form.get_B(), index)
                resultArr[index] = slack_form.get_b()[b_index]
            else:
                resultArr[index] = 0
        # the result contains x0.
        return resultArr, slack_form

    """
    for a given value xi, find out the index of xi within an array
    the array could be N, B, A, b, c
    """
    @staticmethod
    def get_index(arr: list, value: int) -> int:
        for idx, val in enumerate(arr):
            if val == value:
                return idx
        return -1

    """
    prints the slack form out
    """
    @staticmethod
    def print_slack_form(slack_form: SlackForm):
        np.set_printoptions(formatter={'float': '{: 0.6f}'.format})
        print("A: ", slack_form.get_A())
        print("b: ", slack_form.get_b())
        print("c: ", slack_form.get_c())
        print("N: ", slack_form.get_N())
        print("B: ", slack_form.get_B())
        v = slack_form.get_v()
        if type(v) == np.ndarray:
            v = v[0]
        v = round(v, 6)
        print("v: ", v)

    """
    check if there is a positive number in c
    if so, then the slack form still needs a pivot
    """
    @staticmethod
    def is_slack_form_c_has_positive(slack_form: SlackForm) -> bool:
        c = slack_form.get_c()
        for val in c:
            if val > 0:
                return True
        return False

    """
    return the index of the value in c which has largest positive co
    """
    def get_largest_positive_in_c(self, slack_form: SlackForm) -> int:
        assert self.is_slack_form_c_has_positive(slack_form)
        c = slack_form.get_c()
        max_value = 0
        max_idx = -1
        for idx in range(len(c)):
            if c[idx] > max_value:
                max_value = c[idx]
                max_idx = idx
        return max_idx

    """
    return the min value and its index within b
    a sub-procedure of initialize-simplex
    """
    @staticmethod
    def get_min_index_and_value_in_b(standard_form: StandardForm) -> tuple:
        b = standard_form.get_b()
        min_value = float('Inf')
        min_index = 0
        for index in range(len(b)):
            if b[index] < min_value:
                min_value = b[index]
                min_index = index
        return min_value, min_index
