#include <iostream>
int main()
{
    std::cout << "Enter two numbers:" << std::endl;
    int q1,q2,w=1;
    std::cin >> q1 >> q2;
    while (q1<q2)
    {
        if (w<=10)
        {
            std::cout << q1 <<" ";
            ++w;
            ++q1;
        }
        else
        {
            std::cout << std::endl;
            w = 1;
        }
    }
    while (q2<=q1)
    {
        if (w <= 10)
        {
            std::cout << q2 << " ";
            ++w;
            ++q2;
        }
        else
        {
            std::cout << std::endl;
            w = 1;
        }
    }
    return 0;
}