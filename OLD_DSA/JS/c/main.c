#include<stdio.h>


int main() {
    int m,n,i;
    printf("enter the value of m&n");
    scanf("%d %d", &m,&n);
    
    for (i=m; i<=n; i++){

        if (i%2==0){
            printf("%d",i);
        }
    }
    return 0;
}