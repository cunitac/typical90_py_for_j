N = int(input())


def rec(result, open_count):
    if len(result) == N:
        if open_count == 0:
            print(result)
        return

    rec(result + '(', open_count + 1)
    if open_count > 0:
        rec(result + ')', open_count - 1)


rec('', 0)
