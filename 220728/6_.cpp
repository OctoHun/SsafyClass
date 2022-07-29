////
//// 미완성
//// 
//// 
//// 
//// 
//// 
//// #include <iostream>
////#include <string>
////#include <vector>
////using namespace std;
////
////
////string find(string new_id) {
////    for (int i = 0; i < new_id.length(); i++)
////    {
////        if (new_id[i] >= '0' && new_id[i] <= '9')
////        {
////
////        }
////    }
////    new_id
////    
////
////
////
////}
////
////string solution(vector<string> registered_list, string new_id) {
////    string answer = "";
////    int c = 0;
////    //1. new_id 는 registered_list에 포함된 아이디인가?(-> 없다면 사용가능)
////
////    //2. new_id는 어떻게 구성되어있는가?
////
////    // -> S(소문자) + N(숫자)
////    //특징은 S로만으로도 생성가능
////    // 근데 중복됫다면 뒤에 숫자를 붙여서 아이디 추천을
////    //ex) bts <-> 중복 = 새로운 아이디 시작은 bts1 .. 2 .. 3.. 4..
////    // S부분과 N부분을 나눠서
////    // N이 있다면 증가시키고, 없다면 0으로 만들어준다음 1씩더해준다
////    // ex) bts가 중복됫다면 얘는 bts + 0 으로 구성된 아이디라고 생각해야댐
////
////
////    for (int i = 0; i < registered_list.size(); i++)
////    {
////        if (new_id == registered_list[i]) {     //같은게 없다면 그대로 리턴
////            c++;
////            break;
////        }
////    }
////    if (c == 0)
////    {
////        return new_id;
////    }
////    else //같은게 있다면 N+S 형태로 만들고 answer 반환
////    {
////        string answer=find(new_id);
////        new_id.
////
////
////    }
////
////
////
////    return answer;
////}
////
////int main()
////{
////    vector<vector<string>> registered_list = {
////        { "card", "ace13", "ace16", "banker", "ace17", "ace14" },
////        { "cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"},
////        { "bird99", "bird98", "bird101", "gotoxy"},
////        { "apple1", "orange", "banana3"}
////    };
////
////    vector<string> result = {
////        "ace15", "cow10", "bird100", "apple"
////    };
////
////    vector<string> newID = {
////        "ace15", "cow", "bird98", "apple"
////    };
////
////    for (int i = 0; i < registered_list.size(); i++) {
////        string yours = solution(registered_list[i], newID[i]);
////
////        if (yours == result[i]) cout << "GOOD!!\n";
////        else cout << "오답입니다\n";
////    }
////
////    return 0;
//
//
//
//
//완성본
//
//
//
//#include <iostream>
//#include <string>
//#include <vector>
//using namespace std;
//
//vector<string> regs;
//string target;
//
//int isInclude(string word) {
//    for (int i = 0; i < regs.size(); i++) {
//        if (regs[i] == word) return 1;
//    }
//    return 0;
//}
//
//string solution(vector<string> registered_list, string new_id) {
//
//    regs = registered_list;
//    target = new_id;
//
//    while (1) {
//        //1번. 존재하지않으면 끝
//        int ret = isInclude(target);
//        if (ret == 0) {
//            return target;
//        }
//
//        //2. 수 index찾기
//        if (!(target[target.size() - 1] >= '0' && target[target.size() - 1] <= '9')) {
//            target += '0';
//        }
//
//        int a = 0;
//        for (int i = 0; i < target.size(); i++) {
//            if (target[i] >= '0' && target[i] <= '9') {
//                a = i;
//                break;
//            }
//        }
//
//        //3. 앞뒤 잘라
//        string front = target.substr(0, a);
//        string back = target.substr(a);
//
//        //4. 문자열 만들자
//        int num = stoi(back) + 1;
//        target = front + to_string(num);
//    }
//
//    return 0;
//}
//
//int main()
//{
//    vector<vector<string>> registered_list = {
//        { "cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"},
//        { "card", "ace13", "ace16", "banker", "ace17", "ace14" },
//        { "bird99", "bird98", "bird101", "gotoxy"},
//        { "apple1", "orange", "banana3"},
//        {"bt1008","bt1003","bt1004","bt1005","bt1006","bt1007","bt1002"},
//        { "bird99", "bird98", "bird101", "gotoxy"},
//        { "aa9999"},
//    };
//
//    vector<string> result = {
//        "cow10","ace15",  "bird100", "apple", "bt1009", "gotoxy1", "aa10000"
//    };
//
//    vector<string> newID = {
//        "cow", "ace15", "bird98", "apple", "bt1002", "gotoxy", "aa9999"
//    };
//
//    for (int i = 0; i < registered_list.size(); i++) {
//        string yours = solution(registered_list[i], newID[i]);
//
//        if (yours == result[i]) cout << "GOOD!!\n";
//        else cout << "오답입니다\n";
//    }
//
//    return 0;
//}