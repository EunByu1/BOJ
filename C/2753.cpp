# include <stdio.h>

int main()
{

// [0] ���� �����  
	int year; 


// [1] ������ �Է�
	scanf("%d", &year);


// [2] ���� �� �� ���
	if (( year % 4 ) == 0) 
	{
		if ((year % 100 ) != 0)
		{ 
        	printf("1");
    	}
		
		else if (( year % 400 ) == 0) 
		{
			printf("1");
		}
    	
		else 
		{
    		printf("0");
		}
	}		// if ( ( year % 4 ) == 0 ) 
	else 
	{
    	printf("0");
	}		//else 

return 0;

}
