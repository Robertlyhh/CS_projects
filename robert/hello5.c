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
    while(1)
    {
        scanf("%d", &j);
        if(j==99999)
        {
            break;
        }
        M=j-j/1000*1000;
        if((j/10000+(j-j/10000*10000)/1000)%2!=0)
        {
            printf("\nleft, %d\n", M);
            b=0;
        }
        else if(j<1000)
        {
            if(b==0)
            {
                printf("\nleft, %d\n", M);
            }
            else
            {
                printf("\nright, %d\n", M);
            }
        }
        else
        {
            b=1;
            printf("\nright, %d\n", M);
        }
    }
}