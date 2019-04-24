#include <iostream>
#include "tsil_cpp.h"

int main()
{
   TSIL_DATA data;
   TSIL_REAL x = 1.0, y = 2.0, z = 3.0, u = 4.0, v = 5.0, s = 6.0, qq = 7.0;

   TSIL_SetParameters_(&data, x, y, z, u, v, qq);
   TSIL_Evaluate_(&data, s);

   const auto M     = TSIL_GetFunction (&data, "M");
   const auto Uzxyv = TSIL_GetFunction (&data, "Uzxyv");
   const auto Uuyxv = TSIL_GetFunction (&data, "Uuyxv");
   const auto Uxzuv = TSIL_GetFunction (&data, "Uxzuv");
   const auto Uyuzv = TSIL_GetFunction (&data, "Uyuzv");
   const auto Tvyz  = TSIL_GetFunction (&data, "Tvyz");
   const auto Tuxv  = TSIL_GetFunction (&data, "Tuxv");
   const auto Tyzv  = TSIL_GetFunction (&data, "Tyzv");
   const auto Txuv  = TSIL_GetFunction (&data, "Txuv");
   const auto Tzyv  = TSIL_GetFunction (&data, "Tzyv");
   const auto Tvxu  = TSIL_GetFunction (&data, "Tvxu");
   const auto Svyz  = TSIL_GetFunction (&data, "Svyz");
   const auto Suxv  = TSIL_GetFunction (&data, "Suxv");

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
