import os
import curses
import pycfg
from pyarch import load_binary_into_memory
from pyarch import cpu_t

class os_t:
	def __init__ (self, cpu, memory, terminal):
	#inicia memporia,cpu e terminal.
		self.cpu = cpu
		self.memory = memory
		self.terminal = terminal

		self.terminal.enable_curses()

		self.console_str = ""
		self.terminal.console_print("this is the console, type the commands here\n")

	def printk(self, msg):
		self.terminal.kernel_print("kernel: " + msg + "\n")

	def panic (self, msg):
		self.terminal.end()
		self.terminal.dprint("kernel panic: " + msg)
		self.cpu.cpu_alive = False
		#cpu.cpu_alive = False
		
	def interrupt_keyboard (self):
		key = self.terminal.get_key_buffer()

		if ((key >= ord('a')) and (key <= ord('z'))) or ((key >= ord('A')) and (key <= ord('Z'))) or ((key >= ord('0')) and (key <= ord('9'))) or (key == ord(' ')) or (key == ord('-')) or (key == ord('_')) or (key == ord('.'))or (key == ord(',')):
			self.console_str += chr(key)
			# ord transforma em numeros que representam o caracter digitado(unicode)
			# chr transforma o unicode em caracter 
			# adiciona o valor da "key" na variavel controle_str
			
		elif key == curses.KEY_BACKSPACE:
			self.console_str = self.console_str[:-1]
			#[:-1] remove o ultimo valor no console
			return
			
		elif (key == curses.KEY_ENTER) or (key == ord('\n')):
			if(self.console_str == "sair"):
			# digite "sair" para encerrar o programa
				exit()  
				#funcao para encerrar o programa

			if(self.console_str== "iniciar"):
				self.terminal.console_print("\r"+"Iniciando...")

				
			self.console_str = ""

			return
			
	def handle_interrupt(self, interrupt):
		# realiza o print das funcoes
		# \r um caractere de retorno, ele diz ao seu emulador de terminal para mover o cursor no inicio da linha
		self.terminal.console_print("\r"+self.console_str)
		
		
		# Utiliza o arquivo "pycfg.py" para se referenciar ao "INTERRUPT_KEYBOARD" e verificar se o teclado foi usado
		# Se for usado segue para o metodo abaixo
		if interrupt == pycfg.INTERRUPT_KEYBOARD:
			self.interrupt_keyboard()
		return	
		
	def syscall (self):
	#self.terminal.app_print(msg)
		

		return
