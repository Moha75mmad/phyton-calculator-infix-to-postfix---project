
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
#---------------------------------------------------
class calc:
    def __init__(self,s):
        self.S=s
        self.S+=';'
    def convert_to_postfix(self):
        self.sr=[]
        b=len(self.S)
        stack1=Stack()
        stack1.push('')
        i=0
        sum=0
        while(i<b) : 
            if (self.S[i]=='1' or self.S[i]=='2' or self.S[i]=='3' or self.S[i]=='4' or self.S[i]=='5' or self.S[i]=='6' or self.S[i]=='7' or self.S[i]=='8' or self.S[i]=='9'):
                sum=sum*10+int(self.S[i])
            if(self.S[i]=='+' or self.S[i]=='-' or self.S[i]=='*' or self.S[i]=='/' or self.S[i]=='^' or self.S[i]==';' or self.S[i]==')'):
                if(self.S[i-1]!= ')' or self.S[i-1]!= ')'):
                    self.sr.append(sum)
                    sum=0
            if(self.S[i]=='+' or self.S[i]=='-' or self.S[i]=='*' or self.S[i]=='/' or self.S[i]=='^' or self.S[i]=='(' or self.S[i]==')'):
                top=stack1.pop()
                stack1.push(top)
                if(Value(self.S[i]) >= Value(top) or self.S[i]=='(' or self.S[i]==')'):
                    stack1.push(self.S[i])
                    if(self.S[i]==')'):
                        k=0
                        while(k!=1):
                            e=stack1.pop()
                            if(e == '('):
                                k=1
                            if(e!='(' and e!=')'):
                                self.sr.append(e)
                else:
                    c=stack1.pop()   
                    stack1.push(self.S[i])
                    self.sr.append(c)          
            i+=1

        c='0'
        while(c!=''):
            c=stack1.pop()
            if(c!='') : 
                self.sr.append(c)
        
        #print(self.sr)
    def calculate(self):
        A=self.sr
        s=len(A)
        i=0
        while(i<s) :
            if(A[i]=='+' or A[i]=='-' or A[i]=='*' or A[i]=='/' or A[i]=='^') :
                x=i
                k=x
                i=-1
                if(A[x]=='+') :
                    b=A[x-2]+A[x-1]
                if(A[x]=='-') :
                    b=A[x-2]-A[x-1]
                if(A[x]=='*') :
                    b=A[x-2]*A[x-1]
                if(A[x]=='/') :
                    b=A[x-2]/A[x-1]
                if(A[x]=='^') :
                    b=A[x-2]**A[x-1]

                A[x-2]=b
                while(k<s-1):
                    A[k-1]=A[k+1]
                    k+=1
                k-=1
                while(k<s):
                    A[k]='null'
                    k+=1
            i+=1
        print(A[0])

#----------------------------------------------------- 
def Value(s):
    if(s=='') : 
        value=0
    if(s=='+' or s=='-') : 
        value=1
    if(s=='*' or s=='/') : 
        value=2
    if(s=='^') : 
        value=3
    if(s=='(' or s==')'):
        value=0   
    return value   
#-----------------------------------------------------
def main():
    f=open("calculator.txt","r") 
    d=f.read()
    calc1=calc(d)
    calc1.convert_to_postfix()
    calc1.calculate()
    f.close()

main()