#include <stdio.h>

int main()
{

// [0] ���� ����� 
	int user = 0;
	
	
// [1] ������ �Է�  
	scanf("%d", &user);


// [2] ù° �ٺ��� N��° �� ���� ���ʴ�� ���
	for(int i=0; i<user; i++)
	{
		printf("%d \n", i+1);
	}
	
	
	return 0;

}

