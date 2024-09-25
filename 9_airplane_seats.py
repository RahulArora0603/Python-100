class WCT20():
    def __init__(self, num_of_seats):
        self.seats = num_of_seats
        self.passengers = []
    def add_passenger(self, name):
        if not self.available_seats():
            return False
        self.passengers.append(name)
        return True
    def available_seats(self):
        return self.seats - len(self.passengers)

squad = WCT20(15)
people = ["Virat","Surya","Rohit","Bumrah","Arshdeep","Siraj","Jadeja","Samson","Pant",
          "Yuzi","Kuldeep","Yashasvi","Hardik","Axar","Dubey","Rinku"]
for person in people:
    success = squad.add_passenger(person)
    if success:
        print(f"Player {person} will play T20 WC 2024.")
    else:
        print(f"Player {person} will not play in T20 WC 2024🥲.")   