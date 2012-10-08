#include<stdio.h>
#include <stdlib.h>
#include <conio.h>

#define max 10
#define datos 1 //1=char,2=int,3=float


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

void pop(stack *s,stackEntry *val,stack *s2)
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
     push(s2,*val);
     free(aux);
     return;
}

void pop2(stack *s,stackEntry *val)
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
        
     stack ss;
     createStack(&ss);
     
     stackEntry aux2;
     
     while(s.top != NULL)
     {
                 

        aux2 = s.top->data;
        s.top = s.top->next;
        push(&ss,aux2);
        
   
     }
     while(ss.top != NULL){
                       
                  printf("%c,",ss.top->data);         
          ss.top = ss.top->next; 
          }
          
     
}



main ()
{
     stack s1,s2;
     int indaux=0;

createStack(&s1);
   createStack(&s2);
 int i=1;
  while(i)
   {
    system("CLS");
    
        char op;
    printf("\nSelecciona una opcion del siguiente menu: \n1) Ingresar caracter a la cadena \n2) Deshacer \n3) Rehacer \n4) Imprimir pila \n 5) Salir \n\n\t Opcion deseada?: ");
    fflush(stdin);
    scanf("%c",&op);
    stackEntry aux2;
    switch(op)
    {
       case '1':
           char car[max];
            system("cls");
           printf("Introduce un caracter para la cadena: ");
           fflush(stdin);
           gets(car);
           
           push(&s1,*car);
           s2.top = NULL;
           system("PAUSE");
           continue;
       break;
       case '2':
          system("cls");
             if(s1.top == NULL)
             {
               printf("No se han realizado acciones\n");
               system("PAUSE");
               continue;
             }
             
             printf("Deshecho\n\n");
             pop(&s1,&aux2,&s2);
             system("PAUSE");
         continue;
       break;
       case '3':
         system("cls");
         if(s2.top == NULL)
         {
           printf("No hay acciones deshechas\n");
           system("PAUSE");
          continue;
         }
         indaux--;
         pop2(&s2,&aux2);
         push(&s1,aux2);
         printf("Rehecho\n\n");
         system("PAUSE");
        continue;
       break;
       case '4':
            system("CLS");
            if(s1.top == NULL)
            {
                 printf("No hay nada en la pila\n");
                 system("PAUSE");
                 continue;    
            }
            printStack(s1);
            printf("\n");
            system("PAUSE");
            continue;
       break;
       case '5':
            i=0;
       break;
       default:
          continue;
       break;
    }        
}
exit(0);
}
