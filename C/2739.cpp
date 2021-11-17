#include <stdio.h>

int main()
{
	
	// [0] 변수 선언부 
	int iStep = 0;
	 
	 
	// [1] 데이터 입력 
	scanf("%d", &iStep);
	
	
	// [2] for문을 통해 구구단 출력 
	for(int iValue = 1; iValue < 10; iValue++)
	{
		printf("%d * %d = %d \n", iStep, iValue, iStep * iValue);
	}

	return 0; 
	 
}
