6


yil=int(input("Yilni kiriting: "))
year=2022
month=1
day=7
dic1={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,0:31,12:31}
dic2={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,0:31,12:31}
juma=0
if year>yil:
    while True:
        if year==yil and day==13:
            juma+=1
        day-=7
        if not month>0:
            year-=1
            month+=12
        if year%4:
            if not day >0:
                month-=1
                day+=dic1[month]
        else:
            if not day >0:
                month-=1
                day+=dic2[month]
        if year<yil:
            break
else:
    while True:
        if year==yil and day==13:
            juma+=1
        day+=7
        if month>12:
            year+=1
            month=1
        if year%4:
            if day>dic1[month]:
                day=day-dic1[month]
                month+=1
        else:
            if day>dic2[month]:
                day=day-dic2[month]
                month+=1
        if year>yil:
            break
print(juma)
