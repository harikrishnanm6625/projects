class Vehicle:
    name='Kochi Travellers'
    def main(self,driver,conductor,travellers):
        self.driver=driver
        self.conductor=conductor
        self.travellers=travellers
    def print(self):
        print(self.driver)
        print(self.conductor)
        print(self.travellers)
class Bus(Vehicle):
    def submain(self):
        print(Vehicle.name)
obj=Bus()
obj.submain()
obj.main("Hari","Arun",46)
obj.print()

