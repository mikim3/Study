#include <stdio.h>
int main(void)
{
    char s[50];
    int i=0;
    printf("문자열을 입력하세요: ");
    gets(s);
    while(s[i]!='\0')
    {
        printf("%c",s[i]^32); //32는 2진수로 100000
        i++;
    }
    printf("\n");
    return 0;
}