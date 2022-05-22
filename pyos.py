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

		if ((key >= ord('a')) and (key <= ord('z'))) or ((key >= ord('A')) and (key <= ord('Z'))) or ((key >= ord('0')) and (key <= ord('9'))) or (key == ord(' ')) or (key == ord('-')) or (key == ord('_')) or (key == ord('.')):
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
			elif(self.console_str == "run"):
			#placeholder
				self.terminal.app_print("\r"+"Iniciando...")
				exit()  
				#funcao para encerrar o programa
			
			elif(self.console_str[0:7]== "iniciar"):
			#placeholder syscall
				self.console_str= self.console_str[8:]
				self.syscall()
					
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
		self.terminal.console_print("\r"+"Carregando processo {}".format(self.console_str))

		if(self.console_str == "idle"):
			self.terminal.app_print("idle nao implementado")
		elif(self.console_str == "perfect-squares"):
			self.terminal.app_print("perfect-squares nao implementado")
		elif(self.console_str == "print"):
			self.terminal.app_print("print nao implementado")
		elif(self.console_str == "print2"):
			self.terminal.app_print("print2 nao implementado")
		elif(self.console_str == "test-gpf"):
			self.terminal.app_print("test-gpf nao implementado")
		elif(self.console_str == "teste"):
			self.terminal.app_print("teste nao implementado")
		else:
			self.terminal.console_print("\r"+"Comando {} nao existe".format(self.console_str))

		self.console_str = ""

		return
		
		
