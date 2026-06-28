from quant_eng.math.gaussian import solve
def main():
    A = [
        [2.0, 1.0],
        [1.0, 3.0]
    ]

    b = [5.0, 6.0]

    solution = solve(A, b)

    print("Coefficient Matrix (A):")
    for row in A:
        print(row)

    print("\nVector (b):")
    print(b)

    print("\nSolution:")
    print(solution)


if __name__ == "__main__":
    main()

