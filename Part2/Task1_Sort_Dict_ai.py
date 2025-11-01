
sample_data = [
    {'name': 'Wakanene',   'age': 24, 'score': 85},
    {'name': 'Purity',     'age': 25, 'score': 92},
    {'name': 'Annie',      'age': 35, 'score': 88},
    {'name': 'Frank',      'age': 28, 'score': 95},
    {'name': 'Mike',       'age': 22, 'score': 87}
]


# 2. AI-Generated sorting function

def sort_list_of_dicts(data, key, reverse=False):
    return sorted(data, key=lambda d: d[key], reverse=reverse)


if __name__ == "__main__":
    print("Original:")
    for person in sample_data:
        print(f"  {person}")

    print("\nSorted by score (descending):")
    result = sort_list_of_dicts(sample_data.copy(), 'score', reverse=True)
    for person in result:
        print(f"  {person}")