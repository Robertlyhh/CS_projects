#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#define SIZE 10000
int N;
int L;
int S;
int c;
int d;
int f;
int g;
int h;

/*void ignoreRestOfLine(FILE* fp)
{
   int c;
   while ( (c = fgetc(fp)) != EOF && c != '\n');
}*/


int main(void)
{
    scanf("%d%d%d", &N, &L, &S);
    int a[SIZE];
    int b[SIZE];
    int e[SIZE];
    int i=0;
    int s[SIZE];
    for(c=0; c<N; c++)
    {
        printf("Please enter :\n");
        //rewind(stdin);
        if ( scanf("%d%d%d", &a[c], &b[c], &s[c]) > 0 )
        {
            printf("%d, %d, %d\n", a[c], b[c], s[c]);
        } /*else {
            ignoreRestOfLine(stdin);
        }*/

    }
    for(f=0; f<N; f++)
    {
        e[f]=0;
    }
    for(d=0; d<N; d++)
    {
        for(g=a[d]; g<=b[d]; g++)
        {
            e[g]+=s[d];
        }
    }
    for(h=0; h<L; h++)
    {
        if(e[h]<S)
        {
            i++;
        }
    }
    printf("%d\n", i);

}
/*int main(void)
{
    int a;
    int c[10];
    int b;
    int d[10];
    int e;
    scanf("%d", &a);
    for(b=0;b<a;b++)
    {
        printf("ddd");
        scanf("%d%d", &c[b], &d[b]);
    }
    for(e=0;e<a;e++)
    {
        printf("%d %d\n", c[e], d[e]);
    }
}*/