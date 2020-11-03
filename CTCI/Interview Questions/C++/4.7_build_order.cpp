// You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project). All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.

// Example:
// Input:
//       projects : a, b, c, d, e, f
//       dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
// Output: f, e, a, b, d, c

#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;

class Graph{
private:
    unordered_map <char, vector <char>> graph;
    int num_projects = 0;
public:
    Graph(vector <vector <char>> connections, vector <char> projects){
        for(auto nodes : connections){
            if(graph.find(nodes[1]) == graph.end())
                graph[nodes[1]] = vector <char> {};
            graph[nodes[1]].push_back(nodes[0]);
        }
        for(auto project : projects){
            num_projects++;
            if(graph.find(project) == graph.end())
                graph[project] = vector <char> {};
        }
    }
    void remove_node_from_dependencies(char node_to_remove){
        // for(auto const &node : graph)
        unordered_map <char, vector <char>>::iterator it;
        for(it = graph.begin(); it != graph.end(); it++)
            if(find(it -> second.begin(), it -> second.end(), node_to_remove) != it -> second.end())
                it -> second.erase(find(it -> second.begin(), it -> second.end(), node_to_remove));
    }
    bool has_dependencies(){
        for(auto const &node : graph)
            if(graph[node.first].size() > 0) return true;
        return false;
    }
    vector <char> build_order(){
        vector <char> build_order = {};
        vector <char> removed_nodes = {};
        while(removed_nodes.size() < num_projects){
            for(auto const& node : graph){
                if(find(removed_nodes.begin(), removed_nodes.end(), node.first) == removed_nodes.end() && node.second.size() == 0){
                    build_order.push_back(node.first);
                    remove_node_from_dependencies(node.first);
                    removed_nodes.push_back(node.first);
                }
            }
        }
        if(has_dependencies()) return vector <char> {};
        return build_order;
    }
    void print(){
        for(auto const& node : graph){
            cout << node.first << ": ";
            for(auto adjacent : node.second)
                cout << adjacent << " ";
            cout << endl;
        }
    }
};

void print_vector(vector <char> vect){
    for (auto ch : vect) cout << ch << " ";
    cout << endl;
}

int main(void){
    vector <vector <char>> connections = {
        {'a', 'd'}, {'f', 'b'}, {'b', 'd'}, {'f', 'a'}, {'d', 'c'}
    };
    vector <char> projects = {'a', 'b', 'c', 'd', 'e', 'f', 'g'};
    Graph graph(connections, projects);
    graph.print();
    print_vector(graph.build_order());
}
