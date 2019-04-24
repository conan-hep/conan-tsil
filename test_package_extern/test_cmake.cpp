#include <iostream>
#include "tsil_cpp.h"

int main()
{
   TSIL_DATA data;
   TSIL_REAL x = 1.0, y = 2.0, z = 3.0, u = 4.0, v = 5.0, s = 6.0, qq = 7.0;

   TSIL_SetParameters_(&data, x, y, z, u, v, qq);
   TSIL_Evaluate_(&data, s);

   const auto M     = TSIL_GetFunction_(&data, "M");
   const auto Uzxyv = TSIL_GetFunction_(&data, "Uzxyv");
   const auto Uuyxv = TSIL_GetFunction_(&data, "Uuyxv");
   const auto Uxzuv = TSIL_GetFunction_(&data, "Uxzuv");
   const auto Uyuzv = TSIL_GetFunction_(&data, "Uyuzv");
   const auto Tvyz  = TSIL_GetFunction_(&data, "Tvyz");
   const auto Tuxv  = TSIL_GetFunction_(&data, "Tuxv");
   const auto Tyzv  = TSIL_GetFunction_(&data, "Tyzv");
   const auto Txuv  = TSIL_GetFunction_(&data, "Txuv");
   const auto Tzyv  = TSIL_GetFunction_(&data, "Tzyv");
   const auto Tvxu  = TSIL_GetFunction_(&data, "Tvxu");
   const auto Svyz  = TSIL_GetFunction_(&data, "Svyz");
   const auto Suxv  = TSIL_GetFunction_(&data, "Suxv");

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
