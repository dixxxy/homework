def dayOfYear(year,month,day):
    daynum = 0
    if ((year % 4 == 0 and year % 100 != 0)or year % 400 == 0):
        print("%s年是闰年" % (year))
        L1 = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        for i in range(month-1):
            j = L1[i+1]
            print(j)
            daynum += j
            daynum = daynum + day
            print("第%s天" % (daynum))

    else:
        print("%s年不是闰年" % (year))
        L1 = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        for i in range (month-1):
            j = L1[i+1]
            print(j)
            daynum += j
            daynum = daynum +day
            print("第%s天" % (daynum))

print(dayOfYear(1998,1,8))
