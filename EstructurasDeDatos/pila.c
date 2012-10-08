#include<stdio.h>
#include <conio.h>
#define max 4
#define datos 1 //1=char,2=int,3=float
typedef char stack_entry;

typedef struct stack
{
     int index;
     stack_entry data[max];
}stack;

void menu(int);
stack s1;
int indaux=0;

void create_stack(stack *a)
{
     a->index=-1;
}

int size(stack a)
{
    return(a.index +1);
}


stack_entry top(stack a)
{
    return (a.data[a.index]);
}

int isempty(stack a)
{
    return(a.index==-1);
}

int isfull(stack a)
{ 
    return(a.index+1==max);
}

void push (stack *a,stack_entry b)
{
    if(isfull(*a))
    {
        printf("La pila esta llena\n");
        return;
    }
    
    a->index++;
    a->data[a->index]=b;
}

void pop (stack *a, stack_entry *b)
{
     if(isempty(*a))
     {
         printf("La pila esta vacia\n");
         return;
     }
     
     *b=a->data[a->index];
     a->index--;
}

void imprimir(stack a)
{
    int i;
    switch(datos)
    {
        case 1: 
             for(i=a.index;i>=0;i--)
                printf("%c,",a.data[i]);
        break;
           case 2: 
             for(i=a.index;i>=0;i--)
                printf("%d,",a.data[i]);
        break;
        case 3:
             for(i=a.index;i>=0;i--)
                printf("%f,",a.data[i]);
        break;
    }
    
    printf("\n");
}





void main(){
char var;
stack s1,s2,s3;
create_stack(&s1);
create_stack(&s2);
create_stack(&s3);
push(&s1,'a');
push(&s1,'b');
push(&s1,'c');
push(&s1,'a');
push(&s1,'a');
imprimir(s1);
push(&s2,'1');
push(&s2,'2');
push(&s2,'3');
imprimir(s2);
push(&s3,'x');
push(&s3,'y');
push(&s3,'z');
imprimir(s3);
pop(&s1,&var);
imprimir(s1);
pop(&s1,&var);
pop(&s1,&var);
pop(&s1,&var);

getch();
}



