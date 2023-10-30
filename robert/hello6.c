#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <math.h>
int a,b,c,d,e,f=0,g,h=1;
float i,o=0,p,q,r,s,t;
int j,k,l,m,n;

int main(void)
{
    int x;
    scanf("%d", &x);
    float a[x];
    float c[x];
    for(b=0;b<x;b++)
    {
        scanf("%f", &a[b]);

    }
    for (d=0;d<x;d++)
    {
        for(e=0;e<x;e++)
        {
            if(a[d]>a[e])
            {
                f++;
            }
            else if(a[d]==a[e])
            {
                h++;
            }
        }
        for(j=0;j<h;j++)
        {
            c[f+j]=a[d];
        }
        f=0;
        h=0;
    }
    for(g=0;g<x;g++)
    {
        printf("%f\n", c[g]);
        o+=c[g];

    }
    printf("the average is %f", o/x);
    scanf("%d", &k);
    p=x*k/100;
    q=p;
    l=(int)(p);
    if(q>l)
    {
       r=c[l];
    }
    else
    {
        r=(c[l-1]+c[l])/2;
    }
    printf("what you want is %f", r);



}