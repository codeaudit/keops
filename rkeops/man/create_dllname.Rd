% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/utils.R
\name{create_dllname}
\alias{create_dllname}
\title{Create name of shared library from formula and arguments}
\usage{
create_dllname(formula, args)
}
\arguments{
\item{formula}{text string}

\item{args}{vector of text string}
}
\value{
dll name (text string)
}
\description{
Using input formula and arguments along with current value of \code{"precision"}
option, the function \code{dllname} creates a hashed name for the shared
library where the operators defined by the formula and arguments will be
compiled.
}
\details{
When compiling a user-defined operators, a shared object (so) library
(or dynamic link library, dll) file is created in the directory \code{build_dir}
specified in compile options of \code{rkeops}. For every new operators, such a
file is created.

The shared library file associated to a user-defined operator has a unique
name so that it can be reused without compilation when calling again the
associated operator.
}
\author{
Ghislain Durif
}
\keyword{internal}
