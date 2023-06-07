#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Insert a number to a sorted list
 * @head: pointer to the pointer of the linked list
 * @number: the number to be inserted
 *
 * Return: address to the new node or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = NULL, *ptr = NULL, *new_node = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	ptr = *head;
	if ((*head)->n > number)
	{
		new_node->next = ptr;
		*head = new_node;
		return (new_node);
	}

	while (ptr != NULL)
	{
		temp = ptr;
		if (ptr->next != NULL)
			ptr = ptr->next;
		else
			break;

		if (ptr->n > number)
		{
			new_node->next = ptr;
			temp->next = new_node;
			return (new_node);
		}
	}
	if (ptr != NULL)
		ptr->next = new_node;
	return (new_node);
}
