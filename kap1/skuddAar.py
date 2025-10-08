def skuddaar(aar):
    """Sjekker om et gitt år er et skuddår."""
    if (aar % 4 == 0 and aar % 100 == 0) and (aar % 400 == 0):
        return False
    elif (aar % 4 == 0 and aar % 100 != 0) or (aar % 400 == 0):
        return True
    return False


if __name__ == "__main__":
    aar = 2004
    print(f"Er {aar} et skuddår? {skuddaar(aar)}")