class TestClass:

    def __init__(self, num):
        self.num = num
    
    def show_num(self):
        print("num:", self.num)

if __name__ == "__main__":
    test_1 = TestClass(3)
    test_1.show_num() #3
    test_2 = TestClass(10)
    test_2.show_num() #10