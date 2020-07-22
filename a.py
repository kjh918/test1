class C:
    def __init__(self):
        print('class C의 인스턴스가생성됨')
        self.name = 'ccc'
        self.age = 0
    
    def say_hi(self):
        print('hi')
    
    def add_age(self,n: int):
        self.age += 1 
    
    def __str__(self):
        return '__str__'
        # print에서 호출이 되는 부분   
    def __repr__(self):
        return '__repr__'
        # 변수값을 호출하면 나오는 부분
    def __abs__(self):
        print('__abs__')
 
    def __len__(self):
        print('__len__')
    
    def __add__(self,other):
        return self.age + other.age
