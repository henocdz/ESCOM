#include<stdio.h>
#include <stdlib.h>
#include <conio.h>
#define max 10
#define datos 2 //1=char,2=int,3=float

typedef int stackEntry;
        
typedef struct nodo{
               
               stackEntry data;
               struct nodo *next;
        }node;
        
typedef struct stack{
               node *top;
        }stack;
        
void createStack(stack *);
node *makeNode(stackEntry);
void push(stack *,stackEntry);
void printStack(stack);
void pop(stack *,stackEntry *);



void createStack(stack *s)
{
   s->top = NULL;
}

node *makeNode(stackEntry val)
{
     node *ap_return;
     if((ap_return = (node *)malloc(sizeof(node))) == NULL)
     {
          printf("No hay memoria");
          system("PAUSE");
          exit(0);
     }
     else
     {
         ap_return->data = val;
         ap_return->next = NULL;
     }
     
     return ap_return;
}


void push(stack *s, stackEntry val)
{
     node *new_node;
     new_node = makeNode(val);
     
     if(s->top == NULL) // Es el comienzo de la pila
         s->top = new_node;
     else //NO  es el comienzo de la pila
     {
          new_node->next = s->top;
          s->top = new_node;
     }
}

void pop(stack *s,stackEntry *val)
{
     if(s->top == NULL)
     {
        printf("\nLa pila esta vacia\n");
        return;
     }
     
     
     *val = s->top->data;
     
     node *aux;
     aux = s->top;
     
     s->top = s->top->next;
     free(aux);
     return;
}

void printStack(stack s)
{
     if(s.top == NULL)
        printf("\nLa pila esta   vacia\n");
         
     return;
     while(s.top != NULL)
     {
        printf("\nEl dato es %d \n",s.top->data);
        s.top = s.top->next;
     }
}





main(){
     char a[10];
     int i,var1,var2;
     stack s1;
     createStack(&s1);
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
     printStack(s1);
     getch();
}



