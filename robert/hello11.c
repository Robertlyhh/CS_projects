# include <stdio.h>
int main(void)
{
    char str[20] = "\0";  //字符数组初始化\0
    printf("请输入字符串：");
    gets(str);
    printf("%s\n", str);
    return 0;
}