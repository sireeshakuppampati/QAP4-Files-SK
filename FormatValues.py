
def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr

def FDateS(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd.

    DateValueStr = DateValue.strftime("%Y-%m-%d")
    return DateValueStr

import datetime
def first_day_of_next_month(dt):
#Get the first day of the next month. Preserves the timezone.
# dt = first_day_of_next_month(datetime.datetime.now())
 if dt.day == 25:
     dt.month += 1
 if dt.month == 12:
        return datetime.datetime(year=dt.year+1,
                                 month=1,
                                 day=1,
                                 tzinfo=dt.tzinfo)
 else:
     return datetime.datetime(year=dt.year,
                                 month=dt.month+1,
                                 day=1,
                                 tzinfo=dt.tzinfo)

#first_day_of_next_month(datetime.datetime.now())
