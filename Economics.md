# Micro & Models

Models

- Exogenous vs endogenous: **Exo** = input, **endo** = output

- Behavioral equation = based on the circumstances, what action will people take?
  - Equilibrium relationship = the steady-state of this model

$Q^D = Q^S$

- $Q^D = \alpha - \beta P + \gamma G$

  - $P$ = Price

  - $G$ = Price of sub goods

    

- $Q^S = \theta + \lambda P + \phi N$

  - $N$ = Cost of production



### Elasticity

```python
import sympy as sym
sym.init_printing(use_unicode=False, wrap_line=True)

# We can declare symbols / variables for elasticity
a = sym.Symbol('a') # Price intercept
b = sym.Symbol('b') # Slope intercept
q = sym.Symbol('q')
p = sym.Symbol('p')
Q = sym.Symbol('Q')
P = sym.Symbol('P')
m = sym.Symbol('m') # Income
j = sym.Symbol('j') # Change resulting from other good's price change

# For revenue
TR = sym.Symbol('TR') # Total revenue
MR = sym.Symbol('MR') # Marginal revenue
AR = sym.Symbol('AR') # Average revenue
p = sym.Symbol('p')
```



```python
# Information we are given
a = 5
b = -2
#q = 
p = 2
#Q = 
#P =
```



$$Demand\:curve\:(Whole\:Market): \\
Q = \frac{a-P}{b}$$



$$Demand\:curve\:(Individual): \\
q = \frac{a-p}{b}$$



$$Inverse\:Demand\:curve\:(Whole\:Market): \\
P = a - bQ$$



$$Inverse\:Demand\:curve\:(Individual): \\
P = a - bQ$$



$$Price\:elasticity\:of\:demand = \frac{dQ}{dP} * \frac{P}{Q}$$



$$Income\:elasticity = \frac{dQ}{dm} * \frac{m}{Q}$$



$$Cross\:price\:elasticity\:of\:demand = \frac{dQ}{dP} * \frac{P}{Q}$$



# Macro

## Data

- Harvard
  - [Python Dataverse](https://github.com/gdcc/pyDataverse)
  - [R Dataverse](https://github.com/IQSS/dataverse-client-r)
  - [Harvard Economic Complexity](https://atlas.cid.harvard.edu/)
    - [Growth Lab](https://growthlab.app/#hub)
- Govt
  - [Bureau of Economic Analysis](https://www.bea.gov/data)
  - [Bureau of Labor Stats](https://www.bls.gov/cex/tables.htm)
  - [GeoCodes](https://unstats.un.org/unsd/methodology/m49/)
- [Energy](https://www.eia.gov/opendata/qb.php)
  - [Future Outlook](https://www.eia.gov/outlooks/aeo/)
- [DataCommons](https://datacommons.org/)
- [NASA](https://ghrc.nsstc.nasa.gov/home/access-data)
- Indicators
  - GDP
  - CPI
  - Unemployment

---





## 1. Aggregate Income

GDP = $Y = C + I + G + NX$

- I = investment
  - Business fixed investment: normal business investments
  - Residential investment: new housing by households and landlords
  - Inventory investment: increase in inventory

GNP

Gross domestic product

- Gross national product 

  GDP + Res Income - NonRes Income

  - Net national product

    GNP - Depreciation

    - National income

      NNP - Stat discrepancy

      - Personal income

        Only households and non-corps

        - Disposable income

          Availability after taxes

## 2. Inflation Rate

**Price Indexes**: Fixed basket = Laspeyres, changing basket = Paasche

- CPI = basket of consumer goods

- PPI = Producer price index = basket of firms good

- Core inflation = consumer basket without food or energy products because they are too volatile in the short term

- GDP Inflator

- PCE = Personal consumption expenditure

  

## 3. Unemployment Rate

1. Employed
2. Unemployed
3. Not in the labor force









---

## Structure

Sectors

1. **Primary**
   1. Materials
   2. Energy
2. **Secondary (finished goods) **- VDC
   1. Industrials (Manufacturing, Construction) - VIS
   2. Utilities - VPU
3. **Tertiary (services)**
   1. Retail - VCR
   2. Financial - VFH
   3. Communication - VOX
   4. Hospitality, leisure
   5. Real estate - VNQ
   6. Info tech - VGT
   7. Healthcare - VHT
4. **Quaternary (knowledge)**
   1. Education
   2. Public sector
   3. Research and dev

---



### Ch 3: National Income

*General equilibrium model*

**Conclusions**

- **Factor prices** equilibrate factor markets
  - Firm demands each factor until MP = real factor price
- **Interest rate** equilibrates demand for g&s

**Assumptions:**

- Doesn't account for money
- Doesn't account for international trade
- Labor force is fully employed
- Capital, labor, and technology are fixed
- Ignored sticky short-run prices

**Math**:

- $Y = C(Y-T) + I(r) + G$
- "The demand for the economy’s output comes from consumption, investment, and government purchases. Consumption depends on disposable income, investment depends on the real interest rate, and government purchases and taxes are the exogenous variables set by fiscal policymakers"



### Ch 4: Monetary Policy





# Integrate

## Dalio - Econ Machine

**Introduction**

- Economy = sum of the transactions that make it up
- Total spending = money spent + credit spent

People, Businesses, Banks, Governments   

- Central government = collects taxes & spends money 

- Central bank = controls amount of money & credit in the economy (print money, interest rates)

  

Credit matters most in the short run, productivity matters most in the long run

- Business cycles depend on how much credit is available

- Exponential cycle based on borrowing - all the way up the chain



- Total credit in US: $50 Trillion

- Total money in US: $3 Trillion



- Credit is bad when used for overconsumption that can’t be repaid (Buy a TV)
- Credit is good when it helps to produce income so you can repay (Buy a tractor)



**Short Term**

Short term debt cycle: Driven by the federal reserve (5 to 8 years)

Exponential cycle based on borrowing - all the way up the chain

- Expansion = spending increases, prices rise
- Fed raises interest rates when too much inflation
  - Less borrowing = high debt payments = less money to spend = less spending = less income = prices fall = deflation



**Long Term**

Long term debt cycle : Human nature, people want to push their spending and consume more

Debt burden = debt to income ratio

- As long as incomes continue to rise, the debt burden is manageable
- In 2008:    Total US Debt as % of GDP = 350%   
- When this happens, economy goes thru deleveraging
  - Cut spending = income fall = asset prices fall = stocks fall = social issues = less spending
    - Interest rates cant be lowered to save this



Recession vs deleveraging = in a deleveraging, borrowing too much, cant be helped by lowering interest rates

​     To solve deleveraging, need to bring down debt burden

​       4 deflationary ways

​        (1) Cut spending (people, businesses, and government) (called austerity) (causes deflation)

​        (2) Reduce debt (faults, restructuring)

​        (3) Redistribute wealth

​        (4) Print money

​       2 inflationary ways       

​       (1) Central bank needs to print money, buys financial assets

​       (2) Central government needs to buy goods and services to put money in peoples hands

​          Central banks buy government bonds, essentially lending money to government allowing it to run a deficit and increase spending  

​     

​       4 deflationary ways and 2 inflationary ways need to balance each other out

​         Beautiful : debts decline relative to income, real economic growth is positive, and inflation is okay

​           Printing money won’t cause inflation if it offsets falling credit



**Rules**

**(1) Don’t let debt rise faster than income**

**(2) Don't let income rise faster than productivity**

**(3) Do everything you can to raise productivity**

---





## Energy

[BP Stats Review World Energy](https://www.bp.com/content/dam/bp/business-sites/en/global/corporate/pdfs/energy-economics/statistical-review/bp-stats-review-2020-full-report.pdf)

[Strategic Analysis Paper](https://www.sciencedirect.com/science/article/pii/S2352484719300034#b10)

Natural gas, oil, coal, electricity











# Investing

## Long (years, months)

- Macro

  - Political

  - Economic

  - Social

  - Natural resources / technogical change

    

- Industry

  - Creative destruction

  - Temporary shifts

  - Power change within industry

  - Changes in connected industries

    

- Opportunity costs

  - Where is the money right now? Where will it go next?
  
- Odd

  - Current quarter
  - ma(1) through ma(99): how deep is the trend? Convert with PCA
  - Who is hiring? Glassdoor and new job postings

---

## Medium (quarter, weeks)

- Recurring patterns
  - Week trends
    - People tend to be paid every other Friday
    - Strategy changes over the weekend?
    - Holidays

- Temporary patterns
  - Corporation rebalancing
  - News each day
  - Sentiment change

---

## Short (trading)

- Players
  - High frequency trading
  - Time zones / time of day
- Biases

  - Time
    - Computers: Differentiate by time
    - Humans: Differentiate by round numbers (resistance points)
  - Order constraints
    - Fees, platforms
  - Human bias
    - Fear
    - What % am I up / down?
    - Loss aversion
    - Insecurity / pack movement
    - Days until Q end
- Repetitive behavior
  - Adaptive behavior
  - Volume drop = direction, volume size = magnitude
    - Computers: Sequence of order flows
    - Humans: Jumping in on the trend? (tag-alongs)
      - Consecutive minutes in a row trending up



## Together

- Trading trends: when are long & short turning together?
- Do more severe ups and downs happen at "key" prices?