class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []
        length = 0
        idx = 0
        while idx < len(words):
            #Line completed
            if length + len(line) + len(words[idx]) > maxWidth:
                extra = maxWidth - length
                spaces = extra // max(len(line) - 1 , 1)
                remainder = extra % max(len(line) - 1 , 1)

                for idj in range(max(1, len(line) - 1)):
                    line[idj] += " " * spaces
                    if remainder:
                        line[idj] += " "
                        remainder -= 1 
                result.append("".join(line))
                line, length = [], 0

            line.append(words[idx])
            length += len(words[idx])
            idx += 1
        
        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        last_line += " " * trail_space

        result.append(last_line)
        return result