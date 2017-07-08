def dayOfYear(year,month,day):
    daynum = 0
    j = 1
    if ((year % 4 == 0 and year % 100 != 0)or year % 400 == 0):
        print("%s年是闰年" % (year))
        L1 = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        for i in L1.values():
            if j < month:
                daynum += i
                j += 1
        daynum = daynum + day
        print("%s.%s.%s是该年第%s天" % (year, month, day, daynum))
    else:
        print("%s年不是闰年" % (year))
        L1 = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        for i in L1.values():
            if j < month:
                daynum += i
                j += 1
        daynum = daynum + day
        print("%s.%s.%s是该年第%s天" % (year, month, day, daynum))
dayOfYear(1998,3,8)



