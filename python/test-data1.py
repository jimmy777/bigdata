import datetime

d = datetime.datetime.now()

for i in range(10):
    a = "INSERT INTO  `dev`.`t2` (`id`, `name`, `price`, `typeid`, `created`) VALUES ('%s', 'X', '0', 0 , '%s');"  % (str(i+1), d)
    with open("a.sql", "a") as fp:
        fp.write(a+"\n")
