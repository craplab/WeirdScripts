#include <bits/stdc++.h>
using namespace std;
 
#define fast                    ios_base::sync_with_stdio(false);  cin.tie(NULL);
#define time                    cerr<<"Time taken : " <<(float)clock()/CLOCKS_PER_SEC <<" secs"<<"\n"  ;
#define F                       first
#define S                       second
#define pb                      push_back
typedef long long int           ll  ;
 
 
const ll INF = (ll)1e18   ;
const ll MOD = (ll)1e9 + 7 ;
 
 
void solve() {
 
    int n;
    cin >> n ;
 
    vector<int>arr(n) ;
 
    for(int i=0 ; i<n ; i++){
 
        arr[i]=i+1;
    }
 
    while(arr.size() > 1 ){
 
        vector<int>s ;
        for(int i=0 ;i<arr.size() ;i++){
            if(i%2){
                cout << arr[i] <<" "  ;
            }
            else{
                s.pb(arr[i])  ;
            }
 
        }
        if(arr.size()%2==1){
            int last = s.back() ;
            s.pop_back()  ;
            //trace(last)  ;
            arr.clear()  ;
 
            arr.pb(last) ;
            for(int i=0; i<s.size(); i++){
                arr.pb(s[i]) ;
            }
 
 
        }
        else
        if(arr.size() % 2 == 0){
 
            arr = s;
        }
 
 
    }
    cout << arr[0] <<"\n" ;
}
 
 
int32_t main() {
 
       fast ; time;
 
       int t = 1;
     //  cin >> t;
 
       while (t--) {
              solve()  ;
       }
 
 
       return 0  ;
}
