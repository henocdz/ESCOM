#include<stdio.h>
#include <stdlib.h>
#include <conio.h>

#define max 10
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

/*
stack_entry top(stack a)
{
    return (a.*data[a.index]);
}*/

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
     
     *b = a->data[a->index];
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


void menu(int e)
{
    system("CLS");
    if(e>0)
    {
       printf("Opcion incorrecta");
    }
    
    
    char op;
    printf("\nSelecciona una opcion del siguiente menu: \n1) Ingresar caracter a la cadena \n2) Deshacer \n3) Rehacer \n4) Imprimir pila \n 5) Salir \n\n\t Opcion deseada?: ");
    fflush(stdin);
    scanf("%c",&op);
    
    switch(op)
    {
       case '1':
           char car[max];
            system("cls");
           printf("Introduce un caracter para la cadena: ");
           fflush(stdin);
           gets(car);
           
           push(&s1,*car);
           indaux = 0;
           system("PAUSE");
           menu(0);
       break;
       case '2':
          system("cls");
             if(isempty(s1))
             {
               printf("No se han realizado acciones\n");
               system("PAUSE");
               menu(0);
             }
             indaux++;
             printf("Deshecho\n\n");
             s1.index--;
             system("PAUSE");
         menu(0); 
       break;
       case '3':
         system("cls");
         if(isfull(s1) || indaux<1)
         {
           printf("No hay acciones deshechas\n");
           system("PAUSE");
           menu(0);
         }
         indaux--;
         s1.index++;
         printf("Rehecho\n\n");
         system("PAUSE");
         menu(0);
       break;
       case '4':
            system("CLS");
            if(isempty(s1))
            {
                 printf("No hay nada en la pila\n");
                 printf("%d",s1.index);
                 system("PAUSE");
                 menu(0);    
            }
            imprimir(s1);
            printf("\n");
            system("PAUSE");
            menu(0);
       break;
       case '5':
            exit(0);
       break;
       default:
          menu(1);
       break;
    }        
}


main ()
{
   create_stack(&s1);
   menu(0); 
   getch();
}
