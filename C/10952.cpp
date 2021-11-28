# include <stdio.h>
# pragma warning (disable:4996)

# define SIZE 500

int main()
{

// [0] 변수 선언부 
	int Store[SIZE] = {0};
	int A = 0;
	int B = 0;
	int Count = 0;


// [1] 입력 후 연산 & 저장
	while (1) 
	{
		scanf("%d %d", &A, &B);
		Store[Count] = A + B;

		if (Store[Count] == 0)
			break;

		Count += 1;
	}
	Count = 0;


// [2] 저장된 값 출력
	while (1)
	{
		if (Store[Count] == 0)
			break;

		printf("%d \n", Store[Count]);
		Count += 1;
	}

	return 0;

}


