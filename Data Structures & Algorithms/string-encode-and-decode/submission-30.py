class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for element in strs:
            new_str+=str(len(element))
            new_str+="#"
            new_str+=element
        print(new_str)
        return new_str

    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        while i < len(s):
            check = ""
            # Step 1: Read the length until '#'
            while s[i].isdigit():
                check += s[i]
                i += 1
            
            # Step 2: Skip the '#' character
            if i < len(s) and s[i] == '#':
                i += 1
            else:
                break  # malformed string

            if check == "":
                break  # no length found

            word_len = int(check)

            # Step 3: Extract the word
            word = s[i:i+word_len]
            lst.append(word)

            # Step 4: Move i past the word
            i += word_len

        return lst


                    


        

