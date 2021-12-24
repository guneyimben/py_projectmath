while True:
    num = int(input("Sayınızı giriniz :"))
    if int(num) < 0:
        for i in range(int(num),0):
            if int(num) % i == 0:
                num2 = int(num / i)
                print(str(i) + "x" + str(num2))
    else:
        for i in range(0,int(num+1)):
            if i == 0:
                continue
            if int(num) % i == 0:
                num2 = int(num / i)
                print(str(i) + "x" + str(num2))