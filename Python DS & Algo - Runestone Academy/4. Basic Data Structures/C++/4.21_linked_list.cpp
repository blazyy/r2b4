#include<iostream>
using namespace std;

struct Node{
	int data;
	struct Node * next = NULL;
};

class LinkedList{
private:
	Node * head = NULL;
public:
	bool isEmpty(){
		return (head == NULL) ? true : false;
	}
	void add(int data){
		Node * newNode = new Node;
		newNode -> data = data;
		if(head == NULL)
			head = newNode;
		else{
			Node * current = head;
			while(current -> next != NULL)
				current = current -> next;
			current -> next = newNode;
		}
	}

	int pop(int index_to_pop = -1){
		Node * current = head;
		int return_num, idx = 0;
		if(index_to_pop == -1){ // Pops from the end of the list by default
			while(current -> next -> next)
				current = current -> next;
			return_num = current -> next -> data;
			current -> next = NULL;
		}
		else if(index_to_pop == 0){ // If index to pop is head, make next of head as the new head.
			return_num = current -> data;
			head = current -> next;
		}
		else{ // If the index to pop from is neither the head nor the last
			Node * previous = head;
			while(current -> next){
				if(idx == index_to_pop){
					return_num = current -> data;
					previous -> next = current -> next;
				}
				idx += 1;
				previous = current;
				current = current -> next;
			}
		}
		return return_num;
	}

	void remove(int ele){
		Node * current = head;
		Node * previous = head;
		(current -> data == ele) ? head = current -> next : current = current -> next;
		while(current){
			if(current -> data == ele){
				previous -> next = current -> next;
				return;
			}
			previous = current;
			current = current -> next;
		}
	}

	bool search(int ele){
		Node * current = head;
		while(current){
			if(current -> data == ele)
				return true;
			current = current -> next;
		}
		return false;
	}

	int get_size(){
		Node * current = head;
		int size = 0;
		while(current){
			size += 1;
			current = current -> next;
		}
		return size;
	}

	int get_index(int data){
		int idx = 0;
		Node * current = head;
		while(current){
			if(current -> data == data)
				return idx;
			idx += 1;
			current = current -> next;
		}
		return -1;
	}

	void display(){
		Node * current = head;
		while(current){
			cout << current -> data << " ";
			current = current -> next;
		}
		cout << endl;
	}
};

int main(void){
	LinkedList ll;
	ll.add(5);
	ll.display();
	ll.remove(5);
	ll.display();
}
