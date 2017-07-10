#统计某组织各年龄段的人数，年龄由随机函数自动生成，范围0~100。
#输入为人数和年龄段并以英文分号分隔，年龄段之间以英文逗号分隔；
#输出为两部分：第一部分是生成的所有年龄，第二部分为各年龄段的人数。详见示例。
#其中区间定义(10,20)={x∈R：x>10且x<20}, [10,20)={x∈R：x>=10且x<20}, (10,20]={x∈R：x>10且x<=20}, [10,20]={x∈R：x>=10且x<=20}。
import random

def age_num(people_num):
    age_list = [random.randint(10,100) for _ in range(people_num)]
    print(age_list)
    j = 0
    k = 0
    l = 0
    for i in age_list:
        if 10<= i <20:
            j += 1
        elif 20<= i <40:
            k += 1
        else:
            l += 1
    print("[10,20):%s" % (j))
    print("[20,40):%s" % (k))
    print("[40,100):%s" % (l))

age_num(20)





