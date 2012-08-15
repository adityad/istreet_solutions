import sys

def count_ones_positive(num):
    count = 0
    while True:
        if num:
            count += 1
        else:
            break
        num = num & (num-1)
    return count

def solve( num ):
    if !num:
        return 0
    else if num%2 == 0:
        return solve( num - 1 ) + count_ones_positive( num )
    else:
        return ( num + 1 )/ 2 + 2 * solve( num / 2 )

def find_ones(a,b):
    sum = 0
    if a >= 0:
        sum = solve( b )
        if( a > 0 ):
            sum -= solve( a - 1 )
        return sum    
    else:
        sum = 32 * a - solve( ~a )
        if b > 0:
            return sum += solve( b )
        else:
           if b < -1:
               b += 1
               return sum -= 32 * b - solve(~b)
           else:
               return sum - 32

for line in sys.stdin:
    try:
        (a,b) = line.split()
        ans = find_ones(int(a),int(b))
        print(ans)        
    except:
        continue

