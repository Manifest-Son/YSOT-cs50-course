"""Day 30: Parameters and return values -- calculate_fees with default parameters.

Run it from the python-daily-practice/ folder:

    python "level-1-beginner/Day 30/day_30.py"

The full instructions are in README.md (same folder).
"""


def calculate_fees(tuition, transport=0, discount=0):
    """Return the fees to pay, in KES, as a float.

    tuition   -- the tuition fee
    transport -- the transport fee (default 0)
    discount  -- a percentage taken off the total, e.g. 5 means 5% (default 0)

    Examples:
        >>> calculate_fees(45000)
        45000.0
        >>> calculate_fees(45000, 12000, discount=5)
        54150.0
    """
    # TODO 1: work out the subtotal (tuition + transport)
    # TODO 2: work out the discount amount (the discount percentage of the subtotal)
    # TODO 3: return the subtotal minus the discount amount
    raise NotImplementedError


def main():
    # Call calculate_fees in three different ways and print each result with a label.

    # 1. tuition only
    # print("Tuition only:", calculate_fees(45000))

    # 2. tuition and transport

    # 3. with a discount, using keyword arguments (with and without transport)
    pass


if __name__ == "__main__":
    main()
