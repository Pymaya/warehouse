from mergedict import mergedict
test_a={
    'name':'jack',
    'age':'19',
    'weight':'70kg',
    'gender':'male',
}
f_1=test_a.keys()
f_2=test_a.values()

vv={}
vv=mergedict(f_1,f_2)

print(vv)