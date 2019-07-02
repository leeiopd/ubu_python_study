import my_module

my_module.greeting()
my_module.greeting('이주호')

from my_module import greeting

greeting('이재찬')

print(my_module.pi)

from my_module import pi as p

print(my_module.pi)
print(p)