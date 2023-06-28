class Person
attr_accessor :name, :age

def initialize(name, age)
@name = name
@age = age.to_i
end

def inspect
"#{name} (#{age})"
end
end

p1 = Person.new("Elmo", 4)
p2 = Person.new("Zoe", 7)

p1 # => Elmo (4)
p2 # => Zoe (7)


