make empty slice using make keyword

mySlice = make([]Type, size)
e.g.
myIntSlice = make([]int, 0)

append to slice using append function

myIntSlice = append(myIntSlice, val)
  - This is O(1), despite the reassignment.

Alternatively allocate the correct number of size for the slice and set the values via index, e.g.
myIntSlice[i] = val
