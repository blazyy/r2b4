#include<iostream>
#include<cstring>
using namespace std;

class Stack{
	public:
        int size = 50;
        char * items = new char[size];
	    int top = 0;
    	bool isEmpty(){
    		return (top == 0) ? true : false;
    	}
    	void push(char item){
    		items[++top] = item;
    	}
    	char pop(){
    		 return items[top--];
    	 }
    	char peek(){
    		return items[top];
    	}
    	int get_size(){
    		return top;
    	}
};

bool isOpener(char token){
	string openers = "({[";
	for(int i = 0; i < openers.length(); i++)
		if(openers[i] == token)
			return true;
	return false;
}

bool indexMatches(char opener, char closer){
	string openers = "({[";
	string closers = ")}]";
	for(int i = 0; i < openers.length(); i++){
		if(openers[i] == opener){
			if(closers[i] == closer)
				return true;
			return false;
		}
	}
}

bool checkParentheses(string expr){
	Stack stack;
	for(int i = 0; i < expr.length(); i++){
		if(isOpener(expr[i]))
			stack.push(expr[i]);
		else
			if((stack.isEmpty()) || (!indexMatches(stack.pop(), expr[i])))
				return false;
	}
	if(stack.isEmpty())
		return true;
	return false;
}

int main(void){

	cout << checkParentheses("{{([][])}()}") << endl;
	cout << checkParentheses("[[{{(())}}]]") << endl;
	cout << checkParentheses("[][][](){}") << endl;

	cout << checkParentheses("([)]") << endl;
	cout << checkParentheses("((()]))") << endl;
	cout << checkParentheses("[{()]") << endl;

}
