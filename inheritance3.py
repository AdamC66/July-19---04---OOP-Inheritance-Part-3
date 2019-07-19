# First we'll need a class to represent the solar system. Let's call it System, 
# and give it an attribute bodies. bodies will start as an empty list (ie. []).

class System:
    def __init__(self):
        self.bodies = []
    def add(self,to_add):
        self.bodies.append(to_add)
    def total_mass(self):
        total = 0        
        for item in self.bodies:
            total += item.mass
        return(total)

# Let's give System an instance method called add which will add a celestial body to the list. 
# We'll also need an instance method called total_mass which should add up the mass of all the bodies in bodies, and return it.

# We'll also need a class to represent the various celestial bodies. We'll call it Body. Each of them will need a name and a mass. 
# We'll assign them when we create the body.

class Body:
    def __init__(self,name, mass):
        self.name = name
        self.mass = mass

# There are several types of bodies we're concerned about in our solar system: planets, stars (like our sun), and moons. 
# We'll ignore asteroids and smaller planetoids (sorry Pluto).
# Each of our body types needs a class: Planet, Star, and Moon. All of these bodies have some similarities: 
# they all have a name and a mass. So, let's also make them inherit from Body. They do have some unique qualities though.

# Planets:
# Have a day, which is the number of hours it takes for the planet to rotate all the way around once.
# Have a year, which is the number of days it takes for the planet to orbit the sun once. 
# Whether you want to express this in Earth days or the planet's days is up to you.

class Planets(Body):
    def __init__(self, name, mass, day, year):
        super().__init__(name, mass)
        self.day = day
        self.year = year
# Stars:
# Have a type (ie. our Sun is a G-type star)

class Stars(Body):
    def __init__(self, name, mass, type):
        super().__init__(name, mass)
        self.type = type

# Moons:
# Have a month, which is the number of days it takes for the moon to orbit its planet. Again, this can either be Earth days or the planet's days, your choice.
# Have a planet that they orbit. We want to store the whole Planet object here.

# Once we have our structure defined, let's start adding some things to our solar system. We can start with the Sun, the Earth, and the Earth's moon. 
# Don't worry too much about getting the masses correct, any number really will do, although you can find their masses on Wikipedia if you want.

class Moons(Body):
    def __init__(self,name, mass, month,planet_i_orbit):
        super().__init__(name,mass)
        self.month = month
        self.planet_i_orbit = planet_i_orbit
# Stretch Exercises
# Here's a couple extra things you can try out for extra cool points:

# Don't allow the same celestial body to be added to the system more than once. There's only one Mars.
# Add some class methods to Planet, Star, and Moon that will return all the planets, stars, and moons in the system, respectively (ie. Planet.all(system) should return all the planets in system)
# There's more than just our system in the galaxy, so let's make a couple others. Maybe the Alpha Centauri system, our closest neighbour, only 4.24 lightyears away.
# Now that we have a couple systems, what would it take to calculate our total galactic mass? (ie, the mass of all the bodies in all our systems) Find a way to write a class method on System that will return the total mass of all bodies in every system.
# Once you're done, commit and push your work to GitHub!

sun = Stars("The Sun", 100000000000, "G-type")
earth = Planets("Earth",100000,24,365)
moon = Moons("The Moon", 10000, 28, earth)

solarsystem = System()
solarsystem.add(sun)
solarsystem.add(earth)
solarsystem.add(moon)
print(solarsystem.total_mass())
