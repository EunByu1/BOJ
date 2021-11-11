# include <stdio.h>

int main()
{

// [0] 변수 선언부  
	int A;
	int B;


// [1] 값 입력 받기 
	scanf("%d %d", &A, &B);
	
	
// [2] 입력받은 값 비교해서 출력하기 
	if (A > B)
	{
		printf(">");
	}
	else if (A < B)
	{
		printf("<");
	}
	else 
	{
		printf("==");
	}
	
	
	return 0;

} // int main()
