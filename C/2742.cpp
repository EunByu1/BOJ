#include <stdio.h>

int main()
{

// [0] ���� ����� 
	int user = 0;


// [1] ������ �Է� 
	scanf("%d", &user); 


// [2] N���� 1���� �� �ٿ� �ϳ��� ���
	while(1)
	{
		printf("%d \n", user);
		user = user - 1;
		
		if (user == 0)
		{
			break;
		} 
	}
	
	return 0;
	
}
 
