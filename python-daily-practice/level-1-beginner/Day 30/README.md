# Day 30: Parameters and return values

> Estimated time: 30-45 minutes

## Goal

By the end of today you can write a function with **default parameters**, and call it in different ways: with positional arguments, with some arguments left out, and with keyword arguments.

## Concepts

- Parameters are the names a function receives: `def calculate_fees(tuition, transport=0, discount=0):`
- A **default value** (`transport=0`) is used when the caller leaves that argument out
- **Positional** calls give values in order: `calculate_fees(45000, 12000)`
- **Keyword** calls name the parameters: `calculate_fees(45000, discount=5)`
- `return` sends the answer back (Day 29)

Useful docs: [Default argument values](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values) · [Keyword arguments](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)

## Scenario

The **Mavuno School** bursar calculates a parent's fees in many situations: tuition only, tuition and transport, with or without a discount. One function should handle all of them, so that every part of the school system uses the same rule.

## Task

In `day_30.py`, write the function:

```python
def calculate_fees(tuition, transport=0, discount=0):
```

- `tuition` and `transport` are amounts in KES. `transport` defaults to `0`.
- `discount` is a **percentage**: `5` means 5%. It defaults to `0`.
- It **returns** the amount to pay as a float: `(tuition + transport)` minus the discount percentage of that sum.

Then, in `main()`, call it in **three different ways** and print each result:

1. tuition only: `calculate_fees(45000)`
2. tuition and transport: `calculate_fees(45000, 12000)`
3. with a discount, using **keyword** arguments: `calculate_fees(45000, 12000, discount=5)`, and also tuition and discount without transport: `calculate_fees(45000, discount=5)`

## Examples

```python
>>> calculate_fees(45000)
45000.0
>>> calculate_fees(45000, 12000)
57000.0
>>> calculate_fees(45000, discount=5)
42750.0
>>> calculate_fees(45000, 12000, discount=5)
54150.0
>>> calculate_fees(tuition=45000, transport=12000, discount=10)
51300.0
```

## How to do it

1. Open `day_30.py`. The function header is given. Read its docstring.
2. **Subtotal first:** `subtotal = tuition + transport`.
3. **Discount amount:** `subtotal * discount / 100`. Return `subtotal` minus that amount. Make sure the result is a float (dividing by `100` already gives one).
4. **Return, do not print**, inside the function.
5. **Call it in `main()`** in the ways listed and print each result with a label so you can see which call gave which answer.
6. **Check by hand:** 57,000 with a 5% discount is 57,000 - 2,850 = 54,150. Does your output agree?
7. **Experiment:** what happens if you call `calculate_fees(45000, 5)`? Is the `5` the transport or the discount? Write your answer in `NOTES.md`: this is why keyword arguments help.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 30/day_30.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] `calculate_fees` has the three parameters with the defaults described
- [ ] It returns the correct amount for all the examples, and does not print
- [ ] `main()` calls it in at least three different ways and prints the results
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Return `0` if the discount is below 0 or above 100 (invalid).
- Add a parameter `terms=1` that multiplies the fees by the number of terms.
