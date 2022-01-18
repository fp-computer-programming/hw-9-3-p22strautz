# Auhtor: SCT (AMDG) 1/18/22

print('Enter the net sales for')

try:
    previous = float(input('- Prior period:'))
    current = float(input('- Current period:'))

    change = (current - previous) * 100 / previous

    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'

    print(result)

except ValueError:
    print("Invalid input. Please enter numerical values for both prior and current")

except ZeroDivisionError:
    print("Please enter a different value that is not zero.")

finally:
    print("Thank you, have a great day.")