def plot_graph(arr: list) -> None:
    """
    Takes in an Array of numbers and plots a graph for it.
    Works by using a Arr[Max] x Arr.Len list.
    Plot for max numbers satisfying the condition else don't plot. 
    """
    m = max(arr)
    for i in range(m, 0, -1):
        for j in arr:
            if j >= i:
                print("*\t", end="")
            else:
                print("\t", end="")
        print()


arr = []
t = int(input("Provide no of Testcases"))
for test in range(t):
    i = int(input())
    arr.append(i)
plot_graph(arr)
