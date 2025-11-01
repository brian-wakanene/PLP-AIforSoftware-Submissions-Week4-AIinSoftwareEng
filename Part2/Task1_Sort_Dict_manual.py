#Sample data

sample_data = [
    {'name': 'Wakanene',   'age': 24, 'score': 85},
    {'name': 'Purity',     'age': 25, 'score': 92},
    {'name': 'Annie', 'age': 35, 'score': 88},
    {'name': 'Frank',   'age': 28, 'score': 95},
    {'name': 'Mike',     'age': 22, 'score': 87}
]

def sort_list_of_dicts(data, key, reverse=False):
    sorted_data = data.copy()          
    n = len(sorted_data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            a = sorted_data[j][key]
            b = sorted_data[j + 1][key]
            # decide whether to swap
            if (a > b) if not reverse else (a < b):
                sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]
                swapped = True
        if not swapped:              
            break
    return sorted_data


if __name__ == "__main__":
    print("Original:")
    for d in sample_data:
        print(d)

    print("\nSorted by score (descending):")
    result = sort_list_of_dicts(sample_data, 'score', reverse=True)
    for d in result:
        print(d)