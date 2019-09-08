from operator import attrgetter


def push_locked_to_bottom(seq):
    """Moves all the locked entries in a list of entries to
    the bottom of the list.

    Args:
        seq: The EncEntry list to sort.

    Returns:
        list: Sorted version of the given sequence
    """
    seq.sort(reverse=True, key=attrgetter('locked'))

    return seq
