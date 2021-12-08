class RecursifCollection:
    def factorial(self,n):
        print(n)
        if n == 1:
            return n
        else:
            return n*self.factorial(n-1)

    def sum_recursif(self,seq):
        if seq == []:
            return 0
        else: 
            return seq[0]+self.sum_recursif(seq[1:])

    def count_recursif(self,seq):
        if seq == []:
            return 0
        else: 
            return 1+self.count_recursif(seq[1:])

    def max_recursif(self,list):
        if len(list) == 2:
            return list[0] if list[0] > list[1] else list[1]
        sub_max = self.max_recursif(list[1:])
        return list[0] if list[0] > sub_max else sub_max