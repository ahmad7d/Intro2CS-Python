from itertools import combinations


class Node:
    def __init__(self, data, positive_child=None, negative_child=None):
        self.data = data
        self.positive_child = positive_child
        self.negative_child = negative_child


class Record:
    def __init__(self, illness, symptoms):
        self.illness = illness
        self.symptoms = symptoms


def parse_data(filepath):
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    def __init__(self, root):
        self.root = root

    def diagnose(self, symptoms):
        node = self.root  # copy root

        # keep going in decision tree till reaching a leaf
        while not is_leaf(node):
            if node.data in symptoms:
                node = node.positive_child
            else:
                node = node.negative_child
        return node.data  # leaf is answer so return it

    def calculate_success_rate(self, records):
        if len(records) == 0:  # if no record is in list
            raise ValueError('No records!')

        success_count = 0  # no success at start

        # iterate over all records and check if the illnes is same in the decision tree
        for record in records:
            if record.illness == self.diagnose(record.symptoms):
                success_count += 1
            # return success rate
        return success_count / len(records)

    def all_illnesses(self):
        # count for every illness how many times it appeared
        illnesses_with_count = count_list_elements(get_all_leaves(self.root))

        # return illnesses sorted by frequency
        result = [elem[0] for elem in sorted(illnesses_with_count.items(), key=lambda elem: elem[1])]
        result.reverse()
        return result

    def paths_to_illness(self, illness):
        return get_paths_to_illness(self.root, illness)

    def minimize(self, remove_empty=False):
        if remove_empty:
            self.root = remove_all_none_symptoms(self.root)
        self.root = remove_nonessacry_nodes(self.root)


def remove_nonessacry_nodes(root):
    if not is_leaf(root):
        root.positive_child = remove_nonessacry_nodes(root.positive_child)
        root.negative_child = remove_nonessacry_nodes(root.negative_child)
    return remove_nonessacry_nodes_helper(root)

def remove_nonessacry_nodes_helper(root):
    if root is not None and not is_leaf(root) and equal_nodes(root.positive_child, root.negative_child):
        return root.positive_child
    return root


def equal_nodes(node1, node2):
    if node1.data == node2.data:
        if is_leaf(node1) and is_leaf(node2):
            return True
        return (equal_nodes(node1.positive_child, node2.positive_child) and
                equal_nodes(node1.negative_child, node2.negative_child))
    return False


def remove_all_none_symptoms(root):
    if not is_leaf(root):
        root.negative_child = remove_all_none_symptoms(root.negative_child)
        root.positive_child = remove_all_none_symptoms(root.positive_child)
        if all_leaves_are_none(root):
            return Node(None)
        elif all_leaves_are_none(root.positive_child):
            return root.negative_child
        elif all_leaves_are_none(root.negative_child):
            return root.positive_child
    return root


def all_leaves_are_none(node):
    if is_leaf(node):
        if node.data is None:
            return True
        return False

    return all_leaves_are_none(node.positive_child) and all_leaves_are_none(node.negative_child)


def get_paths_to_illness(node, illness, path=None):
    if path is None:
        path = []  # set path is an empty one

    if is_leaf(node):
        if illness == node.data:
            return [path]  # if leaf is the illness then return the path
        return []  # leaf is not the illness so we don't need to include its path

    # return list of all paths to the illness
    return (get_paths_to_illness(node.positive_child, illness, path=path + [True]) +
            get_paths_to_illness(node.negative_child, illness, path=path + [False]))


def count_list_elements(l):
    d_count = {}  # empty dictionary
    for elem in l:
        if elem in d_count:  # if element is a key in dictionary then it was found before so add 1
            d_count[elem] += 1
        else:  # first time found so it will be 1
            d_count[elem] = 1
    return d_count


def get_all_leaves(root):
    # if node is leaf then return its data
    if is_leaf(root):
        if root.data is None:
            return []
        return [root.data]
    # return left and right child data appended together
    return get_all_leaves(root.positive_child) + get_all_leaves(root.negative_child)


def is_leaf(node):
    return node.negative_child is None and node.positive_child is None


def build_tree(records, symptoms):
    root = build_descision_tree(symptoms)  # build a decision tree with no answer
    add_records_to_tree(root, records)  # add answers to descision tree
    return Diagnoser(root)  # create diagnoser for it


def add_records_to_tree(root, records, path=None):
    if path is None:
        path = []
    if root.data is None:  # we reached a leaf so we find the most relevant record for it
        root.data = get_most_relevant_record(records, path)
    else:
        # check till reaching a leaf (negative and positive children)
        add_records_to_tree(root.positive_child, records, path=path + [(root.data, True)])
        add_records_to_tree(root.negative_child, records, path=path + [(root.data, False)])


def get_most_relevant_record(records, symptoms_path):
    illnes_count = []  # counter for records how many true symptoms are there
    for record in records:
        if type(record) != Record:
            raise TypeError('Record is not correct!')
        for symptom in symptoms_path:
            if symptom[1] is True and symptom[0] not in record.symptoms \
                    or symptom[1] is False and symptom[0] in record.symptoms:
                break
        else:
            illnes_count.append(record.illness)
    if len(illnes_count) == 0:
        return None
    result = sorted(set(illnes_count), key=lambda ele: illnes_count.count(ele))
    result.reverse()
    return result[0]


def build_descision_tree(symptoms):
    if len(symptoms) == 0:  # if there is no symptom left then this is a leaf
        return Node(None)
    if type(symptoms[0]) != str:
        raise TypeError('Symptom is not correct')
    root = Node(symptoms[0])  # create root and its children
    root.positive_child = build_descision_tree(symptoms[1:])
    root.negative_child = build_descision_tree(symptoms[1:])
    return root


def optimal_tree(records, symptoms, depth):
    if depth > len(records) or depth < 0:
        raise ValueError('Incorrect depth!')
    if type(symptoms[0]) != str:
        raise TypeError('Symptom is not correct')
    best_tree = None
    best_success_rate = 0
    for sub_symptoms in combinations(symptoms, depth):
        tree = build_tree(records, sub_symptoms)
        success_rate = tree.calculate_success_rate(records)
        if success_rate > best_success_rate:
            best_tree = tree
            best_success_rate = success_rate
    return best_tree


if __name__ == "__main__":

    # Manually build a simple tree.
    #                cough
    #          Yes /       \ No
    #        fever           healthy
    #   Yes /     \ No
    # influenza   cold
    #
    flu_leaf = Node("influenza", None, None)
    cold_leaf = Node("cold", None, None)
    inner_vertex = Node("fever", flu_leaf, cold_leaf)
    healthy_leaf = Node("healthy", None, None)
    root = Node("cough", inner_vertex, healthy_leaf)

    diagnoser = Diagnoser(root)

    # Simple test
    diagnosis = diagnoser.diagnose(["cough"])
    if diagnosis == "cold":
        print("Test passed")
    else:
        print("Test failed. Should have printed cold, printed: ", diagnosis)

# Add more tests for sections 2-7 here.

# from itertools import combinations
# a = [1,2,3,4]
# for i in combinations(a, 2):
#     print(i)
