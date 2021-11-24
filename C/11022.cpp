#include <stdio.h>

#define SIZE 500
typedef unsigned int UINT;
 
 
int main()
{

// [0] 변수 선언부 
	UINT T         = 0;
	UINT A         = 0;
	UINT B         = 0;
	UINT uiCount   = 0;
	UINT Store_A[SIZE]		= {};
	UINT Store_B[SIZE]		= {};
	UINT Store_Cal[SIZE]	= {};



// [1] 데이터 입력 후 테스트 케이스(T)에 할당 
	scanf("%d", &T);
	

// [2] 테이스 케이스(T)의 값에 따라, 입력 후 연산 실행 -> 저장 
	while(uiCount < T)
	{
		scanf("%d %d", &A, &B);
		Store_A[uiCount] 	= A;
		Store_B[uiCount] 	= B;
		Store_Cal[uiCount]	= A+B;
		
		uiCount ++;
	}
	uiCount = 0;
	
	
// [3] 저장된 값을 이용하여 "Case #x: A + B = C" 형식으로 출력
	while(uiCount<T)
	{
		printf("Case #%d: %d + %d = %d \n", uiCount+1, Store_A[uiCount], Store_B[uiCount], Store_Cal[uiCount]);
		uiCount ++;
	}
	
	return 0;
	
}

