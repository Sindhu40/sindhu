#include<stdio.h>
#include<conio.h>
int main()
{
  char c;
    printf("Enter a character: ");
    scanf("%c",&c);
   if( (c>='a' && c<='z') || (c>='A' && c<='Z'))
         printf("this is an alphabet",c);
   else:
         printf("this is not an alphabet",c); 
         return 0;
}
