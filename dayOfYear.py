def dayOfYear(year,month,day):
    day_num = 0
    if ((year % 4 == 0 and year % 100 != 0)or year % 400 == 0):
        print("%s年是闰年" % (year))
        MD = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        for i in MD.keys():
            if i == month:
                M = list(MD.values())
                D = M[:i-1]
                for j in D:
                    day_num += j
                day_num = day_num + day
        print("%s.%s.%s是该年第%s天" % (year, month, day, day_num))
    else:
        print("%s年不是闰年" % (year))
        MD = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        for i in MD.keys():
            if i == month:
                M = list(MD.values())
                D = M[:i - 1]
                for j in D:
                    day_num += j
                day_num = day_num + day
        print("%s.%s.%s是该年第%s天" % (year, month, day, day_num))

dayOfYear(2000,1,8)  #运行程序时可以在此任意修改日期

