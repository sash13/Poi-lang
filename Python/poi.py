from __future__ import print_function
import sys, re, getopt, os
import click

VERSION = '1.0'

class PoiPoi:
	def __init__(self):
		self.array = [0]*30000
		self.instructions = []
		self.loop_count = 0
		self.index = 0
		self.pc = 0
	def forward(self):
		self.index+=1
	def backward(self):
		self.index-=1
	def inc(self):
		self.array[self.index]+=1
	def dec(self):
		self.array[self.index]-=1
	def put(self):
		print(chr(self.array[self.index]),end ='')
	def get(self):
		self.array[self.index] = int(input())
	def op(self):
		if self.array[self.index] == 0:
			self.loop_count+=1
			while self.loop_count:
				self.pc+=1
				if self.instructions[self.pc] == 'POi': self.loop_count+=1
				if self.instructions[self.pc] == 'pOI': self.loop_count-=1
	def cl(self):
		if self.array[self.index] == 0:
			pass
		else:
			if self.instructions[self.pc] == 'pOI': 
				self.loop_count+=1 
			while self.loop_count:
				self.pc-=1
				if self.instructions[self.pc] == 'POi': self.loop_count-=1
				if self.instructions[self.pc] == 'pOI': self.loop_count+=1
			self.pc-=1

	def lex(self, value):
		cases = {
			'Poi': lambda idx: self.forward(),		# >
			'poI': lambda idx: self.backward(),		# <
			'POI': lambda idx: self.inc(),				# +
			'poi': lambda idx: self.dec(),				# -
			'Poi!':lambda idx: self.put(),				# .
			'Poi?':lambda idx: self.get(),				# ,
			'POi': lambda idx: self.op(),					# [
			'pOI': lambda idx: self.cl()					# ]
		}
		try:										# my bad
			cases[value](None)
		except:
			print("\nUnrecognized op code: ", value)

	def load(self, file):
		read_data = re.sub(r"\s+", "", file)
		end = 0
		ind=0
		while ind < len(read_data):
			pice = read_data[ind:ind+4]
			if (pice[-1] == '?') or (pice[-1] == '!'):
				ind+=4
				self.instructions.append(pice[:])
			else:
				ind+=3
				if len(pice) == 3:
					self.instructions.append(pice[:])
				else:
					self.instructions.append(pice[:-1])
	def run(self):
		inst_count = len(self.instructions)
		while self.pc<inst_count:
			self.lex(self.instructions[self.pc])
			self.pc+=1

@click.command()
@click.argument('programm_file', type=click.File('r'))
@click.version_option(VERSION, '-V', '--version')
def main(programm_file): 
	poi = PoiPoi()
	poi.load(programm_file.read())
	poi.run()

if __name__ == '__main__':
	main()
