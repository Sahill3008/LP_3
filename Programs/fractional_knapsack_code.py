
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fracknapsack(W, arr):
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)
    final_value = 0.0

    for item in arr:
        if item.weight <= W:
            W -= item.weight
            final_value += item.profit
        else:
            final_value += item.profit * W / item.weight
            break

    return final_value

if __name__ == "__main__":
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    max_val = fracknapsack(W, arr)
    print("Maximum profit:", max_val)
