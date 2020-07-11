from pyqubo import Array, SubH

N = [1, 2, 4, 7]
s = Array.create("s", shape=len(N), vartype="SPIN")

H = SubH(s.dot(N), label="diff")
model = H.compile()
qubo, offset = model.to_qubo()

sol = {"s[0]": -1, "s[1]": -1, "s[2]": -1, "s[3]": 1}

decoded_sol = model.decode_sample(sol, vartype="SPIN")
print("diff =", decoded_sol.subh_values)
