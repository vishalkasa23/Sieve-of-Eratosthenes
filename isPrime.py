def solve(self, A):
        if(A>1):
            isPrime = [1] * A
            isPrime[0] = 0
            isPrime[1] = 0  
            for i in range(2, int(math.sqrt(A))+1):
                if(isPrime[i]!=0):
                    isPrime[i*i:A:i] = [0] * len(isPrime[i*i:A:i])
            i=2
            flag=0
            while(i*i<=A):
                if(A%i==0):
                    flag=2
                i+=1
            if(flag==2):
                return(sum(isPrime))
            else:
                return(sum(isPrime)+1)
        else:
            return 0
solve(20)

#Method is Sieve-of-Eratosthenes
