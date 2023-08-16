from package1.package2.module2 import Module2
from package1.package2.package4.module4 import Module4
from ..package3.module3 import Module3
# from ..package3.module3 import Module3 # doesn't work, don't know why
# phai chạy theo kiểu này mới work: python3 -m package1.package2.module1

class Module1:
	def __init__(self):
		return True