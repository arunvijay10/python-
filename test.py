print("\nPassing the value in specifier area")
def user38(a=45,b=85):
    c=a+b;
    print(c);
user38();

print("\nwill Not Take the default value")
def user39(a=85,b=85):
    c=a+b;
    print(c);
user38(44,88);