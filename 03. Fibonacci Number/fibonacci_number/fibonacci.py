class FibonnaciCollection:
    """Collection of Fibonacci number calculation"""

    # def is_positive(self,num):
    #     """Check whether the value is positive or negative

    #     Parameters
    #     ----------
    #     num : `int`
    #         number that will checked

    #     Returns
    #     -------
    #         Boolean Value: bool
    #     """
    #     if num >= 0:
    #         return True
    #     else:
    #         return False
        

    def fibonnaci(self,n):
        """Calculate the fibonacci number and return the last number from input

        Parameters
        ----------
        n : `int`
            the last position number of fibonacci that will be generate

        Returns
        -------
            fibonacci number : `int`
        """

        assert n >= 0     
        # if self.is_positive(n) == True:

        if n <=1 :
            return n
        else:
            first=0
            second=1
            for num in range(n-1):
                if second >= first:
                    first+=second
                else:
                    second+=first

            return max(first,second)
        # else:
        #     return None

    def seq_fibonnaci(self,n):
        """ Calculate sequence of fibonacci number and return the list

        Parameters
        ----------
        n : `int`
            length of fibonacci number that will be generated

        Returns
        -------
        sequence of fibonacci number : list
            sequence of fibonacci number that store in list    

        """
        assert n >= 0

        list_fib=[]

        if n <=1 :
            list_fib+=[n]
            return list_fib

        for num in range(n+1):
            if num == 0 or num == 1:
                list_fib+=[num]
            else:
                list_fib+=[list_fib[num-2]+list_fib[num-1]]
        return list_fib
# fc=FibonnaciCollection()
# print(fc.fibonnaci(1))
# print(fc.fibonnaci(0))
# print(fc.fibonnaci(-1))