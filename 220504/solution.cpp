#include<stdio.h>
#include <iostream>
#include<deque>

using namespace std;

int solution(int total, deque<int> selectdeq){
    int totalnum = total;
    int result = 0;
    
    deque<int> currentdeq = selectdeq;

    for(int i = 0; i < selectdeq.size(); i++){
        int num = currentdeq.front();
        currentdeq.pop_front();
        int rot = num - 1;
        int reverserot = totalnum - num + 1;

        if(rot > reverserot){
            for(int j = 0 ; j < currentdeq.size(); j++){
                int item = currentdeq.front();
                currentdeq.pop_front();
                if(item > num){
                    currentdeq.push_back(item - num);
                }
                else{
                    currentdeq.push_back( totalnum-(num-item));
                }
            }
            result += reverserot;
        }
        else{
            for(int i = 0 ; i<currentdeq.size(); i++){
                int item = currentdeq.front();
                currentdeq.pop_front();
                if(item > num){
                    currentdeq.push_back(item - num);
                }
                else{
                    currentdeq.push_back( totalnum-(num-item));
                }
            }
            result += rot;
        }
        totalnum--;
    }
    return result;
}
