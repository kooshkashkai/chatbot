---
title: Curve Build and Calibration
author: george
tags: [setup]
---

<h2>Curve Build and Calibration</h2>

The steps required to build then calibrate a curve group are as follows:

1. <a href="#curveGroup">Create</a> (or edit) a curve group
2. <a href="#curveConfig">Define</a> a curve configuration that will link a curve group to a market data group and to preferred data providers on an instrument type basis
3. <a href="#curveCalibration">Calibrate</a> the curve group, after selecting <a href="/docs.xplainfinancial/docs/userGuide/data/dataMenu/"> market data</a> sources, discount ccy and stripping type (see <a href="#discountCcy">here</a>) 
4. Export <a href="#curveCalibrationResults">curve calibration results</a>, if need be

<h3><a class="anchor" id="curveGroup"></a>1. Creating a Curve Group </h3>

Under <xplmenuitem> CURVES/CURVE GROUPS</xplmenuitem>, at the curve group list level, we can create a new curve group (e.g., NEW CURVE GROUP) by clicking on <xplbutton>ADD NEW</xplbutton> (or edit by double-clicking on the line item).

For the purpose of this example, we will import setup data to replicate the LONDON curve configuration and LONDON_FICC company setup. These data can be downloaded <a href="/docs.xplainfinancial/curveImportTemplates/#irInflationCurveImportTemplates">here</a>.

{% include image.html img="\userGuide\curves\createCurveGroup.png" lightbox="true" alt="Alt for image" caption="Creating a Curve Group<br> <xplmenuitem>CURVES/CURVE GROUPS/</xplmenuitem>" %}

{% include image.html img="\userGuide\curves\createCurveGroup2.png" lightbox="true" alt="Alt for image" caption="After clicking on <xplbutton>ADD NEW</xplbutton> and setting NAME = NEW CURVE GROUP" %}

{% include image.html img="\userGuide\curves\createCurveGroup3.png" lightbox="true" alt="Alt for image" caption="After clicking on <xplbutton>SAVE</xplbutton>" %}

A curve group is then defined by a list of:

1. <a href="/docs.xplainfinancial/docs/userGuide/curves/irCurves/"> IR + INFLATION</a> curves (IR_INDEX, TENOR_BASIS, XCCY)
2. <a href="/docs.xplainfinancial/docs/userGuide/curves/FXRateList/">FX RATES</a>
3. <a href="/docs.xplainfinancial/docs/userGuide/curves/irVolSurface/">IR VOLATILITY</a> surfaces
4. <a href="/docs.xplainfinancial/docs/userGuide/curves/fxVolSurface/">FX VOLATILITY</a> surfaces
5. <a href="/docs.xplainfinancial/docs/userGuide/curves/creditCurves/">CREDIT</a> curves
6. <a href="/docs.xplainfinancial/docs/userGuide/curves/bondYieldCurves/">BOND YIELD</a> curves

For more details, please refer to the relevant section.

<h3><a class="anchor" id="curveConfig"></a>2. Defining a Curve Configuration </h3>

The curve configuration process comprises two steps:

- <a href="#curveConfig2">Create</a> a curve configuration that links a curve group to a market data group and to preferred market data providers (primary and secondary, if any) on an instrument type basis <br>
- <a href="#mappingException">Add</a> provider mapping exceptions (if any)

<h4> <a class="anchor" id="curveConfig2"></a>2.1. Creating a Curve Configuration </h4>

Under <xplmenuitem> CURVES/CURVE CONFIGURATIONS</xplmenuitem>, at the curve configuration list level, we can <xplgreybutton>IMPORT</xplgreybutton> a list of curve configurations, or manually create one (e.g., NEW CURVE CONFIGURATION) by clicking on <xplbutton>ADD NEW</xplbutton> (or edit by double-clicking on the line item).

{% include image.html img="\userGuide\curves\createCurveConfig.png" lightbox="true" alt="Alt for image" caption="Creating a Curve Configuration<br> <xplmenuitem>CURVES/CURVE CONFIGURATIONS/</xplmenuitem>" %}

{% include image.html img="\userGuide\curves\createCurveConfig2.png" lightbox="true" alt="Alt for image" caption="Case 1: After clicking on <xplbutton>ADD NEW</xplbutton> and setting NAME = NEW CURVE CONFIGURATION and Curve Group = NEW CURVE GROUP" %}

In this example, we will not click on <xplbutton>SAVE</xplbutton>, and will instead <xplgreybutton>IMPORT</xplgreybutton> the curve configuration.

{% include image.html img="\userGuide\curves\createCurveConfig3.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplgreybutton>IMPORT / Curve Configurations</xplgreybutton> and selecting the relevant configuration file - Versioning options" %}

{% include image.html img="\userGuide\curves\createCurveConfig4.png" lightbox="true" alt="Alt for image" caption="Case 2: After clicking on <xplbutton>IMPORT</xplbutton>" %}

A description of a curve configuration’s attributes and corresponding permissible values are set out in the table below.

<table>
<col style="width:20%">
<col style="width:55%">
<col style="width:25%">
  {% for row in site.data.userGuide.curves.curveConfig %}
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
<a class="anchor" id="mappingException"></a>
<h4> 2.2. Adding a Provider Mapping Exception </h4>

The default mapping between instrument types and preferred providers can be overridden on an instrument type basis.

At the curve configuration level (or also globally at the curve configuration list level when importing), we can <xplgreybutton>IMPORT</xplgreybutton> a list of mapping exceptions or manually create one by clicking on <xplbutton>EDIT</xplbutton>, then on <xplbutton>ADD EXCEPTION</xplbutton> (or edit by double-clicking on the exception number).

{% include image.html img="\userGuide\curves\createCurveConfig6.png" lightbox="true" alt="Alt for image" caption="Viewing or editing a curve configuration<br> <xplmenuitem>CURVES/CURVE CONFIGURATIONS/NEW CURVE CONFIGURATION/</xplmenuitem>" %}

{% include image.html img="\userGuide\curves\addException.png" lightbox="true" alt="Alt for image" caption="Adding a provider mapping exception<br> <xplmenuitem>CURVES/CURVE CONFIGURATIONS/NEW CURVE CONFIGURATION/</xplmenuitem>" %}

In this example, we will <xplgreybutton>IMPORT</xplgreybutton> the curve configuration overrides.

A description of a mapping exception’s attributes and corresponding permissible values are set out in the table below.

<table>
<col style="width:20%">
<col style="width:55%">
<col style="width:25%">
  {% for row in site.data.userGuide.curves.configProviderMapping %}
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

{% include image.html img="\userGuide\curves\addException2.png" lightbox="true" alt="Alt for image" caption="After clicking on <xplgreybutton>IMPORT</xplgreybutton> or on <xplgreybutton>IMPORT / Overrides</xplgreybutton> ,<br>selecting the relevant configuration override file - Versioning options, and<br>clicking on <xplbutton>IMPORT</xplbutton>" %}

{% include image.html img="\userGuide\curves\createCurveConfig5.png" lightbox="true" alt="Alt for image" caption="After adding a curve configuration override at the curve configuration list level" %}

<h3> <a class="anchor" id="curveCalibration"></a>3. Curve Calibration </h3>

Under <xplmenuitem> CURVES/CURVE CONFIGURATIONS </xplmenuitem>, at a curve configuration level, once we have i) <a href="/docs.xplainfinancial/docs/userGuide/data/marketDataMapping/">mapped</a> market data keys and corresponding market data tickers, ii) uploaded the relevant <a href="/docs.xplainfinancial/docs/userGuide/data/marketData/">market data</a>, and iii) define <a href="#discountCcy">discount ccy and stripping type settings</a>, we can calibrate the underlying curves as at a given curve date and valuation date, by clicking on <xplbutton>CALIBRATE</xplbutton> and visualise the calibration results at the curve level.

{% include image.html img="\userGuide\curves\calibrateCurve.png" lightbox="true" alt="Alt for image" caption="Calibrating a Curve Group <xplmenuitem> <br> CURVES/CURVE CONFIGURATIONS/DEMO CURVE CONFIGURATION/</xplmenuitem>" %}

{% include image.html img="\userGuide\curves\calibrateCurve2.png" lightbox="true" alt="Alt for image" caption="After clicking on <xplbutton>CALIBRATE</xplbutton> <br><xplmenuitem> CURVES/CURVE CONFIGURATIONS/DEMO CURVE CONFIGURATION/GBP SONIA/</xplmenuitem>" %}

{% include image.html img="\userGuide\curves\calibrateCurve3.png" lightbox="true" alt="Alt for image" caption="After clicking on <xplbutton>CALIBRATE</xplbutton> <br><xplmenuitem> CURVES/CURVE CONFIGURATIONS/DEMO CURVE CONFIGURATION/GBP SONIA/</xplmenuitem>" %}

<a class="anchor" id="curveCalibrationParametersSettings"></a>

A description of the curve calibration parameters and corresponding permissible values are set out in the table below.

<table>
<col style="width:20%">
<col style="width:55%">
<col style="width:25%">
  {% for row in site.data.userGuide.curves.curveCalibration %}
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

<h3> <a class="anchor" id="discountCcy"></a>Discount Currency and Stripping Type Parameters</h3>

Let's take the example of a portfolio with three IRS (FIX vs. 3M PLN WIBOR, FIX vs. 6M PLN WIBOR and FIX vs. 6M EURIBOR), to be priced with a curve group which comprises four index curves (3M PLN WIBOR, 6M PLN WIBOR, 6M EURIBOR and ESTR) and a EUR/PLN XCCY curve.

Dual curve stripping will be applied with _Stripping Type_ = "OIS (Dual)". If _Discount Ccy_ is set to a specified single ccy (e.g. EUR), the constraint will be that such ccy has an OIS curve. If _Discount Ccy_ is set to "Local Ccy", sub-portfolios of trades with the same discount ccy will be priced independently. We will still have the ability to discount using _Stripping Type_ = "SINGLE" (i.e. same index for projection and discounting), but only with _Discount Ccy_ = "Local Ccy". This is illustrated using our example portfolio below.

<em><b>Case 1</b></em>: _Discount Ccy_ = "EUR" & _Stripping Type_ = "OIS (Dual)"

The portfolio will be valued using the relevant OIS curve and associated XCCY curves as discount curves (for cashflows in that single ccy and foreign cashflows respectively).
Note that an error will be thrown if no OIS curve exists.

In our example, the applied discount curves will be as follows:

ESTR curve → IRS vs. 6M EURIBOR<br>
EUR/PLN CCY curve → IRS vs. 3M PLN WIBOR<br>
EUR/PLN CCY curve → IRS vs. 6M PLN WIBOR

<em><b>Case 2</b></em>: _Discount Ccy_ = "Local Ccy" & _Stripping Type_ = "OIS (Dual)"

When the "Local Ccy" discounting is applied, the portfolio will be split into sub-portfolios of trades mapped to the same Discount Ccy (see Discount Ccy definition <a href="/docs.xplainfinancial/docs/userGuide/valuations/valuationSettings/#discCcy">here</a>). For each sub-portfolio, the OIS curve for the Discount Ccy (and associated XCCY curves) will be used as discount curves for all trades. If such OIS curve does not exist, there will be a further portfolio split per underlying index (see underlying index mapping <a href="/docs.xplainfinancial/docs/userGuide/valuations/valuationSettings/#indexMapping">here</a>), and such index curve will then be used for discounting.

In our example (where there is no OIS curve for PLN), the applied discount curves will be as follows:

ESTR curve → IRS vs. 6M EURIBOR<br>
3M PLN WIBOR curve → IRS vs. 3M PLN WIBOR<br>
6M PLN WIBOR curve → IRS vs. 6M PLN WIBOR

<em><b>Case 3</b></em>: _Discount Ccy_ = "Local Ccy" & _Stripping Type_ = "SINGLE"

The portfolio will be split in sub-portfolios of the same underlying index whose corresponding curve will then be used for discounting.

In our example, the applied discount curves will be as follows:

6M EURIBOR curve → IRS vs. 6M EURIBOR<br>
3M PLN WIBOR curve → IRS vs. 3M PLN WIBOR<br>
6M PLN WIBOR curve → IRS vs. 6M PLN WIBOR

<h3>CSA Discounting</h3>

If _CSA Discounting_ is set to TRUE (see <a href="/docs.xplainfinancial/docs/userGuide/valuations/pvCalculations/#setParameters">valuation parameters</a>), where a CSA Ccy has been defined at <a href="/docs.xplainfinancial/docs/userGuide/portfolios/portfolioList/#genericFields">trade level</a>, the portfolio will be split in sub-portfolios of trades with the same CSA Ccy.

Currently, the permissible CSA Ccy values are the same as the permissible values for single _Discount Ccy_:

ALLOWED_DISCOUNTING_CURRENCIES = List.of(USD, EUR, GBP, AUD, CAD, CHF, JPY, NZD, SGD)

For each CSA Ccy, the corresponding sub-portfolio will be valued using <em></b>Case 1</b></em> above (with _Discount Ccy_ = CSA Ccy & _Stripping Type_ = "OIS (Dual)").

<h3> <a class="anchor" id="curveCalibrationResults"></a>4. Export Zero Coupons and Discount Factors </h3>

In the "<small>CURVE LIST</small>" window, once the curve group has successfully been calibrated, we can export the calibration outputs for the curves within the curve group.

To export forward price indices, zero coupons or forward rates (as applicable), click on <xplgreybutton>EXPORT</xplgreybutton> and select "Price Indices/ZC/FWD Rates" in the dropdown menu.

{% include image.html img="\userGuide\curves\exportZeroCoupons.png" lightbox="true" alt="Alt for image" caption="Export Price Indices, Zero Coupons or Forward Rates" %}

To export discount Factors for the curves used as discounting curves in the curve group, click on <xplgreybutton>EXPORT</xplgreybutton> and select "Discount Factors" in the dropdown menu.

{% include image.html img="\userGuide\curves\exportDiscountFactors.png" lightbox="true" alt="Alt for image" caption="Export the Discount Factors" %}
