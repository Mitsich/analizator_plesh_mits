class Token:
	TYPE = None
	VALUE = None

class Lexier:
	listType = ['+','-','*','/','(',')', '=',';',' ']
	INT_LIT = "Число"
	IDENT = "Слово"
	ASSIGN_OP = "Символ равенства"
	ADD_OP = "Плюс"
	SUB_OP = "Минус"
	MULT_OP = "Символ умножения"
	DIV_OP = "Символ деления"
	LEFT_PAREN = "Левая скобка"
	RIGHT_PAREN = "Правая скобка"
	KOMA_POINT = "Точка с запятой"
	PROBEL = "Пробел"

	token = Token()
	lexemeList = list()

	def analyzer(self,inputString):
		def getIdent(self, input, index):
			count = index
			while(count < len(input) and input[count] != ' ' ):
				if(input[count] in self.listType):
					return input[index:count]
				count+=1
			return input[index:count]

		def switch(x):
			default = lambda x: x
			return {
				'+' : (self.ADD_OP, '+'),
				'-' : (self.SUB_OP, '-'),
				'*' : (self.MULT_OP, '*'),
				'/' : (self.DIV_OP, '/'),
				'(' : (self.LEFT_PAREN, '('),
				')' : (self.RIGHT_PAREN, ')'),
				';' : (self.KOMA_POINT, ';'),
				' ' : (self.PROBEL, ' '),
				'=' : (self.ASSIGN_OP,'='),
			}.get(x,-1)

		i = 0

		while(i < len(inputString)):
			newToken = Token()		
			if(switch(inputString[i]) == -1):
				ident = getIdent(self,inputString, i)				
				if(self.isNum(ident)):
					newToken.TYPE = self.INT_LIT
					newToken.VALUE = ident
					self.lexemeList.append(newToken)
					i += (len(ident)-1)
				else:
					if(ident and ident.strip()):					
						newToken.TYPE = self.IDENT
						newToken.VALUE = ident
						self.lexemeList.append(newToken)
						i += (len(ident))		
			else:
				newToken.TYPE = switch(inputString[i])[0]
				newToken.VALUE = switch(inputString[i])[1]
				self.lexemeList.append(newToken)
			i+=1


	def isNum(self,n):
		if (n.isdigit()):
			return True
		else:
			return False

	def getNext(self):
		if(len(self.lexemeList) > 0):
			output = self.lexemeList.pop(0)
			print("Тип: %s    Подстрока: %s" % (output.TYPE,output.VALUE))
			return output
		else:
			tmpToken = Token()
			tmpToken.TYPE = -100
			tmpToken.VALUE = "Ошибка"
			return tmpToken