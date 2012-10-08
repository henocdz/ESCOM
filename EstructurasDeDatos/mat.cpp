#include<stdio.h>
#include <stdlib.h>
#include <conio.h>
#define max 10
#define datos 2 //1=char,2=int,3=float
typedef int stack_entry;

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
             for(i=0;i<=a.index;i++)
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





main(){
     char a[10];
     int i,var1,var2;
     stack s1;
     create_stack(&s1);
     gets(a);
     for(i=0;a[i]!='\0';i++){
        switch(a[i]){
            case '+':
                 pop(&s1,&var2);
                 pop(&s1,&var1);
                 push(&s1,var1+var2);
            break;
            case '-':
                 pop(&s1,&var2);
                 pop(&s1,&var1);
                 push(&s1,var1-var2);
            break;
            case '*':
                 pop(&s1,&var2);
                 pop(&s1,&var1);
                 push(&s1,var1*var2);
            break;
            case '/':
                 pop(&s1,&var2);
                 pop(&s1,&var1);

                 var2=var1/var2;
                 push(&s1,var2);
            break;
            default:
             if(a[i]<48||a[i]>57){
                                  printf("error en la cadena de entrada:%c\n",a[i]);
                                  break;
                               }
             
             push(&s1,a[i]-48);
            }
        }
     imprimir(s1);
     getch();
}



