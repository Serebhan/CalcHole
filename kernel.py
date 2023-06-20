class Kernel:
	def __init__(self, ui):
		self.ui=ui
		self.drilling=self.ui.settings.driling
		self.body=''
		self.body_part=''
		self.sthaketin=int(self.ui.lnput_number_of_shtaketins.text())



	def body_generate (self):
		print ("Генерую розкладку загалом:")
		self.body=''
		self.body_part=''
		if self.ui.radioBtn_one_pack.isChecked():
			self.body=self.one_pack_hole()
		elif self.ui.radioBtn_gate_up_down.isChecked():
			if self.ui.radio_btn_old_gate.isChecked():
				self.body=self.old_gate_up_down_hole(length=float(self.ui.lnput_part_length.text()))
			elif self.ui.radio_btn_new_gate.isChecked():
				self.body=self.new_gate_up_down_hole(length=float(self.ui.lnput_part_length.text()))
		elif self.ui.radioBtn_main_set.isChecked():
			self.body=self.main_set_hole()
		elif self.ui.radioBtn_second_set.isChecked():
			self.body=self.second_set()
		elif self.ui.radioBtn_gate_set.isChecked():
			if self.ui.radio_btn_old_gate.isChecked():
				self.body=self.gate_set_hole(False)
			elif self.ui.radio_btn_new_gate.isChecked():
				self.body=self.gate_set_hole(True)
			

	def old_gate_up_down_hole(self,  length, position_gate=0):
		print ("Поклав старi калiтки")
		self.body_part=self.breakdown_old_gate_hole_up(length=length, position=position_gate, limit60=self.ui.cb.isChecked())
		self.body_part=self.body_part+self.breakdown_old_gate_hole_down(length=length, position=position_gate+30, direct='from_fall', limit60=self.ui.cb.isChecked())
		return self.body_part

	def new_gate_up_down_hole(self,  length, position_gate=0):
		print ("Поклав новi калiтки")
		self.body_part=self.breakdown_new_gate_hole_up(length=length, position=position_gate, limit60=self.ui.cb.isChecked())
		self.body_part=self.body_part+self.breakdown_new_gate_hole_down(length=length, position=position_gate+30, direct='from_fall', limit60=self.ui.cb.isChecked())
		return self.body_part
	
	def one_pack_hole(self):
		print ("Розкладаю сет на 1 манеж")
		self.body_part=''
		how_mode=''
		self.body_part=self.body_part+self.breakdown_linear_hole_up( position=0, limit60=self.ui.cb.isChecked(), mode='Full')
		self.body_part=self.body_part+self.breakdown_linear_hole_down(direct='from_tail', position=30, limit60=self.ui.cb.isChecked(), mode='Full')
		if self.ui.radio_btn_old_gate.isChecked():
			how_mode='old_gate'
		elif self.ui.radio_btn_new_gate.isChecked():
			how_mode='new_gate'
		self.body_part=self.body_part+self.breakdown_linear_hole_down( position=60, limit60=self.ui.cb.isChecked(), mode=how_mode)
		if self.ui.radio_btn_old_gate.isChecked():
			how_mode='old_gate_railing'
		elif self.ui.radio_btn_new_gate.isChecked():
			how_mode='new_gate_railing'
		self.body_part=self.body_part+self.breakdown_linear_hole_up(direct='from_tail', position=90, limit60=self.ui.cb.isChecked(), mode=how_mode)
		if self.ui.radio_btn_old_gate.isChecked():
			self.body_part=self.body_part+self.old_gate_up_down_hole(position_gate=259, length=self.ui.gate)
		elif self.ui.radio_btn_new_gate.isChecked():
			self.body_part=self.body_part+self.new_gate_up_down_hole(position_gate=259, length=self.ui.gate)
		self.body_part=self.body_part+self.breakdown_linear_hole_up(position=319, limit60=self.ui.cb.isChecked(), mode='#13')
		return self.body_part
	

	def main_set_hole(self):
		print ("Розкладаю на весь стiл, верхи низи й під калiтку")
		self.body_part=''
		how_mode=''
		for i in (0,30,60,90):
			if i in (30, 90):
				direct='from_tail'
			else:
				direct='from_zero'
			self.body_part=self.body_part+self.breakdown_linear_hole_up(direct, position=i, limit60=self.ui.cb.isChecked(), mode='Full')
		for i in (259, 289, 319, 349):
			if i in (289, 349):
				direct='from_tail'
			else:
				direct='from_zero'
			self.body_part=self.body_part+self.breakdown_linear_hole_down(direct, position=i, limit60=self.ui.cb.isChecked(), mode='Full')

		if self.ui.radio_btn_old_gate.isChecked():
			how_mode='old_gate'
		elif self.ui.radio_btn_new_gate.isChecked():
			how_mode='new_gate'

		for i in (518, 548, 578, 608):
			if i in (548, 608):
				direct='from_tail'
			else: 
				direct='from_zero'

			self.body_part=self.body_part+self.breakdown_linear_hole_down(direct, position=i, limit60=self.ui.cb.isChecked(), mode=how_mode)
		return self.body_part

	def second_set(self):
		print ("Розкладаю на весь стіл - просто верхи й низи")
		self.body_part=''
		for i in (0,30,60,90,259,289):
			if i in (30, 90, 289):
				direct='from_tail'
			else:
				direct='from_zero'
			self.body_part=self.body_part+self.breakdown_linear_hole_up(direct, position=i, limit60=self.ui.cb.isChecked(), mode='Full')
		for i in (319, 349, 518, 548, 578, 608):
			if i in (349, 548, 608):
				direct='from_tail'
			else:
				direct='from_zero'
			self.body_part=self.body_part+self.breakdown_linear_hole_down(direct, position=i, limit60=self.ui.cb.isChecked(), mode='Full')
		return self.body_part
		
	def gate_set_hole(self, newgate):
		print ("Розкладаю на весь стiл - калiтки")
		self.body_part=''
		if newgate:
			for i in (0,30,60,90,259,289):
				if i in (30, 90, 289):
					direct='from_tail'
				else:
					direct='from_zero'
				self.body_part=self.body_part+self.breakdown_new_gate_hole_up(length=float(self.ui.lnput_part_length.text()), direct='from_zero', position=i, limit60=self.ui.cb.isChecked())
			for i in (319, 349, 518, 548, 578, 608):
				if i in (349, 548, 608):
					direct='from_tail'
				else:
					direct='from_zero'
				self.body_part=self.body_part+self.breakdown_new_gate_hole_down(length=float(self.ui.lnput_part_length.text()), direct='from_zero', position=i, limit60=self.ui.cb.isChecked())
		elif not newgate:
			for i in (0,30,60,90,259,289):
				if i in (30, 90, 289):
					direct='from_tail'
				else:
					direct='from_zero'
				self.body_part=self.body_part+self.breakdown_old_gate_hole_up(length=float(self.ui.lnput_part_length.text()), direct='from_zero', position=i, limit60=self.ui.cb.isChecked())
			for i in (319, 349, 518, 548, 578, 608):
				if i in (349, 548, 608):
					direct='from_tail'
				else:
					direct='from_zero'
				self.body_part=self.body_part+self.breakdown_old_gate_hole_down(length=float(self.ui.lnput_part_length.text()), direct='from_zero', position=i, limit60=self.ui.cb.isChecked())
		return self.body_part


	def breakdown_linear_hole_up(self, direct='from_zero', position=0, limit60=False, mode='Full'):
		part_prog=''
		length=float(self.ui.lnput_part_length.text())
		step, step_one=self.get_linear_step(length=length, limit60=limit60)

		if direct=='from_zero':
			for i in range(self.sthaketin+1):
				if i==1:
					part_prog=f'G0X{position+15}Y{step_one}\n{self.drilling}'
				elif mode=='old_gate_railing' and (self.sthaketin+1-i)>5:
					part_prog=part_prog + f'G0Y{step_one+step*(i-1)}\n{self.drilling}'
				elif mode=='new_gate_railing' and (self.sthaketin+1-i)>7:
					part_prog=part_prog + f'G0Y{step_one+step*(i-1)}\n{self.drilling}'
				elif mode=='Full' and i>1:
					part_prog=part_prog + f'G0Y{step_one+step*(i-1)}\n{self.drilling}'
				elif mode=='#13' and i==2 and self.ui.radio_btn_new_gate.isChecked():
					part_prog=part_prog + f'G0Y{step_one+step*(i-1)}\n{self.drilling}'


		elif direct!='from_zero':
			for i in range(self.sthaketin+1):
				if i==1 and mode=='Full':
					part_prog=f'G0X{position+15}Y{length-step_one}\n{self.drilling}'
				elif i==1 and mode!='Full':
					part_prog=f'G0X{position+15}'
				elif mode=='old_gate_railing' and i>5:
					part_prog=part_prog + f'G0Y{length-(step_one+step*(i-1))}\n{self.drilling}'
				elif mode=='new_gate_railing' and i>7:
					part_prog=part_prog + f'G0Y{length-(step_one+step*(i-1))}\n{self.drilling}'
				elif mode=='Full' and i>1:	
					part_prog=part_prog + f'G0Y{length-(step_one+step*(i-1))}\n{self.drilling}'
				elif mode=='#13' and i==(self.sthaketin-1) and self.ui.radio_btn_new_gate.isChecked():
					part_prog=part_prog + f'G0Y{step_one+step*(i-1)}\n{self.drilling}'
				elif mode=='#13' and i==(self.sthaketin):
					part_prog=part_prog + f'G0Y{step_one+step*(i-1)}\n{self.drilling}'
		return part_prog

	def get_linear_step(self, length, limit60=False):
		self.sthaketin=int(self.ui.lnput_number_of_shtaketins.text())
		if limit60:
			step=round(((length-(35*self.sthaketin))/(self.sthaketin+1))+35, 3)
			step_one=step-17.5
		else:
			step=round(((length-(40*self.sthaketin))/(self.sthaketin+1))+40, 3)
			step_one=step-20
		return step, step_one



	def breakdown_linear_hole_down (self, direct='from_zero', position=0, limit60=False, mode='Full'):
		part_prog=''
		length=float(self.ui.lnput_part_length.text())
		step, step_one=self.get_linear_step(length=float(self.ui.lnput_part_length.text()), limit60=limit60)
		

		if direct=='from_zero':
			for i in range(self.sthaketin+1):
				if i==1:
					part_prog=f'G0X{position+15}Y{step_one-8}\n{self.drilling}G0Y{step_one+8}\n{self.drilling}'
				elif mode=='old_gate' and ((self.sthaketin+1-i)>5 or i==self.sthaketin):
					part_prog=part_prog + f'G0Y{(step_one-8)+step*(i-1)}\n{self.drilling}G0Y{(step_one+8)+step*(i-1)}\n{self.drilling}'
				elif mode=='new_gate' and (i==(self.sthaketin+1-2) or i==(self.sthaketin) or (self.sthaketin+1-i)>7):
					part_prog=part_prog + f'G0Y{(step_one-8)+step*(i-1)}\n{self.drilling}G0Y{(step_one+8)+step*(i-1)}\n{self.drilling}'
				elif mode=='Full' and i>1:
					part_prog=part_prog + f'G0Y{(step_one-8)+step*(i-1)}\n{self.drilling}G0Y{(step_one+8)+step*(i-1)}\n{self.drilling}'
		
		elif direct!='from_zero':
			for i in range(self.sthaketin+1):
				if i==1:
					part_prog=f'G0X{position+15}Y{length+8-step_one}\n{self.drilling}G0Y{length-8-step_one}\n{self.drilling}'
				elif mode=='old_gate' and i>5:
					part_prog=part_prog + f'G0Y{length+8-(step_one+step*(i-1))}\n{self.drilling}G0Y{length-8-(step_one+step*(i-1))}\n{self.drilling}'
				elif mode=='new_gate' and i==2 or i>7:
					part_prog=part_prog + f'G0Y{length+8-(step_one+step*(i-1))}\n{self.drilling}G0Y{length-8-(step_one+step*(i-1))}\n{self.drilling}'
				elif mode=='Full' and i>1:
					part_prog=part_prog + f'G0Y{length+8-(step_one+step*(i-1))}\n{self.drilling}G0Y{length-8-(step_one+step*(i-1))}\n{self.drilling}'
		return part_prog




	def breakdown_old_gate_hole_up(self, length, direct='from_zero', position=0, limit60=False):
		self.part_prog=''

		if limit60:
			self.step=round(((length-220)/5)+35, 3)
			self.step_one=round(((length-220)/5)+37.5, 3)
		else:
			self.step=round(((length-240)/5)+40, 3)

		if direct=='from_zero' and limit60==False:
			for i in range(7):
				if i==1:
					self.part_prog=f'G0X{position+15}Y20.000\n{self.drilling}'
				if i>1:
					self.part_prog=self.part_prog + f'G0Y{20+self.step*(i-1)}\n{self.drilling}'
		elif direct!='from_zero' and limit60==False:
			for i in range(7):
				if i==1:
					self.part_prog=f'G0X{position+15}Y{length-20}\n{self.drilling}'
				if i>1:
					self.part_prog=self.part_prog + f'G0Y{length-(20+self.step*(i-1))}\n{self.drilling}'

		elif direct=='from_zero' and limit60:
			for i in range(7):
				if i==1:
					self.part_prog=f'G0X{position+15}Y20.000\n{self.drilling}'
				if i==2 :
					self.part_prog=self.part_prog + f'G0Y{20+self.step_one}\n{self.drilling}'
				if i==6:
					self.part_prog=self.part_prog + f'G0Y{20+self.step_one*2+self.step*3}\n{self.drilling}'
				if 6>i>2:
					self.part_prog=self.part_prog + f'G0Y{20+self.step_one+self.step*(i-2)}\n{self.drilling}'
					
		elif direct!='from_zero' and limit60:
			for i in range(7):
				if i==1:
					self.part_prog=f'G0X{position+15}Y{length-20}\n{self.drilling}'
				if i==6:
					self.part_prog=self.part_prog + f'G0Y{length-20-(self.step_one*2+self.step*3)}\n{self.drilling}'
				if i==2 :
					self.part_prog=self.part_prog + f'G0Y{length-20-self.step_one}\n{self.drilling}'
				if 6>i>2:
					self.part_prog=self.part_prog + f'G0Y{length-(20+self.step_one+self.step*(i-2))}\n{self.drilling}'
		
		return self.part_prog


	def breakdown_old_gate_hole_down(self, length, direct='from_zero', position=0, limit60=False):
		if limit60:
			self.step=round(((length-220)/5)+35, 3)
			self.step_one=round(((length-220)/5)+37.5, 3)
		else:
			self.step=round(((length-240)/5)+40, 3)

		if direct=='from_zero' and limit60==False:
			for i in range(7):
				if i==1:
					self.part_prog=f'G0X{position+15}Y12.000\n{self.drilling}G0Y28.000\n{self.drilling}'
				if i>1:
					self.part_prog=self.part_prog + f'G0Y{12+self.step*(i-1)}\n{self.drilling}G0Y{28+self.step*(i-1)}\n{self.drilling}'
		
		elif direct!='from_zero' and limit60==False:
			for i in range(7):
				if i==1:
					self.part_prog=f'G0X{position+15}Y{length-12}\n{self.drilling}G0Y{length-28}\n{self.drilling}'
				if i>1:
					self.part_prog=self.part_prog + f'G0Y{length-(12+self.step*(i-1))}\n{self.drilling}G0Y{length-(28+self.step*(i-1))}\n{self.drilling}'

		elif direct=='from_zero' and limit60:
			for i in range(7):
				if i==1:
					self.part_prog=f'G0X{position+15}Y12.000\n{self.drilling}G0Y28.000\n{self.drilling}'
				if i==2:
					self.part_prog=self.part_prog + f'G0Y{12+self.step_one}\n{self.drilling}G0Y{28+self.step_one}\n{self.drilling}'
				if 6>i>2:
					self.part_prog=self.part_prog + f'G0Y{12+self.step_one+self.step*(i-2)}\n{self.drilling}G0Y{28+self.step_one+self.step*(i-2)}\n{self.drilling}'
				if i==6:
					self.part_prog=self.part_prog + f'G0Y{12+self.step_one*2+self.step*3}\n{self.drilling}G0Y{28+self.step_one*2+self.step*3}\n{self.drilling}'

		elif direct!='from_zero' and limit60:
			for i in range(7):
				if i==1:
					self.part_prog=f'G0X{position+15}Y{length-12}\n{self.drilling}Y{length-28}\n{self.drilling}'
				if i==2:
					self.part_prog=self.part_prog + f'G0Y{length-(12+self.step_one)}\n{self.drilling}G0Y{length-(28+self.step_one)}\n{self.drilling}'
				if 6>i>2:
					self.part_prog=self.part_prog + f'G0Y{length-(12+self.step_one+self.step*(i-2))}\n{self.drilling}G0Y{length-(28+self.step_one+self.step*(i-2))}\n{self.drilling}'
				if i==6:
					self.part_prog=self.part_prog + f'G0Y{length-12-(self.step_one*2+self.step*3)}\n{self.drilling}G0Y{length-28-(self.step_one*2+self.step*3)}\n{self.drilling}'

		return  self.part_prog


	def breakdown_new_gate_hole_up(self, length, direct='from_zero', position=0, limit60=False):
		self.part_prog=''

		if limit60:
			self.step=round(((length-255)/6)+35, 3)
			self.step_one=round(((length-255)/6)+37.5, 3)
		else:
			self.step=round(((length-280)/6)+40, 3)

		if direct=='from_zero' and limit60==False:
			for i in range(8):
				if i==1:
					self.part_prog=f'G0X{position+15}Y20.000\n{self.drilling}'
				if i>1:
					self.part_prog=self.part_prog + f'G0Y{20+self.step*(i-1)}\n{self.drilling}'
		elif direct!='from_zero' and limit60==False:
			for i in range(8):
				if i==1:
					self.part_prog=f'G0X{position+15}Y{length-20}\n{self.drilling}'
				if i>1:
					self.part_prog=self.part_prog + f'G0Y{length-(20+self.step*(i-1))}\n{self.drilling}'

		elif direct=='from_zero' and limit60:
			for i in range(8):
				if i==1:
					self.part_prog=f'G0X{position+15}Y20.000\n{self.drilling}'
				if i==2:
					self.part_prog=self.part_prog + f'G0Y{20+self.step_one}\n{self.drilling}'
				if 7>i>2:
					self.part_prog=self.part_prog + f'G0Y{20+self.step_one+self.step*(i-2)}\n{self.drilling}'
				if i==7:
					self.part_prog=self.part_prog + f'G0Y{20+self.step_one*2+self.step*4}\n{self.drilling}'
					
		elif direct!='from_zero' and limit60:
			for i in range(8):
				if i==1:
					self.part_prog=f'G0X{position+15}Y{length-20}\n{self.drilling}'
				if i==2:
					self.part_prog=self.part_prog + f'G0Y{length-20-self.step_one}\n{self.drilling}'
				if 7>i>2:
					self.part_prog=self.part_prog + f'G0Y{length-(20+self.step_one+self.step*(i-2))}\n{self.drilling}'
				if i==7:
					self.part_prog=self.part_prog + f'G0Y{length-20-(self.step_one*2+self.step*4)}\n{self.drilling}'
		
		return self.part_prog



	def breakdown_new_gate_hole_down(self, length, direct='from_zero', position=0, limit60=False):

		if limit60:
			self.step=round(((length-255)/6)+35, 3)
			self.step_one=round(((length-255)/6)+37.5, 3)
		else:
			self.step=round(((length-280)/6)+40, 3)

		if direct=='from_zero' and limit60==False:
			for i in range(8):
				if i==1:
					self.part_prog=f'G0X{position+15}Y12.000\n{self.drilling}G0Y28.000\n{self.drilling}'
				if i>1:
					self.part_prog=self.part_prog + f'G0Y{12+self.step*(i-1)}\n{self.drilling}G0Y{28+self.step*(i-1)}\n{self.drilling}'
		
		elif direct!='from_zero' and limit60==False:
			for i in range(8):
				if i==1:
					self.part_prog=f'G0X{position+15}Y{length-12}\n{self.drilling}G0Y{length-28}\n{self.drilling}'
				if i>1:
					self.part_prog=self.part_prog + f'G0Y{length-(12+self.step*(i-1))}\n{self.drilling}G0Y{length-(28+self.step*(i-1))}\n{self.drilling}'

		elif direct=='from_zero' and limit60:
			for i in range(8):
				if i==1:
					self.part_prog=f'G0X{position+15}Y12.000\n{self.drilling}G0Y28.000\n{self.drilling}'
				if i==2:
					self.part_prog=self.part_prog + f'G0Y{12+self.step_one}\n{self.drilling}G0Y{28+self.step_one}\n{self.drilling}'
				if 7>i>2:
					self.part_prog=self.part_prog + f'G0Y{12+self.step_one+self.step*(i-2)}\n{self.drilling}G0Y{28+self.step_one+self.step*(i-2)}\n{self.drilling}'
				if i==7:
					 self.part_prog=self.part_prog + f'G0Y{12+self.step_one*2+self.step*4}\n{self.drilling}G0Y{28+self.step_one*2+self.step*4}\n{self.drilling}'

		elif direct!='from_zero' and limit60:
			for i in range(8):
				if i==1:
					self.part_prog=f'G0X{position+15}Y{length-12}\n{self.drilling}Y{length-28}\n{self.drilling}'
				if i==2:
					self.part_prog=self.part_prog + f'G0Y{length-(12+self.step_one)}\n{self.drilling}G0Y{length-(28+self.step_one)}\n{self.drilling}'
				if 7>i>2:
					self.part_prog=self.part_prog + f'G0Y{length-(12+self.step_one+self.step*(i-2))}\n{self.drilling}G0Y{length-(28+self.step_one+self.step*(i-2))}\n{self.drilling}'
				if i==7:
					self.part_prog=self.part_prog + f'G0Y{length-12-(self.step_one*2+self.step*4)}\n{self.drilling}G0Y{length-28-(self.step_one*2+self.step*4)}\n{self.drilling}'


		return  self.part_prog