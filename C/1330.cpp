# include <stdio.h>

int main()
{

// [0] ���� �����  
	int A;
	int B;


// [1] �� �Է� �ޱ� 
	scanf("%d %d", &A, &B);
	
	
// [2] �Է¹��� �� ���ؼ� ����ϱ� 
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
