class Computer:
    def __init__(self,name,make,os):
        self.name = name
        self.cpu = self.CPU(make)
        self.os = self.OS(os)

    def __str__(self):
        return 'Name: ' + str(self.name) + '\nMaker: ' + str(self.cpu.get_make()) + '\nOperating System: ' +  str(self.os.get_name())

    class CPU:
        def __init__(self,make):
            self.maker = make
        def get_make(self):
            return self.maker

    class OS:
        def __init__(self,os):
            self.Operating_System = os
        def get_name(self):
            return self.Operating_System

c1 = Computer("Vivek's Computer",'AMD','Windows 11')
print(c1)




