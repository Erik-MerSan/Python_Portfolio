# Course Name: CS303E
# Unique Number: 50695
# Description of Program: a program to figure out an individual's paycheck based on the individual's pay information

# first we create the input variables that the user will enter (employee name, # of hours worked, hourly wage, fed tax rate,
# and state tax rate
name1 = input("Enter employee name: ")
workHours = float(input("Enter number of hours worked in a week: "))
payRate = float(input("Enter hourly pay rate: "))
fedTaxWithholdRate = float(input("Enter federal tax withholding rate: "))
stateTaxWithholdRate = float(input("Enter state tax withholding rate: "))

# total deduction and gross pay are created from input from the user
totalDeduction = float((fedTaxWithholdRate*(payRate*workHours)) + (stateTaxWithholdRate*(payRate * workHours)))
grossPay = float(payRate * workHours)

# print out the output
print()
print("Employee Name: " + name1)
print("Hours Worked: " + format(workHours, ".1f"))
print("Pay Rate: $" + str(payRate))
print("Gross Pay: ", format((payRate*workHours), ".2f"), sep="$")
print("Deductions:")
print("  Federal Withholding ", "(", (format(fedTaxWithholdRate, ".1%")), ")", ": ", "$",
      format((fedTaxWithholdRate*(payRate*workHours)), ".2f"), sep="")
print("  State Withholding ", "(", (format(stateTaxWithholdRate, ".1%")), ")", ": ", "$",
      format((stateTaxWithholdRate*(payRate * workHours)), ".2f"), sep="")
print("  Total Deduction: ", (format((fedTaxWithholdRate*(payRate*workHours) + (stateTaxWithholdRate*(payRate *
                                                                                                      workHours))),
                                     ".2f")), sep="$")
print("Net Pay: ", (format((grossPay - totalDeduction), ".2f")), sep="$")
