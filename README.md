# OpenEIS

A repository with teaching and tutorial materials for electrochemical impedance spectroscopy. This is currently under construction. Most of the materials are developed using Python 3 and many of the packages that makes up the "SciPy-stack". Contributions are most welcome (soon CONTRIBUTING.md will be available).

## Resources for CNLS Analysis of EIS Data
* [Elchemea Analytical](http://www.elchemea.dk/) is an easy to use impedance fitting and plotting application that is available to download and install (although it is ), or use directly online through your browser. It is free and open source software distributed under the [GNU GPL](https://www.gnu.org/licenses/gpl.html). OS: Linux 
* [EIS Spectrum Analyser](http://www.abc.chemistry.bsu.by/vi/analyser/) is a standalone program for analysis and simulation of impedance spectra. It has also a built-in impedance spectra simulation routine, tools for impedance data processing (subtraction of circuit elements and subcircuits, normalisation for electrode surface area) and plotting in various formats. The program is free for noncommercial use. OS: Windows

## Data Validation Tools
Kramers-Kronig transform *compliance* testing is a valuable tool for quantification of errors in impedance spectroscopy data. There are currently a number of tools freely available that implements the method proposed by [B.A. Boukamp](https://www.utwente.nl/en/tnw/ims/people/boukamp/) in his article "A Linear Kronig-Kramers Transform Test for Immittance Data Validation" [1, 2].

* Boukamp's **KKtest for Windows** is free for non-commercial use and can be downloaded from https://www.utwente.nl/en/tnw/ims/publications/downloads/KK-windows.zip
* **EIS Spectrum Analyser** also incorporates the linear KK transform test docs [here](http://www.abc.chemistry.bsu.by/vi/analyser/linearkk.html)
* The **Lin-KK** tool is more recent and incorporates a few advanced features to protect against over/under-fitting during Kramers-Kronig validity tests of the impedance spectra. This page also has a nice introduction to  the method and the algorithm used is discussed in [3,4] https://www.iam.kit.edu/wet/english/Lin-KK.php

## Distribution of Relaxation Times (DRT)

## References

[1] B.A. Boukamp, "A Linear Kronig-Kramers Transform Test for Immittance Data Validation", Journal of the Electrochemical Society. 142 (1995) 1885–1894, https://doi.org/10.1149%2F1.2044210

[2] B. A. Boukamp, Solid State Ionics, 169, 65–73 (2004), https://doi.org/10.1016%2Fj.ssi.2003.07.002

[3] M. Schönleber and E. Ivers-Tiffée, "Approximability of impedance spectra by RC elements and implications for impedance analysis", Electrochemistry Communications 58 (2015) 15-19, https://dx.doi.org/10.1016/j.elecom.2015.05.018 

[4] M. Schönleber, D. Klotz and E. Ivers-Tiffée, "A Method for Improving the Robustness of linear Kramers-Kronig Validity Tests", Electrochimica Acta (2014), https://dx.doi.org/10.1016/j.electacta.2014.01.034 