from pyqubo import UnaryEncInteger, Array, Placeholder, Constraint
from neal import SimulatedAnnealingSampler

v = [5, 8, 3, 2, 8, 4]
w = [3, 5, 2, 1, 3, 2]
W = 12

x = Array.create('x', shape=len(v), vartype='BINARY')

w_int = UnaryEncInteger('w_int', (0, W))

a = Placeholder('a')

H = x.dot(v) + a*Constraint(x.dot(w) - w_int, 'weight')**2

model = H.compile()
a = 1.0
qubo, offset = model.to_qubo(feed_dict={'a': a})
sol = SimulatedAnnealingSampler().sample_qubo(qubo)
print(sol)
# decode_solution = model.decode_sample(
#   sol, feed_dict={'a': a}, vartype='BINARY')
