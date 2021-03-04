# Week 4: Array

![image-20210222112110170](C:\Users\alienware\AppData\Roaming\Typora\typora-user-images\image-20210222112110170.png)

Each placement in array takes up to **2 bytes**

## 1, Shallow and deep Copies

```python
colours1 = ["red", "green"] 
colours2 = colours1 
colours2 = ["rouge", "vert"] 
print(colours1)

# Output: ["red", "green"]
# Worst copy
```

### 1, Shallow Copy(不会进行深层复制)

#### Copying with slice Operator

```python
# Shallow Copy
list1 = ['a','b','c','d'] 
list2 = list1[:] 
list2[1] = 'x' 
print(list2)
print(list1)

# Output:
# ["a","x","c","d"]
# ["a","b","c","d"]

#----------------------------------------

old = [1,[1,2,3],3]
new = old[:]
 
new[0] = 3
new[1][0] = 3
 
'''
------------------
Before:
[1, [1, 2, 3], 3]
[1, [1, 2, 3], 3]
After:
[1, [3, 2, 3], 3]
[3, [3, 2, 3], 3]
------------------
'''
```

### 2, Deep Copy(可以进行深层复制）

```python
import copy
old = [1,[1,2,3],3]
new = copy.deepcopy(old)
 
new[0] = 3
new[1][0] = 3
 
'''
-----------------------
Before:
[1, [1, 2, 3], 3]
[1, [1, 2, 3], 3]
After:
[1, [1, 2, 3], 3]
[3, [3, 2, 3], 3]
-----------------------
'''
```

## 2, Arrays

### **Asymptotic Performance of Nonmutating Behaviors**

![image-20210222123844037](C:\Users\alienware\AppData\Roaming\Typora\typora-user-images\image-20210222123844037.png)

### **Asymptotic Performance of mutating behavior**

![image-20210222124205786](C:\Users\alienware\AppData\Roaming\Typora\typora-user-images\image-20210222124205786.png)

## 3, 2-D List

Create a 2-D list:

```python
data = [ [0]*c for j in range(r) ]
```



