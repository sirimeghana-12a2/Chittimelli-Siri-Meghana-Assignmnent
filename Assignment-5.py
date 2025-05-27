lines = ['Hello World','Welcome to Capgemini','We have summer holidays']
with open('sample.txt','w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

data = ['We have python training','We have PowerBI training','We have SQL training']
with open('sample.txt','a+') as f:
    for line in data:
        f.write(line)
        f.write('\n')
    f.seek(0)
    content = f.read()
    print(f"Content from sample.txt:\n {content}")
#Output
# Content from sample.txt:
# Hello World
# Welcome to Capgemini
# We have summer holidays
# We have python training
# We have PowerBI training
# We have SQL training