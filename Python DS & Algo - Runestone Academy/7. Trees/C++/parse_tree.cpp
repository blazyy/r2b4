#include<iostream>
#include<bits/stdc++.h>
using namespace std;

class BinaryTree{
private:
    char root;
    BinaryTree * left = NULL;
    BinaryTree * right = NULL;
public:
    void insert_left(char data){
        BinaryTree * new_node = new BinaryTree;
        new_node -> root = data;
        if(!left)
            left = new_node;
        else{
            new_node -> left = left;
            left = new_node;
        }
    }

    void insert_right(char data){
        BinaryTree * new_node = new BinaryTree;
        new_node -> root = data;
        if(!right)
            right = new_node;
        else{
            new_node -> right = right;
            right = new_node;
        }
    }

    BinaryTree * get_left(){
        return left;
    }

    BinaryTree * get_right(){
        return right;
    }

    void set_root(char token){
        root = token;
    }

    char get_root_val(){
        return root;
    }
};

bool is_operand(char token){
    string operands = "0123456789";
    for(auto operand : operands)
        if(operand == token)
            return true;
    return false;
}

bool is_operator(char token){
    string ops = "^/*+-";
    for(auto op : ops)
        if(op == token)
            return true;
    return false;
}

int eval_parse_tree(BinaryTree * parse_tree){
    BinaryTree * left = (*parse_tree).get_left();
    BinaryTree * right = (*parse_tree).get_right();
    if(left && right){
        char op = (*parse_tree).get_root_val();
        switch(op){
            case '+':
                return eval_parse_tree(left) + eval_parse_tree(right);
                break;
            case '-':
                return eval_parse_tree(left) - eval_parse_tree(right);
                break;
            case '/':
                return eval_parse_tree(left) / eval_parse_tree(right);
                break;
            case '*':
                return eval_parse_tree(left) * eval_parse_tree(right);
                break;
        }
    }
    else{
        return int((*parse_tree).get_root_val()) - '0';
    }
}

BinaryTree * build_parse_tree(string expr){
    BinaryTree * tree = new BinaryTree();
    vector <BinaryTree *> parent_stack;
    parent_stack.push_back(tree);
    for(auto token : expr){
        if(token == '('){
            (*tree).insert_left(' ');
            parent_stack.push_back(tree);
            tree = (*tree).get_left();
        }
        else if(is_operand(token)){
            (*tree).set_root(token);
            tree = parent_stack.back();
            parent_stack.pop_back();
        }
        else if(is_operator(token)){
            (*tree).set_root(token);
            (*tree).insert_right(' ');
            parent_stack.push_back(tree);
            tree = (*tree).get_right();
        }
        else{
            tree = parent_stack.back();
            parent_stack.pop_back();
        }
    }
    return tree;
}

int main(void){
    cout << eval_parse_tree(build_parse_tree("(5+(6/3))")) << endl;
}
