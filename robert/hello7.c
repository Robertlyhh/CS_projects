#include <stdio.h>
int x;
int main()
{
    printf("get x:");
    scanf("%d",&x);
    int i,i2=1,i3,i4,i5,i7;
    int j=1,k;
    for(i=1;i<=x;i++) j*=i;
    printf("%d\n",j);
    int num[j][2*x-1];
    int num4[j][2*x-1];
    for(i=0;i<j;i++)
        for(k=0;k<2*x-1;k++)
             num4[i][k]=0;
    for(i=0;i<j;i++)
        for(k=0;k<2*x-1;k++)
        {
             num[i][k]=0;
        }
    num[0][0]=1;num[0][1]=2;
    num[1][0]=2;num[1][1]=1;
    for(i=2;i<x;i++){
        i2=1;
        for(k=1;k<=i;k++) i2*=k;
        for(k=0;k<i2;k++)
        {
            int num3[i];
            for(i5=0;i5<i;i5++)
                num3[i5]=0;         
            int i6=0;
            for(i5=0;i5<=2*i;i5++)
                if(num[k][i5]){
                     num3[i6]=num[k][i5];
                     i6++;}
            for(i3=k*(i+1);i3<(k+1)*(i+1);i3++)
                for(i4=0,i6=0;i4<=2*i;i4+=2,i6++)
                    {num4[i3][i4]=0;
                    num4[i3][i4+1]=num3[i6];}
            for(i3=k*(i+1),i4=0;i3<(k+1)*(i+1)&&i4<=2*i;i3++,i4+=2)
                 num4[i3][i4]=i+1;
        }
        for(k=0;k<j;k++)
             for(i5=0;i5<2*x-1;i5++)
                 num[k][i5]=num4[k][i5];}     
    i7=0;
    int i8=0;
    for(i=0;i<j;i++)
        for(k=0;k<2*x-1;k++){
             if(num[i][k]>0){
                 printf("%d",num[i][k]);
                 i7++;}
             if(i7==x){
                     printf("\n");
                     i7=0;
                     i8++;}}
    printf("%d\n", i8);
    printf("%d\n",j);
}
