#pragma once

#ifdef _WIN32
  #define qt5Example_EXPORT __declspec(dllexport)
#else
  #define qt5Example_EXPORT
#endif

qt5Example_EXPORT void qt5Example();
