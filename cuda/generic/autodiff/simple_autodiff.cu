
// nvcc -std=c++11 -Xcompiler -fPIC -shared -o simple_autodiff.so simple_autodiff.cu


#include "GpuConv2D.cu"
#include "autodiff.h"

// define variables
using X = Var<0,3>; 	// X is the first variable and represents a 3D vector
using Y = Var<1,3>; 	// Y is the second variable and represents a 3D vector
using U = Var<2,4>; 	// U is the third variable and represents a 4D vector
using V = Var<3,4>; 	// V is the fourth variable and represents a 4D vector
using Beta = Var<4,3>;	// Beta is the fifth variable and represents a 3D vector
using C = Param<0>;		// C is the first extra parameter

// define F = <U,V>^2 * exp(-C*|X-Y|^2) * Beta in usual notations
using F = Scal<Square<Scalprod<U,V>>,GaussKernel<C,X,Y,Beta>>;

// define which variables are indexed by i and which are indexed by j 
using FVARSI = univpack<X,U>;
using FVARSJ = univpack<Y,V,Beta>;
const int FDIMPARAM = 1;

using FUNCONVF = typename Generic<F,FVARSI,FVARSJ,FDIMPARAM>::sEval;

extern "C" int FConv(float ooSigma2, float* x, float* y, float* u, float* v, float* beta, float* gamma, int nx, int ny) 
{
	float params[1];
	params[0] = ooSigma2;
	return GpuConv2D(FUNCONVF(), params, nx, ny, gamma, x, y, u, v, beta); 
}


// now define the gradient wrt X
using Eta = Var<5,F::DIM>;	// new variable is in sixth position and is input of gradient
using G = Grad<F,X,Eta>;
using GVARSI = univpack<Eta,X,U>;
using GVARSJ = univpack<Y,V,Beta>;
const int GDIMPARAM = 1;

using FUNCONVG = typename Generic<G,GVARSI,GVARSJ,GDIMPARAM>::sEval;

extern "C" int GConv(float ooSigma2, float* x, float* y, float* u, float* v, float* beta, float* eta, float* gamma, int nx, int ny) 
{
	float params[1];
	params[0] = ooSigma2;
	return GpuConv2D(FUNCONVG(), params, nx, ny, gamma, x, y, u, v, beta, eta); 
}



