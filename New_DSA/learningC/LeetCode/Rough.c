#include <stdio.h>
#include <stdlib.h>

// Define a node structure
struct Node {
    int data;
    struct Node* next;
};

// Function to insert a new node at the beginning of the linked list
struct Node* insertAtBeginning(struct Node* head, int newData) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = newData;
    newNode->next = head;
    return newNode;
}

// Function to insert a new node at the end of the linked list
struct Node* insertAtEnd(struct Node* head, int newData) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = newData;
    newNode->next = NULL;

    if (head == NULL) {
        return newNode;
    }

    struct Node* current = head;
    while (current->next != NULL) {
        current = current->next;
    }

    current->next = newNode;
    return head;
}

// Function to insert a new node at a given location in a sorted list
struct Node* insertAtLocation(struct Node* head, int newData, int position) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = newData;

    if (position == 1) {
        newNode->next = head;
        return newNode;
    }

    struct Node* current = head;
    int i;
    for ( i = 1; i < position - 1 && current != NULL; i++) {
        current = current->next;
    }

    if (current == NULL) {
        printf("Invalid position for insertion.\n");
        return head;
    }

    newNode->next = current->next;
    current->next = newNode;
    return head;
}

// Function to delete the first node of the linked list
struct Node* deleteFirstNode(struct Node* head) {
    if (head == NULL) {
        printf("List is empty. Cannot delete.\n");
        return NULL;
    }

    struct Node* temp = head;
    head = head->next;
    free(temp);
    return head;
}

// Function to delete the last node of the linked list
struct Node* deleteLastNode(struct Node* head) {
    if (head == NULL) {
        printf("List is empty. Cannot delete.\n");
        return NULL;
    }

    if (head->next == NULL) {
        free(head);
        return NULL;
    }

    struct Node* current = head;
    struct Node* previous = NULL;

    while (current->next != NULL) {
        previous = current;
        current = current->next;
    }

    free(current);
    previous->next = NULL;
    return head;
}

// Function to delete a node with a given item in the linked list
struct Node* deleteItem(struct Node* head, int key) {
    struct Node* current = head;
    struct Node* previous = NULL;

    while (current != NULL && current->data != key) {
        previous = current;
        current = current->next;
    }

    if (current == NULL) {
        printf("Item not found. Cannot delete.\n");
        return head;
    }

    if (previous == NULL) {
        // Deleting the first node
        head = head->next;
    } else {
        previous->next = current->next;
    }

    free(current);
    return head;
}

// Function to display the linked list
void displayList(struct Node* head) {
    struct Node* current = head;

    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }

    printf("NULL\n");
}

// Function to free the memory allocated for the linked list
void freeList(struct Node* head) {
    struct Node* current = head;
    struct Node* nextNode = NULL;

    while (current != NULL) {
        nextNode = current->next;
        free(current);
        current = nextNode;
    }
}

int main() {
    struct Node* head = NULL;

    // Insertion at the beginning
    head = insertAtBeginning(head, 5);
    head = insertAtBeginning(head, 3);
    head = insertAtBeginning(head, 1);

    // Display the list
    printf("Linked List after insertion at the beginning: ");
    displayList(head);

    // Insertion at the end
    head = insertAtEnd(head, 7);
    head = insertAtEnd(head, 9);

    // Display the list
    printf("Linked List after insertion at the end: ");
    displayList(head);

    // Insertion at a given location
    head = insertAtLocation(head, 6, 4);

    // Display the list
    printf("Linked List after insertion at position 4: ");
    displayList(head);

    // Deletion of the first node
    head = deleteFirstNode(head);

    // Display the list
    printf("Linked List after deleting the first node: ");
    displayList(head);

    // Deletion of the last node
    head = deleteLastNode(head);

    // Display the list
    printf("Linked List after deleting the last node: ");
    displayList(head);

    // Deletion of a given item
    head = deleteItem(head, 6);

    // Display the list
    printf("Linked List after deleting item 6: ");
    displayList(head);

    // Free the memory
    freeList(head);

    return 0;
}

