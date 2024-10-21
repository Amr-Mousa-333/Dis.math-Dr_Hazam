def print_union(amor1, amor2, name1, name2):
    union_set = set(amor1).union(set(amor2))  # اتحاد
    print(f"Union of {name1} and {name2}: ", " ".join(map(str, union_set)))

def print_intersection(amor1, amor2, name1, name2):
    intersection_set = [num for num in amor1 if num in amor2]  # التقاطع
    print(f"Intersection of {name1} and {name2}: ", " ".join(map(str, intersection_set)))

def print_difference(amor1, amor2, name1, name2):
    difference_set = [num for num in amor1 if num not in amor2]  # الفرق
    print(f"Difference of {name1} and {name2}: ", " ".join(map(str, difference_set)))

def print_complement(amor1, universal_set, name):
    complement_set = [num for num in universal_set if num not in amor1]  # المكمله
    print(f"Complement of {name}: ", " ".join(map(str, complement_set)))

def check_subset(subset, amor2, subset_name, superset_name):
    is_subset = all(num in amor2 for num in subset)  # الجزء
    print(f"Is {subset_name} a subset of {superset_name}? {'Yes' if is_subset else 'No'}")

def main():
    universal_set = [1, 2, 3, 4, 5, 6, 7, 8]
    A = [2, 4, 8, 6, 6]
    B = [3, 4, 5, 6]
    C = [7, 8]
    D = [1, 3, 5, 7]
    
    # test
    print_union(A, B, "A", "B")
    print_intersection(C, D, "C", "D")
    print_difference(A, B, "A", "B")
    print_complement(A, universal_set, "A")
    check_subset(A, B, "A", "B")

if __name__ == "__main__":
   main()
