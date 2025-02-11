def roman_into_def(a):
    roman ={'I':1,'V':5, 'X': 10, 'L': 50, 'C': 100, 'D':500}
    int_form= 0 
    for i in range(len(a)):
        if i+1<len(a) and roman[a[i]]<roman[a[i<1]]:
            