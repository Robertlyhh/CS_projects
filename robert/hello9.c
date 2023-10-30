#include <math.h>
#include<stdio.h>
#include <stdlib.h>
int n=5;
int k,a,c,max,i;
int row,col,min;
int place[5];
int main(void){
     /*printf("put in n");
     scanf("%d", &n);*/
     row=0;
     int count=1;
     int b[5][5]={0};
     col=0;
     while(count<=n*n)
     {
         b[row][col]=count;
         int i=row;
         int j=col;
         if(i==0)
             i=n-1;
         else
             i-=1;
         j=(j+1)%n;
         if((b[i][j]!=0)||(row==0&&col==n-1))
         {
             i=row+1;
             j=col;
         }
         row=i;
         col=j;
         count++;
     }
     for(int i=0;i<n;i++)
     {
         for(k=0;k<n;k++)
             printf("%d%c", b[i][k],32);
         printf("\n");
     }
     for(i=0;i<n;i++)
     {
         max=b[i][0];
         for(k=0;k<n;k++)
         {
            if(b[i][k]>max)
            {
                max=b[i][k];
            }
         }
         for(k=0;k<n;k++)
         {
             if(b[i][k]==max)
             {
                 place[i]=k;
             }
         }
     }
     for(i=0;i<n;i++)
     {
         printf("%d  ",place[i]);
     }
     for(i=0;i<n;i++)
     {
         min=b[0][place[i]];
         for(k=0;k<n;k++)
         {
            if(b[k][place[i]]<min)
            {
                min=b[k][place[i]];
            }

         }
         if(b[i][place[i]]==min)
         {
             printf("the point is in row %d column %d\n", i, place[i]);
             break;
         }
     }
     printf("there is no point");
}