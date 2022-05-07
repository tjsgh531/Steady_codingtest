#include<stdio.h>
#include<deque>

using namespace std;

deque<int> solution(int cardnum, int skills[], int skillnum){
    deque<int> deq, result;
    for(int i =1; i <= cardnum; i++ ){
        deq.push_back(i);
    }
    
    for(int i = skillnum-1; i>0; i++){
        int cur = skills[i];
        int item = deq.front();
        deq.pop_front();

        if(cur == 1){
            result.push_front(item);
        }
        else if(cur == 3){
            result.push_back(item);
        }
        else{
            int temp = result.front();
            result.pop_front();
            result.push_front(item);
            result.push_front(temp);
        }
    }
    return result;
}