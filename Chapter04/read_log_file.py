from Chapter01.price_log import PriceLog
from collections import Counter


########### read log file

print("read log file ...")
with open('documents/example_logs.log') as file:
    logs = [PriceLog.parse(log) for log in file]

print(len(logs))
print(logs[0])
print()

################ sum log price

print("sum log price ...")
total = sum(log.price for log in logs)
print(total)
print()


################ count units sold

print("count units sold ...")
counter = Counter(log.product_id for log in logs)
print(counter)
print()

########### filter product
print("filter product ...")
logs = [log for log in logs if log.product_id == 1489]

print(len(logs))
print(logs)
print()
