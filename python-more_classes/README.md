Class attributes vs Instance attributes

Class attributes are shared by all instances (User.id = 1)
Once you set an attribute on an instance (u.id = 89), that instance gets its own copy and stops reading the class attribute
Changing the class attribute after an instance has its own copy does not affect that instance
If an instance has no own copy, it reads from the class attribute — so changing the class attribute does affect it

Special methods

__init__ → called when object is created
__str__ → called by print() and str() → informal, human-readable string
__repr__ → called by repr() → official string, ideally used to recreate the object with eval()
__del__ → called when object is deleted
__doc__ → the docstring of an object, not a method that prints — it just stores the string
