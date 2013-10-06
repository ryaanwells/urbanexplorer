% =============================================================================
% l3proj.cls
%
% Template for level 3 projects in the Department of Computing Science at the
% University of Glasgow. Please contact Colin Perkins <csp@dcs.gla.ac.uk> with 
% any questions, comments, or corrections.
%
% =============================================================================
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{l3proj}[%
2009/01/09 Colin Perkins <csp@dcs.gla.ac.uk>.%
2009/09/16 Modified by Tim Storer <tws@dcs.gla.ac.uk> to support non pdf modes.%
2010/03/20 Hacked by Carly O'Neil for Level 4 Project
]
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}
\ProcessOptions
\LoadClass[11pt,a4paper]{report}

\usepackage{ifpdf}
\ifpdf
\usepackage[pdftex]{graphicx}
\else
\usepackage{graphicx}
\fi
\usepackage{times}
\setlength{\parindent}{0pt}
\setlength{\parskip}{11pt plus 2pt}
\addtolength\textwidth{1.0in}
\addtolength\oddsidemargin{-0.50in}
\addtolength\textheight{1.0in}
\addtolength\topmargin{-0.5in}

\renewcommand\maketitle{\begin{titlepage}%
\let\footnotesize\small
\let\footnoterule\relax
\let\footnote \thanks
\center
\includegraphics[trim=0.7cm 0.7cm 0.7cm 0.7cm]{images/SchCompSci_colour}
  \Large
  \vskip 8em%
  {\LARGE \@title \par}%
  \large
  \lineskip .75em%
 \Large
 {\@author \par}
 \@date 
  \vfill
\end{titlepage}%
\setcounter{footnote}{0}%
\global\let\thanks\relax
\global\let\maketitle\relax
\global\let\@thanks\@empty
\global\let\@author\@empty
\global\let\@date\@empty
\global\let\@title\@empty
\global\let\title\relax
\global\let\author\relax
\global\let\date\relax
\global\let\and\relax
}

