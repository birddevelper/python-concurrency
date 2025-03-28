import multiprocessing

def compute_square(n):
    return n * n

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    with multiprocessing.Pool(processes=3) as pool:
        results = pool.map(compute_square, numbers)

    print("Squares:", results)
