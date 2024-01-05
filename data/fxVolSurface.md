---
title: FX Volatility
tags: [FX, setup, FX Rate]
author: george/TU
---

<h2>Expiry Date Calculation Rules</h2>

For the purpose of volatility interpolation, the rules used for expiry date calculation are as follows:

<b>If Expiry is expressed in #D or #W</b>

Unadjusted Expiry Date = Valuation Date + Expiry<br>
Expiry Date = BusinessDay[ Unadjusted Expiry Date, Ccy1 calendar and Ccy2 calendar, Following BDC ] (i.e. rolling forward until a good business day for both currencies)

<b>If Expiry is expressed in #M or #Y</b>

Delivery Date = Spot Date + Expiry <br>
Expiry Date = first date prior to Delivery Date whose corresponding Spot Date = Delivery Date<br>
See <a href="/docs.xplainfinancial/docs/userGuide/curves/FXRateList/#spotDateRules"> Spot Date calculation rules</a>.

<h2>FX Volatility Surface Configuration</h2>

Once we have created a <a href="/docs.xplainfinancial/docs/userGuide/curves/curvesMenu/#curveGroup">curve group</a>, the two steps required to define the FX volatility surface are as follows:

1. <a href= "#createVolSurface">Define</a> the FX ATM volatility surface
2. <a href= "#addSkew">Add</a> the FX volatility skew configuration

<h3><a class="anchor" id="createVolSurface"></a>1. Defining the FX ATM Volatility Surface</h3>

Under <xplmenuitem> CURVES/CURVE GROUPS</xplmenuitem>, at the curve group level, in <xpltabitem>FX VOLATILITY</xpltabitem>, we can <xplgreybutton>IMPORT</xplgreybutton> the FX ATM volatility surface or manually edit it by first clicking on <xplbutton>EDIT</xplbutton>, then on <xplbutton><large>+</large></xplbutton>, to add either a <em>CURRENCY PAIR</em> (e.g., EUR/USD) or an <em>EXPIRY</em>. While in EDIT mode, we can also define the various <a href="/docs.xplainfinancial/docs/permissibleValues/curves/curveInterpolators/"> interpolation / extrapolation</a> settings.

{% include image.html img="\userGuide\curves\addFXVolSurface.png" lightbox="true" alt="Alt for image" caption="Defining the FX ATM volatility surface<br><xplmenuitem>CURVES/CURVE GROUPS/NEW CURVE GROUP/FX VOLATILITY</xplmenuitem>" %}

{% include image.html img="\userGuide\curves\addFXVolSurface2.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>EDIT</xplbutton>" %}

{% include image.html img="\userGuide\curves\addFXVolSurface3.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton><large>+</large></xplbutton> CURRENCY PAIR and inputting Base Ccy = EUR and Counter Ccy = USD" %}

{% include image.html img="\userGuide\curves\addFXVolSurface4.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>ADD NEW</xplbutton>" %}

If the FX ATM volatility surface is empty, adding a new <em>CURRENCY PAIR</em> will automatically associate it to a 1Y <em>EXPIRY</em>.

{% include image.html img="\userGuide\curves\addFXVolSurface5.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton> - Versioning options" %}

{% include image.html img="\userGuide\curves\addFXVolSurface6.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton>" %}

{% include image.html img="\userGuide\curves\addFXVolSurface7.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplgreybutton>IMPORT</xplgreybutton> and selecting the relevant FX ATM volatility points list file - Versioning options" %}

{% include image.html img="\userGuide\curves\addFXVolSurface8.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplbutton>IMPORT</xplbutton>" %}

A description of an FX ATM volatility point’s attributes and corresponding permissible values are set out in the table below.

<table>
<col style="width:15%">
<col style="width:55%">
<col style="width:30%">
  {% for row in site.data.userGuide.curves.addFXVolSurfacePoints %}
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

Permissible currency values can be split into the two categories that are specified <a href="/docs.xplainfinancial/docs/userGuide/curves/FXRateList/"> here. </a>

At the curve configuration level, when hovering on the ATM FX volatility for a given currency and a given option tenor, we can see the actual expiry date which will be applicable by reference to the prevailing anchor date.

{% include image.html img="\userGuide\curves\FXVols_ExpiryDate.png" lightbox="true" alt="Alt for image" caption="Expiry Date - After hovering on a given FX ATM volatility" %}

<h3><a class="anchor" id="addSkew"></a>2. Adding the FX Volatility Skew Configuration </h3>

Under <xplmenuitem> CURVES/CURVE GROUPS</xplmenuitem>, at the curve group level, in <xpltabitem>FX VOLATILITY</xpltabitem>, we can <xplgreybutton>IMPORT</xplgreybutton> the FX volatility skew configuration or manually define one by first clicking on <xplbutton>EDIT</xplbutton>, then on <xplbutton>ADD NEW</xplbutton>. While in EDIT mode, we can also define the various <a href="/docs.xplainfinancial/docs/permissibleValues/curves/curveInterpolators/"> interpolation / extrapolation</a> settings.

{% include image.html img="\userGuide\curves\addFXVolSkew.png" lightbox="true" alt="Alt for image" caption="Defining the FX volatility skew configuration<br><xplmenuitem>CURVES/CURVE GROUPS/NEW CURVE GROUP/FX VOLATILITY</xplmenuitem>" %}

{% include image.html img="\userGuide\curves\addFXVolSkew2.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>EDIT</xplbutton>" %}

{% include image.html img="\userGuide\curves\addFXVolSkew3.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>ADD NEW</xplbutton>, selecting (the existing) Currency Pair = EUR/USD and inputting Delta 1 = 10 and Delta 2 = 25" %}

{% include image.html img="\userGuide\curves\addFXVolSkew4.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton>" %}

{% include image.html img="\userGuide\curves\addFXVolSkew5.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton> - Versioning options" %}

{% include image.html img="\userGuide\curves\addFXVolSkew6.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton>" %}

{% include image.html img="\userGuide\curves\addFXVolSkew7.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplgreybutton>IMPORT</xplgreybutton> and selecting the relevant FX skews list file - Versioning options" %}

{% include image.html img="\userGuide\curves\addFXVolSkew6.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplbutton>IMPORT</xplbutton>" %}

In this example, there are no additional FX skews.

A description of an FX volatility skew’s attributes and corresponding permissible values are set out in the table below.

<table>
<col style="width:20%">
<col style="width:50%">
<col style="width:30%">
  {% for row in site.data.userGuide.curves.fxRateSkew %}
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
