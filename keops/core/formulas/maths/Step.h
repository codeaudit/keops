#pragma once

#include <sstream>

#include "core/autodiff/UnaryOp.h"
#include "core/formulas/constants/Zero.h"

#include "core/pre_headers.h"

namespace keops {

//////////////////////////////////////////////////////////////
////             STEP : Step< F >                         ////
//////////////////////////////////////////////////////////////

template < class F >
struct Step : UnaryOp< Step, F > {
  static const int DIM = F::DIM;

  static void PrintIdString(::std::stringstream &str) {
    str << "Step";
  }

  static DEVICE INLINE void Operation(__TYPE__ *out, __TYPE__ *outF) {
#if USE_HALF && GPU_ON
#pragma unroll
    for (int k = 0; k < DIM; k++)
      if hlt2(outF[k],0)
        out[k] = 0.0;
      else
        out[k] = 1.0;
#elif USE_HALF
#pragma unroll
    for (int k = 0; k < DIM; k++)
      if (outF[k] < (half)0)
        out[k] = 0.0;
      else
        out[k] = 1.0;
#else
#pragma unroll
    for (int k = 0; k < DIM; k++)
      if (outF[k] < 0)
        out[k] = 0.0;
      else
        out[k] = 1.0;
#endif
  }
  template < class V, class GRADIN >
  using DiffT = Zero< V::DIM >;
};

#define Step(f) KeopsNS<Step<decltype(InvKeopsNS(f))>>()

}
