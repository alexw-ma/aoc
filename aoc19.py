#towel_pattern = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br" ]
_pattern_memo = {

}

def towelPatternExists(pattern):
    global _pattern_memo
    print(pattern)
    if pattern == "":
        return True
    if pattern in towel_pattern:
        return True
    if pattern in _pattern_memo:
        return _pattern_memo[pattern]
    if len(pattern) == 1:
        _pattern_memo[pattern] = False
        return False
    
    pos = 1
    while( pos < len(pattern)):
        if( towelPatternExists(pattern[:pos]) and towelPatternExists(pattern[pos:])):
            _pattern_memo[pattern] = True
            return True
        pos += 1
    _pattern_memo[pattern] = False
    return False

with open('c:\\Users\Alex\Documents\Code\Python\\input2.txt', 'r') as file:
    lines = file.readlines()

towel_pattern = lines[0].rstrip().split(", ")
print(towel_pattern)
num_patterns = 0
for patterns in lines[2:]:
    if( towelPatternExists(patterns.rstrip()) ):
        num_patterns += 1
    
print(num_patterns)
