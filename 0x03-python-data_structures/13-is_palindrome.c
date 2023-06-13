#include "lists.h"

int check_palindrome(listint_t **head, listint_t **new_list, int node);
/**
 * is_palindrome - Check if a singly linked list is a palindrome
 * @head: double pointer to the beginning of the list
 *
 * Return: 1 (if a palindrome), 0 (if not)
 */
int is_palindrome(listint_t **head)
{
	listint_t *new_list = NULL, *temp = NULL, *temp1 = NULL;
	int node = 0, status;

	temp = *head;
	while (temp != NULL)
	{
		add_nodeint_end(&new_list, temp->n);
		temp = temp->next;
		node++;
	}

	if (node == 1 || node == 0)
	{
		free_listint(new_list);
		return (1);
	}

	temp = new_list->next;
	new_list->next = NULL;
	while (temp != NULL)
	{
		temp1 = temp->next;
		temp->next = new_list;
		new_list = temp;
		temp = temp1;
	}

	status = check_palindrome(head, &new_list, node);

	free_listint(new_list);
	if (status)
		return (1);
	return (0);
}

/**
 * check_palindrome - Compare data of two list
 * @head: first list
 * @new_list: second list
 * @node: list length
 *
 * Return: 1 (if equal), 0 (if not)
 */
int check_palindrome(listint_t **head, listint_t **new_list, int node)
{
	listint_t *temp = NULL, *temp1 = NULL;
	int status = 1, i = 0;

	temp = *head, temp1 = *new_list;
	while (i++ < (node / 2))
	{
		if (temp->n != temp1->n)
		{
			status = 0;
			break;
		}
		temp = temp->next;
		temp1 = temp1->next;
	}

	return (status);
}
