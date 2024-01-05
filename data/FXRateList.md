---
title: FX Rates
tags: [FX, setup, FX Rate]
author: george/TU
---

<h2><a class="anchor" id="spotDateRules"></a>Spot Date Calculation Rules</h2>

For the purpose of curve calibration, the rules used for spot date calculation are as follows:

<b>If USD is one of the currencies (except if other ccy is MXN, ARS or CLP)</b>

T1 = T + 1BD based on Ccy calendar<br>
Spot Date = T1 + 1BD based on Ccy calendar and US calendar

<b>For USD vs. MXN/ARS/CLP or any other ccy pair excluding CAD/TRY/PHP/RUB</b>

T1 = T+2BD for Ccy1 calendar (i.e. at least 2BD between trade date and settlement)<br>
T2 = T+2BD for Ccy2 calendar (i.e. at least 2BD between trade date and settlement)<br>
Spot Date = BusinessDay[ Max(T1, T2), all calendars including US, Following BDC ] (i.e. rolling forward until a good business day for all)

<b>For USD/CAD, USD/TRY, USD/PHP and USD/RUB</b>

Spot Date = T + 1BD based on Ccy calendar and US calendar<br>

<b>For CAD/TRY/PHP/RUB vs. CAD/TRY/PHP/RUB</b>

T1 = T+1BD for Ccy1 calendar (i.e. at least 1BD between trade date and settlement)<br>
T2 = T+1BD for Ccy2 calendar (i.e. at least 1BD between trade date and settlement)<br>
Spot Date = BusinessDay[ Max(T1, T2), all calendars including US, Following BDC ] (i.e. rolling forward until a good business day for all)

<h2>Adding an FX Rate</h2>

Under <xplmenuitem> CURVES/CURVE GROUPS</xplmenuitem>, at the <a href="/docs.xplainfinancial/docs/userGuide/curves/curvesMenu/#curveGroup">curve group</a> level, in <xpltabitem>FX RATES</xpltabitem>, we can <xplgreybutton>IMPORT</xplgreybutton> a list of FX rates or manually create one (e.g. EUR/USD) by first clicking on <xplbutton>EDIT</xplbutton>, then on <xplbutton>ADD NEW</xplbutton> (or edit by double-clicking on the line item).

{% include image.html img="\userGuide\curves\addNewFXRate.png" lightbox="true" alt="Alt for image" caption="Case 1: Adding an FX Rate<br><xplmenuitem>CURVES/CURVE GROUPS/NEW CURVE GROUP/FX RATES</xplmenuitem>" %}

{% include image.html img="\userGuide\curves\addNewFXRate2.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>ADD NEW</xplbutton> and inputting Base Ccy = EUR and Counter Ccy = USD" %}

{% include image.html img="\userGuide\curves\addNewFXRate3.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton> on the Add FX Rate form" %}

{% include image.html img="\userGuide\curves\addNewFXRate4.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton> - Versioning options" %}

{% include image.html img="\userGuide\curves\addNewFXRate5.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton>" %}

{% include image.html img="\userGuide\curves\addNewFXRate6.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplgreybutton>IMPORT</xplgreybutton> and selecting the relevant FX Rate list file - Versioning options" %}

{% include image.html img="\userGuide\curves\addNewFXRate7.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplbutton>IMPORT</xplbutton>" %}

A description of an FX rate's attributes and corresponding permissible values are set out in the table below.

<table>
<col style="width:20%">
<col style="width:50%">
<col style="width:30%">
  {% for row in site.data.userGuide.curves.fxRateAttributes %}
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

Permissible currencies and currency pairs are set out <a href= "/docs.xplainfinancial/docs/permissibleValues/curves/fxRate#FxRateRule">here</a>.
