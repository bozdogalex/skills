def median(values):
    """Return the median; caller supplies a sequence of finite real numbers."""
    if len(values) == 0:
        raise ValueError("empty sequence")
    ordered = sorted(values)
    n = len(ordered)
    middle = n // 2
    if n % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2
