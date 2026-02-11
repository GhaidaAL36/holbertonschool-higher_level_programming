# Introduction

In Python, everything is an object. Numbers, strings, lists, functions, and even classes are all objects stored somewhere in memory. Variables do not store values directly — instead, they reference (point to) objects in memory.

# id and type

Every object in Python has:
* A type (what kind of object it is)
* An identity (its memory address)

we use 
```python
type()
``` 
to check the object type

```python
id()
```
to check the object identity

* Example:

```python
a = 9
print(type(a))
print(id(a))
```

* Output:

```python
<class 'int'>
140712345678912   # example memory address
```

If two variables point to the same object, their id() will be equal:

```python
a = 89
b = a

print(a is b)      # True
print(id(a) == id(b))  # True
```

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True (same value)
print(a is b)  # False (different objects)
```

# Mutable Objects

Mutable objects can be modified in place after creation.
* Example:

```python
l1 = [1, 2, 3]
l2 = l1

l1.append(4)
print(l2)
```

* Output:

```python
[1, 2, 3, 4]
```
Because l1 and l2 point to the same object

```python
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]

print(l1)  # [1, 2, 3, 4]
print(l2)  # [1, 2, 3]
```
Here, l1 + [4] creates a new list object, so l2 remains unchanged.

# Immutable Objects
Immutable objects cannot be changed after creation.

* Example (integers):

```python
a = 9
print(id(a))

a += 1
print(a)
print(id(a))
```

* Output:
```python
10
```
A new object was created when a changed.

* Example (strings):

```python
s = "Hello"
print(id(s))

s += " World"
print(s)
print(id(s))
```

A new string object is created, because strings are immutable.

# Mutable vs Immutable Objects

<img width="633" height="357" alt="1668804912016" src="https://github.com/user-attachments/assets/8f53de54-e83c-4e90-8bbd-08605f8f00a1" />

| Feature                                            | Mutable Objects                    | Immutable Objects                                   |
| -------------------------------------------------- | ---------------------------------- | --------------------------------------------------- |
| Can be modified after creation?                    | ✅ Yes                              | ❌ No                                                |
| Object identity (`id`) changes after modification? | ❌ No (usually same object)         | ✅ Yes (new object created)                          |
| Common Types                                       | `list`, `dict`, `set`, `bytearray` | `int`, `float`, `str`, `tuple`, `bool`, `frozenset` |
| Memory behavior                                    | Modified in place                  | New object created on change                        |
| Function side effects                              | Changes affect original object     | No effect unless returned and reassigned            |


# Why It Matters & How Python Treats Mutable vs Immutable Objects

## Identity behavior

```python
a = 1
b = 1
print(a is b)  # Often True (small int reuse)
```

```python
a = [1]
b = [1]
print(a is b)  # False
```

## Side effects

```python
def add_item(lst):
    lst.append(4)

l = [1, 2, 3]
add_item(l)
print(l)
```

* Output:

```python
[1, 2, 3, 4]
```

* Immutable objects cannot be modified:

```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

* Output:

```python
1
```

Because n += 1 created a new object locally.

# How Arguments Are Passed to Functions

Python uses object reference passing (sometimes called "pass-by-assignment").
When you call a function:
#### The parameter becomes a new reference to the same object.

### Immutable example:

```python
def increment(n):
    n += 1
    return n

a = 1
a = increment(a)
print(a)
```

* Output:
```python
2
```

Without returning, original a is unchanged.

### Mutable example:
```python
def add_value(lst):
    lst.append(4)

l = [1, 2, 3]
add_value(l)
print(l)
```

```python
[1, 2, 3, 4]
```
Because the function modified the object in place.

#### Rebinding inside function does NOT affect original

```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]

assign_value(l1, l2)
print(l1)
```

* Output:
```python
[1, 2, 3]
```
Because n = v only reassigns the local variable n, not l1.

# Final Summary

| Concept            | Meaning                                  |
|--------------------|------------------------------------------|
| `type()`           | Returns object type                      |
| `id()`             | Returns object identity (memory address) |
| `==`               | Compares values                          |
| `is`               | Compares identity                        |
| Mutable            | Can change in place                      |
| Immutable          | Cannot change after creation             |
| Function arguments | References to objects are passed         |
