---
title: IR Volatility
tags: [IR Volatility, setup, IR Volatility Surface]
author: george/TU
---

<h2>IR Volatility Surface Configuration</h2>

Once we have created a <a href="/docs.xplainfinancial/docs/userGuide/curves/curvesMenu/#curveGroup">curve group</a>, the four steps required to build an IR Volatility Surface are as follows:

1. <a href= "#createVolSurface">Create</a> (or edit) an IR volatility surface;
2. <a href= "#createATMVolMatrix">Add</a> an ATM swaption matrix (optional);
3. <a href= "#createCapFloorSurface">Add</a> a Cap/Floor strike matrix (optional); and
4. <a href= "#addSkew">Add</a> a swaption skew configuration (optional).

<h3><a class="anchor" id="createVolSurface"></a>1. Creating a Volatility Surface</h3>

Under <xplmenuitem> CURVES/CURVE GROUPS</xplmenuitem>, at the curve group level, in <xpltabitem>IR VOLATILITY</xpltabitem>, we can <xplgreybutton>IMPORT</xplgreybutton> a list of volatility surfaces or manually create one (e.g., USD SOFR Vols) by clicking on <xplbutton>ADD NEW</xplbutton> (or edit by double-clicking on the line item).

{% include image.html img="\userGuide\curves\addIRVolSurface.png" lightbox="true" alt="Alt for image" caption="Creating a volatility surface<br><xplmenuitem>CURVES/CURVE GROUPS/NEW CURVE GROUP/IR VOLATILITY</xplmenuitem>" %}

{% include image.html img="\userGuide\curves\addIRVolSurface2.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>ADD NEW</xplbutton> and selecting Name = USD SOFR Vols,<br>selecting the interpolation and extrapolation settings,<br>Swaption Skew Type = Moneyness and Cap/Floor Model = Normal" %}

{% include image.html img="\userGuide\curves\addIRVolSurface3.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton> - Versioning options" %}

{% include image.html img="\userGuide\curves\addIRVolSurface4.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton>" %}

{% include image.html img="\userGuide\curves\addIRVolSurface5.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplgreybutton>IMPORT/Index Volatility Surface List</xplgreybutton> and selecting the relevant index surface volatility list file - Versioning options" %}

{% include image.html img="\userGuide\curves\addIRVolSurface6.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplbutton>IMPORT</xplbutton>" %}

A description of an IR volatility surface’s attributes and corresponding permissible values are set out in the table below.

<table>
<col style="width:20%">
<col style="width:52%">
<col style="width:28%">
  {% for row in site.data.userGuide.curves.irVolSurface %}
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

<h3><a class="anchor" id="createATMVolMatrix"></a>2. Adding ATM Swaption Points </h3>

Under <xplmenuitem> CURVES/CURVE GROUPS</xplmenuitem>, at the curve group level, in <xpltabitem>IR VOLATILITY</xpltabitem>, at the volatility surface level (or also globally at the volatility surface list level when importing), we can <xplgreybutton>IMPORT</xplgreybutton> a list of ATM swaption points or manually edit it by first clicking on <xplbutton>EDIT</xplbutton>, then on <xplbutton><large>+</large></xplbutton>, to add either a <em>TENOR</em> (e.g., a 5Y tenor) or an <em>EXPIRY</em>.

The import example below is performed at the volatility surface level but in practice, the ATM swaption point import should be performed at the IR volatility surface list level (i.e. across all IR volatility surfaces).

{% include image.html img="\userGuide\curves\addNewIRVolNode.png" lightbox="true" alt="Alt for image" caption="Case 1: Adding a new ATM swaption point after clicking on <xplbutton>EDIT</xplbutton><br><xplmenuitem>CURVES/CURVE GROUPS/NEW CURVE GROUP/IR VOLATILITY/USD SOFR Vols</xplmenuitem>" %}

{% include image.html img="\userGuide\curves\addNewIRVolNode2.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton><large>+</large></xplbutton> TENOR and inputting 5Y" %}

If the ATM swaption volatility surface is empty, adding a new <em>TENOR</em> (<em>EXPIRY</em>) will automatically associate it to a 1Y <em>EXPIRY</em> (<em>TENOR</em>).

{% include image.html img="\userGuide\curves\addNewIRVolNode3.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>ADD NEW</xplbutton>" %}

{% include image.html img="\userGuide\curves\addNewIRVolNode4.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton> - Versioning options" %}

{% include image.html img="\userGuide\curves\addNewIRVolNode5.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton>" %}

{% include image.html img="\userGuide\curves\addNewIRVolNode6.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplgreybutton>IMPORT</xplgreybutton> and selecting the relevant ATM swaption point list file - Versioning options" %}

{% include image.html img="\userGuide\curves\addNewIRVolNode7.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplbutton>IMPORT</xplbutton>" %}

It does not have to be a full matrix (i.e. all expiries vs. all tenors). The same configuration will automatically be applied to the corresponding <a href= "#addSkew">skew surfaces</a> (if any).

A description of an ATM swaption point’s attributes and corresponding permissible values are set out in the table below.

<table>
<col style="width:20%">
<col style="width:52%">
<col style="width:28%">
  {% for row in site.data.userGuide.curves.irATMSwaption %}
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

<h3><a class="anchor" id="createCapFloorSurface"></a>3. Adding Cap/Floor Strike Points </h3>

Under <xplmenuitem> CURVES/CURVE GROUPS</xplmenuitem>, at the curve group level, in <xpltabitem>IR VOLATILITY</xpltabitem>, at the volatility surface level (or also globally at the volatility surface list level when importing), we can <xplgreybutton>IMPORT</xplgreybutton> a list of cap/floor strike points or manually edit it by first clicking on <xplbutton>EDIT</xplbutton>, then on <xplbutton><large>+</large></xplbutton>, to add either a <em>STRIKE</em> (e.g., a 5% strike) or a <em>MATURITY</em>.

The import example below is performed at the volatility surface level but in practice, the cap/floor strike point import should be performed at the IR volatility surface list level (i.e. across all IR volatility surfaces).

{% include image.html img="\userGuide\curves\addCapFloorPoint.png" lightbox="true" alt="Alt for image" caption="Case 1: Adding a new cap/floor strike point after clicking on <xplbutton>EDIT</xplbutton><br><xplmenuitem>CURVES/CURVE GROUPS/NEW CURVE GROUP/IR VOLATILITY/EUR 6M Vols</xplmenuitem>" %}

{% include image.html img="\userGuide\curves\addCapFloorPoint2.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton><large>+</large></xplbutton> STRIKE and inputting 5(%)" %}

If the cap/floor volatility surface is empty, adding a new <em>STRIKE</em> (<em>MATURITY</em>) will automatically associate it to a 1Y <em>MATURITY</em> (or a 1% <em>STRIKE</em>).

{% include image.html img="\userGuide\curves\addCapFloorPoint3.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>ADD NEW</xplbutton>" %}

{% include image.html img="\userGuide\curves\addCapFloorPoint4.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton> - Versioning options" %}

{% include image.html img="\userGuide\curves\addCapFloorPoint5.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton>" %}

{% include image.html img="\userGuide\curves\addCapFloorPoint6.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplgreybutton>IMPORT</xplgreybutton> and selecting the relevant cap/floor points list file - Versioning options" %}

{% include image.html img="\userGuide\curves\addCapFloorPoint7.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplbutton>IMPORT</xplbutton>" %}

It does not have to be a full matrix (i.e. all maturities vs. all strikes).

A description of a cap/floor strike point’s attributes and corresponding permissible values are set out in the table below.

<table>
<col style="width:20%">
<col style="width:52%">
<col style="width:28%">
  {% for row in site.data.userGuide.curves.addCapFloor %}
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

<h3><a class="anchor" id="addSkew"></a>4. Adding Swaption Skew Configuration </h3>

Under <xplmenuitem> CURVES/CURVE GROUPS</xplmenuitem>, at the curve group level, in <xpltabitem>IR VOLATILITY</xpltabitem>, at the volatility surface level (or also globally at the volatility surface list level when importing), we can <xplgreybutton>IMPORT</xplgreybutton> a list of skew values or manually edit it by first clicking on <xplbutton>EDIT</xplbutton>, then on <xplbutton>ADD NEW</xplbutton> to add a new skew value (e.g., 100bps) (or edit by double-clicking on the line item). Where applicable, volatility skew can be defined per "Monyeness" or per "Absolute Strike", as defined by the <em>Swaption Skew Type</em>.

The import example below is performed at the volatility surface level but in practice, the swaption skew import should be performed at the IR volatility surface list level (i.e. across all IR volatility surfaces).

{% include image.html img="\userGuide\curves\moneyness.png" lightbox="true" alt="Alt for image" caption="Case 1: Adding a new skew value after clicking on <xplbutton>EDIT</xplbutton><br><xplmenuitem>CURVES/CURVE GROUPS/NEW CURVE GROUP/IR VOLATILITY/USD SOFR Vols</xplmenuitem>" %}

{% include image.html img="\userGuide\curves\moneyness2.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>ADD NEW</xplbutton> and inputting 100(bps)" %}

{% include image.html img="\userGuide\curves\moneyness3.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton>" %}

{% include image.html img="\userGuide\curves\moneyness4.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton> - Versioning options" %}

{% include image.html img="\userGuide\curves\moneyness5.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>SAVE</xplbutton>" %}

{% include image.html img="\userGuide\curves\moneyness6.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplgreybutton>IMPORT</xplgreybutton> and selecting the relevant skew values list file - Versioning options" %}

{% include image.html img="\userGuide\curves\moneyness7.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplbutton>IMPORT</xplbutton>" %}

The skew matrix configuration will automatically be inherited from the corresponding <a href= "#createATMVolMatrix">IR ATM swaption matrix</a>.

A description of a swaption skew’s attributes and corresponding permissible values are set out in the table below.

<table>
<col style="width:20%">
<col style="width:52%">
<col style="width:28%">
  {% for row in site.data.userGuide.curves.moneynessSkewTable %}
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
