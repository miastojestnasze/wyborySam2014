from models import Election


def find_idx_dict(dict_arr, val, property):
    if len(dict_arr) == 0:
        return -1

    for idx, el in enumerate(dict_arr):
        if el[property] == val:
            return idx
    return -1


def create_district(tree, circuit):
    idx_district = find_idx_dict(tree, circuit.district, 'name')
        
    if idx_district == -1:
        district = {
            'name': circuit.district, 
            'url': circuit.election_type + '/district-' + circuit.district + '/', 
            'children': []
        }
        tree.append(district)
        return tree[len(tree)-1]
    else:
        return tree[idx_district]


def create_circle(tree, circuit, is_first_child=False):
    children = tree if True == is_first_child else tree['children']
    url = circuit.election_type + '/' if True == is_first_child else tree['url']
    idx_circle = find_idx_dict(children, str(circuit.number_of_district), 'name')
    if idx_circle == -1:
        new_circle = {
            'name': str(circuit.number_of_district),
            'url': url + 'circle-' + str(circuit.number_of_district) + '/',
            'children': []
        }
        children.append(new_circle)
        return children[len(children)-1]
    else:
        return children[idx_circle]


def create_circuit(tree, circuit, is_first_child=False):
    children = tree if True == is_first_child else tree['children']
    url = circuit.election_type + '/' if True == is_first_child else tree['url']
    new_circuit = {
        'name': str(circuit.number_of_electoral_circuit),
        'url': url + 'circuit-' + str(circuit.number_of_electoral_circuit) + '/',
    }
    children.append(new_circuit)
    return children[len(children)-1]


def without_districts(tree, circuit):
    circle = create_circle(tree, circuit, True)
    circuit = create_circuit(circle, circuit)
    return tree


def without_circles(tree, circuit):
    district = create_district(tree, circuit)
    circuit = create_circuit(district, circuit)
    return tree


def full_tree(tree, circuit):
    district = create_district(tree, circuit)
    circle = create_circle(district, circuit)
    circuit = create_circuit(circle, circuit)
    return tree


def get_election_tree(type):
    tree = []
    for c in Election.objects.filter(election_type=type).distinct('number_of_electoral_circuit'):
        if 'district' == type:
            tree = full_tree(tree, c)
        elif 'city_council' == type:
            tree = without_districts(tree, c)
        elif type in ['president_first_turn', 'president_second_turn', 'voivodeship']:
            tree = without_circles(tree, c)
    return tree
