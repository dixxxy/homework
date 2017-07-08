def dayOfYear(year,month,day):
    monthnum = 1
    daynum = 0
    if ((year % 4 == 0 and year % 100 != 0)  or year % 400 == 0):
        print("%s年是闰年" % (year))
        L1 = [31,29,31,30,31,30,31,31,30,31,30,31]
        for i in L1:
            if monthnum < month:
                daynum += i
                monthnum += 1
        daynum += day
        #return daynum
        print("%s.%s.%s是该年第%s天" % (year,month,day,daynum))
    else:
        print("%s年不是闰年" %(year))
        L1 = [31,28,31,30,31,30,31,31,30,31,30,31]
        for i in L1:
            if monthnum < month:
                daynum += i
                monthnum += 1
        daynum += day
        print("%s.%s.%s是该年第%s天" % (year, month, day,daynum))
        #return daynum

dayOfYear(2000,1,8)