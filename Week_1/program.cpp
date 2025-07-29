#include<bits/stdc++.h>
using namespace std;
int main(){
    deque<int>dq;
    for(int i=0;i<20;i+=3){
        dq.push_back(i);
    }

    for(int i=0;i<dq.size()/2;i++){
        dq.pop_front();
    }

    for(int i=0;i<dq.size();i++){
        cout<<dq[i]<<" ";
    }
}