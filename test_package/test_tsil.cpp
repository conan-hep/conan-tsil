#include <iostream>
#include <typeinfo>
#include "tsil_cpp.h"

int main()
{
   TSIL_DATA data;
   TSIL_REAL x = 1.0, y = 2.0, z = 3.0, u = 4.0, v = 5.0, s = 6.0, qq = 7.0;

   TSIL_SetParameters_(&data, x, y, z, u, v, qq);
   TSIL_Evaluate_(&data, s);

   const TSIL_COMPLEXCPP M     = TSIL_GetFunction_(&data, "M");
   const TSIL_COMPLEXCPP Uzxyv = TSIL_GetFunction_(&data, "Uzxyv");
   const TSIL_COMPLEXCPP Uuyxv = TSIL_GetFunction_(&data, "Uuyxv");
   const TSIL_COMPLEXCPP Uxzuv = TSIL_GetFunction_(&data, "Uxzuv");
   const TSIL_COMPLEXCPP Uyuzv = TSIL_GetFunction_(&data, "Uyuzv");
   const TSIL_COMPLEXCPP Tvyz  = TSIL_GetFunction_(&data, "Tvyz");
   const TSIL_COMPLEXCPP Tuxv  = TSIL_GetFunction_(&data, "Tuxv");
   const TSIL_COMPLEXCPP Tyzv  = TSIL_GetFunction_(&data, "Tyzv");
   const TSIL_COMPLEXCPP Txuv  = TSIL_GetFunction_(&data, "Txuv");
   const TSIL_COMPLEXCPP Tzyv  = TSIL_GetFunction_(&data, "Tzyv");
   const TSIL_COMPLEXCPP Tvxu  = TSIL_GetFunction_(&data, "Tvxu");
   const TSIL_COMPLEXCPP Svyz  = TSIL_GetFunction_(&data, "Svyz");
   const TSIL_COMPLEXCPP Suxv  = TSIL_GetFunction_(&data, "Suxv");

   std::cout << "=========\n"
             << "TSIL " TSIL_VERSION << '\n'
             << "=========\n"
             << "TSIL_REAL = " << typeid(TSIL_REAL).name() << '\n'
             << "TSIL_COMPLEXCPP = " << typeid(TSIL_COMPLEX).name() << '\n';

   std::cout << "M     = " << M << '\n'
             << "Uzxyv = " << Uzxyv << '\n'
             << "Uuyxv = " << Uuyxv << '\n'
             << "Uxzuv = " << Uxzuv << '\n'
             << "Uyuzv = " << Uyuzv << '\n'
             << "Tvyz  = " << Tvyz << '\n'
             << "Tuxv  = " << Tuxv << '\n'
             << "Tyzv  = " << Tyzv << '\n'
             << "Txuv  = " << Txuv << '\n'
             << "Tzyv  = " << Tzyv << '\n'
             << "Tvxu  = " << Tvxu << '\n'
             << "Svyz  = " << Svyz << '\n'
             << "Suxv  = " << Suxv << std::endl;

   return 0;
}
