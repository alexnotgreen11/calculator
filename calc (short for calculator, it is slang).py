argument = input("ennter >>> ")
#"3 +(25* ( 2  *  1 +   3 )*2 +2*4 + 2* 2 ) *3"
#"( ( 1 + 4 )*4 +3 ) *3"
#"(( 1 + 14 ) *(4 + 9)) + (3 * 4)"
#


#removes spaces
j = ""
for n in argument:
    if n != " ":
        j += n
argument = j


#find position of next set of brakets
def next_brac(aoa):
    brackets = []
    m = 0
    for n in aoa:

        if n == "(":
            brackets.append([int(m), 0])
        elif n == ")":
            brackets.append([int(m), 1])
        m += 1

    bracket_set = []
    m = brackets[0]
    for n in brackets:
        if n[1] != m[1]:
            bracket_set.append([m[0], n[0]])
            brackets.remove(m)
            brackets.remove(n)
               
        m = n
    return bracket_set



#arranging steps without brakets
steps_1 = []

while argument.count("(") != 0:
    n = next_brac(argument)
    steps_1.append(str(argument [ int(n[0][0]) +1  : int(n[0][1]) ]))
    argument = argument[ :n[0][0] ] + "x" + argument[ n[0][1]+1: ]
steps_1.append(argument)


#opperations

def mult(arg, x, x_coun):
    j = -1
    k = -1
    numbers = []
    ans_1 = 1
    for n in arg:
        j += 1
        k += 1
        if n == "*":
            numbers.append(arg[(j - k) :j ])
            k = -1
    numbers.append(arg[(j - k) :])
    

    for n in numbers:
        if n == "x":
            n = int(x[x_coun])
            x_coun += 1
        else:
            n = int(n)
        
        ans_1 *= n
    return ans_1


#finilasation of steps
negative = []
steps_2 = []
for n in steps_1:
    steps_2.append([])
    negative.append("")

    
end = False
while not(end):
    j = 0
    a = 0
    
    for n in steps_1:

        b=0
        for m in n:


            if m == "+":
                
                steps_2[a].append(negative[a] + n[:b ])
                steps_1[a] = n[ b + 1: ]
                
                negative[a] = ""
                
                
                break
            
            elif m == "-":
                
                if n[b-1] == "*":
                    if negative[a] == "-":
                        negative[a] = ""
                    else:
                        negative[a] = "-" 
    
                    steps_1[a] = n[:b ] + n[b+1:]
                    
                    
                    
                elif b != 0:
                    steps_2[a].append(negative[a] + n[:b ])
                    steps_1[a] = n[ b+1: ]
                    negative[a] = "-" 
                    

                else:
                    steps_1[a] = n[ b+1: ]
                    
                    negative[a] = "-" 
                   
                
                break
                
            
            elif n.count("+") == 0 and  n.count("-") == 0:
                j += 1
                break
                
            
            
            
            b+=1   
        a += 1
        
    if j == a:
        end = True
        for n in range(0, a):
            steps_2[n].append(negative[n] + steps_1[n])


#calculation
x = []
x_counter = 0
for n in steps_2:
    ans = 0
    for m in n:
        if m.count("x") >= 1 and m.count("*") != 0:
            ans += int( mult(m, x, x_counter) )
            x_counter += m.count("x")
            
        elif m.count("*") != 0:
            ans += int( mult(m, 1, 1) )
            
        elif m.count("x") >= 1:
            for b in x:
                if x_counter == len(x):
                    break
                if m[0] == "-":
                    ans -= int(x[x_counter])
                else:
                    ans += int(x[x_counter])
                x_counter += 1

        else:
            ans += int(m)
            
    x.append(ans)

print(ans)
