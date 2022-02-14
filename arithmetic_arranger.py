def arithmetic_arranger(problems):

  import re
  
  # Too many problems
  if len(problems) > 5:
    return "Error: Too many problems."

  # Check operations in str format
  ops = list(map(lambda x: x.split()[1], problems))
  if set(ops) != {'+', '-'} and len(set(ops)) != 2:
    return "Error: Operator must be '+' or '-'."

  # Check operands in str format
  # Check operands not more than 4 digits
  topnumbers = []
  bottomnumbers = []
  ops = []
  top_row = ''
  dashes = ''
  bottom_row = ''
  solutions = ''

  for i in problems:
      x = i.split()
      if x[0].isdigit() and x[2].isdigit():
        if len(x[0])<5 and len(x[2])<5:
          # Checks are done, can now parse for return
          # print(x)
          topnumbers.append(x[0])
          ops.append(x[1])
          bottomnumbers.append(x[2])
        else:
          return "Error: Numbers cannot be more than four digits."
      else:
        return "Error: Numbers must only contain digits."

  # Format the output
  for i in range(len(topnumbers)):
    space_width = max(len(topnumbers[i]), len(bottomnumbers[i])) + 2
    top_row += topnumbers[i].rjust(space_width)
    dashes += '-' * space_width
    bottom_row += ops[i] + " "
    bottom_row += " " * (space_width - len(str(bottomnumbers[i]))-2)
    bottom_row += bottomnumbers[i]
    if ops[i]=="+":
      calc_sol = int(topnumbers[i]) + int(bottomnumbers[i])
    else:
      calc_sol = int(topnumbers[i]) - int(bottomnumbers[i])
    solutions += str(calc_sol).rjust(space_width)

    top_row += " " * 4
    dashes += " " * 4
    bottom_row += " " * 4
    solutions += " " * 4

  arranged_problems = '\n'.join((top_row, bottom_row, dashes, solutions))
  return arranged_problems