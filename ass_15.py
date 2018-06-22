#1
import re
test_string = 'zuck26@facebook.com' #enter the e-mail addresses here plz
domain = re.search('@*?\.', test_string)
print (domain.group())


#2
z = 'Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better.'
import re
print (re.findall(r'[b]\S*', z))

#3
import re
text = """\
A, very very; irregular_sentence
"""
sentences = re.split(r' *[\.\?!][\'"\)_;\]]* *', text)

for stuff in sentences:
        print(stuff)

