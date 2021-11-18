#include <stdio.h>

#define SIZE 100

int main()
{

// [0] 변수 선언부 
	int iTestCase = 0;
	int iSum[SIZE] = {};
	int i, j  = 0;
	int index = 0;
	int A 	  = 0;
	int B 	  = 0;

	
// [1] 테스트 케이스의 개수 입력 
	scanf("%d", &iTestCase);
	
	
// [2] 테스트 케이스의 개수만큼 값을 입력&연산 후 저장  
	while(i < iTestCase)
	{
		
		scanf("%d %d", &A, &B);
		iSum[index] = A + B;
		
		index++;  	
		i++;
	
	}


// [3] 테스트 케이스의 개수만큼 배열 값 출력 	
	for(int i = 0; i < iTestCase; i++)
	{
		printf("%d \n", iSum[i]);
	} 
	
	
	return 0;
	
}
