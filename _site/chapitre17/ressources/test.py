import dis

code = """
a = 5
b = 3
a = a + b
print(a)
"""

def f():
    a = 5
    b = 3
    a = a + b
    print(a)
    


    
codesource2 = '''
x = 7
if x < 0:
    y = 2 * x
else:
    y = -2 * x
'''
for instruction in dis.get_instructions(codesource2):
    print(instruction)
    
code_object2 = compile(codesource2,'<string>','exec')
for octet in code_object2.co_code:
    print(octet, end = " ")
    
f = open('code-objet.b','wb')
f.write(code_object2.co_code)
f.close()

# In [104]: dis.dis(code_object2.co_code)
#           0 LOAD_CONST               0 (0)
#           3 STORE_NAME               0 (0)
#           6 LOAD_NAME                0 (0)
#           9 LOAD_CONST               1 (1)
#          12 COMPARE_OP               0 (<)
#          15 POP_JUMP_IF_FALSE       31
#          18 LOAD_CONST               2 (2)
#          21 LOAD_NAME                0 (0)
#          24 BINARY_MULTIPLY
#          25 STORE_NAME               1 (1)
#          28 JUMP_FORWARD            10 (to 41)
#     >>   31 LOAD_CONST               4 (4)
#          34 LOAD_NAME                0 (0)
#          37 BINARY_MULTIPLY
#          38 STORE_NAME               1 (1)
#     >>   41 LOAD_CONST               3 (3)
#          44 RETURN_VALUE
         
##
g = open('code-objet.b','rb')
code_objectmodif2 = g.read()
g.close()

# In [107]: dis.dis(code_objectmodif2)
#           0 LOAD_CONST               0 (0)
#           3 STORE_NAME               0 (0)
#           6 LOAD_NAME                0 (0)
#           9 LOAD_CONST               1 (1)
#          12 COMPARE_OP               4 (>)
#          15 POP_JUMP_IF_FALSE       31
#          18 LOAD_CONST               2 (2)
#          21 LOAD_NAME                0 (0)
#          24 BINARY_MULTIPLY
#          25 STORE_NAME               1 (1)
#          28 JUMP_FORWARD            10 (to 41)
#     >>   31 LOAD_CONST               4 (4)
#          34 LOAD_NAME                0 (0)
#          37 BINARY_MULTIPLY
#          38 STORE_NAME               1 (1)
#     >>   41 LOAD_CONST               3 (3)
#          44 RETURN_VALUE
    