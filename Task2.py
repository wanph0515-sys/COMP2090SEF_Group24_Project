class Graph:
    
    def __init__(self):
        self.nodes = {} 
    
    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = []
    
    def connect(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        if node2 not in self.nodes[node1]:
            self.nodes[node1].append(node2)
        if node1 not in self.nodes[node2]:
            self.nodes[node2].append(node1)
    
    def get_adjacent(self, node):
        return self.nodes.get(node, [])
    
    def dfs(self, start):
        seen = set()
        path = []
        
        def _dfs(current):
            if current not in seen:
                seen.add(current)
                path.append(current)
                for neighbor in self.nodes[current]:
                    _dfs(neighbor)
        
        _dfs(start)
        return path
    
    def show(self):
        for node, neighbors in self.nodes.items():
            print(f"{node}: {neighbors}")

def _adjust_heap(data, size, idx, sort_key=None):
    
    max_idx = idx
    left = 2 * idx + 1
    right = 2 * idx + 2
    
    if left < size:
        left_val = data[left][sort_key] if sort_key else data[left]
        current_val = data[idx][sort_key] if sort_key else data[idx]
        if left_val > current_val:
            max_idx = left
    
    if right < size:
        right_val = data[right][sort_key] if sort_key else data[right]
        max_val = data[max_idx][sort_key] if sort_key else data[max_idx]
        if right_val > max_val:
            max_idx = right
    
    if max_idx != idx:
        data[idx], data[max_idx] = data[max_idx], data[idx]
        _adjust_heap(data, size, max_idx, sort_key)

def heap_sort(data, key=None):
    arr = data.copy()
    n = len(arr)
    
    if n <= 1:
        return arr

    for i in range(n // 2 - 1, -1, -1):
        _adjust_heap(arr, n, i, key)
    
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _adjust_heap(arr, i, 0, key)
    
    return arr

def test_graph_interactive():
    print("\n" + "-" * 40)
    print("Graph Testing")
    print("-" * 40)
    
    graph = Graph()
    edges_added = False
    
    print("Build your graph (enter 'stop' when done)")
    print("Example: A B  (creates edge between A and B)")
    
    while True:
        user_input = input("Add edge: ").strip()
        if user_input.lower() in ['stop', 'done', 'exit', '']:
            break
            
        parts = user_input.split()
        if len(parts) < 2:
            print("Need two nodes. Example: A B")
            continue
            
        node1, node2 = parts[0], parts[1]
        graph.connect(node1, node2)
        edges_added = True
        print(f"Linked {node1} with {node2}")
    
    if not edges_added:
        print("No edges added. Using default graph...")
        graph.connect('A', 'B')
        graph.connect('A', 'C')
        graph.connect('B', 'D')
        print("Default graph created")

    print("\nYour graph:")
    graph.show()
    
    if graph.nodes:
        start = input("\nStart DFS from which node? ").strip()
        if start in graph.nodes:
            result = graph.dfs(start)
            print(f"DFS from {start}: {result}")
        else:
            print(f"Node '{start}' not found. Available nodes: {list(graph.nodes.keys())}")
            
        check_node = input("Check neighbors for which node? ").strip()
        if check_node in graph.nodes:
            neighbors = graph.get_adjacent(check_node)
            print(f"Neighbors of {check_node}: {neighbors}")

def test_heap_sort_interactive():
    print("\n" + "-" * 40)
    print("Sort Testing")
    print("-" * 40)
    print("\n1. Sort numbers")
    numbers_input = input("Numbers to sort (space separated): ").strip()
    
    if numbers_input:
        try:
            numbers = [int(x) for x in numbers_input.split()]
            print(f"Before: {numbers}")
            sorted_nums = heap_sort(numbers)
            print(f"After:  {sorted_nums}")
        except:
            print("Invalid numbers. Example: 5 2 9 1")
    else:
        default_nums = [5, 2, 9, 1, 6]
        print(f"Using example: {default_nums}")
        sorted_default = heap_sort(default_nums)
        print(f"Sorted: {sorted_default}")
    
    print("\n2. Sort student grades")
    students = []
    print("Add students (name score), 'stop' to finish")
    print("Example: Alice 85")
    
    while True:
        entry = input("Student: ").strip()
        if entry.lower() in ['stop', 'done', '']:
            break
            
        parts = entry.split()
        if len(parts) >= 2:
            try:
                name = parts[0]
                score = int(parts[1])
                students.append({'name': name, 'grade': score})
                print(f"Added {name}: {score}")
            except:
                print("Invalid score. Use: Name Number")
        else:
            print("Need name and score")
    
    if students:
        print("\nStudents (unsorted):")
        for s in students:
            print(f"  {s['name']}: {s['grade']}")
            
        sorted_students = heap_sort(students, key='grade')
        print("\nStudents (by grade):")
        for s in sorted_students:
            print(f"  {s['name']}: {s['grade']}")
    else:
        print("No students added")

def main():
    print("Algorithm Tester")
    print("=" * 30)
    
    while True:
        print("\nOptions:")
        print("1 - Test Graph")
        print("2 - Test Sorting") 
        print("3 - Test Both")
        print("0 - Quit")
        
        choice = input("Choose: ").strip()
        
        if choice == '1':
            test_graph_interactive()
        elif choice == '2':
            test_heap_sort_interactive()
        elif choice == '3':
            test_graph_interactive()
            test_heap_sort_interactive()
        elif choice in ['0', 'q', 'quit']:
            print("Bye!")
            break
        else:
            print("Choose 1, 2, 3, or 0")

if __name__ == "__main__":
    main()
