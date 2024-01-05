---
title: Permissible Values for Curves
author: TU
tags: [setup]
---


The two steps required to build a credit curve are as follows:

1.	Create a CDS curve, or; 
2.	Create a credit index curve; and
3.	Add credit curve nodes (CDS or funding).


<h3>1. Creating a Credit Curve </h3>

A credit curve is defined as either a CDS or Credit Index curve and are uniquely represented by the Curve Id: *Reference & “_” & Ccy & “_” & Seniority & “_” & Doc Clause* for CDS curves and *Reference & “_” & Ccy* for credit index. However, for the purposes of FVA calculations, a funding curve can also be specified.

At the credit curve list level, we can <xplbutton>IMPORT</xplbutton> a list of credit curves or manually create one by clicking on the <xplbutton>ADD NEW</xplbutton> button (or edit by double-clicking on the line item).

