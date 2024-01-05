---
title: IR + Inflation
author: george / TU
tags: [setup]
---

There are four types of curves in Xplain:
- IR_INDEX curves (e.g. USD SOFR)
- INFLATION_INDEX curves (e.g. GBP RPI)
- INDEX_BASIS curves (e.g. AUD 3M)
- XCCY curves (e.g. GBP/USD)

The difference between an IR_INDEX curve and an INDEX_BASIS curve will be driven by the permissible node types, e.g. FixedIborSwap or IborIborSwap respectively.

XCCY curves can be defined as hybrid curves with a mix of FxSwap, XCCYIborIborSwap or XCCYIborOvernightSwap, as applicable.

Permissible values for curve names and associated nodes per currency can be found <a href="/docs.xplainfinancial/docs/permissibleValues/curves/irInflationCurve/#curvePermissibleValues">here</a>.

In this section, we will discuss:
- how to build a <a href= "#curveConstruction">generic interest rate or inflation curve</a>
- how to define an <a href= "#offshoreCurves">offshore curve</a> vs. a standard/onshore curve
- how to define a curve for <a href= "#clearedInflationCurves">cleared inflation swaps</a> vs. bilateral

<h2><a class="anchor" id="curveConstruction"></a>Curve Construction</h2>

Once we have created a <a href="/docs.xplainfinancial/docs/userGuide/curves/curvesMenu/#curveGroup">Curve Group</a>, the two steps required to build an IR or inflation curve are as follows:

1. <a href= "#createCurve">Create</a> (or edit) a curve
2. <a href= "#addNode">Add</a> curve nodes

Permissible values for curve definitions are set out in the <a href= "/docs.xplainfinancial/docs/permissibleValues/curves/irInflationCurve#curvePermissibleValues">Curve Permissible Values</a> section.

<h3><a class="anchor" id="createCurve"></a>1. Creating an IR + INFLATION Curve</h3>

Under <xplmenuitem> CURVES/CURVE GROUPS</xplmenuitem>, at the curve group level, in <xpltabitem>IR + INFLATION</xpltabitem>, we can <xplgreybutton>IMPORT</xplgreybutton> a list of interest rate and inflation curves, or manually create one (e.g., a EUR €STR curve) by clicking on <xplbutton>ADD NEW</xplbutton> (or edit by double-clicking on the line item).

{% include image.html img="\userGuide\curves\creatingACurve.png" lightbox="true" alt="Alt for image" caption="Creating an IR or Inflation Curve<br><xplmenuitem>CURVES/CURVE GROUPS/NEW CURVE GROUP/IR + INFLATION</xplmenuitem>" %}

{% include image.html img="\userGuide\curves\creatingACurve2.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>ADD NEW</xplbutton> and selecting Curve Type = IR_INDEX and Name = EUR ESTR" %}

{% include image.html img="\userGuide\curves\creatingACurve3.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton> - Versioning options" %}

{% include image.html img="\userGuide\curves\creatingACurve4.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton>" %}

{% include image.html img="\userGuide\curves\creatingACurve5.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplgreybutton>IMPORT / Curve List</xplgreybutton> and selecting the relevant curve list file - Versioning options" %}

{% include image.html img="\userGuide\curves\creatingACurve6.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplbutton>IMPORT</xplbutton>" %}

A description of a curve’s attributes and corresponding permissible values are set out in the table below.

<table>
<col style="width:20%">
<col style="width:55%">
<col style="width:25%">
  {% for row in site.data.userGuide.curves.creatingACurve %}
    {% if forloop.first %}
    <tr>
      {% for pair in row %}
        <th>{{ pair[0] }}</th>
      {% endfor %}
    </tr>
    {% endif %}

    {% tablerow pair in row %}
      {{ pair[1] }}
    {% endtablerow %}

{% endfor %}

</table>

<p class="tableFooter" ><sup>(*)</sup> IR_INDEX and IR_INFLATION curves are single currency curves built with FIX vs. float instruments. INDEX_BASIS are single currency curves built with float vs. float instruments. XCCY curves can be built with either FxSwap nodes, XCCY swaps, or a combination of both. </p>
<p class="tableFooter" ><sup>(**)</sup> Only applicable for 3M projection indices </p>

<h3><a class="anchor" id="addNode"></a>2. Adding Curve Nodes </h3>

Under <xplmenuitem> CURVES/CURVE GROUPS</xplmenuitem>, at the curve level (or also globally at the curve list level when importing), we can <xplgreybutton>IMPORT</xplgreybutton> a list of curve nodes or manually create one (e.g., a 5Y node) by first clicking on <xplbutton>EDIT</xplbutton>, then on <xplbutton>ADD NEW</xplbutton> (or edit by double-clicking on the line item).

The import example below is performed at the curve level but in practice, the curve node import should be performed at the curve list level (i.e. across all IR + INFLATION curves).

{% include image.html img="\userGuide\curves\addCurveNode.png" lightbox="true" alt="Alt for image" caption="Case 1: Adding a Curve Node after clicking on <xplbutton>EDIT</xplbutton><br> <xplmenuitem>CURVES/CURVE GROUPS/NEW CURVE GROUP/IR + INFLATION/EUR ESTR</xplmenuitem>" %}

{% include image.html img="\userGuide\curves\addCurveNode2.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>ADD NEW</xplbutton>, selecting Convention = EUR-FIXED-1Y_ESTR-OIS and inputting Tenor = 5Y" %}

{% include image.html img="\userGuide\curves\addCurveNode3.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton>" %}

{% include image.html img="\userGuide\curves\addCurveNode4.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton> on the left handside - Versioning options" %}

{% include image.html img="\userGuide\curves\addCurveNode5.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton>" %}

{% include image.html img="\userGuide\curves\addCurveNode6.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplgreybutton>IMPORT</xplgreybutton> and selecting the relevant curve node list file - Versioning options" %}

{% include image.html img="\userGuide\curves\addCurveNode7.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplbutton>IMPORT</xplbutton>" %}

Permissible curve nodes will be a function of the <em>Curve Type</em> and <em>Name</em>.
A description of a curve node’s attributes and corresponding permissible values are set out in the table below.

<table>
<col style="width:20%">
<col style="width:55%">
<col style="width:25%">
  {% for row in site.data.userGuide.curves.addingACurveNode %}
    {% if forloop.first %}
    <tr>
      {% for pair in row %}
        <th>{{ pair[0] }}</th>
      {% endfor %}
    </tr>
    {% endif %}

    {% tablerow pair in row %}
      {{ pair[1] }}
    {% endtablerow %}

{% endfor %}

</table>

<p class="tableFooter" ><sup>(*)</sup> For FxSwap Curve Nodes, "ON", "TN" and "SN" can also be used as tenors, in addition to the number of Days (except for "1D"), Months or Years </p>
<p class="tableFooter" ><sup>(**)</sup> Only applicable for 3M projection indices </p>

<h2><a class="anchor" id="offshoreCurves"></a>Offshore Interest Rate Curves</h2>

To price offshore IRS trades, we need to create the relevant offshore curve (i.e. different from the standard/onshore equivalent) which will be calibrated as a projection curve alongside the relevant discounting curve (e.g. USD).

The permissible offshore IRS curves are:

- CNY 1W Offshore (vs. CNY 1W)
- INR OMIBOR Offshore (vs. INR OMIBOR)
- THB 6M Offshore (vs. THB 6M)
- THB THOR Offshore (vs. THB THOR)
- TWD 3M Offshore (vs. TWD 3M)

Each offshore curve will be associated to curve nodes with specific conventions (e.g. CNY-FIXED-3M-REPO-1W-OFFSHORE vs. CNY-FIXED-3M-REPO-1W).

See permissible values for <a href="/docs.xplainfinancial/docs/permissibleValues/curves/irInflationCurve/#CNY">CNY</a>, <a href="/docs.xplainfinancial/docs/permissibleValues/curves/irInflationCurve/#INR">INR</a>, <a href="/docs.xplainfinancial/docs/permissibleValues/curves/irInflationCurve/#THB">THB</a> and <a href="/docs.xplainfinancial/docs/permissibleValues/curves/irInflationCurve/#TWD">TWD</a> in the <a href= "/docs.xplainfinancial/docs/permissibleValues/curves/irInflationCurve#curvePermissibleValues">Curve Permissible Values</a> section.

At the trade level, the Onshore / Offshore dropdown will flag offshore IRS trades.

{% include image.html img="\userGuide\curves\offshoreDropdown.png" lightbox="true" alt="Alt for image" caption="Onshore / Offshore dropdown in the IRS floating leg (Overnight or Ibor)" %}

See permissible values for Overnight and Ibor legs in the <a href="/docs.xplainfinancial/docs/permissibleValues/portfolios/portfolioList/#legFields">Trade leg attributes</a> section.

<h2><a class="anchor" id="clearedInflationCurves"></a>Cleared vs. Bilateral Inflation Curves</h2>

To price cleared inflation trades, we need to create the relevant CCH curve (i.e. different from the standard/"bilateral" equivalent).

The permissible CCH inflation curves are:

- EU EXT CPI LCH (vs. EU EXT CPI)
- FR EXT CPI LCH (vs. FR EXT CPI)
- GB RPI LCH (vs. GB RPI)
- US CPI U LCH (vs. US CPI U)

Each CCH curve will be associated to curve nodes with specific conventions (e.g. GBP-FIXED-ZC-GB-RPI-CLEARED vs. GBP-FIXED-ZC-GB-RPI).

See permissible values for <a href="/docs.xplainfinancial/docs/permissibleValues/curves/irInflationCurve/#EUR">EUR</a>, <a href="/docs.xplainfinancial/docs/permissibleValues/curves/irInflationCurve/#GBP">GBP</a> and <a href="/docs.xplainfinancial/docs/permissibleValues/curves/irInflationCurve/#USD">USD</a> in the <a href= "/docs.xplainfinancial/docs/permissibleValues/curves/irInflationCurve#curvePermissibleValues">Curve Permissible Values</a> section.

At the trade level, the counterparty type and the counterparty dropdowns will flag cleared inflation trades and which CCH curve they should be mapped to.

{% include image.html img="\userGuide\curves\clearedDropdown.png" lightbox="true" alt="Alt for image" caption="Counterparty Type dropdown in the inflation trade" %}

See permissible values for <a href="/docs.xplainfinancial/docs/permissibleValues/portfolios/portfolioList/#genericFields">generic trade attributes</a>.