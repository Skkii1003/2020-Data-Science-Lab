a = 1
b = 2

c = a + b
d = a - b
e = a * b
f = a / b
print(c,d,e,f)

g = a % b
print(g)

h = 3 ** 3
i = 5 // 2
print(h,i)

equal = a==b
not_equal = a!=b
print(equal,not_equal)

bigger = a>b
smaller = a<b
biggerandequal = a>=b
smallerandequal = a<=b
print(bigger,smaller,biggerandequal,smallerandequal)

And = bigger and smaller


if a>b :
    print("a>b")
else:
    print("a<=b")

if a>b:
    print("a>b")
elif a==b:
    print("a==b")
else:
    print("a<b")

x = 0
while(x<9):
    print(x)
    x += 1

nums = [1,2,3,4,5]
strs = ["a","b","c"]

for num in nums:
    print(num)

for i in range(0,5):
    print(nums[i])