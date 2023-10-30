#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
int a;
int b;
int c;
char *s;
int d;
int f;
char *k;
int g=0;
int h=100000;
int i=5;
long l;
int m;
int main(void)
{
    
    scanf("%d", &a);
    int c[a];
    int f[a];
    for(b=0;b<a;b++)
    {
       scanf("%d", &c[b]);
       if(c[b]<=191)
       {
           c[b]=191;
       }
       while(1)
       {
          c[b]++;
          l=c[b]*c[b]*c[b];
          /*sprintf(s,"%d", c[b]*c[b]*c[b]);
          d= sizeof(s);
          if(s[d-1]==56 &&s[d-2]==56 && s[d-3]==56 )
          {
              f[g]=c[b]*c[b]*c[b];
              g++;
              break;
          }*/
          if(l-l/1000*1000==888)
          {
              f[g]=c[b];
              g++;
              break;
          }
          else if(c[b]>=2097152)
          {
              break;
          }
       }
    }
    for(h=0;h<g;h++)
    {
        printf("%d\n", f[h]);
    }
    
}