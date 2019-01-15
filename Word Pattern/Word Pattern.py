class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern_dict={}
        str_dict={}
        str_list=str.split()
        length_str=len(str_list)
        pattern_length=len(pattern)
        if length_str!= pattern_length:
            return False
        
        for i in range(length_str):
            char=pattern[i]
            word= str_list[i]
            
            if char not in pattern_dict and word not in str_dict:
                pattern_dict[char]= word
                str_dict[word]=char
                #print(char)
            else:
                #print(word)
                if char in pattern_dict:
                    correct_word= pattern_dict[char]
                    if word!= correct_word:
                        return False
                if word in str_dict:
                    correct_char=str_dict[word]
                    if char!= correct_char:
                        return False
        return True 