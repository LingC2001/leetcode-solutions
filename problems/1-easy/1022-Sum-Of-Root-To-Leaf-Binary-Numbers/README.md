For Golang:
Slices are already pointers so we do not need to pass them into functions as pointers like this `*[]T` when we just want to modify the values.
However, when changing the size of the slice, we need to return it, therefore in that case we pass in as a pointer `*[]T`