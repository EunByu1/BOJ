#include <stdio.h>

#define SIZE 150

int main()
{
	
// [0] 변수 선언부
	int TestCase = 0;
	int iCount   = 0;
	int A	     = 0;
	int B	     = 0;
	int iStore[SIZE] = {0};
	
			
// [1] 데이터 입력 (테스트 케이스의 개수 입력) 
	scanf("%d", &TestCase);
	
	
// [2] 테스트 케이스의 개수만큼 데이터 추가 입력 후 연산 -> 저장  
	while(iCount < TestCase)
	{
		scanf("%d %d", &A, &B);
		iStore[iCount] = A+B;
		
		iCount++;
	}
	iCount = 0;
	 
	  
// [3] 저장된 값 출력 
	while(iCount < TestCase)
	{
		printf("Case #%d: %d \n", iCount+1, iStore[iCount]);
		
		iCount ++;
	}

	return 0;
	 
}
