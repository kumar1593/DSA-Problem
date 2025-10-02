# Find maximum element in an array

def find_max(arr):
    return max(arr)

if __name__ == "__main__":
    n = int(input("Enter size of array: "))
    arr = list(map(int, input("Enter elements: ").split()))
    
    print("Maximum element:", find_max(arr))
