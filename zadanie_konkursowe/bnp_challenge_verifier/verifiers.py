from bnp_challenge_verifier.utils import _get_hash


def _verify_solution(counts: dict, task_id: int, quiet=False):
    COUNT_LENGTH = {1:5, 2:7, 3:8, 4:9}
    # seeds: 40 42 45 46
    HASH = {1: "813832628aafe978f64aac7c56c8e2a345b89c12cddbd3fcc09f6a6e95478ab10ce5c1def2f836a75ff8675bbe1b44946ec3662459c936a3dde6f53d45ba217b",
            2: "c607f4936a9bb12ca87ab45d1b85b5cdaeaf819c5ccd16940f8d45d3c147692189b8807c2154c675b76e0c040224b3a519ed66cd56b2b32eb23a6fca4d05ebd7",
            3: "7b57295e95bcb3780d9ab5f95d12dfc14ba318f5da3efdf630c66d95793231ca72512cbed85faad3e9eccb41b166f829353923761090a6e3890ea3fbdb443d83",
            4: "36a334f95b3a6bf46edf34bc184b3f9d0296da2e8ba6d4726a07971328d564cabf4b0844d94708673dfa43b3f6b848036cf92deeada91e27e2a716f998d4f9cd"} 

    if not isinstance(counts, dict):
        print("Nie wprowadziłeś wyników pomiaru (błędny typ).")
        return False
    if not all(isinstance(k, str) for k in counts.keys()):
        print("Nie wprowadziłeś wyników pomiaru (błędny typ).")
        return False
    if not all(isinstance(v, int) for v in counts.values()):
        print("Nie wprowadziłeś wyników pomiaru (błędny typ).")
        return False

    if not all(len(k) == COUNT_LENGTH[task_id] for k in counts.keys()):
        if not quiet:
            print("Nie wprowadziłeś poprawnych wyników pomiaru (być może dodałeś lub usunąłeś pomiar kubitu?)")
        return False

    if _get_hash(counts) == HASH[task_id]:
        if not quiet:
            print("Gratulacje, twój obwód wygenerował poprawne wyniki pomiaru! Upewnij się, że twój obwód spełnia pozostałe wymogi zadania.")
        return True
    else:
        if not quiet:
            print("Niestety, twoje wyniki pomiaru nie są poprawne, sprawdź swój obwód!")
        return False
     
def verify_solution1(counts):
    _verify_solution(counts, 1)

def verify_solution2(counts):
    _verify_solution(counts, 2)

def verify_solution3(counts):
    _verify_solution(counts, 3)

def verify_solution4(counts):
    _verify_solution(counts, 4)