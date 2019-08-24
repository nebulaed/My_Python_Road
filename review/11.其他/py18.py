# RegEx 正则表达式

import re

# matching string
pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"
print (pattern1 in string)
print (pattern2 in string)

# regular expression
pattern1 = "cat"
pattern2 = "bird"
string = "odg runs to cat"
print(re.search(pattern1,string))
print(re.search(pattern2,string))

# multiple patterns ("run" or "ran")
ptn = r"r[au]n" # r表示正则表达式
print (re.search(ptn,"dog runs to cat"))

# continue 匹配更多种可能
print(re.search(r"r[A-Z]n","dog runs to cat"))
print(re.search(r"r[a-z]n","dog runs to cat"))
print(re.search(r"r[0-9]n","dog r2ns to cat"))
print(re.search(r"r[0-9a-z]n","dog runs to cat"))

# 特殊种类匹配

# 数字
# \d : decimal digit
print(re.search(r"r\dn","run r4n"))
# \D : any non-decimal digit
print(re.search(r"r\Dn","run r4n"))

# 空白
# \s : any white space {\t\n\r\f\v}
print (re.search(r"r\sn","r\nn r4n"))
# \S : opposite to \s, any non-white space
print (re.search(r"r\Sn", "r\nn r4n"))

# 所有字母数字和"_"
# \w : {a-zA-Z0-9_}
print (re.search(r"r\wn","r\nn r4n"))
# \W : opposite to \w
print (re.search(r"r\Wn","r\nn r4n"))

# 空白字符
# \b : empty string (only at the start or end of the word)
print (re.search(r"\bruns\b","dog runs to cat"))
# \B : empty string (but not at the start or end of the word)
print(re.search(r"\B runs \B","dog  runs  to cat"))

# 转义字符
# \\ : match \
print (re.search(r"runs\\","runs\ to me"))
# . : match anything (except \n)
print(re.search(r"r.n","r[ns to me"))

# 句尾句首
# ^ : match line beginning 
print (re.search(r"^dog","dog runs to cat"))
# $ : match line ending
print (re.search(r"cat$","dog runs to cat"))

# 是否
# ? : may or may not occur
print(re.search(r"Mon(day)?","Monday"))
print(re.search(r"Mon(day)?","Mon"))

# 多行匹配
# multi-line
string = """
dog runs to cat.
I runs to dog.
"""
print(re.search(r"^I",string))
print(re.search(r"^I",string,flags=re.M))

# 0或多次
# * : occur 0 or more times
print(re.search(r"ab*","a"))
print(re.search(r"ab*","abbbbb"))

# 1或多次
# + : occur 1 or more times
print(re.search(r"ab+","a"))
print(re.search(r"ab+","abbbb"))

# 可选次数
# {n,m} : occur n to m times
print(re.search(r"ab{2,10}","a"))
print(re.search(r"ab{2,10}","abbbbb"))

# group组
match = re.search(r"(\d+), Date: (.+)", "ID: 021532, Date: Feb/12/2017")
print(match.group())
print(match.group(1))
print(match.group(2))

match = re.search(r"(?P<id>\d+), Date: (?P<date>.+)", "ID: 021523, Date: Feb/12/2017")
print (match.group('id'))
print (match.group('date'))

# 寻找所有匹配
# findall
print (re.findall(r"r[ua]n","run ran ren"))

# | : or
print (re.findall(r"(run|ran)","run ran ren"))

# 替换
# re.sub() replace
print(re.sub(r"r[au]ns","catches","dog runs to cat"))

# 分裂
# re.split()
print(re.split(r"[,;\.]","a;b,c.d;e"))

# compile
compiled_re = re.compile(r"r[ua]n")
print(compiled_re.search("dog ran to cat"))
