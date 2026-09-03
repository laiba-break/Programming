//C++ Program on HOSTEL MANAGEMENT for Final FOP Project
// these are our standard library header files
#include <iostream>
#include <string>       //string library
#include <fstream>      //fstream library
#include <windows.h>    // for sleep and color
// gob stands for go back to main menu
char gob; // a global variable used for returning to mainmenu again and again from different functions
using namespace std;

// our structure
struct student    //structure for student data
{
    string name;
    string fn;
    string phone_number;
    string f_number;
    string birth;
    string address;
    string mess_bill;
    string paid_mess;
    string hostel_bill;
    string paid_hostel;
    string pay_method;
};

// Function prototypes
void mainmenu();
void bdinf();
void recd(int*, struct student std[], fstream&);
void edit(int*, struct student std[], fstream&);
void delet(int*, struct student std[], fstream&);
void duty();
void MessI();
void HostelR();
void laundry(int*);
void backToMenu(char*);   // RENAMED from exit(char*) -- this was colliding with std::exit(int)
void student();
void display(int*, struct student std[], fstream&);

int main()
{
    system("color c");
    cout << "\n\n\n";
    Sleep(150);
    cout << "\t\t\t\t * * *  **** *      ****  ***   ***   ****   " << endl;
    Sleep(150);
    cout << "\t\t\t\t * * * *     *     *     *   * * * * *        " << endl;
    Sleep(150);
    cout << "\t\t\t\t * * * ***** *     *     *   * * * * *****    " << endl;
    Sleep(150);
    cout << "\t\t\t\t * * * *     *     *     *   * * * * *         " << endl;
    Sleep(150);
    cout << "\t\t\t\t  ***   **** *****  ****  ***  * * *  ****     " << endl;
    Sleep(150);
    cout << endl;
    cout << "\t\t\t\t=============================================" << endl;
    Sleep(150);
    cout << "\t\t\t\t     DE-42'S HOSTEL MANEGEMENT SYSTEM " << endl;
    Sleep(150);
    cout << "\t\t\t\t=============================================" << endl;
    Sleep(150);
    cout << endl;
    Sleep(150);
    cout << "\n\t\t\t**********************************************************************";
    Sleep(150);
    cout << "\n\t\t\t\t\t       *GROUP MEMBERS*" << endl;
    Sleep(150);
    cout << "\n\t\t\t\t\t        LAIBA MEMON" << endl;
    Sleep(150);
    cout << "\n\t\t\t\t\t        AYESHA NAVEED" << endl;
    Sleep(150);
    cout << "\n\t\t\t\t\t       SARIM FARQALEET" << endl;
    Sleep(150);
    cout << "\n\t\t\t\t\t         ROHAB IMRAN" << endl;
    Sleep(150);
    cout << "\n\t\t\t      PRESENTED TO SIR AQIB PERWAIZ AND MA'AM AYESHA BATOOL " << endl;
    Sleep(150);
    cout << "\n\t\t\t*************************************************************************";
    Sleep(150);
    cout << "\n\n\t\t\t\tPress any key to continue!" << endl;
    cin.ignore();
    mainmenu();
    system("pause");
    return 0;
}

void mainmenu()
{
    system("cls");
    system("color 3");
    int selection, selection2;
    string Password, username;
    fstream Hostel;
    struct student std[30];

    cout << "\n\t\t\t\t\t\t*************";
    cout << "\n\t\t\t\t\t\t* MAIN MENU *";
    cout << "\n\t\t\t\t\t\t*************";
    cout << endl;
    cout << "\n\t\t\t1. Student" << endl;
    Sleep(150);
    cout << "\n\t\t\t2. Admin" << endl;
    Sleep(150);
    cout << "\n\t\t\t3. Exit" << endl;
    Sleep(150);
    cout << "Enter Your Choice:";
    cin >> selection;

    switch (selection)
    {
    case 1:
    {
        student();
        break;
    }
    case 2:
    {
        int attemptcount = 0;
        while (attemptcount < 3)
        {
            cout << " Enter Your Username:" << endl;
            cin >> username;
            cout << " Enter Your Password: " << endl;
            cin >> Password;
            if (username != "admin" || Password != "1234")
            {
                cout << "Invalid username or password...Please try again." << "\n" << endl;
                attemptcount++;
            }
            else
            {
                cout << "Welcome Admin";
                system("cls");
                system("Color 9");
                cout << "Congratulations You Logged In!!!" << endl;
                cout << endl;
                cout << "\t\t\t\t  ===================ADMIN MENU===================" << endl << endl;
                Sleep(100);
                cout << "\n\t\t\t1. Enter Student Hostel Records" << endl;
                Sleep(100);
                cout << "\n\t\t\t2.  Display Student Information " << endl;
                Sleep(100);
                cout << "\n\t\t\t3.  Edit Information" << endl;
                Sleep(100);
                cout << "\n\t\t\t4. Delete Information" << endl;
                Sleep(100);
                cout << "\n\t\t\t5. Exit" << endl;
                Sleep(100);
                cout << "Enter Your Choice:";
                cin >> selection2;

                switch (selection2)
                {
                case 1:
                {
                    int s;
                    cout << "Enter the Number of Students Data you want to enter:";
                    cin >> s;
                    recd(&s, std, Hostel);
                    break;
                }
                case 2:
                {
                    int s;
                    cout << "Enter the Number of Students Data you want to display?:";
                    cin >> s;
                    display(&s, std, Hostel);
                    break;
                }
                case 3:
                {
                    int data;
                    cout << "How many Students Data have you entered already?";
                    cin >> data;
                    edit(&data, std, Hostel);
                    break;
                }
                case 4:
                {
                    int data1;
                    cout << "How many Students Data have you entered already?";
                    cin >> data1;
                    delet(&data1, std, Hostel);
                    break;
                }
                case 5:
                {
                    break;
                }
                default:
                {
                    cout << "Invalid Response" << endl;
                }
                }
                break;
            }
            if (attemptcount == 3)
            {
                cout << "You are not registered in the system." << endl;
            }
        }
        break;
    }
    case 3:
    {
        break;
    }
    default:
    {
        cout << "  Invalid Response" << endl;
        break;
    }
    }
}

void student()
{
    system("cls");
    system("color 6");
    cout << "\t\t\t\t  ===================STUDENT MENU===================" << endl << endl;
    Sleep(100);
    cout << "\n\t\t\t1. Hostel Rules" << endl;
    Sleep(100);
    cout << "\n\t\t\t2. Mess Section Information" << endl;
    Sleep(100);
    cout << "\n\t\t\t3. Hostel Building Information" << endl;
    Sleep(100);
    cout << "\n\t\t\t4. Hostel Duty" << endl;
    Sleep(100);
    cout << "\n\t\t\t5. Laundry" << endl;
    Sleep(100);
    cout << "\n\t\t\t6. Exit " << endl;
    Sleep(100);

    int selection1;
    cout << "Enter Your Choice:";
    cin >> selection1;

    switch (selection1)
    {
    case 1:
    {
        HostelR();
        break;
    }
    case 2:
    {
        MessI();
        break;
    }
    case 3:
    {
        bdinf();
        break;
    }
    case 4:
    {
        duty();
        break;
    }
    case 5:
    {
        int num;
        cout << "Enter room number(1-10) to access washerman info " << endl;
        cin >> num;
        laundry(&num);
        break;
    }
    case 6:
    {
        break;
    }
    default:
    {
        cout << "Invalid Response" << endl;
        break;
    }
    }
}

void HostelR()
{
    system("cls");
    system("color F");
    cout << "\t\t\t\t*******HOSTEL RULES*******" << endl;
    cout << endl;
    cout << "\t\tAny student not observing the following rules will be fined and in some cases expelled from the hostel." << "\n" << endl;
    cout << endl;
    cout << "\t\t1) Smoking, Alcohol & Narcotic consumption is strictly prohibited in and around the Hostel premises." << "\n" << endl;
    cout << endl;
    cout << "\t\t2) Strict adherence to the prescribed dress code is required. Decency in dressing and demeanor is a must." << "\n" << endl;
    cout << endl;
    cout << "\t\t3) Loitering in the Hostel campus during the class hours will not be appreciated." << "\n" << endl;
    cout << endl;
    cout << "\t\t4) The Management and Staff will not be responsible for personal belongings." << "\n" << endl;
    cout << endl;
    cout << "\t\t5) Late comers will be penalized." << "\n" << endl;
    cout << endl;
    cout << "\t\t6) Students must keep the campus and rooms clean. Defacing walls, equipment, furniture etc. is strictly prohibited." << "\n" << endl;
    cout << endl;
    cout << "\t\t7) Birthdays or other Celebrations are strictly prohibited in Hostel." << "\n" << endl;
    cout << endl;
    cout << "\t\t8) Students must turn off all the electrical equipments & lights before leaving their rooms." << "\n" << endl;
    cout << endl;
    cout << "\t\t9) Students are not allowed to use electric stoves, heaters etc in rooms except in designated places." << "\n" << endl;
    cout << endl;
    cout << "\t\t10) Students are not allowed to organize any group activities in their room." << "\n" << endl;
    cout << endl;
    cout << "\t\t11) Food will be served only in the designated mess and only during the specified timings. Wasting food and water will not be encouraged." << "\n" << endl;
    cout << endl;
    cout << "\t\t12) All lights must be switched off before 11 pm in the rooms. Only study lamps are permitted." << "\n" << endl;
    cout << endl;
    cout << "\t\t13) Students are not allowed to use mobile phones after 10 pm. Cell phones of those at fault will be confiscated." << "\n" << endl;
    cout << endl;
    cout << "\t\t14) Visitors are allowed only in AV Room between 4:30 p.m. and 6:30 p.m." << "\n" << endl;
    cout << endl;
    cout << "\t\t15) Any complaints regarding electric equipment, plumbing etc. is required to be entered in the Complaints Book." << "\n" << endl;
    cout << endl;
    cout << "\t\t16) Students should not enter rooms of other students without permission." << "\n" << endl;
    cout << endl;
    cout << "\t\t17) Strict silence shall be observed in hostel from 11.00 pm to 5.30 am." << "\n" << endl;
    cout << endl;
    cout << "\t\t18) Any manner of festivities and noise making, celebrations will not be entertained" << "\n" << endl;
    cout << endl;
    cout << "\t\t    which may cause disturbance to other inmates in the hostel premises." << "\n" << endl;
    cout << endl;
    cout << "\t\t19) Any student caught in a sexual act will be expelled immediately." << "\n" << endl;
    cout << endl;
    cout << "\t\t20) Students during their stay in the hostel will be governed by the management rules." << "\n" << endl;
    cout << endl;
    cout << "Do you want to back to main menu(Y/N)?";
    cin >> gob;
    backToMenu(&gob);
}

void bdinf()
{
    system("cls");
    system("color 9");
    cout << endl;
    cout << "\t ===================42 Mechanical B Hostel Information===================" << endl << endl;
    cout << "\n\t\t\tHostel Manager: Sir Aqib" << endl;
    cout << "\n\t\t\tVice Hostel Manager: Maam Ayesha Batool" << endl;
    cout << "\n\t\t\tTotal Number of Floors: 2" << endl;
    cout << "\n\t\t\tTotal Number of Rooms: 10 " << endl;
    cout << "\n\t\t\tRoom Type: For 3 people only" << endl;
    cout << "\n\t\t\tStudent Capacity: 30" << endl;
    cout << "\n\t\t\tStudent Programmes: For Undergraduate Boys Only" << endl;
    cout << "\n\t\t\tSports Details:" << endl;
    cout << "\n\t\t\t1.Basketball Court" << endl;
    cout << "\n\t\t\t2.Lawn" << endl;
    cout << "\n\t\t\t3.Football Ground" << endl;
    cout << "\n\t\t\tWashroom Details:" << endl;
    cout << "\n\t\t\tTotal Number of Toilets: 12 " << endl;
    cout << "\n\t\t\tNumber of Toilets (First Floor): 6" << endl;
    cout << "\n\t\t\tNumber of Toilets (Second Floor): 6" << endl;
    cout << "\n\t\t\tTotal number of sinks: 12" << endl;
    cout << "\n\t\t\tNumber of Sinks (First Floor): 6" << endl;
    cout << "\n\t\t\tNumber of Sinks (Second Floor): 6" << endl;
    cout << endl << endl;
    cout << "Do you want to back to main menu(Y/N)?";
    cin >> gob;
    backToMenu(&gob);
}

void edit(int* wanda, struct student std[], fstream& Hostel)
{
    system("cls");
    system("color B");
    Hostel.open("hostel data.txt", ios::in);
    if (Hostel.is_open())
    {
        for (int i = 0; i < *wanda; i++)
        {
            Hostel >> std[i].name;
            Hostel >> std[i].fn;
            Hostel >> std[i].phone_number;
            Hostel >> std[i].f_number;
            Hostel >> std[i].birth;
            Hostel >> std[i].address;
            Hostel >> std[i].mess_bill;
            Hostel >> std[i].paid_mess;
            Hostel >> std[i].hostel_bill;
            Hostel >> std[i].paid_hostel;
            Hostel >> std[i].pay_method;
        }
    }
    else
    {
        cout << "\n\tFile Not Found";
    }
    Hostel.close();

    int edit;
    cout << " 1 means YES and 0 means NO " << endl << endl;
    cout << "Do you want to edit Name(1/0):";
    cin >> edit;
    if (edit == 1)
    {
        int num;
        cout << "Enter roll number";
        cin >> num;
        string newname;
        cout << "Enter new word/integer:";
        cin >> newname;
        std[num - 1].name = newname;
    }
    else
    {
        cout << "Not edited" << endl;
    }

    int edit1;
    cout << "Do you want to edit Father Name(1/0):";
    cin >> edit1;
    if (edit1 == 1)
    {
        int num;
        cout << "Enter roll number";
        cin >> num;
        string newfname;
        cout << "Enter new word/integer:";
        cin >> newfname;
        std[num - 1].fn = newfname;
    }
    else
    {
        cout << "Not edited" << endl;
    }

    int edit2;
    cout << "Do you want to edit Student Phone Number(1/0):";
    cin >> edit2;
    if (edit2 == 1)
    {
        int num;
        cout << "Enter roll number";
        cin >> num;
        string newname;
        cout << "Enter new word/integer:";
        cin >> newname;
        std[num - 1].phone_number = newname;
    }
    else
    {
        cout << "Not edited" << endl;
    }

    int edit3;
    cout << "Do you want to edit Father Phone Number(1/0):";
    cin >> edit3;
    if (edit3 == 1)
    {
        int num;
        cout << "Enter roll number";
        cin >> num;
        string newname;
        cout << "Enter new word/integer:";
        cin >> newname;
        std[num - 1].f_number = newname;
    }
    else
    {
        cout << "Not edited" << endl;
    }

    int edit4;
    cout << "Do you want to edit Date of Birth(1/0):";
    cin >> edit4;
    if (edit4 == 1)
    {
        int num;
        cout << "Enter roll number";
        cin >> num;
        string newname;
        cout << "Enter new word/integer:";
        cin >> newname;
        std[num - 1].birth = newname;
    }
    else
    {
        cout << "Not edited" << endl;
    }

    int edit5;
    cout << "Do you want to edit Address(1/0):";
    cin >> edit5;
    if (edit5 == 1)
    {
        int num;
        cout << "Enter roll number";
        cin >> num;
        string newname;
        cout << "Enter new word/integer:";
        cin >> newname;
        std[num - 1].address = newname;
    }
    else
    {
        cout << "Not edited" << endl;
    }

    int edit6;
    cout << "Do you want to edit Total Mess Bill(1/0):";
    cin >> edit6;
    if (edit6 == 1)
    {
        int num;
        cout << "Enter roll number";
        cin >> num;
        string newname;
        cout << "Enter new word/integer:";
        cin >> newname;
        std[num - 1].mess_bill = newname;
    }
    else
    {
        cout << "Not edited" << endl;
    }

    int edit8;
    cout << "Do you want to edit Paid Mess Bill(1/0):";
    cin >> edit8;
    if (edit8 == 1)
    {
        int num;
        cout << "Enter roll number";
        cin >> num;
        string newname;
        cout << "Enter new word/integer:";
        cin >> newname;
        std[num - 1].paid_mess = newname;
    }
    else
    {
        cout << "Not edited" << endl;
    }

    int edit9;
    cout << "Do you want to edit Total Hostel Bill(1/0):";
    cin >> edit9;
    if (edit9 == 1)
    {
        int num;
        cout << "Enter roll number";
        cin >> num;
        string newname;
        cout << "Enter new word/integer:";
        cin >> newname;
        std[num - 1].hostel_bill = newname;
    }
    else
    {
        cout << "Not edited" << endl;
    }

    int edit10;
    cout << "Do you want to edit Paid Hostel Bill(1/0):";
    cin >> edit10;
    if (edit10 == 1)
    {
        int num;
        cout << "Enter roll number";
        cin >> num;
        string newname;
        cout << "Enter new word/integer:";
        cin >> newname;
        std[num - 1].paid_hostel = newname;
    }
    else
    {
        cout << "Not edited" << endl;
    }

    int edit11;
    cout << "Do you want to edit Payment Method (1/0):";
    cin >> edit11;
    if (edit11 == 1)
    {
        int num;
        cout << "Enter roll number";
        cin >> num;
        string newname;
        cout << "Enter new word/integer:";
        cin >> newname;
        std[num - 1].pay_method = newname;
    }
    else
    {
        cout << "Not edited" << endl;
    }

    Hostel.open("hostel data.txt", ios::out);
    if (Hostel.is_open())
    {
        for (int i = 0; i < *wanda; i++)
        {
            Hostel << std[i].name << endl;
            Hostel << std[i].fn << endl;
            Hostel << std[i].phone_number << endl;
            Hostel << std[i].f_number << endl;
            Hostel << std[i].birth << endl;
            Hostel << std[i].address << endl;
            Hostel << std[i].mess_bill << endl;
            Hostel << std[i].paid_mess << endl;
            Hostel << std[i].hostel_bill << endl;
            Hostel << std[i].paid_hostel << endl;
            Hostel << std[i].pay_method << endl;
        }
    }
    else
    {
        cout << "\n\tFile Not Found";
    }
    Hostel.close();

    cout << "Do you want to back to main menu(Y/N)?";
    cin >> gob;
    backToMenu(&gob);
}

void duty()
{
    system("cls");
    int duty, week;
    cout << "\t\t\t\t\t\t1.MONDAY" << endl;
    cout << "\t\t\t\t\t\t2.TUESDAY" << endl;
    cout << "\t\t\t\t\t\t3.WEDNESDAY" << endl;
    cout << "\t\t\t\t\t\t4.THURSDAY" << endl;
    cout << "\t\t\t\t\t\t5.FRIDAY" << endl;
    cout << "\t\t\t\t\t\t6.SATURDAY" << endl;
    cout << "\t\t\t\t\t\t7.SUNDAY" << endl;

AYESHA:
    cout << "Enter the day of week(1-7):" << endl;
    cin >> week;
    switch (week)
    {
    case 1:
        cout << "1.Day Duty" << endl;
        cout << "2.Night Duty" << endl;
        cout << "Enter 1 or 2 to check Hostel Duty" << endl;
        cin >> duty;
        switch (duty)
        {
        case 1: cout << "HOSTEL DUTY=WASIM" << endl; break;
        case 2: cout << "HOSTEL DUTY=MUSTAFA" << endl; break;
        default: cout << "INVALID NUMBER ENTERED" << endl; break;
        }
        break;
    case 2:
        cout << "1.Day Duty" << endl;
        cout << "2.Night Duty" << endl;
        cout << "Enter 1 or 2 to check Hostel Duty" << endl;
        cin >> duty;
        switch (duty)
        {
        case 1: cout << "HOSTEL DUTY=IBRAHIM" << endl; break;
        case 2: cout << "HOSTEL DUTY=MUSA" << endl; break;
        default: cout << "INVALID NUMBER ENTERED" << endl; break;
        }
        break;
    case 3:
        cout << "1.Day Duty" << endl;
        cout << "2.Night Duty" << endl;
        cout << "Enter 1 or 2 to check Hostel Duty" << endl;
        cin >> duty;
        switch (duty)
        {
        case 1: cout << "HOSTEL DUTY=IRFAN" << endl; break;
        case 2: cout << "HOSTEL DUTY=FAISAL" << endl; break;
        default: cout << "INVALID NUMBER ENTERED" << endl; break;
        }
        break;
    case 4:
        cout << "1.Day Duty" << endl;
        cout << "2.Night Duty" << endl;
        cout << "Enter 1 or 2 to check Hostel Duty" << endl;
        cin >> duty;
        switch (duty)
        {
        case 1: cout << "HOSTEL DUTY=HASSAN" << endl; break;
        case 2: cout << "HOSTEL DUTY=ADIL" << endl; break;
        default: cout << "INVALID NUMBER ENTERED" << endl; break;
        }
        break;
    case 5:
        cout << "1.Day Duty" << endl;
        cout << "2.Night Duty" << endl;
        cout << "Enter 1 or 2 to check Hostel Duty" << endl;
        cin >> duty;
        switch (duty)
        {
        case 1: cout << "HOSTEL DUTY=KASHIF" << endl; break;
        case 2: cout << "HOSTEL DUTY=ABUBAKAR" << endl; break;
        default: cout << "INVALID NUMBER ENTERED" << endl; break;
        }
        break;
    case 6:
        cout << "1.Day Duty" << endl;
        cout << "2.Night Duty" << endl;
        cout << "Enter 1 or 2 to check Hostel Duty" << endl;
        cin >> duty;
        switch (duty)
        {
        case 1: cout << "HOSTEL DUTY=ARSLAN" << endl; break;
        case 2: cout << "HOSTEL DUTY=AHAD" << endl; break;
        default: cout << "INVALID NUMBER ENTERED" << endl; break;
        }
        break;
    case 7:
        cout << "1.Day Duty" << endl;
        cout << "2.Night Duty" << endl;
        cout << "Enter 1 or 2 to check Hostel Duty" << endl;
        cin >> duty;
        switch (duty)
        {
        case 1: cout << "HOSTEL DUTY=IMRAN" << endl; break;
        case 2: cout << "HOSTEL DUTY=MEHMOOD" << endl; break;
        default: cout << "INVALID NUMBER ENTERED" << endl; break;
        }
        break;
    }

    char yesno;
    cout << "If you want to check Hostel Duty again press Y" << endl;
    cin >> yesno;
    if (yesno == 'Y' || yesno == 'y')
    {
        goto AYESHA;
    }
    else
    {
        cout << "If you want to go back to main menu press Y" << endl;
        cin >> gob;
        backToMenu(&gob);
    }
}

void recd(int* wanda, struct student std[], fstream& Hostel)
{
    system("cls");
    system("color 8");
    int i;
    cout << endl << endl;
    cout << "\t\t\t\t  -------Welcome to ME-B Boys Hostel-------" << endl;
    cout << endl;
    cout << "\t\t\t\t      -------Entering Data Form-------" << endl;
    cout << endl;
    Hostel.open("hostel data.txt", ios::out);
    if (Hostel.is_open())
    {
        for (i = 0; i < *wanda; i++)
        {
            cout << "Roll Number: " << i + 1 << endl;
            cout << "Enter Name:";
            cin >> std[i].name;
            Hostel << std[i].name << " " << endl;
            cout << "Enter your Father's/Guardian's name:";
            cin >> std[i].fn;
            Hostel << std[i].fn << " " << endl;
            cout << "Enter phone number(without spaces):";
            cin >> std[i].phone_number;
            Hostel << std[i].phone_number << " " << endl;
            cout << "Enter your Father/Guardian's phone number(without spaces):";
            cin >> std[i].f_number;
            Hostel << std[i].f_number << " " << endl;
            cout << "Date of Birth(DD/MM/YYYY):";
            cin >> std[i].birth;
            Hostel << std[i].birth << " " << endl;
            cout << "Address:";
            cin >> std[i].address;
            Hostel << std[i].address << " " << endl;
            cout << "Enter the total mess bill: ";
            cin >> std[i].mess_bill;
            Hostel << std[i].mess_bill << " " << endl;
            cout << "Enter paid mess bill: ";
            cin >> std[i].paid_mess;
            Hostel << std[i].paid_mess << " " << endl;
            cout << "Enter total hostel bill: ";
            cin >> std[i].hostel_bill;
            Hostel << std[i].hostel_bill << " " << endl;
            cout << "Enter paid hostel bill: ";
            cin >> std[i].paid_hostel;
            Hostel << std[i].paid_hostel << " " << endl;
            cout << "Enter payment method: ";
            cin >> std[i].pay_method;
            Hostel << std[i].pay_method << " " << endl;
            cout << endl;
        }
        Hostel.close();
    }
    else
    {
        cout << "\n\tFile Not Found";
    }
    cout << "Do you want to back to main menu(Y/N)?";
    cin >> gob;
    backToMenu(&gob);
}

void delet(int* wanda, struct student std[], fstream& Hostel)
{
    system("cls");
    system("color C");
    Hostel.open("hostel data.txt", ios::in);
    for (int vw = 0; vw < *wanda; vw++)
    {
        Hostel >> std[vw].name;
        Hostel >> std[vw].fn;
        Hostel >> std[vw].phone_number;
        Hostel >> std[vw].f_number;
        Hostel >> std[vw].birth;
        Hostel >> std[vw].address;
        Hostel >> std[vw].mess_bill;
        Hostel >> std[vw].paid_mess;
        Hostel >> std[vw].hostel_bill;
        Hostel >> std[vw].paid_hostel;
        Hostel >> std[vw].pay_method;
    }
    Hostel.close();

    int del;
    cout << "Do you want to Delete All the Student's Data(1/0):";
    cin >> del;
    if (del == 1)
    {
        int num;
        cout << "Enter Roll Number Of Student:";
        cin >> num;
        string newname;
        std[num - 1].name = newname;
        std[num - 1].fn = newname;
        std[num - 1].phone_number = newname;
        std[num - 1].f_number = newname;
        std[num - 1].birth = newname;
        std[num - 1].address = newname;
        std[num - 1].mess_bill = newname;
        std[num - 1].paid_mess = newname;
        std[num - 1].hostel_bill = newname;
        std[num - 1].paid_hostel = newname;
        std[num - 1].pay_method = newname;
    }
    else
    {
        cout << "Not deleted" << endl;
    }

    Hostel.open("hostel data.txt", ios::out);
    for (int vw = 0; vw < *wanda; vw++)
    {
        Hostel << std[vw].name << endl;
        Hostel << std[vw].fn << endl;
        Hostel << std[vw].phone_number << endl;
        Hostel << std[vw].f_number << endl;
        Hostel << std[vw].birth << endl;
        Hostel << std[vw].address << endl;
        Hostel << std[vw].mess_bill << endl;
        Hostel << std[vw].paid_mess << endl;
        Hostel << std[vw].hostel_bill << endl;
        Hostel << std[vw].paid_hostel << endl;
        Hostel << std[vw].pay_method << endl;
    }
    Hostel.close();

    cout << endl;
    cout << "Do you want to back to main menu(Y/N)?";
    cin >> gob;
    backToMenu(&gob);
}

void MessI()
{
stark:
    system("cls");
    system("color E");
    int Mi;
    cout << endl;
    cout << "\t\t\t\t\t---------- MESS INFORMATION ----------" << endl;
    cout << endl;
    cout << "\t\t\t\t\t\t1.Dining Rules " << endl;
    cout << endl;
    cout << "\t\t\t\t\t\t2.Dining Menu " << endl;
    cout << endl;
    cout << " \t\t\t\t\t\t3.Mess Timings " << endl;
    cout << endl;
    cout << " \t\t\t\tChoose An Option: ";
    cin >> Mi;

    switch (Mi)
    {
    case 1:
    {
        system("cls");
        cout << "\t\t\t\t\t ---------- Dining rules ---------- " << endl;
        cout << endl;
        cout << " 1. Please arrive at the mess at the time mentioned for breakfast,lunch and dinner. You will not be entertained at " << endl;
        cout << endl;
        cout << " any other time. " << endl;
        cout << endl;
        cout << " 2. Proper clothing is must at mess area. The person wearing inappropriate clothes will be asked to leave. " << endl;
        cout << endl;
        cout << " 3. No weapons are allowed in the mess area. Violation of this will cause the cancellation of the hostel room. " << endl;
        cout << endl;
        cout << " 4. No fights,use of bad language or name calling will not be tolerated in the mess area. " << endl;
        cout << endl;
        cout << " 5. Food is a blessing of Allah so don't waste your food and finish what you take. " << endl;
        cout << endl;
        cout << " 6. Keep the mess area clean furthermore no food fights are allowed. " << endl;
        cout << endl;
        cout << " 7. Violation of above mentioned rules could result in expulsion or cancellation of hostel room or even suspension " << endl;
        char tony;
        cout << endl;
        cout << " Do you want to go back to mess section(Y/N) " << endl;
        cin >> tony;
        if (tony == 'Y' || tony == 'y')
        {
            goto stark;
        }
        cout << "Do you want to back to main menu(Y/N)?";
        cin >> gob;
        backToMenu(&gob);
        break;
    }
    case 2:
    {
        system("cls");
        int mn;
        cout << "\t\t\t\t\t ---------- Mess Menu ---------- " << endl;
        cout << endl;

    Khaana:
        cout << endl;
        cout << " Enter the number of month of semester(1-6): ";
        cin >> mn;

        switch (mn)
        {
        case 1:
        {
            int md1;
            cout << " Which day you want to check the menu of in month 1(1-7) " << endl;
            cin >> md1;
            switch (md1)
            {
            case 1:
                cout << " Monday " << endl;
                cout << " BreakFast: Aanda-Paratha-Tea " << endl;
                cout << " Lunch: Daal Maash-Roti-Achaar" << endl;
                cout << " Dinner: Beef Pulao-Raita-Gajar Ka Halwa" << endl;
                break;
            case 2:
                cout << " Tuesday " << endl;
                cout << " BreakFast: Black Beans-Paratha-Tea" << endl;
                cout << " Lunch: Daal Masoor-Boiled Rice-Salad-Fruit" << endl;
                cout << " Dinner: Chiken Roast-Slice-Chips-Ketchup" << endl;
                break;
            case 3:
                cout << " Wednesday " << endl;
                cout << " BreakFast: Aalo ki bhujiya-Paratha-Tea" << endl;
                cout << " Lunch: Fish Pulao-Seekh Kabab" << endl;
                cout << " Dinner: Eggplant-Roti" << endl;
                break;
            case 4:
                cout << " Thursday " << endl;
                cout << " BreakFast: Aalo Anda-Paratha-Tea" << endl;
                cout << " Lunch: Vegetable-Roti-Fruit" << endl;
                cout << " Dinner: Chicken Manchorian-Egg Fried Rice-Soup " << endl;
                break;
            case 5:
                cout << " Friday " << endl;
                cout << " BreakFast: Slice-Jam-Egg-Tea" << endl;
                cout << " Lunch: Kari Pakora-Roti" << endl;
                cout << " Dinner: Chiken Biryani-Raita-Soup" << endl;
                break;
            case 6:
                cout << " Saturday " << endl;
                cout << " BreakFast: Aalo Paratha-Tea" << endl;
                cout << " Lunch: Red Beans-Boiled Rice-Salad " << endl;
                cout << " Dinner: Meatballs-Roti-Soup" << endl;
                break;
            case 7:
                cout << " Sunday " << endl;
                cout << " Brunch: Aalo Bhujiya-Channe-Naan-Halwa Poori-Nihari-Tea" << endl;
                cout << " Dinner: Chana Pulao-Shami Kabab-Raita " << endl;
                break;
            }
            char Kh1;
            cout << " Do you want to check the menu of another day(Y/N): ";
            cin >> Kh1;
            if (Kh1 == 'y' || Kh1 == 'Y')
            {
                goto Khaana;
            }
            break;
        }
        case 2:
        {
            int md2;
            cout << " Which day you want to check the menu of in month 2(1-7) " << endl;
            cin >> md2;
            switch (md2)
            {
            case 1:
                cout << " Monday " << endl;
                cout << " BreakFast: Slice-Omellate-Tea" << endl;
                cout << " Lunch: Red Beans-Boiled Rice-Salad" << endl;
                cout << " Dinner: Meatballs-Roti-Soup" << endl;
                break;
            case 2:
                cout << " Tuesday " << endl;
                cout << " BreakFast: Aanda-Paratha-Tea" << endl;
                cout << " Lunch: Kari Pakora-Roti" << endl;
                cout << " Dinner: Beef Pulao-Raita-Gajar Ka Halwa" << endl;
                break;
            case 3:
                cout << " Wednesday " << endl;
                cout << " BreakFast: Black Beans-Paratha-Tea" << endl;
                cout << " Lunch: Vegetable-Roti-Fruit " << endl;
                cout << " Dinner: Chiken Roast-Slice-Chips-Ketchup" << endl;
                break;
            case 4:
                cout << " Thursday " << endl;
                cout << " BreakFast: Aalo ki bhujiya-Paratha-Tea" << endl;
                cout << " Lunch: Aalo ki bhujiya-roti" << endl;
                cout << " Dinner: Eggplant-Roti" << endl;
                break;
            case 5:
                cout << " Friday " << endl;
                cout << " BreakFast: Aalo Anda-Paratha-Tea" << endl;
                cout << " Lunch: Daal Masoor-Boiled Rice-Salad-Fruit" << endl;
                cout << " Dinner: Chicken Manchorian-Egg Fried Rice-Soup" << endl;
                break;
            case 6:
                cout << " Saturday " << endl;
                cout << " BreakFast: Slice-Jam-Egg-Tea" << endl;
                cout << " Lunch: Daal Maash-Roti-Achaar" << endl;
                cout << " Dinner: Chiken Biryani-Raita-Soup" << endl;
                break;
            case 7:
                cout << " Sunday " << endl;
                cout << " Brunch: Aalo Bhujiya-Channe-Naan-Halwa Poori-Nihari-Tea" << endl;
                cout << " Dinner: Chana Pulao-Shami Kabab-Raita" << endl;
                break;
            }
            char Kh2;
            cout << " Do you want to check the menu of another day(Y/N): ";
            cin >> Kh2;
            if (Kh2 == 'y' || Kh2 == 'Y')
            {
                goto Khaana;
            }
            break;
        }
        case 3:
        {
            int md3;
            cout << " Which day you want to check the menu of in month 3(1-7) " << endl;
            cin >> md3;
            switch (md3)
            {
            case 1:
                cout << " Monday " << endl;
                cout << " BreakFast: Slice-Jam-Egg-Tea" << endl;
                cout << " Lunch: Daal Masoor-Boiled Rice-Salad-Fruit" << endl;
                cout << " Dinner: Chiken Biryani-Raita-Soup" << endl;
                break;
            case 2:
                cout << " Tuesday " << endl;
                cout << " BreakFast: Naan-Chaane-Tea" << endl;
                cout << " Lunch: Red Beans-Boiled Rice-Salad" << endl;
                cout << " Dinner: Meatballs-Roti-Soup" << endl;
                break;
            case 3:
                cout << " Wednesday " << endl;
                cout << " BreakFast: Aanda-Paratha-Tea" << endl;
                cout << " Lunch: Kari Pakora-Roti" << endl;
                cout << " Dinner: Beef Pulao-Raita-Gajar Ka Halwa" << endl;
                break;
            case 4:
                cout << " Thursday " << endl;
                cout << " BreakFast: Black Beans-Paratha-Tea" << endl;
                cout << " Lunch: Vegetable-Roti-Fruit " << endl;
                cout << " Dinner: Chiken Roast-Slice-Chips-Ketchup" << endl;
                break;
            case 5:
                cout << " Friday " << endl;
                cout << " BreakFast: Aalo ki bhujiya-Paratha-Tea" << endl;
                cout << " Lunch: Aalo ki bhujiya-Roti" << endl;
                cout << " Brunch: Aalo Bhujiya-Channe-Naan-Halwa Poori-Nihari-Tea" << endl;
                cout << " Dinner: Chana Pulao-Shami Kabab-Raita" << endl;
                break;
            }
            char Kh6;
            cout << " Do you want to check the menu of another day(Y/N): ";
            cin >> Kh6;
            if (Kh6 == 'y' || Kh6 == 'Y')
            {
                goto Khaana;
            }
            break;
        }
        }
        char black;
        cout << " Do you want to go to mess section(Y/N) " << endl;
        cin >> black;
        if (black == 'Y' || black == 'y')
        {
            goto stark;
        }
        cout << "Do you want to back to main menu(Y/N)";
        cin >> gob;
        backToMenu(&gob);
        break;
    }
    case 3:
    {
        cout << " The timings from Monday to Sunday are: " << endl;
        cout << " Breakfast: 6:30 am to 7:30 am" << endl;
        cout << " Lunch: 1:00 pm to 3:00 pm " << endl;
        cout << " Dinner: 7:00 pm to 9:00 pm " << endl;
        cout << endl;
        char thor;
        cout << " Do you want to go mess section(Y/N) " << endl;
        cin >> thor;
        if (thor == 'Y' || thor == 'y')
        {
            goto stark;
        }
        cout << "Do you want to go back to main menu(Y/N)" << endl;
        cin >> gob;
        backToMenu(&gob);
        break;
    }
    default:
    {
        cout << " Invalid Option " << endl;
        break;
    }
    }
}

void laundry(int* vision)
{
    system("cls");
    system("color A");
    switch (*vision)
    {
    case 1: cout << "WASHERMAN ALI" << endl; cout << "05104959834" << endl; break;
    case 2: cout << "WASHERMAN UMER" << endl; cout << "03337467826" << endl; break;
    case 3: cout << "WASHERMAN USMAN" << endl; cout << "05128273981" << endl; break;
    case 4: cout << "WASHERMAN USAMA" << endl; cout << "05187608893" << endl; break;
    case 5: cout << "WASHERMAN WASEEM" << endl; cout << "05172318739" << endl; break;
    case 6: cout << "WASHERMAN HASAN" << endl; cout << "05193189893" << endl; break;
    case 7: cout << "WASHERMAN HUSSAIN" << endl; cout << "03337665453" << endl; break;
    case 8: cout << "WASHERMAN IBRAHIM" << endl; cout << "03336342342" << endl; break;
    case 9: cout << "WASHERMAN MUSTAFA" << endl; cout << "05118787992" << endl; break;
    case 10: cout << "WASHERMAN AHMAD" << endl; cout << "03336832917" << endl; break;
    default: cout << "Invalid Input" << endl;
    }
    cout << "Do you want to back to main menu(Y/N)?";
    cin >> gob;
    backToMenu(&gob);
}

// RENAMED from exit(char*) -- the original name collided with the standard
// library's exit(int) function, which was silently terminating the whole
// program every time one of the exit(0) calls ran anywhere in the file.
void backToMenu(char* yn)
{
    if (*yn == 'y' || *yn == 'Y')
    {
        system("cls");
        mainmenu();
    }
}

void display(int* gg, struct student std[], fstream& Hostel)
{
    Hostel.open("hostel data.txt", ios::in);
    for (int wv = 0; wv < *gg; wv++)
    {
        Hostel >> std[wv].name;
        Hostel >> std[wv].fn;
        Hostel >> std[wv].phone_number;
        Hostel >> std[wv].f_number;
        Hostel >> std[wv].birth;
        Hostel >> std[wv].address;
        Hostel >> std[wv].mess_bill;
        Hostel >> std[wv].paid_mess;
        Hostel >> std[wv].hostel_bill;
        Hostel >> std[wv].paid_hostel;
        Hostel >> std[wv].pay_method;
    }
    Hostel.close();

    for (int wv = 0; wv < *gg; wv++)
    {
        cout << "\n\tRoll Number " << wv + 1 << endl;
        cout << "\n\t Name: " << std[wv].name;
        cout << "\n\t Father Name: " << std[wv].fn;
        cout << "\n\t Student Phone Number: " << std[wv].phone_number;
        cout << "\n\t Father Phone Number: " << std[wv].f_number;
        cout << "\n\t Date of Birth: " << std[wv].birth;
        cout << "\n\t Address: " << std[wv].address;
        cout << "\n\t Total Mess Bill: " << std[wv].mess_bill;
        cout << "\n\t Paid Mess Bill: " << std[wv].paid_mess;
        cout << "\n\t Total Hostel Bill: " << std[wv].hostel_bill;
        cout << "\n\t Paid Hostel Bill: " << std[wv].paid_hostel;
        cout << "\n\t Method of the Payment: " << std[wv].pay_method << endl;
    }
    cout << "Do you want to back to main menu(Y/N)?";
    cin >> gob;
    backToMenu(&gob);
}
