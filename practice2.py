#실수형, 정수형으로 출력하기
a=123
b=123.45
print(a+b)
print("answer is %d" %(a+b))   #정수형
print("answer is %.2f" %(a+b)) #실수형

print("---------------------------")

#숫자 제곱하기
c=2
d=c**3
print(d)
print("answer is %d" %(c**3))

print("---------------------------")

#한줄 뛰어넘기, 스페이스바 4번 \n,\t
e = 1234
print("answer is %d\n" %e)
print("answer is %d\t" %e)###### 물어보기##############################
print('e\n')                    ######################################
print("---------------------------")

#나머지 구하기
num1 = 10
num2 = 15
print("answer is %d" %(num1%2))
print("answer is %d" %(num2%2))
print("answer is %.2f" %(num1%2))
print("answer is %s" %(num2%2))

print("---------------------------")

#문자열 프린트하기
print("Hello World")
print("Jaeyun's favorite color is red")
print('I said "Jaeyun is kind"')

str1 = "Jaeyun"
str2 = " is kind"
print(str1 + str2)

str3 = " python"
str4 = str3*3
print("answer is %s\t" %str4)

print("---------------------------")

#문자열 길이 구하기
str5 = "abcdefg"
print(len(str5))
print(str5[0])
print(str5[3])
print(str5[-1])

print("---------------------------")

