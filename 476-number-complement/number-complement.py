class Solution:
    def int_to_binary(self, num):
        return "{0:b}".format(num)
    
    def binary_to_int(self, binary_num):
        return int(binary_num, 2)
    
    def findComplement(self, num: int) -> int:
        binary = self.int_to_binary(num)
        complement = ""
        for ch in binary:
            if int(ch) == 1:
                complement += '0'
            else:
                complement += '1'
        
        return self.binary_to_int(complement)
        