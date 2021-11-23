class FibonnaciCollection:
    """Collection of Fibonacci number calculation"""

    def is_positive(self,num):
        """Check whether the value is positive or negative

        Parameters
        ----------
        num : `int`
            number that will checked

        Returns
        -------
            Boolean Value: bool
        """
        if num >= 0:
            return True
        else:
            return False
        

    def fibonnaci(self,seq):
        """Calculate the fibonacci number and return the last number from input

        Parameters
        ----------
        seq : `int`
            the last position number of fibonacci that will be generate

        Returns
        -------
            fibonacci number : `int`
        """
        
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
        """ Calculate sequence of fibonacci number and return the list

        Parameters
        ----------
        seq : `int`
            length of fibonacci number that will be generated

        Returns
        -------
        sequence of fibonacci number : list
            sequence of fibonacci number that store in list    

        """
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