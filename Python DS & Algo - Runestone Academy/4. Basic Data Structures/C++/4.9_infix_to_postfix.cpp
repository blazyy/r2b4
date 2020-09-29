#include<iostream>
#include <bits/stdc++.h>
#include<string>
using namespace std;

int precedence(char operand){
    int i;
    string operands = "^/*+-(";
    int precedences[] = {4, 3, 3, 2, 2, 1};
    for(i = 0; i < operands.length(); i++)
        if(operands[i] == operand)
            break;
    return precedences[i];
}

string infix_to_postfix(string expr){
    stack <char> op_stack;
    string postfix = "";
    for(int i = 0; i < expr.length(); i++){
        if(expr[i] == '(')
            op_stack.push(expr[i]);
        else if(isalpha(expr[i]))
            postfix += expr[i];
        else if(expr[i] == ')'){
            char top = op_stack.top();
            op_stack.pop();
            while(top != '(' && !op_stack.empty()){
                postfix += top;
                top = op_stack.top();
                op_stack.pop();
            }
        }
        else{
            while(!op_stack.empty() && precedence(op_stack.top()) >= precedence(expr[i])){
                postfix += op_stack.top();
                op_stack.pop();
            }
            op_stack.push(expr[i]);
        }
    }
    while(!op_stack.empty()){
        postfix += op_stack.top();
        op_stack.pop();
    }
    return postfix;
}

int main(void){
    cout << infix_to_postfix("A*B+C*D") << endl;                // A B * C D * +
    cout << infix_to_postfix("(A+B)*C-(D-E)*(F+G)") << endl;    // A B + C * D E - F G + * -
}
