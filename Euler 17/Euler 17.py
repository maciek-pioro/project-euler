import math
def spellItOut(num):
    if num==0:
        return " "
    elif num==1:
        return 'one'
    elif num==2:
        return 'two'
    elif num==3:
        return 'three'
    elif num==4:
        return 'four'
    elif num==5:
        return 'five'
    elif num==6:
        return 'six'
    elif num==7:
        return 'seven'
    elif num==8:
        return 'eight'
    elif num==9:
        return 'nine'
    elif num==10:
        return 'ten'
    elif num==11:
        return 'eleven'
    elif num==12:
        return 'twelve'
    elif num==13:
        return 'thirteen'
    elif num==14:
        return 'fourteen'
    elif num==15:
        return 'fifteen'
    elif num==16:
        return 'sixteen'
    elif num==17:
        return 'seventeen'
    elif num==18:
        return 'eighteen'
    elif num==19:
        return 'nineteen'
    elif 20<=num<=29:
        return 'twenty'+' '+spellItOut(num%10)
    elif 30<=num<=39:
        return 'thirty'+' '+spellItOut(num%10)
    elif 40<=num<=49:
        return 'forty'+' '+spellItOut(num%10)
    elif 50<=num<=59:
        return 'fifty'+' '+spellItOut(num%10)
    elif 60<=num<=69:
        return 'sixty'+' '+spellItOut(num%10)
    elif 70<=num<=79:
        return 'seventy'+' '+spellItOut(num%10)
    elif 80<=num<=89:
        return 'eighty'+' '+spellItOut(num%10)
    elif 90<=num<=99:
        return 'ninety'+' '+spellItOut(num%10)
    elif 100<=num<=999:
        if num%100==0:
            return spellItOut(num/100)+' '+'hundred'
        else:
            return spellItOut(num-num%100)+' and '+spellItOut(num%100)
    elif num==1000:
        return 'one thousand'
sum=0
for i in range(1, 1001):
    print(spellItOut(i))
    sum+=len(spellItOut(i).replace(" ", ""))
print(sum)

