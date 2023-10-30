#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <cstring>
#define dec 1
int i,j,k,n,mid,i1,i2;
int main(){
    float arg[5][6];
    float argj[5][6];
    for(i=0;i<5;i++)
    {
        for(j=0;j<6;j++)
        {
             printf("put in the %d arguments of the %d equationn\n", j, i);
             scanf("%f" ,&arg[i][j]);
        }
    }
    for(i=0;i<5;i++)
    {
        for(j=0;j<5;j++)
        {
            for(k=0;k<5;k++)
                argj[i][k]=arg[i][k];
        }
        for(j=0;j<5;j++)
        {
            mid=argj[j][0];
            argj[j][0]=argj[j][i];
            argj[j][i]=mid;
        }
        for(j=0;j<4;j++)
        {
            for(k=j+1;k<5;k++)
            {
                if(argj[k][j+1]==0)
                    continue;
                for(i1=0;i1<6;i1++)
                {
                    argj[k][i1]*=argj[j][j+1]/argj[k][j+1];
                    argj[k][i1]-=argj[j][i1];
                    printf("%f ", argj[k][i1]);
                }
                printf("\n");
            }
        }
        printf("x%d = %f\n", i, argj[4][5]/argj[4][0]);
    }
}