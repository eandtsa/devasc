
with open("pv.yaml", "a+") as data:
    data.write('\nLast line added by Python script')

with open("pv.yaml", "r") as data:
    print(data.read())