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


print("\nThis is to write Upper and Lower Case");
low=("THIS IS TO BE IN THE LOWER CASE");
upp=("this is to be in the upper case");
print(low.lower());
print(upp.upper());


print("\nReplace");
rep=("replace this line with other line of sentence");
print(rep.replace("replace this line with other line of sentence","This line is been replaced"));

print("\nchecking weather the object or string is present or not");
objects="Arun Vijay ,Someone,Other";
store="Arun Vijay"in objects
print("This will return a boolean value\t"+str(store));


print("\nstring formatter")
name="Arun Vijay";
profession ="Programmer"
show ="My Name is {} and profession is {}";
print(show.format(name,profession));


print("\nFinding The index of a Text");
search = ("We have to find the index of Arun Vijay");
print(search.index("Arun Vijay"));

print("\nTo check weather its all upper lower alpha digit");
checkupper="ARUN VIJAY";
checklower="arun vijay";
checkdigit="12345";
checkalpha="ArunVijay";
checkascii="00000000";
print("This is Upper\t"+str(checkupper.isupper()));
print("This is Upper\t"+str(checklower.islower()));
print("This is a integer\t"+ str(checkdigit.isdigit()));
print("This is alphabet\t"+str(checkalpha.isalpha()));
print("This is ascii\t"+ str(checkascii.isascii()));