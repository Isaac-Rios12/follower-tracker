from typing import Set, Tuple

def compare_followers(
        previous: Set[str],
        current: Set[str]
) -> Tuple[Set[str], Set[str]]:
    ''' 
    Compara 2 capturas de seguidores
    '''
    unfollowers = previous - current
    new_followers = current - previous

    return unfollowers, new_followers