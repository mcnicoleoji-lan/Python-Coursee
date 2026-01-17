class Nigeria():
    def capital(self):
           print("The capital of Nigeria is Abuja")

    def language(self):
            print("The official language of Nigeria is English")

    def type(self):
            print("Nigeria is a Federal Republic")

class USA():

    def capital(self):
            print("The capital of USA is Washington D.C.")

    def language(self):
            print("The official language of USA is English")

    def type(self):
             print("USA is a Federal Republic")

obj_ng = Nigeria()
obj_usa = USA()

for country in (obj_ng, obj_usa):
    country.capital()
    country.language()
    country.type()

    