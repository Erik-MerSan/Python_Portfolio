# File: Payroll2.py
# Student: Erik Mercado
# UT EID: emm4376
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: September 18, 2020
# Date Last Modified: September 18,2020
# Description of Program: Figuring out an employee's pay slip with given information
name1 = input("Enter employee name: ")
workHours = float(input("Enter number of hours worked in a week: "))
payRate = float(input("Enter hourly pay rate: "))
fedTaxWithholdRate = float(input("Enter federal tax withholding rate: "))
stateTaxWithholdRate = float(input("Enter state tax withholding rate: "))
totalDeduction = float((fedTaxWithholdRate*(payRate*workHours)) + (stateTaxWithholdRate*(payRate * workHours)))
grossPay = float(payRate * workHours)
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
