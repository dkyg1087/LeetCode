class Solution:
    def compress(self, chars: List[str]) -> int:
        
        chars.append("end")

        write_idx = 0
        read_idx = 0
        count = 0
        cur_char = ""
        total_length = 0

        while True:
            if cur_char != chars[read_idx] and cur_char != "":
                chars[write_idx] = cur_char
                cur_char = chars[read_idx]
                write_idx += 1
                total_length += 1
                read_idx += 1
                if count > 1:
                    count_str = str(count)
                    for i in range(len(count_str)):
                        chars[write_idx] = count_str[i]
                        write_idx += 1
                        total_length += 1
                
                count = 1
                if cur_char == "end":
                    break
                    
            elif cur_char == "":
                cur_char = chars[read_idx]
                read_idx += 1
                count += 1
            else:
                count += 1
                read_idx += 1
        

        return total_length

                    
            