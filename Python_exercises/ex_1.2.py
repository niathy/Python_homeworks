"""
Shoemaker (approx. 1 hours)
Ask the user to provide a number of days of the week (Monday=1, Sunday=7)
when he left his shoes at the shoemaker shop for a repair.
Ask him also how many days the repair will take. As an output,
inform the user at which day of the week he should get back his shoes.
For example, leaving shoes on Tuesday with 3 days needed for the repair, should output Friday.

"""


day = int(input("Enter number of the day (Monday=1 to Sunday=7): "))
duration = int(input('How many days repair will take? '))

due_day = day + duration
i = 7


if due_day == 1 or due_day == 1 + i:
    print('you will get your shoes back on Monday')
elif due_day == 2 or due_day == 2 + i:
    print('you will get your shoes back on Tuesday')
elif due_day == 3 or due_day == 3 + i:
    print('you will get your shoes back on Wednesday')
elif due_day == 4 or due_day == 4 + i:
    print('you will get your shoes back on Thursday')
elif due_day == 5 or due_day == 5 + i:
    print('you will get your shoes back on Friday')
elif due_day == 6 or due_day == 6 + i:
    print('you will get your shoes back on Saturday')
elif due_day == 7 or due_day == 7 + i:
    print('you will get your shoes back on Sunday')



