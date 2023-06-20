class Saver:
	def __init__(self, calc):
		self.ui=calc
		self.get_name=""
		self.settings=self.ui.settings
		self.kernel=self.ui.kernel
		self.filename = ''
		self.chek_flag=False

	def prepare_save(self):
		self.chek_flag=self.ui.input_validator()
		if self.chek_flag:
			self.chek_flag=False
			self.get_name=f"{self.ui.get_file_name()}"
			self.filename = f"{self.settings.save_route}/{self.get_name} 30x40.NC"
			self.kernel.body_generate()
			return True
		else:
			return False

		


	def save_cp(self):
		if self.prepare_save():
			with open(self.filename, 'w') as file_object:
				file_object.write(f"{self.settings.header}{self.kernel.body}{self.settings.footer}")

			self.ui.reset_config()


