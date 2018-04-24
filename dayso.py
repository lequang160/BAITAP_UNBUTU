a = []
n = int(input('nhap n :'))
for b in range(0,n):
	a.append(b)

print 'day so tu 0 den n-1'
for c in range(0,n):
	print a[c]

print 'Tong phan tu chan'
tong = 0
for c in a:
	if c%2 == 0:
		tong += c
print tong



	
	
