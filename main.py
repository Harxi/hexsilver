# Copyright (c) 2022-2023 Harxi

class HexTable():
	def __init__(self):
		self.hex = []

	def newline(self):
		self.hex.append([f"{'0'*(2-len(hex(0).lstrip('0x')))}{hex(0).lstrip('0x').upper()}"]*16)
					
	def edit(self, y: int, x: int, value: int):
		self.hex[y][x] = f"{'0'*(2-len(hex(value).lstrip('0x')))}{hex(value).lstrip('0x').upper()}"
		
	def insert(self, value: str, exist: bool = True):
		y = 0
		x = 0
		if not exist:
			for _ in range(len(value)//15+1):
				self.newline()
			
		for ind, char in enumerate(value):
			self.edit(y, x, ord(char))
			if x == 15:
				y += 1
				x = 0
			else:
				x += 1
				
	def visualization(self, raw: bool = 0):
		print(f"{' '*len(str(len(self.hex)))}   00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F{'' if not raw else '   0123456789ABCDEF'}")
		print(f"{' '*len(str(len(self.hex)))} ┌{'─'*46}{'───┐' if not raw else f'''{'─'*3}┬{'─'*17}─┐'''}")
		for ind, line in enumerate(self.hex):
			print(f"{hex(ind).lstrip('0x').upper()}{'0'*(len(str(len(self.hex)))-len(hex(ind).lstrip('0x')))}", end=" │ ")
			for digit in line:
				print(digit, end=" ")
			print("│ ", end="")
			if raw:
				for digit in line:
					print(f"{chr(int(digit, 16))}", end="")
				spaces = 1
				for digit in line[::-1]:
					if digit == "00":
						spaces += 1
					else:
						break
				print(f"{' '*spaces}│", end=' ')
			print()
		print(f"{' '*len(str(len(self.hex)))} └{'─'*46}{'───┘' if not raw else f'''{'─'*3}┴{'─'*17}─┘'''}")
			
	def raw(self):
		for ind, line in enumerate(self.hex):
			for digit in line:
				print(f"{chr(int(digit, 16))}", end=" ")
			print()
