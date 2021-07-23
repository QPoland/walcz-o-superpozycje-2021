import json
from bnp_challenge_verifier.graders import grade_circuit
from bnp_challenge_verifier.verifiers import _verify_solution
from bnp_challenge_verifier.utils import _counts_to_str, _get_hash

def create_submission(qc, counts, user_id):
    filename = "zgloszenie_konkursowe.json"

    score = grade_circuit(qc, quiet=True)
    if score == None:
        return None

    if not _verify_solution(counts, 4, quiet=True):
        print("Nie podałeś poprawnego rozwiązania (zweryfikuj wyniki pomiaru)")
        return None

    if not isinstance(user_id, str):
        print("ID użytkownika powinno być typu string.")
        return None

    if len(user_id) == "":
        print("Nie podałeś ID użytkownika")
        return None

    data = {"task_id": 4, 
            "user_id": user_id, 
            "score": str(score),
            "counts": str(_counts_to_str(counts)),
            "hash": _get_hash(counts)}

    
    json_string = json.dumps(data)
    json_file = open(filename, "w")
    json_file.write(json_string)
    json_file.close()

    print("Wygenerowaliśmy plik do wysłania o nazwie: {}. Nie zapomnij wysłać notebooka z rozwiązaniem!".format(filename))
