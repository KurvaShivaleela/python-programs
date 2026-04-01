def nextGreaterElement(nums1,nums2):
    
    s=[]
    nge={}
    for n in nums2:
        while s and s[-1]<n:
            prev=s.pop()
            nge[prev]=n
        s.append(n)
    while s:
      nge[s.pop()]=-1
    return [nge[x] for x in nums1]
nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
print(nextGreaterElement(nums1,nums2))

      

   