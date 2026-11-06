# Day 5: Fee receipt generator

> Estimated time: 45-60 minutes

## Goal

By the end of today you can combine variables, operators and `input()` in one program and print a neatly aligned receipt.

## Concepts

- Everything from Days 1-4: `print`, variables, arithmetic, `input()`, `int()` / `float()`
- Percentages: 5% of an amount is `amount * 0.05`
- Aligned output with f-strings: `f"{label:<12}{value:>12,.2f}"`
  - `:<12` left-aligns in a width of 12; `:>12` right-aligns
  - `,` adds thousands separators; `.2f` shows 2 decimal places

Useful docs: [Format specification](https://docs.python.org/3/library/string.html#format-specification-mini-language)

## Scenario

Parents at **Mavuno School** pay school fees every term: **tuition** plus **transport**. The bursar needs a program that prints a receipt for a parent who pays for several terms at once and gets a **5% discount** for paying in advance.

## Task

Write a program that:

1. Asks for the **student name**, the **tuition fee per term**, the **transport fee per term** (both in KES, may have decimals) and the **number of terms** (a whole number).
2. Calculates:
   - `subtotal = (tuition + transport) * terms`
   - `discount = 5%` of the subtotal (use the constant `DISCOUNT_RATE`)
   - `total = subtotal - discount`
3. Prints a receipt with the school name, the student name, and the subtotal, discount and total **aligned in columns**, with 2 decimal places, in KES.

## Examples

```text
Student name: Alice Wanjiku
Tuition fee per term (KES): 45000
Transport fee per term (KES): 12000
Number of terms: 3

========== MAVUNO SCHOOL ==========
Fee receipt for: Alice Wanjiku
-----------------------------------
Subtotal           171,000.00 KES
Discount (5%)        8,550.00 KES
Total              162,450.00 KES
===================================
```

The exact look is up to you, but the three amounts must be right and lined up.

## How to do it

1. Open `day_05.py`. The discount rate is given as a constant, and the first question is done for you.
2. **Ask for the rest.** `tuition` and `transport` need `float(input(...))`; `terms` needs `int(input(...))`.
3. **Do the arithmetic** step by step, one variable per line. Check with the example: (45000 + 12000) × 3 = 171,000.
4. **Print the receipt.** Start with plain `print` lines for the title. For the amounts, an f-string with a format spec lines them up: `print(f"{'Subtotal':<15}{subtotal:>14,.2f} KES")`.
5. **Try other numbers**, including a fee with decimals like `1250.50`, and check your answers with a calculator.
6. Read your output like a parent would: are the columns straight? Is the discount smaller than the subtotal?

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 5/day_05.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] The program asks for the name, tuition, transport and number of terms
- [ ] Subtotal, discount and total match the formulas (check the example)
- [ ] The amounts are aligned and show 2 decimal places
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Also show the fee per term after discount.
- Print the amount per month if the total is paid over 3 months.
