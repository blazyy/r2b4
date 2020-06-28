from stack import Stack
import re

# This ain't pretty code by any means, but it works. It's almost midnight and I wanna go to sleep.
def html_verifier(filepath):
    stack = Stack()
    with open('html.txt') as f:
        content = [x.strip() for x in f.readlines()]
        for word in content:
            if '<' in word and '</' not in word:  # opening tag
                stack.push(word.strip('<').strip('>'))
            elif '</' in word and word.count('<') <= 1:
                top = stack.pop()
                if top != word.strip('</').strip('>'):
                    return False
            elif word.count('<') > 1:
                tags = list(re.findall('<(.*)>(.*)</(.*)>', word)[0])
                if tags[0] != tags[len(tags)-1]:
                    return False
            else:
                continue
    if stack.isEmpty():
        return True
    return False

print(html_verifier('html.txt'))
