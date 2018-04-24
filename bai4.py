class MyClass:
	MSSV = "" 
	HoTen = ""
	MaKhoa = ""
	def __init__(self,mssv,hoten,makhoa):
		self.MSSV = mssv
		self.HoTen = hoten
		self.MaKhoa = makhoa
		
	def display(self):
		print "| MSSV: " , self.MSSV, "|  Ho Ten : ", self.HoTen, "|  Ma Khoa : ", self.MaKhoa
	
		
abc = []
abc.append(MyClass('001','Mai A','01'))
abc.append(MyClass('002','Tran B','01'))
abc.append(MyClass('002','Van C','01'))
abc.append(MyClass('004','Tran D','01'))
abc.append(MyClass('005','Tran E','01'))

for a in abc:
	a.display()
		


		
	

