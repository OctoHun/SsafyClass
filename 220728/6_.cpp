////
//// �̿ϼ�
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
////    //1. new_id �� registered_list�� ���Ե� ���̵��ΰ�?(-> ���ٸ� ��밡��)
////
////    //2. new_id�� ��� �����Ǿ��ִ°�?
////
////    // -> S(�ҹ���) + N(����)
////    //Ư¡�� S�θ����ε� ��������
////    // �ٵ� �ߺ��̴ٸ� �ڿ� ���ڸ� �ٿ��� ���̵� ��õ��
////    //ex) bts <-> �ߺ� = ���ο� ���̵� ������ bts1 .. 2 .. 3.. 4..
////    // S�κа� N�κ��� ������
////    // N�� �ִٸ� ������Ű��, ���ٸ� 0���� ������ش��� 1�������ش�
////    // ex) bts�� �ߺ��̴ٸ� ��� bts + 0 ���� ������ ���̵��� �����ؾߴ�
////
////
////    for (int i = 0; i < registered_list.size(); i++)
////    {
////        if (new_id == registered_list[i]) {     //������ ���ٸ� �״�� ����
////            c++;
////            break;
////        }
////    }
////    if (c == 0)
////    {
////        return new_id;
////    }
////    else //������ �ִٸ� N+S ���·� ����� answer ��ȯ
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
////        else cout << "�����Դϴ�\n";
////    }
////
////    return 0;
//
//
//
//
//�ϼ���
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
//        //1��. �������������� ��
//        int ret = isInclude(target);
//        if (ret == 0) {
//            return target;
//        }
//
//        //2. �� indexã��
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
//        //3. �յ� �߶�
//        string front = target.substr(0, a);
//        string back = target.substr(a);
//
//        //4. ���ڿ� ������
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
//        else cout << "�����Դϴ�\n";
//    }
//
//    return 0;
//}