class room(object):
    def enter(self):
        exit(1)
    
class Engine(object):
    
    def __init__(self, arrange_room):
  
        self.arrange_room = arrange_room        

    def go(self):
        
        current_room = self.arrange_room.opening_room()
        
        last_room = self.arrange_room.next_room('room3')
        
        while current_room != last_room:
        
            current_roomname = current_room.enter()
        
            current_room = self.arrange_room.next_room(current_roomname) 
            
        current_room.enter   
    
    
class room1(room):
    
    def enter(self):
    
        print "Attibute Error."
    
        raw_input()
    
        return 'room2'
    
class room2(room):

    def enter(self):

        print "But what can I do?"
     
        raw_input()
    
        return 'room3'
        
class room3(room):

    def enter(self):

        print "Riddle"
     
    
    
class Map(object):

    rooms = {'room1': room1(), 'room2': room2(), 'room3': room3()}
    
    def __init__(self, start_room):
        self.start_room = start_room
        
    def next_room(self, room_number):
        val = Map.rooms.get(self.room_number)
        return val
        
    def opening_room(self):
    
        return self.next_room(self.start_room)
    
    
A_map = Map('room1')
A_go = Engine(A_map)
A_go.go()


# 1. I did not put object in class xx(), no : after ()

# 2. I did not put : after while

# 3. did not indent under while.

# 4. did not put : after def openning():

# 5. did not even define any enter() function in each room class..

# 6. import non-exitened modules
