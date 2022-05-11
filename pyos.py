import os
import curses
import pycfg
from pyarch import load_binary_into_memory
from pyarch import cpu_t


class os_t:
	def __init__(self, cpu, memory, terminal):
		self.cpu = cpu
		self.memory = memory
		self.terminal = terminal

		self.terminal.enable_curses()

		self.console_str = ""
		self.command = ""
		self.terminal.console_print("Bem vindo ao console, digite os comandos.\n\n")

	def printk(self, msg):
		self.terminal.kernel_print("kernel: " + msg + "\n")

	def panic(self, msg):
		self.terminal.end()
		self.terminal.dprint("kernel panic: " + msg)
		self.cpu.cpu_alive = False
		#cpu.cpu_alive = False

	def interrupt_keyboard(self):
		key = self.terminal.get_key_buffer()

		if ((key >= ord('a')) and (key <= ord('z'))) or ((key >= ord('A')) and (key <= ord('Z'))) or ((key >= ord('0')) and (key <= ord('9'))) or (key == ord(' ')) or (key == ord('-')) or (key == ord('_')) or (key == ord('.')) or (key == ord(',')):
			# JUNTA A STRING QUE O USUARIO DIGITAR AO CONSOLE
			self.console_str += chr(key)
			# IMPRIMI O QUE ESTA NA VARIAVEL STRING
			self.terminal.console_print("\r" + self.console_str)
			# "\r" RETORNO REAL DA STRING (EVITA ERROS COM CARACTER ESPECIAL)

		elif key == curses.KEY_BACKSPACE:
			# REMOVE O ULTIMO CARACTER DA STRING
			self.console_str = self.console_str[:-1]
			# IMPRIME O QUE ESTA NA STRING
			self.terminal.console_print("\r" + self.console_str)
			return

		elif (key == curses.KEY_ENTER) or (key == ord('\n')):
			# VERIFICA SE ESTA VAZIO OU SE CONTEM CARACTERES ESPECIAIS
			if (self.console_str == "" or self.console_str.isspace()):
				self.terminal.console_print("Digite caracteres validos \n")
				self.console_str = ""

			else:
				self.terminal.console_print("\n")
				
				if(self.console_str == "sair"):
					exit()  # DIGITE "sair" PARA SAIR DO SISTEMA

				if(self.console_str[0:3] == "iniciar"):
					# COMANDO SEM EFEITO NO SISTEMA
					self.command = self.console_str[4:]
					self.syscall()

				self.console_str = ""

			return

	def handle_interrupt(self, interrupt):

		# VERIFICA SE HA INTERRUPCAO DO TECLADO E SE HOUVER SEGUE PARA O METODO ABAIXO
		if interrupt == pycfg.INTERRUPT_KEYBOARD:
			self.interrupt_keyboard()
		return

	def syscall(self):
		self.terminal.console_print("Loading Process{}".format(self.command))

		if(self.command == "print"):
			self.terminal.app_print("print nao implementado")
		elif(self.command == "teste"):
			self.terminal.app_print("teste nao implementedo")
		else:
			self.terminal.console_print("Comando {} não existe".format(self.command))

		self.command = ""

		return
