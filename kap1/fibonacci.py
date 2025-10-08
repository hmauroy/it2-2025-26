"""
Genererer fibonacci-tall n.
"""

def fibonacci(n):
    """Genererer Fibonacci-sekvensen opp til det n-te tallet og returnerer det."""
    a, b = 0, 1
    for i in range(10):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    nummer = 8
    print(f"fibonacci-tall nr. {nummer} er {fibonacci(nummer)}")