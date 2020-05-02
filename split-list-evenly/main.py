#!/usr/bin/env python3

def _which_is_smaller(l, r):
    sum_l = sum(l)
    sum_r = sum(r)

    if sum_l > sum_r:
        return 'left'

    if sum_l < sum_r:
        return 'right'

    return None

def find_best_splits(items):
    assert len(items) >= 2, \
        "input must contain at least two elements"

    # initialize left and right buckets
    items = list(items)
    l = [] # left
    r = [] # right

    # it's always safe to assume that either bucket

    while items:
        print("\n".join((
            "l: {}".format(l),
            "r: {}".format(r),
            "items: {}".format(items),
        )))
        smaller = _which_is_smaller(l, r)

        # only one item left, it goes to the smaller bucket
        # ...but if both buckets are equal size, there are two solutions!
        if len(items) == 1:
            if smaller == 'left':
                l.append(items.pop())
                return (len(l),)
            elif smaller == 'right':
                r.insert(0, items.pop())
                return (len(l),)
            else:
                return (len(l), len(l) + 1)

        # if there are at least two items left, just give the next item to the smaller bucket.
        # grab this next item from the smaller bucket's end of the list.
        # if the buckets are equal size, default to grabbing from the left (could grab from either end).
        if smaller == 'left' or smaller is None:
            l.append(items.pop(0))
        elif smaller == 'right':
            r.append(items.pop())
        else:
            raise Exception("unsupported smaller: {}".format(smaller))

    return len(l)


def run_tests():
    test_data = (
        # input list, output list
        ((1, 2, 3), (2)),
        ((3, 2, 1), (1)),
        ((1, 5, 3, 2, 4), (2, 3)),
        ((1, 2, 4, 8, 16), (4)),
        ((1, 1, 1, 1, 1), (2, 3)),
    )

    for (input_, exp_output_) in test_data:
        obs_output_ = find_best_splits(input_)
        assert obs_output_ == exp_output_, "\n".join((
            "input: {}".format(input_),
            "expected output: {}".format(exp_output_),
            "observed output: {}".format(obs_output_),
        ))


if __name__ == '__main__':
    run_tests()
