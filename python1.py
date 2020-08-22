print("This is a type casting of a number");
x=4.5;
print(int(x));

print("\nThis is a type casting to float\n ");
z=85;
print(float(z))

print("\nconcatnation of a string\n");

str1=("This is a string to be concatenate");
str2=("This is the next string to be concatenate with first");
print("\n"+str1+str2);


print("\nconverting integer into a string");
integer = 45;
print("\nThis is a string now \t" +str(integer));

print("\nReversing The String");
rev=("This whole line has to be reversed");
print(rev[::-1]);

print("\nMultiline String to Print use three codes");
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


print("\nTo Check Weather it is staring with or ending with");
checking="This is word starts with and ends with";
print(checking.startswith("This"));
print(checking.endswith("with"));


print("\nTrue or False / Not True And Not False");
true = True;
false= False;
checkfalse = not False;
checktrue = not True;
print(true);
print(false);
print(checkfalse);
print(checktrue);


print("\nOpertors Normal Way");
minus=0;
minus-=55;
print(minus);


print("And or Not ")
compare1=45;
compare2=55;
print(compare1 and compare2);
print(compare1 or compare2);

print("\nValues in a order");
values="This will be printed as same";
for ge in values:
    print(ge);
print(not "This" in values);
print(not "this" in values);


print("\nBinary of Two");
print(2<<1);

print("\nIF else condition");
print("Please Enter One Value To See The Magic");
user1=int(input("Please Enter A Value:\t"));
if user1 == 1:
    print("Wow");
else:
    print("Try");


print("\nBoolean Condtion with little complex");
print("Please Enter A Value");
user2=int(input("Enter A Value:"));
if user2 >= 3:
    print("Please Use Small Number Less Than 3");
elif user2 ==1:
    print("Excellent");
elif user2 ==2:
    print("Good");
else:
    print("Invalid Input By You");


print("\nTo find the type of input by the user");
user3=int(input("Enter The Number:\t"));
user4=str(input("Enter Your Name:\t"));
print(type(user3));
print(type(user4))


print("\nCollections in python");
user5=["Arun Vijay","Anonymous","Coder","Programming"];
print(user5[0]);
user6=("This is a list","collection of Data");
print(user6.__hash__);
for fetching in user5:
    print(fetching);
print(type(user5));
print(type(user6));

print("\nAdding Deleting in a file");
user7=[];
user7.append("This is a function");
print(user7);
user8=[4,2,1,8,5,6];
user8.sort()
print(user8);


print("\nAppend Insert Pop More...");
user9=[]
user9.insert(0,"Arun Vijay");
user9.insert(1,"Arun Vijay");
user9.insert(2,"Programmer in Devlopment");
print(user9);
user9.pop(0);
print(user9);



print("""\nTuple Will Throw an error when there is no comma at the end when we are joining """);
user10=("Tuple","Adding Value");
user11=("Make Sure to add comma at the end or add second value","value");
user12=user10+user11
print(user12);


print("\nset {} don't have a index it will alway's be random");
user13={"The Values are not in order","They will be in unordered list"}
print(user13);
print("\nAdding More Functions in a set");
user13.add("Keep on adding more Function's");
print(user13);
user13.pop();
print(user13);
print(user13.difference());


print("\nThis is a dictionary ");
'''A dictionary is a collection which is unordered, changeable and indexed. 
In Python dictionaries are written with curly brackets, and they have keys and values'''
students={
    "name":"ARUN VIJAY",
    "Passion":"Multi-Talented-Thing's",
    "Hobiess":"Coding , Programming"
}
print(students);
print(students['name']);
print(students['Passion']);


print("\nMore About Dictionary")
user14=[
    {
        "class1": {"name":"arun vijay",
                "passion":"Programming"

    }
    },
    {
    "class2":{
        "name":"Anonymous",
        "passion":"Hacking"
    }
    } 
];
print(user14);
print(user14[0]);
print(user14[1]);
print(user14[0].values());
print(user14[0].keys());


print("\nWhile Loop")
user15=0
while user15<=10:
    user15=user15+1;
    print(user15)
print("\nSum of all Number")
user15=0
sum=0;
while user15<=10:
    user15=user15+1;
    sum = sum+user15;
print(sum)


print("\nContinue And Break")
user16=["arun Vijay","Programmer","Hacker"]
for i in user16:
    if i=="arun Vijay":
        continue
    print(i)

user17=["arun Vijay","coder","hacker"]
for i in user17:
    if i =="arun Vijay":
        break
    print(i)    