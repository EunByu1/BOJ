# include <stdio.h>
# pragma warning (disable:4996)

# define SIZE 500

int main()
{

// [0] ���� ����� 
	int Store[SIZE] = {0};
	int A = 0;
	int B = 0;
	int Count = 0;


// [1] �Է� �� ���� & ����
	while (1) 
	{
		scanf("%d %d", &A, &B);
		Store[Count] = A + B;

		if (Store[Count] == 0)
			break;

		Count += 1;
	}
	Count = 0;


// [2] ����� �� ���
	while (1)
	{
		if (Store[Count] == 0)
			break;

		printf("%d \n", Store[Count]);
		Count += 1;
	}

	return 0;

}


