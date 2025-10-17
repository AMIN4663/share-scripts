# #Q.1
# class user:
#     all_users = []
#     def __init__(self,name,):
#         self.name = name
#         user.all_users.append(self)
#
#     @classmethod
#     def get_user_count(cls):
#         return len(cls.all_users)
# u1 = user('Alic')
# u2 = user('Bob')
# print(user.get_user_count())
#
#
#



#Q.3
class car:
    def __init__(self, car_id:str, model:str,yaer:int,is_available=True ):
        self.car_id = car_id
        self.model = model
        self.yaer = yaer
        self.is_available = is_available
    def rent_car(self):
        if  self.is_available:

            return f"car {self.car_id} available, {self.model} {self.yaer}"

    def return_car(self):
        if not self.is_available:
            self.is_available = True
        #return f"car {self.model} available"
    def display_car(self):
        return f"car_id :  {self.car_id}  model: {self.model}, yaer: {self.yaer}, is_available: {self.is_available}"
class RentalAgency(car):
    def __init__(self,car_id:str,model:str,yaer:int,is_available=True, cars=[] ):
        self.cars = cars
        super().__init__(car_id, model, yaer, is_available)
    def add_car(self,car):
        self.cars.append(car)
    def find_car(self,car_id):
        for car in self.cars:
            if car.car_id == car_id:
                return car
    def rent_car(self,car_id):
            car = self.find_car(car_id)
            if car:
                car.rent_car()
                return car
    def avaialble_car(self):
        for car in self.cars:
            if car.is_available:
                return car

new_car= car("1", "benz",2008,True)
new_car.rent_car()
display = new_car.display_car()
print(display)
#print(new_car.return_car())
print(new_car.rent_car())

