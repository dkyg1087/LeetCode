class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        def get_section_sum(pre_sum,idx1,idx2):
            return pre_sum[idx2] - pre_sum[idx1-1] if idx1 != 0 else pre_sum[idx2]
        
        res = [0] * len(code)

        if k == 0:
            return res
        
        pre_sum = [0] * len(code)
        pre_sum[0] = code[0]
        for i in range(1,len(code)):
            pre_sum[i] = pre_sum[i-1] + code[i]
    
        
        for i in range(len(code)):

            if k < 0:
                if abs(k) > i:
                    res[i] = pre_sum[-1] - get_section_sum(pre_sum,i,i + len(code) + k - 1)
                else:
                    res[i] = get_section_sum(pre_sum,i + k, i-1)
            if k > 0:
                if i + k < len(code):
                    res[i] = get_section_sum(pre_sum,i + 1,i+k)
                else:
                    print(i - len(code) + k - 1,i)
                    res[i] = pre_sum[-1] - get_section_sum(pre_sum,i - len(code) + k + 1,i)
        return res
                
                
