#include <stdio.h>

#define SIZE 500
typedef unsigned int UINT;
 
 
int main()
{

// [0] ���� ����� 
	UINT T         = 0;
	UINT A         = 0;
	UINT B         = 0;
	UINT uiCount   = 0;
	UINT Store_A[SIZE]		= {};
	UINT Store_B[SIZE]		= {};
	UINT Store_Cal[SIZE]	= {};



// [1] ������ �Է� �� �׽�Ʈ ���̽�(T)�� �Ҵ� 
	scanf("%d", &T);
	

// [2] ���̽� ���̽�(T)�� ���� ����, �Է� �� ���� ���� -> ���� 
	while(uiCount < T)
	{
		scanf("%d %d", &A, &B);
		Store_A[uiCount] 	= A;
		Store_B[uiCount] 	= B;
		Store_Cal[uiCount]	= A+B;
		
		uiCount ++;
	}
	uiCount = 0;
	
	
// [3] ����� ���� �̿��Ͽ� "Case #x: A + B = C" �������� ���
	while(uiCount<T)
	{
		printf("Case #%d: %d + %d = %d \n", uiCount+1, Store_A[uiCount], Store_B[uiCount], Store_Cal[uiCount]);
		uiCount ++;
	}
	
	return 0;
	
}

