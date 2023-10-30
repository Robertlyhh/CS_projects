#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
int M;
int t;
int i;
int u;
int h;
int a;
int b;
int c;
int e;
int f;
int main(void)
{    
    int p[M];
    int d=0;
    printf("put M");
    scanf("%d", &M);
    char str[100][100];
    int x[2000];
    for(t=0;t<M;t++)
    {
        printf( "put in the name of the buyer and their prices one by one\n");
        scanf("%s", str[t]);
        scanf("%d,\n", &x[t]);
        

    }
    /*for(e=0;e<M;e++)
    {
        printf("%s\n", str[e]);
        printf("%d\n", x[e]);
    }*/
    for(f=0; f<M; f++)
    {
        p[f]=x[f];
    }
    for(h=0; h<M; h++)
        {
            a=x[h];
            b=x[h+1];
            if(a>=b)
            {
                x[h+1]=x[h];
                c=h;
                d++;
            }
            else
            {
                c=h+1;
                d=0;
            }
        }
    
    printf("the winner is: %s\n", str[c+1-d]);
    printf("he offers: %d\n", p[c+1-d]);
    


    
}
