def get (dinosaur, dinosaurs):
    return dinosaurs[dinosaur][0]

dinosaurs = {
    
    "A" : {"H", "C"},
    "B" : {"H", "T"}
        }

for val in dinosaurs.values():
    print (val)