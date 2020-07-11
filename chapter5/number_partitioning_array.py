from pyqubo import Array, solve_qubo

N = [1, 2, 4, 7]
s = Array.create("s", shape=len(N), vartype="SPIN")

H = s.dot(N)
print(H)

model = H.compile()
qubo, offset = model.to_qubo()
sol = solve_qubo(qubo)
decoded_sol = model.decode_solution(sol, vartype="SPIN")
sol_s = decoded_sol.array_["s"]
