def divide(number, divisor):
	#1,0
	if divisor == 0:
		return "Quotient is undefined"
	negative = False
	if number < 0 or divisor < 0:
		negative = True
	number = abs(number)
	divisor = abs(divisor)
	#11,2
	#10,2
	#-10,2
	#10,-2
	#0,1
	#11,2:
	#2 4 6 8 10 r 1
	sumDiv = 0
	#answers:
	mult = 0
	remainder = 0
	#number - sumDiv
	while sumDiv < number-divisor:
		sumDiv = sumDiv + divisor
		print(sumDiv)
		mult = mult + 1
	#11,2: 
	#mult = 5
	#sumDiv = 10
	if sumDiv + divisor == number:
		remainder = 0
		mult = mult + 1
	else:
		remainder = number - sumDiv
	if negative is True:
		mult = -mult
	answer = []
	answer.append(mult)
	answer.append(remainder)
	return answer

def main():
	answer = divide(-6,-6)
	print(answer)

if __name__ == "__main__":
	main()
