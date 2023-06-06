#include "lists.h"

/**
 * check_cycle - Check if a linked list contains a cycle
 * @list: a pointer to a linked list
 *
 * Return: 0 (if no cycle), 1 (if there's cycle)
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = NULL, *ptr = NULL;
	int check = 0;

	ptr = list;

	if (ptr->next > list)
		check = 1;
	else
		check = 0;

	while (ptr != NULL)
	{
		temp = ptr;
		ptr = ptr->next;
		if (check == 1)
		{
			if (temp > ptr)
				return (1);
		}
		else
		{
			if (temp < ptr)
				return (1);
		}
	}

	return (0);
}
