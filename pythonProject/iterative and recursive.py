# RECURSIVE
def walk(steps):
    if steps == 0:
        return
    walk(steps - 1)
    print(f"you take step #{steps}")
walk(20)