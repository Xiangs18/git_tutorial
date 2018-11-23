class hello_word(object):
    print("Now I am inside a class")

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self):
        print("My first name is {} and my last name is {}".format(self.first_name,self.last_name))

if __name__ == '__main__':
    obj = hello_word("Sean","Xiang")
    obj.introduce()
