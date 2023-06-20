class Settings:
	def __init__(self):
		self.save_route="ready_programs"
		self.header = "%\nT1M6\nG0Z15.000\nG0X0.000Y0.000S6000M3\n"
		self.footer = "G0Z75.000\nG0X319.000Y1200.000\nM30"
		self.driling = "G0Z1.000\nG1Z-34.000F6000.0\nG0Z15.000\n"
		self.table_cell_spacing = 259
