from qiskit import QuantumCircuit
from qiskit.compiler import transpile
from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import Unroller
    
def grade_circuit(qc, quiet=False): 
    if not isinstance(qc, QuantumCircuit):
        print("Proszę prześlij obiekt typu QuantumCircuit!")
        return None

    pass_ = Unroller(['u3', 'cx'])
    pm = PassManager(pass_) 
    try:
        qc = transpile(qc, basis_gates=['u3', 'cx']) 
        qc = pm.run(qc)
    except:
        print("Błąd upraszczania obwodu - prawdopodobnie użyłeś niedozwolonych operacji.")
        return None

    ops_dict = qc.count_ops()
    cnot_counter = ops_dict['cx'] if 'cx' in ops_dict.keys() else 0
    u3_counter = ops_dict['u3'] if 'u3' in ops_dict.keys() else 0

    cost = 10*cnot_counter + u3_counter
    if not quiet:
        print("Koszt twojego obwodu wynosi {}.".format(cost))
    return cost