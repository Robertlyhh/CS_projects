#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
int M;
int i;
int b;
int c;
int f;
int j;
int main(void)
{
 printf("put in the number of code");
 scanf("%d", &M);
 int a[M][3];
 for(i=0;i<M;i++)
 {
     printf("put in code");
     scanf("%d", &j);
     a[i][0]=j/10000;
     a[i][1]=(j-10000*(j/10000))/1000;
     a[i][2]=j-10000*a[i][0]-1000*a[i][1];
     
      
 }
 for(i=0;i<M;i++)
 {   
     if(a[i][0]==9 && a[i][1]==9 && a[i][2]==999)
     {
         break;
     }
     if ((a[i][0]+a[i][1])%2==1)
     {
         printf("left, %d\n", a[i][2]);
         c=0;
     }
      else if ((a[i][0]+a[i][1])%2==0 && a[i][0]+a[i][1]!=0)
      {
          printf("right, %d\n", a[i][2]);
          c=1;
      }
      else
      {
        if (c==0)
         {
            printf("left, %d\n", a[i][2]);
         }
         else
         {
             printf("right, %d\n", a[i][2]);
         }
      }    
 }
}