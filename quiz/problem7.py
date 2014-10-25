def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    if n == 0:
        return True
        
    if n < 0:
        return False
        
    return McNuggets(n-6) or McNuggets(n-9) or McNuggets(n-20)
