# 객체지향 다시

# class Car:
#   number = '54라 9538'

#   def __init__(self) -> None:
#       print('__init__')

#   def __new__(cls):
#       print('__new__')
#       return super().__new__(cls)

#   def __str__(self) -> str:
#       return f'내차 번호는 {self.number} 입니다.'

#   def get_number(self):
#       return self.number
  
# mycar = Car()

# print(mycar)
# print(mycar.get_number())
# print(mycar.number)
# print(type(mycar))

class Car:

    ## __new__ 사용 빈도 낮음, __init__ 사용 빈도 높음
    ## Car() 호춝하면 아래의 메서드가 실행
    ## company, name, plateNumber 모를때는 None
    def __init__(self, company= None, name= None, plateNumber= None):
        self.__company = company # 멤버변수 이름 앞에 __ 쓰면 외부접근 불가
        self.__name = name
        self.__plateNumber = plateNumber
        print('Car 클래스를 새로 생성!')

    # 클래스 자체가 출력되는데, __str__ 문자열로 출력되도록 바꿔줌
    def __str__(self):
        return (f' 제차는 {self.__name}이고, 번호는 {self.__plateNumber}입니다.')

    def setPlateNumber(self, newPlateNumber):
        if type(newPlateNumber) is str:
            self.__plateNumber = newPlateNumber

    def setName(self, newName='??'): # 이름을 모를때 "??"로 대체
        self.__name = newName

    def getName(self):
        return self.__name

# 모듈화 하려면 예제소스는 없어야함
# # myCar = Car('현대차', '아이오닉', '54라9537')
# # 파라미터명 = 값으로 매개변수 순서를 변경 가능
# myCar = Car(name='아이오닉', plateNumber='54라9537', company='현대')

# # print(myCar)
# myCar.__plateNumber = '54라9538' # 클래스 외부에서 잘못된 데이터를 넣어도 문제가 발생하지 않음
# print(myCar)

# myCar.setPlateNumber('54라9999')
# print(myCar)

# yourCar = Car()
# print(yourCar)
# yourCar.setPlateNumber('285구8899')
# print(yourCar)
# yourCar.setName('제네시스')
# print(yourCar)
# print(yourCar.getName())