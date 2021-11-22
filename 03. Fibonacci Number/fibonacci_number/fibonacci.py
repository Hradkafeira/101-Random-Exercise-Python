class FibonnaciCollection:

    def is_positive(self,num):
        if num >= 0:
            return True
        else:
            return False
        

    def fibonnaci(self,seq):
        
        if self.is_positive(seq) == True:
            first=0
            second=1
            for num in range(seq-1):
                if second >= first:
                    first+=second
                else:
                    second+=first

            return max(first,second)
        else:
            return None

    def seq_fibonnaci(self,seq):
        if self.is_positive(seq)==True:
            list_fib=[]
            for num in range(seq+1):
                if num == 0 or num == 1:
                    list_fib+=[num]
                else:
                    list_fib+=[list_fib[num-2]+list_fib[num-1]]
            return list_fib
        else:
            return None