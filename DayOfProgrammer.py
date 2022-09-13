def dayOfProgrammer(year):
    
    if(year == 1918):
            return '26.09.1918'
        
    if(year<1917 and year % 4==0):
        return f'12.09.{year}'
    if year>1917:
        if((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            return f'12.09.{year}'
    return f'13.09.{year}'

print(dayOfProgrammer(1918))
print(dayOfProgrammer(1717))
print(dayOfProgrammer(2520))
print(dayOfProgrammer(2717))
