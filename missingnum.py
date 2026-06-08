import sys

def missing():
    data = sys.stdin.read().split()

    if not data:
        return

    