import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import random
from copy import deepcopy
import pprint

from countries import Australia, Germany

pp = pprint.PrettyPrinter(indent=4)
global assignments
assignments = list()


def plot_country(country, state_colors, save=False, name=""):
    state_dict = country.state_dict
    geojson_file = country.geojson

    plt.rcParams['figure.figsize'] = (9, 6)

    df_country = gpd.read_file(geojson_file)
    ax = df_country.plot(linewidth=0.75, color='white', edgecolor='black')

    for state_abb, state_color in zip(state_colors.keys(), state_colors.values()):
        df_country.loc[df_country['STATE_NAME'] == state_dict[state_abb]].plot(color=state_color, ax=ax)

    plt.axis('off')

    if save:
        plt.savefig(name)
    else:
        plt.show()


def make_constraints_binary(constraints):
    """
    Makes a constraint a binary constraint
    """
    binary_constraints = []
    for state, neighbouring_states in constraints.items():
        for neighbouring_state in neighbouring_states:
            if not (state, neighbouring_state) in binary_constraints and \
                    not (neighbouring_state, state) in binary_constraints:
                binary_constraints.append((state, neighbouring_state))
    return binary_constraints


def ac3(variables, domains, unary_constraints, binary_constraints):
    """

    :param variables: list of variable names, e.g. ['NSW', 'Q', 'NT', ...]
    :param domains: dictionary of domain values for each variable: {'NSW': ['red', 'blue', 'green'], 'Q': ['red', 'blue', 'green'], ...}
    :param unary_constraints: dictionary with unary constraints {'NSW': 'red', 'Q': 'blue', ...]
    :param binary_constraints: list of binary constraints [['Q', 'NSW'], ['NT', 'SA'], ...]
    :return:
    """
    for variable in variables:
        # Make domain consistent with unary constraints
        if variable in unary_constraints.keys():
            domain = [unary_constraints[variable]]
            domains[variable] = domain

    for variable in variables:
        # Make domain consistent with unary constraints
        #if variable in unary_constraints.keys():
        #    domain = [unary_constraints[variable]]
        #    domains[variable] = domain

        worklist = list(filter(lambda binary_constraint: binary_constraint[0] == variable or binary_constraint[1] == variable, binary_constraints))

        while len(worklist) > 0:
            # Select any binary_constraint from the worklist
            binary_constraint = worklist.pop()

            #print(variable)
            domain_y = domains[binary_constraint[0]] if binary_constraint[0] != variable else domains[binary_constraint[1]]

            change, new_domain_x = arc_reduce(binary_constraint, domains[variable], domain_y)
            domains[variable] = new_domain_x
            if change:
                if len(domains[variable]) == 0:
                    return None
                else:
                    worklist += list(filter(lambda new_binary_constraint: (new_binary_constraint[0] == variable and new_binary_constraint[1] != binary_constraint[1]) or
                                                                          (new_binary_constraint[1] == variable and new_binary_constraint[0] != binary_constraint[0]), binary_constraints))

    return domains


def arc_reduce(binary_constraint, domain_x, domain_y):
    change = False
    value_y_found = False
    new_domain_x = []

    for value_x in domain_x:
        for value_y in domain_y:
            if value_x != value_y:
                value_y_found = True
                break

        if value_y_found:
            new_domain_x.append(value_x)
        else:
            change = True

        value_y_found = False

    return change, new_domain_x


def check_validity_assignment(binary_constraints, assignment):
    """
    Checks if an assignment is consistent to binary constraints
    """
    for binary_constraint in binary_constraints:
        if binary_constraint[0] not in assignment or binary_constraint[1] not in assignment:
            continue

        if assignment[binary_constraint[0]] == assignment[binary_constraint[1]]:
            return False
    return True


"""
A CSP is a tuple that consists of:
- List of all variables
- List of domain values
- List of binary constraints
"""


def backtracking_search(csp, mrv=False):
    """
    Main method for backtracking
    """
    global assignments
    assignments = list()
    assignments.append(dict())

    return backtrack(csp, dict(), mrv=mrv)


def select_unassigned_variable(csp, assignment, mrv=False):
    """
    Heuristic to choose which variable to assign a variable next
    """
    if mrv:
        remaining_values = ac3(csp[0], dict(zip(csp[0], [csp[1]]*len(csp[0]))), assignment, csp[2])
        remaining_values = {k: v for k, v in remaining_values.items() if not k in assignment.keys()}
        min_remaining = min(remaining_values.items(), key=lambda x: len(x[1]))
        next_variable = min_remaining[0]
    else:
        unassigned_variables = list(set(csp[0]).difference(set(assignment.keys())))
        # Return just the first unassigned variable
        next_variable = unassigned_variables[0]

    return next_variable


def order_domain_values(var, assignment, domain_values):
    """
    Heuristic to choose which domain value to take next
    """
    random.shuffle(domain_values)
    return domain_values


def backtrack(csp, assignment, mrv=False):
    """
    Recursive backtracking search
    """
    global assignments

    variables = csp[0]
    domain_values = csp[1]
    binary_constraints = csp[2]

    if len(variables) == len(assignment):
        return assignment

    var = select_unassigned_variable(csp, assignment, mrv=mrv)
    for domain_value in order_domain_values(var, assignment, domain_values):
        new_assignment = deepcopy(assignment)
        new_assignment[var] = domain_value
        assignments.append(deepcopy(new_assignment))
        if check_validity_assignment(binary_constraints, new_assignment):
            assignment[var] = domain_value
            result = backtrack(csp, assignment, mrv=mrv)

            if result is not None:
                return result

        assignment.pop(var, None)

    return None


def plot_histogram(xs):
    bins = np.linspace(0, 100, 100)
    for x in xs:
        plt.hist(x, bins=bins, alpha=0.5)

    plt.xlabel("# steps")
    plt.ylabel("# of runs")

    plt.show()


def run_map_coloring(country, mrv=False):
    constraints = country.constraints
    variables = country.variables
    domain_values = ["red", "green", "blue", 'yellow']

    binary_constraints = make_constraints_binary(constraints)

    csp = (variables, domain_values, binary_constraints)

    result = backtracking_search(csp, mrv=mrv)
    return result


def compare_mrv_random(country):
    xs = list()

    for mrv in [True]:
        length_assignments = list()

        for _ in range(100000):
            result = run_map_coloring(mrv=mrv, country=country)
            print(len(assignments))
            length_assignments.append(len(assignments))

        xs.append([length_assignments])

    plot_histogram(xs)


if __name__ == "__main__":
    country = Australia()
    result = run_map_coloring(country=country, mrv=False)

    plot_country(country=country, state_colors=result)
    pp.pprint(assignments)

    #for i, assignment in enumerate(assignments):
    #    plot_country(country=country, state_colors=assignment, save=True, name="img/{}/img{}".format(country.name, str(i).zfill(2)))

    compare_mrv_random(country=country)