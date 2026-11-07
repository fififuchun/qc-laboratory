from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2)
qc.h(0)  # 量子ビット0を重ね合わせにする
qc.cx(0, 1)  # 量子ビット0と1をもつれさせる
qc.measure_all()

sim = AerSimulator()
result = sim.run(transpile(qc, sim), shots=1000).result()
print(qc.draw("text"))
print(result.get_counts())
