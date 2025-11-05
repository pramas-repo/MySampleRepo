# 4. print() with format for specific data types
rno = 100
name = 'yogita'
per = 89.23

print('Rno = {:d}\nName = {:s}\nPercentage = {:.2f}'.format(rno, name, per))
print('Rno = {:20d}\nName = {:20s}\nPercentage = {:20.2f}'.format(rno, name, per))
print('rno = {:<20d}\nName = {:<20s}\nPercentage = {:<20.2f}'.format(rno, name, per))
print('Rno = {:>20d}\nName = {:>20s}\nPercentage = {:>20.2f}'.format(rno, name, per))
print('Rno = {:^20d}\nName = {:^20s}\nPercentage = {:^20.2f}'.format(rno, name, per))
# Padding and filling with *
print('Rno = {:*<20d}\nName = {:*<20s}\nPercentage = {:*<20.2f}'.format(rno, name, per))
print('Rno = {:*>20d}\nName = {:*>20s}\nPercentage = {:*>20.2f}'.format(rno, name, per))
print('Rno = {:%^20d}\nName = {:%^20s}\nPercentage = {:%^20.2f}'.format(rno, name, per))

