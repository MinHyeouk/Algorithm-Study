def solution(sizes):
    sizes = [sorted(a, reverse=True) for a in sizes]
    max_w = max([a[0] for a in sizes])
    max_h = max([a[1] for a in sizes])
    return max_w * max_h

    # max(max(x) for x in sizes) * max(min(x) for x in sizes)