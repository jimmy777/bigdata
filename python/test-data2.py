import datetime

of = "b.sql"
d = datetime.datetime.now()

insert_sql = "INSERT INTO  `dev`.`t2` (`id`, `name`, `price`, `typeid`, `created`) VALUES "

with open(of , "a") as fp:
    fp.write(insert_sql + "\n")

for i in range(1000):
    a = "('%s', 'X', '0', 0 , '%s'),"  % (str(i + 1), d)
    with open(of, "a") as fp:
        fp.write(a + "\n")
