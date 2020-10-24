// Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
// Page 75

#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>
#include <stack>
#include <queue>
using namespace std;

struct Node{
    char val;
    bool visited = false;
    Node(char value){
        val = value;
    }
};

class Graph{
private:
    unordered_map <char, vector<Node *>> graph;
    Node * root = NULL;
    set <Node *> nodes; // This is only used to reset the visited status of all nodes.
public:
    Graph(vector <vector <Node *>> connections){
        add_connections(connections);
    }
    void add_connections(vector <vector <Node *>> connections){
        for(auto vertex_pair : connections){
            if(graph.empty()) root = vertex_pair[0];
            graph[vertex_pair[0] -> val].push_back(vertex_pair[1]); // Connection from node1 to node2
            graph[vertex_pair[1] -> val].push_back(vertex_pair[0]); // Connection from node1 to node2
            nodes.insert(vertex_pair[0]);
            nodes.insert(vertex_pair[1]);
        }
    }
    void print(){
        for(auto const& pair : graph){ // For each pair of vertex and it's adjacent vertices
            cout << pair.first << ": "; // Vertex
            for(auto adjacent : pair.second) // and its neighbours.
                cout << adjacent -> val << " ";
            cout << endl;
        }
    }
    void unvisit_all_nodes(){
        for(auto node : nodes) node -> visited = false;
    }
    Node * get_nearest_unvisited_neighbour(Node * node){
        Node * nearest = NULL;
        for(auto neighbour : graph[node -> val])
            if(!neighbour -> visited)
                if(nearest == NULL || neighbour -> val < nearest -> val)
                    nearest = neighbour;
        return nearest;
    }
    // Solution 1
    // Do BFS starting at node 1. If node2 found during traversal, that means a route exists so return True
    // Time Complexity: O(V + E)
    // Space Complexity: O(V)
    bool is_connected_bfs(Node *node1, Node *node2){
        if(node1 == node2) return true;
        queue <Node *> qqueue;
        Node *neighbour;
        root -> visited = true;
        qqueue.push(root);
        while(!qqueue.empty()){
            neighbour = get_nearest_unvisited_neighbour(qqueue.front());
            if(neighbour != NULL){
                neighbour -> visited = true;
                qqueue.push(neighbour);
                if(neighbour == node2) return true;
            }
            else qqueue.pop();
        }
        unvisit_all_nodes();
        return false;
    }
    // Solution 2
    // Iterative DFS. If node2 found anywhere during traversal, return True
    // I did an iterative version because I needed to return a boolean, and I felt recursion wasn't a good idea due to that.
    // Time Complexity: O(V + E)
    // Space Complexity: O(V)
    bool is_connected_dfs(Node *node1, Node *node2){
        if(node1 == node2) return true;
        stack <Node *> sstack;
        sstack.push(root);
        root -> visited = true;
        while(!sstack.empty()){
            Node * current = get_nearest_unvisited_neighbour(sstack.top());
            if(current == NULL)
            sstack.pop();
            else{
                current -> visited = true;
                sstack.push(current);
                if(current == node2) return true;
            }
        }
        unvisit_all_nodes();
        return false;
    }
};

int main(void){
    Node *node_a = new Node('A'), *node_b = new Node('B'), *node_c = new Node('C'), *node_d = new Node('D'), *node_e = new Node('E'), *node_f = new Node('F'), *node_g = new Node('G'), *node_h = new Node('H');
    Node *node_x = new Node('X');
    vector <vector <Node *>> connections = {{node_a, node_b}, {node_a, node_d}, {node_a, node_g},
                                            {node_b, node_e}, {node_b, node_f},
                                            {node_c, node_f}, {node_c, node_h},
                                            {node_d, node_f},
                                            {node_e, node_g},
                                            };
    Graph graph = Graph(connections);
    graph.print();
    cout << "Route from node A to node B? " << graph.is_connected_dfs(node_a, node_b) << endl;
    cout << "Route from node A to node F? " << graph.is_connected_dfs(node_a, node_f) << endl;
    cout << "Route from node A to node X? " << graph.is_connected_dfs(node_a, node_x) << endl;
    cout << "Route from node A to node B? " << graph.is_connected_bfs(node_a, node_b) << endl;
    cout << "Route from node A to node F? " << graph.is_connected_bfs(node_a, node_f) << endl;
    cout << "Route from node A to node X? " << graph.is_connected_bfs(node_a, node_x) << endl;
}
