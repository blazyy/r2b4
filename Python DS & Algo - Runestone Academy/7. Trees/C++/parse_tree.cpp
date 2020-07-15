#include <iostream>
#include <vector>
using namespace std;

class BinaryTree{
private:
    char root;
    BinaryTree * left = NULL;
    BinaryTree * right = NULL;
public:
    void insert_right(char value){
        BinaryTree * new_node = new BinaryTree();
        if(right == NULL)
            right = new_node;
        else{
            new_node -> right = right;
            right = new_node;
        }
    }
    void insert_left(char value){
        BinaryTree * new_node = new BinaryTree();
        if(left == NULL)
            left = new_node;
        else{
            new_node -> left = left;
            left = new_node;
        }
    }
    BinaryTree * get_right(){
        return right;
    }
    BinaryTree * get_left(){
        return left;
    }
    char get_root(){
        return root;
    }
    void set_root(char value){
        root = value;
    }
};

bool is_operator(char token){
    string ops = "+-/*";
    for(unsigned long long int i = 0; i < ops.length(); i++)
        if(ops[i] == token)
            return true;
    return false;
}

BinaryTree * build_parse_tree(string expr){
    vector <BinaryTree *> stack;
    BinaryTree * tree = new BinaryTree();
    stack.push_back(tree);
    for(long long unsigned int i = 0; i < expr.length(); i++){
        if(expr[i] == '('){
            tree -> insert_left(' ');
            stack.push_back(tree);
            tree = tree -> get_left();
        }
        else if(isdigit(expr[i])){
            tree -> set_root(expr[i]);
            tree = stack.back(); // In C++, pop_back() returns void
            stack.pop_back();
        }
        else if(is_operator(expr[i])){
            tree -> set_root(expr[i]);
            tree -> insert_right(' ');
            stack.push_back(tree);
            tree = tree -> get_right();
        }
        else{
            tree = stack.back();
            stack.pop_back();
        }
    }
    return tree;
}

int eval_parse_tree(BinaryTree * tree){
    //cout << "Root: " << tree -> get_root() << endl;
    char op;
    int left, right;
    BinaryTree * left_child = tree -> get_left();
    BinaryTree * right_child = tree -> get_right();
    if(left_child && right_child){
        op = tree -> get_root();
        left = eval_parse_tree(left_child);
        right = eval_parse_tree(right_child);
        switch(op){
            case '+': return left + right; break;
            case '-': return left - right; break;
            case '*': return left * right; break;
            case '/': return left / right; break;
        }
    }
    else{
        cout << "Returning " << tree -> get_root() << endl;
        return tree -> get_root() - '0';
    }
    return 1;
}

int main(void){
    cout << eval_parse_tree(build_parse_tree("(5+(2*1))")) << endl;
}
