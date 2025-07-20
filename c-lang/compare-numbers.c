#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
 
int solution(int num1, int num2) {
    if (num1 == num2) {
        return 1;
    } else {
        return -1;
    }
}
 
int main() {
    int num1, num2;
    printf("두 정수를 입력하세요: ");
    scanf("%d %d", &num1, &num2);
    
    int result = solution(num1, num2);
    printf("결과: %d\n", result);
    
    return 0;
}
