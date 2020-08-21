print("This is a type casting of a number");
x=4.5;
print(int(x));

print("\nThis is a type casting to float\n ");
z=85;
print(float(z))

print("\n concatnation of a string\n");

str1=("This is a string to be concatenate");
str2=("This is the next string to be concatenate with first");
print("\n"+str1+str2);


print("\nconverting integer into a string");
integer = 45;
print("\nThis is a string now \t" +str(integer));

print("\nReversing The String");
rev=("This whole line has to be reversed");
print(rev[::-1]);

print("\n Multiline String to Print use three codes");
multi="""This 
is a multi
line string 
that i am writing here"""
print(multi);
print("This is the length of a string\t" +str(len(multi)));


print("\nRemoving the white space in a string");
empty =("    this is a space     we have to remove it    so we use strip       ");
print( empty.strip() );