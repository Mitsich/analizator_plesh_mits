from lexier import Lexier
from lexier import Token

class Parser:
	lexier = Lexier()
	token = Token()
	nextToken = None

	def compile(self, inputString):	
		self.lexier.analyzer(inputString)
		self.getNextToken()
		self.expr()

	def expr(self):
		self.term()
		while(self.nextToken.TYPE == self.lexier.ADD_OP or self.nextToken.TYPE == self.lexier.SUB_OP):
			self.getNextToken()
			self.term()


	def term(self):

		self.factor()
		while(self.nextToken.TYPE == self.lexier.ASSIGN_OP or self.nextToken.TYPE == self.lexier.IDENT or self.nextToken.TYPE == self.lexier.MULT_OP or self.nextToken.TYPE == self.lexier.DIV_OP or self.nextToken.TYPE == self.lexier.KOMA_POINT or self.nextToken.TYPE == self.lexier.PROBEL):
			self.getNextToken()
			self.factor()


	def factor(self):

		while(self.nextToken.TYPE == self.lexier.IDENT or self.nextToken.TYPE == self.lexier.INT_LIT):
			self.getNextToken()
		else:
			if(self.nextToken.TYPE == self.lexier.LEFT_PAREN):
				self.getNextToken()
				self.expr()
				if(self.nextToken.TYPE == self.lexier.RIGHT_PAREN):
					self.getNextToken()
				else:
					self.error()

	def getNextToken(self):
		self.nextToken = self.lexier.getNext()

	def error(self):
		print("Синтаксическая ошибка")

parser = Parser()


if __name__ == '__main__':
	print("Лексический анализатор!")

	while 1:
		text = input("Введите выражение: ")
		parser.compile(text)

