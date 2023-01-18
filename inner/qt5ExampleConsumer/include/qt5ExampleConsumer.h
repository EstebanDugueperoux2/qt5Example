#pragma once

#ifdef _WIN32
  #define qt5ExampleConsumer_EXPORT __declspec(dllexport)
#else
  #define qt5ExampleConsumer_EXPORT
#endif

qt5ExampleConsumer_EXPORT void qt5ExampleConsumer();
