class SinhVien:
	ten = ""
	namsinh = ""
	khoa =""
	def __init__(self, ten,namsinh,khoa):
		self.ten = ten
		self.namsinh=namsinh
		self.khoa= khoa
	def getTen(self):
		return self.ten
	def getNamSinh(self):
		return self.namsinh
	def getKhoa(self):
		return self.khoa
	def setTen(self, ten):
		self.ten = ten
	def setNamSinh(self, namsinh):
		self.namsinh = namsinh
	def setKhoa(self, khoa):
		self.khoa = khoa
	def toString(self):
		print 'Ten : ',self.ten,' | Nam Sinh : ',self.namsinh,' | Khoa : ',self.khoa



