import json

subj = {}
prof = 0
i = 0
prof_sred = 0
with open('Firma', 'r') as file:
    for line in file:
        name, typ, doh, ras, = line.split()
        subj[name] = int(doh) - int(ras)
        if subj.setdefault(name) > 0:
            prof = prof + subj.setdefault(name)
            i = i + 1
    if i != 0:
        prof_sred = prof / i
    else:
        print('Все компании работают в убыток')

    print(f' Доходы фирм: {subj}')
    print(f' Общая прибыль доходных фирм: {prof}')
    print(f' Средняя прибыль доходных фирм: {prof_sred:.2f}')

with open("my_file.json", "w") as write_f:
    json.dump(subj, write_f)
