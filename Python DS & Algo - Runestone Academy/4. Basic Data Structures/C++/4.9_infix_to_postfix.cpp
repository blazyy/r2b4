#include<iostream>
#include<cstring>
using namespace std;
class Stack{
	public:
		char items[100];
		int top = 0;
		void push(char item){
			items[++top] = item;
		}
		char pop(){
			return items[top--];
		}
		char peek(){
			return items[top];
		}
		bool isEmpty(){
			return (top == 0) ? true : false;
		}
};

int precedence(char token){
	string operators_ = "^*/+-(";
	string precedences = "433221";
	for(int i = 0; i < operators_.length(); i++)
		if(token == operators_[i])
			return precedences[i];
	return -1;
}

string infix_to_postfix(string expr){
	char output_str[100];
	int output_str_idx = 0;
	Stack stack;
	char top;
	for(int i = 0; i < expr.length(); i++){
		if(isalpha(expr[i]))
			output_str[output_str_idx++] = expr[i];
		else if(expr[i] == '(')
			stack.push(expr[i]);
		else if(expr[i] == ')'){
			top = stack.pop();
			while(top != '(' && !stack.isEmpty()){
				output_str[output_str_idx++] = top;
				top = stack.pop();
			}
		}
		else{
			while(precedence(stack.peek()) >= precedence(expr[i]) & !stack.isEmpty())
				output_str[output_str_idx++] = stack.pop();
			stack.push(expr[i]);
		}
	}
	while(!stack.isEmpty())
		output_str[output_str_idx++] = stack.pop();
	return output_str;
}

int main(void){
    cout << infix_to_postfix("A*B+C*D") << endl;                // A B * C D * +
    cout << infix_to_postfix("(A+B)*C-(D-E)*(F+G)") << endl;    // A B + C * D E - F G + * -
}
