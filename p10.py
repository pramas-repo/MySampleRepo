# 2. print() with format() and padding of data
# calclate student percentage
rno = 109
name = 'Umesh'
ph = 78
ch = 85
ma = 70
per = (ph + ch + ma) / 3.0
# padding of 20 spaces
print('Rno = {:20}\nName = {:20}\nPercentage = {:20.2f}'.format(rno, name, per))
# padding and aligining data usin < left, > right, ^ center
print('-- all Data Left aligned --')
print('Rno = {:<20}\nName = {:<20}\nPercentage = {:<20.2f}'.format(rno, name, per))
print('-- all Data Right aligned --')
print('Rno = {:>20}\nName = {:>20}\nPercentage = {:>20.2f}'.format(rno, name, per))
print('-- all Data Center aligned --')
print('Rno = {:^20}\nName = {:^20}\nPercentage = {:^20.2f}'.format(rno, name, per))
# padding, aligning and filling blank spaces with *
print('Rno = {:*<20}\nName = {:*<20}\nPercentage = {:*<20.2f}'.format(rno, name, per))
print('Rno = {:*>20}\nName = {:*>20}\nPercentage = {:*>20.2f}'.format(rno, name, per))
print('Rno = {:#^20}\nName = {:#^20}\nPercentage = {:#^20.2f}'.format(rno, name, per))