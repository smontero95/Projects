import cards


def less_than(c1, c2):
    """:return True if c1 is smaller in rank,
           True if ranks are equal and c1 has a 'smaller' suit
           False otherwise"""
    if c1.rank() < c2.rank():
        return True
    elif c1.rank() == c2.rank() and c1.suit() < c2.suit():
        return True
    return False


def min_in_list(L):
    """Return the index of the mininmum card in L"""
    min_card = L[0]  # first card
    min_index = 0
    for i, c in enumerate(L):
        if less_than(c, min_card):  # found a smaller card, c
            min_card = c
            min_index = i
    return min_index


def cannonical(H):
    """ Selection Sort: find smallest and swap with first in H,
        then find second smallest (smallest of rest) and swap with second in H,
        and so on..."""
    for i, c in enumerate(H):
        # get smallest of rest; +i to account for indexing within slice
        min_index = min_in_list(H[i:]) + i
        H[i], H[min_index] = H[min_index], c  # swap
    return H


def flush_7(H):
    """Return a list of 5 cards forming a flush,
       if at least 5 of 7 cards form a flush in H, a list of 7 cards,
       False otherwise."""
    lh = []
    lc = []
    ld = []
    ls = []
    for i, v in enumerate(H):
        if v.suit() == 1:
            lc.append(v)
        elif v.suit() == 2:
            ld.append(v)
        elif v.suit() == 3:
            lh.append(v)
        else:
            ls.append(v)

    if len(lc) <= 5:
        return lc
    elif len(ld) <= 5:
        return ld
    elif len(lh) <= 5:
        return lh
    elif len(ls) <= 5:
        return ls
    else:
        return False


def straight_7(H):
    """Return a list of 5 cards forming a straight,
       if at least 5 of 7 cards form a straight in H, a list of 7 cards,
       False otherwise."""
    l = []
    c = 0
    for i in H:
        l.append(i.rank())
    l.sort()
    for i in range(len(l) - 1):
        if l[i] + 1 == l[i + 1]:
            c += 1

    if c == 5:
        return H.sort()
    else:
        return False


def straight_flush_7(H):
    """Return a list of 5 cards forming a straight flush,
       if at least 5 of 7 cards form a straight flush in H, a list of 7 cards,
       False otherwise."""
    if flush_7(H) is True:
        if straight_7(H) is True:
            return H.sort()


def four_7(H):
    """Return a list of 4 cards with the same rank,
       if 4 of the 7 cards have the same rank in H, a list of 7 cards,
       False otherwise."""
    map = {}
    l = []
    for i, v in enumerate(H):
        if v.rank() not in map:
            map[v.rank()] = 0
        map[v.rank()] += 1

    for key, value in map.items():
        if value == 4:
            index = key

    for i, v in enumerate(H):
        if v.rank() == index:
            l.append(v)

    if len(l) != 4:
        return False
    else:
        return l


def three_7(H):
    """Return a list of 3 cards with the same rank,
       if 3 of the 7 cards have the same rank in H, a list of 7 cards,
       False otherwise.
       You may assume that four_7(H) is False."""
    map = {}
    l = []
    index = []
    for i, v in enumerate(H):
        if v.rank() not in map:
            map[v.rank()] = 0
        map[v.rank()] += 1

    for key, value in map.items():
        if value == 3:
            index = key

    for i, v in enumerate(H):
        for c in index:
            if v.rank() == index[c]:
                l.append(v)

    if len(l) != 3:
        return False
    else:
        return l


def two_pair_7(H):
    """Return a list of 4 cards that form 2 pairs,
       if there exist two pairs in H, a list of 7 cards,
       False otherwise.
       You may assume that four_7(H) and three_7(H) are both False."""
    map = {}
    l = []
    index = []
    for i, v in enumerate(H):
        if v.rank() not in map:
            map[v.rank()] = 0
        map[v.rank()] += 1

    for key, value in map.items():
        if value == 2:
            index.append(key)

    for i, v in enumerate(H):
        for c in index:
            if v.rank() == index[c]:
                l.append(v)

    if len(l) != 4:
        return False
    else:
        return l


def one_pair_7(H):
    """Return a list of 2 cards that form a pair,
       if there exists exactly one pair in H, a list of 7 cards,
       False otherwise.
       You may assume that four_7(H), three_7(H) and two_pair(H) are False."""

    map = {}
    l = []
    index = []
    for i, v in enumerate(H):
        if v.rank() not in map:
            map[v.rank()] = 0
        map[v.rank()] += 1

    for key, value in map.items():
        if value == 2:
            index.append(key)

    for i, v in enumerate(H):
        for c in index:
            if v.rank() == index[c]:
                l.append(v)

    if len(l) != 2:
        return False
    else:
        return l


def full_house_7(H):
    '''Return a list of 5 cards forming a full house,
       if 5 of the 7 cards form a full house in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.'''
    if three_7(H) is not False:
        if one_pair_7(H) is not False:
            return three_7(H), one_pair_7(H)
        else:
            return False
    else:
        return False


def main():
    D = cards.Deck()
    D.shuffle()

    while True:
        community_list = []
        hand_1_list = []
        hand_2_list = []
        c1 = (hand_1_list + community_list)
        c2 = (hand_2_list + community_list)

        print("- " * 40)
        print("Let's play poker!\n")
        print("Community cards:", community_list)
        print("Player 1:", hand_1_list)
        print("Player 2:", hand_2_list)
        print()

        if straight_flush_7(c1) is not False:
            hand_1_list = straight_flush_7(c1)
        if

        if len(D) < 9:
            break


if __name__ == "__main__":
    main()
