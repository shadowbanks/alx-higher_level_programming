#include "lists.h"

int check_palindrome(listint_t **head, int node);
/**
 * is_palindrome - Check if a singly linked list is a palindrome
 * @head: double pointer to the beginning of the list
 *
 * Return: 1 (if a palindrome), 0 (if not)
 */
int is_palindrome(listint_t **head)
{
	listint_t *new_list = NULL, *temp = NULL;
	int node = 0, status;

	temp = *head;
	while (temp != NULL)
	{
		temp = temp->next;
		node++;
	}

	if (node == 1 || node == 0)
	{
		free_listint(new_list);
		return (1);
	}

	status = check_palindrome(head, node);

	if (status)
		return (1);
	return (0);
}

/**
 * check_palindrome - Compare data of two list
 * @head: first list
 * @node: list length
 *
 * Return: 1 (if equal), 0 (if not)
 */
int check_palindrome(listint_t **head, int node)
{
	listint_t *temp = NULL;
	int status = 1, i = 0, j = 0, num_arr[node];

	temp = *head;
	while (temp != NULL)
	{
		num_arr[i++] = temp->n;
		temp = temp->next;
	}

	while (j < (node / 2))
	{
		if (num_arr[j++] != num_arr[--i])
		{
			status = 0;
			break;
		}
	}

	return (status);
}
