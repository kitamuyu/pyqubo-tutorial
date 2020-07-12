import neal
from pyqubo import Spin

s1, s2, s3, s4 = Spin('s1'), Spin('s2'), Spin('s3'), Spin('s4')
H = (4*s1 + 2*s2 + 7*s3 + s4)**2
model = H.compile()

bqm = model.to_bqm()

sa = neal.SimulatedAnnealingSampler()
sample_set = sa.sample(bqm, num_reads=10)

print(sample_set)
# print(sample_set.record['sample'])
# print(sample_set.variables)
# print(sample_set.record['energy'])
# print(sample_set.change_vartype('SPIN'))

# ? decoded_samples = model.decode_dimod_sample(sample_set.)
# print(decoded_samples)
