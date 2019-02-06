# Problem 2 (Located: https://www.python.org/dev/peps/pep-0008/#indentation)

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
                       var_one, var_two, var_three,
                       var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
                         var_one, var_two,
                         var_three, var_four)


# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
                       var_one, var_two, var_three,
                       var_four):
    print(var_one)

 
#  Problem 3 (Located: https://www.python.org/dev/peps/pep-0008/#maximum-line-length)

# No: operators sit far away from their operands
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
