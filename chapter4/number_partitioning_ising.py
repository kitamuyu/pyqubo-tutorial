from pyqubo import Spin, solve_ising


def H_number_partitioning(S):
    s = [Spin(f"s[{i}]") for i in range(len(S))]
    H = sum(ni*si for ni, si in zip(S, s))**2
    return H


S = [1, 2, 4, 7]

N = len(S)

H = H_number_partitioning(S)

model = H.compile()

linear, quad, offset = model.to_ising()

sol = solve_ising(linear, quad)

print("linear =", linear)
print("quad =", quad)

print("S_1 =", [S[i] for i in range(N) if sol[f"s[{i}]"] == 1])
print("S_2 =", [S[i] for i in range(N) if sol[f"s[{i}]"] == -1])
