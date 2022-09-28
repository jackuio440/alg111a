q=[0,0,0,0,0]
for a in range(0,70):
    for b in range(0,70):
        for c in range(0,70):
            for d in range(0,70):
                for e in range(0,70):
                    if(4*a + 7*b+ 3*c + 8*d+ 5*e<=211 and 18*a+4*b-	9*c	+10*d+12*e<=285 and 5*a+7*b+9*c+2*d+1*e<=250 and 5*a+13*b+16*c	+3*d-7*e<=315):
                        if(7*a + 8*b + 2*c+ 9*d + 6*e> 7*int(q[0]) + 8*int(q[1]) + 2*int(q[2])+ 9*int(q[3]) + 6*int(q[4])):
                            q=[a,b,c,d,e]
                            
                    else:
                        break
                            

print(q)

#結果[7, 21, 0, 2, 4]

