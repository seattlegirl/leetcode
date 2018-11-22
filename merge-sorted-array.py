class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        last,i,j=m+n-1,m-1,n-1

        while i>=0 and j>=0:

            if A[i]>B[j]:
                A[last]=A[i]
                last=last-1
                i=i-1
            
            else:
                A[last]=B[j]
                last=last-1
                j=j-1
        
        while j>=0:
            A[last]=B[j]
            last=last-1
            j=j-1


if __name__ == "__main__":
    A = [2, 3, 5, 0, 0, 0, 0]
    B = [1, 4, 6, 7]
    Solution().merge(A, 3, B, 4)
    print A