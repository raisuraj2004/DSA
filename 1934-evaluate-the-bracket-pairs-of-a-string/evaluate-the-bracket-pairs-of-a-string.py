class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        kmap={k: v for k,v  in knowledge}
        result=[]
        key=[]
        in_brackets = False
        for ch in s:
            if ch == '(':
                in_brackets = True
                key =[]
            elif ch ==')':
                in_brackets= False
                k="".join(key)
                result.append(kmap.get(k,"?"))
            else:
                if in_brackets:
                    key.append(ch)
                else:
                    result.append(ch)
        return "".join(result)