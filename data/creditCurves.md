---
title: Credit
author: george/TU
tags: [setup]
---

<h2>Credit Curve Construction</h2>

Once we have created a <a href="/docs.xplainfinancial/docs/userGuide/curves/curvesMenu/#curveGroup">curve group</a>, the two steps required to build a credit curve are as follows:

1.	<a href= "#createCurve">Create</a> (or edit) a credit curve (either CDS or credit index)
3.	<a href= "#addNode">Add</a> credit curve nodes

<h3><a class="anchor" id="createCurve"></a>1. Creating a Credit Curve </h3>

Under <xplmenuitem> CURVES/CURVE GROUPS</xplmenuitem>, at the curve group level, in <xpltabitem>CREDIT</xpltabitem>, we can <xplgreybutton>IMPORT</xplgreybutton> a list of CDS or credit index curves or manually create one (e.g., CELESTIAL USD Senior Unsecured CR14) by clicking on <xplbutton>ADD NEW</xplbutton> and selecting <small>CDS</small> or <small>Credit Index</small> (or edit by double-clicking on the line item).

{% include image.html img="\userGuide\curves\createACreditCurve.png" lightbox="true" alt="Alt for image" caption="Creating a CDS or Credit Index Curve<br><xplmenuitem>CURVES/CURVE GROUPS/NEW CURVE GROUP/CREDIT</xplmenuitem>" %}

{% include image.html img="\userGuide\curves\createACreditCurve2.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>ADD NEW/CDS</xplbutton>, inputting Reference = CELESTIAL, Corp Ticker = CELES, Long Name = Celestial Capital Inc, Recovery rate = 0.40 , and selecting Ccy = USD, Sector = Financials, Doc Clause = CR14, Seniority = SNRFOR, Quote Convention = QUOTED_SPREAD and Fixed Coupon (bps) = 100" %}

{% include image.html img="\userGuide\curves\createACreditCurve3.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton> - Versioning options" %}

{% include image.html img="\userGuide\curves\createACreditCurve4.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton>" %}

{% include image.html img="\userGuide\curves\createACreditCurve5.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplgreybutton>IMPORT / Curve List</xplgreybutton> and selecting the relevant curve list file - Versioning options" %}

{% include image.html img="\userGuide\curves\createACreditCurve6.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplbutton>IMPORT</xplbutton>" %}

A <em>Curve Id</em> will be automatically generated as *Reference & “_” & Ccy & “_” & Seniority & “_” & Doc Clause* for a CDS curve and *Reference & “_” & Ccy* for a Credit Index curve. Such <em>Curve Id</em> will constitute the credit curve's unique identifier.

A description of a CDS curve’s attributes and corresponding permissible values are set out in the table below.

<table>
<col style="width:20%">
<col style="width:55%">
<col style="width:25%">
  {% for row in site.data.userGuide.curves.cdsCurveAttributes %}
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

A description of a Credit Index curve’s attributes and corresponding permissible values are set out in the table below. 

<table>
<col style="width:20%">
<col style="width:55%">
<col style="width:25%">
  {% for row in site.data.userGuide.curves.creditIndexAttributes %}
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

A description of a Credit Index Tranche curve’s attributes and corresponding permissible values are set out in the table below. 

<table>
<col style="width:20%">
<col style="width:55%">
<col style="width:25%">
  {% for row in site.data.userGuide.curves.cdtAttributes %}
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

<h3><a class="anchor" id="addNode"></a>2. Adding Credit Curve Nodes </h3>

Under <xplmenuitem> CURVES/CURVE GROUPS</xplmenuitem>, at the curve level (or also globally at the curve list level when importing), we can <xplgreybutton>IMPORT</xplgreybutton> a list of credit curve nodes or manually create them by first clicking on <xplbutton>EDIT</xplbutton>, then on <xplbutton>ADD NEW</xplbutton> (or edit by double-clicking on the line item).

The import example below is performed at the credit curve level but in practice, the curve node import should be performed at the credit curve list level (i.e. across all credit curves).

{% include image.html img="\userGuide\curves\addCreditCurveNode.png" lightbox="true" alt="Alt for image" caption="Case 1: Adding a Curve Node after clicking on <xplbutton>EDIT</xplbutton><br> <xplmenuitem>CURVES/CURVE GROUPS/NEW CURVE GROUP/CELESTIAL_USD_SNRFOR_CR14</xplmenuitem>" %}

{% include image.html img="\userGuide\curves\addCreditCurveNode2.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>ADD NEW</xplbutton>, and inputting Tenor = 5Y" %}

{% include image.html img="\userGuide\curves\addCreditCurveNode3.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton>" %}

{% include image.html img="\userGuide\curves\addCreditCurveNode4.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton> - Versioning options" %}

{% include image.html img="\userGuide\curves\addCreditCurveNode5.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton>" %}

{% include image.html img="\userGuide\curves\addCreditCurveNode6.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplgreybutton>IMPORT</xplgreybutton> and selecting the relevant curve node list file - Versioning options" %}

{% include image.html img="\userGuide\curves\addCreditCurveNode7.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplbutton>IMPORT</xplbutton>" %}

A description of a credit curve node’s attributes and corresponding permissible values are set out in the table below. 

<table>
<col style="width:20%">
<col style="width:55%">
<col style="width:25%">
  {% for row in site.data.userGuide.curves.creditCurveNodes %}
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