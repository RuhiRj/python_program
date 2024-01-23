#include<stdio.h>
#include<conio.h>
int main()
{
float bonus;
int bal;
char doh;
printf("enter the deposite holder persion");
scanf("%c",&doh);
printf("enter the balance:");
scanf("%d",&bal);
if doh=="male"
{
    bonus=bal+bal*0.02;
    printf("%f",bonus);
}
if doh=="female"
{
    if bal<=5000
    bonus=bal+bal*0.02;
    printf("%f",bonus);
    else
    bonus=bal+bal*0.05;
    printf("%f",bonus);
}
return 0;
}
