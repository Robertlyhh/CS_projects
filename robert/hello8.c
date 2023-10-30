#include <stdio.h>
#define max 100
static int cnt = 0;
void swap(int *x, int *y){
    int temp;
    temp = *y;
    *y = *x;
    *x = temp;
}

void permutation(int array[], int begin, int end){
    int i;
    if(begin == end){
        for(i=0; i<=end; i++){
            printf("%d", array[i]);
        }
        printf("\r\n");
        cnt++;
        return;
    }
    else{
        for(i=begin; i<=end; i++){
            swap(&array[i], &array[begin]);
            permutation(array, begin+1, end);
            swap(&array[i], &array[begin]);
        }
    }

}
int main(void){
    int a[6] = {1,2,3,4,5,6};
    permutation(a, 0, sizeof(a)/ sizeof(int)-1);

    printf("array as below: \r\n");
    for(int x=0; x<6; ++x){
        printf("%d", a[x]);
    }
}