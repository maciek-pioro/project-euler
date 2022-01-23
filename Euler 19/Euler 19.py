def search(key, arr):
    for i in arr:
        if i==key:
            return True
    return False
day=7
month=1
year=1901
ans=0
while(year<2001):
    if day==1:
        ans+=1
        print(day,' ',month,' ',year)
    if search(month, [1, 3, 5, 7, 8, 10]):
        if day<=24:
            day+=7
        else:
            month+=1
            day-=24
    elif search(month, [4, 6, 9, 11]):
        if day<=23:
            day+=7
        else:
            month+=1
            day-=23
    elif month==12:
        if day<=24:
            day+=7
        else:
            day-=24
            month=1
            year+=1
    else:
        if year%4==0 and (year%100!=0 or year%400==0):
            if day<=22:
                day+=7
            else:
                month+=1
                day-=22
        else:
            if day<=21:
                day+=7
            else:
                month+=1
                day-=21
print(ans)