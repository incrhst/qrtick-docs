# QRTick Fee Calculation Specification for /initiate-series-payment Endpoint

## Overview
This specification details the proper implementation of fee calculation for the `/initiate-series-payment` POST endpoint. It focuses on ensuring the fee determination logic accurately follows the global fee configuration to correct the current fee calculation issues.

## Form Data Structure
The `/initiate-series-payment` POST endpoint receives form data with the following key elements:
- `csrf_token`: Security token
- `series_id`: UUID of the event series
- `customer_name`, `customer_email`, `customer_phone`: Customer details
- Ticket quantities in format: `quantity-{event_id}-{ticket_type_id}={number_of_tickets}`

Example:
```
csrf_token=ImM1ZTJhMGU3NDg4M2JmZDI5OTA5MWZiZTNmZGFkNjYxMWFlNTMyMWQi.aCNj9Q.4I0q8YHwV85VpnU0vTt-OJAjR58&series_id=f258b463-7045-4e85-a828-4ee45e69dfe5&customer_name=QRTick+Test&customer_email=service%40qrtick.com&customer_phone=&quantity-723a4d22-f064-48e3-9821-f84116de3c35-bf3690c1-016b-4129-82a5-4bea5bd06276=2&quantity-444638cb-d983-48fe-968e-fb6b935e3a6b-5761a7a4-01aa-4033-a329-f1faf9e6f2fd=2
```

## Purpose of This Document
This document is specifically created to help developers troubleshoot and correct the fee calculation issues in the `/initiate-series-payment` endpoint. The current implementation appears to have discrepancies in how fees are being determined and applied. This specification provides a clear, step-by-step guide for calculating fees correctly according to the established configuration.

## Fee Configuration Access
The application provides an existing endpoint to retrieve the current fee configuration:
```
@app.route('/api/fee-config')
def api_fee_config():
    # Queries and returns the fee configuration JSON structure
```

This endpoint returns the complete fee configuration structure, including components, rules, and configuration metadata as shown in the provided JSON example.

## Fee Configuration Hierarchy
1. Check for series-specific fee config matching the `series_id`
2. If not found, check for organization-level fee config
3. If neither exists, use the global fee config from `/api/fee-config`

## Fee Calculation Process

### Step 1: Parse Form Data
- Extract all ticket quantities from the form data
- For each ticket, parse the event_id and ticket_type_id from the field name

### Step 2: Determine Order Total
- For each ticket_type_id, query the database to get the ticket price
- Calculate subtotal for each ticket type: `price × quantity`
- Sum all subtotals to get the order total
- Identify the currency of the transaction (JMD or USD)

### Step 3: Select Applicable Fee Components
Based on the currency and order total:

**For JMD currency:**
1. Always apply: Processor Fee (JMD) - 4.25% (order of application: 1)
2. Always apply: Transaction Fee (JMD) - Fixed JMD 135.00 (order of application: 2)
3. Conditionally apply:
   - If order total < JMD 4,000: Platform Fee Small (JMD) - Fixed JMD 100.00 (order of application: 3)
   - If order total ≥ JMD 4,000: Platform Fee Large (JMD) - 2.7% (order of application: 3)

**For USD currency:**
1. Always apply: Processor Fee (USD) - 4.25% (order of application: 1)
2. Always apply: Transaction Fee (USD) - Fixed USD 0.99 (order of application: 2)
3. Conditionally apply:
   - If order total < USD 30: Platform Fee Small (USD) - Fixed USD 0.75 (order of application: 3)
   - If order total ≥ USD 30: Platform Fee Large (USD) - 2.7% (order of application: 3)

### Step 4: Apply Fees in Order
Apply the fees sequentially according to their `order_of_application` value:

1. Calculate Processor Fee (order of application: 1):
   ```
   processor_fee = order_total × 0.0425
   ```

2. Apply Transaction Fee (order of application: 2):
   ```
   transaction_fee = fixed amount (135.00 JMD or 0.99 USD)
   ```

3. Apply Platform Fee (order of application: 3):
   **For JMD:**
   ```
   if order_total < 4000:
       platform_fee = 100.00  # Fixed amount
   else:
       platform_fee = order_total × 0.027  # Percentage
   ```

   **For USD:**
   ```
   if order_total < 30:
       platform_fee = 0.75  # Fixed amount
   else:
       platform_fee = order_total × 0.027  # Percentage
   ```

4. Calculate Total Fees:
   ```
   total_fees = processor_fee + transaction_fee + platform_fee
   ```

5. Calculate Final Amount:
   ```
   final_amount = order_total + total_fees
   ```

## Critical Implementation Notes

1. **Fee Application Order**: Strictly follow the `order_of_application` values (1, 2, 3) when calculating fees.

2. **Threshold Comparisons**: Use the correct comparison operators:
   - For small fees: Use `<` (less than) the threshold
   - For large fees: Use `>=` (greater than or equal to) the threshold

3. **Currency Handling**: Apply the correct fee components based on the transaction currency.

4. **Percentage Calculations**: Apply percentage calculations on the base order total, not on a cumulative amount that includes other fees.

5. **Rounding**: Round monetary values to 2 decimal places after each calculation.

6. **Fee Rules**: Validate fee component applicability based on both currency and price threshold rules.

7. **Fee Component Selection Logic**: For each fee component in the config:
   - Check if the component's currency matches the transaction currency
   - For each rule associated with the component:
     - If rule_type is "CURRENCY", ensure the currency matches
     - If rule_type is "PRICE_THRESHOLD", apply the comparison using the correct operator

## Fee Component Structure Reference
Each fee component has the following structure:
```json
{
    "component_name": "platform_fee_small",
    "component_type": "FIXED",  // FIXED or PERCENTAGE
    "currency": "JMD",          // JMD or USD
    "fee_configuration_id": "aee8959a-e796-40e5-9e99-662a6345b9cb",
    "id": "22a76d7e-71ed-4851-92ba-9afca7dbbfeb",
    "is_included_in_base": false,
    "order_of_application": 3,  // 1, 2, or 3
    "value": 100.0             // Amount or percentage rate
}
```

## Rule Structure Reference
Each rule has the following structure:
```json
{
    "comparison_value": "4000",
    "fee_component_id": "22a76d7e-71ed-4851-92ba-9afca7dbbfeb",
    "id": "3bd3d807-fc18-4d4a-a9e5-1341de7e0b5e",
    "operator": "<",           // <, >=, or =
    "rule_type": "PRICE_THRESHOLD", // PRICE_THRESHOLD or CURRENCY
}
```

## Testing and Validation
For each transaction, developers should:
1. Log the currency and order total
2. Log which fee components were selected and why
3. Log the calculation of each fee component
4. Verify the final fee matches the expected calculation

## Example Calculation

For a JMD order with total of 3,000:
1. Processor Fee: 3,000 × 0.0425 = 127.50 JMD
2. Transaction Fee: 135.00 JMD (fixed)
3. Platform Fee: 100.00 JMD (fixed, since amount < 4,000)
4. Total Fees: 127.50 + 135.00 + 100.00 = 362.50 JMD
5. Final Amount: 3,000 + 362.50 = 3,362.50 JMD

For a USD order with total of 35:
1. Processor Fee: 35 × 0.0425 = 1.49 USD
2. Transaction Fee: 0.99 USD (fixed)
3. Platform Fee: 35 × 0.027 = 0.95 USD (percentage, since amount ≥ 30)
4. Total Fees: 1.49 + 0.99 + 0.95 = 3.43 USD
5. Final Amount: 35 + 3.43 = 38.43 USD

## Pseudocode Implementation

```python
def calculate_fees(order_total, currency, fee_config):
    # Get all fee components for the given currency
    components = [c for c in fee_config['components'] if c['currency'] == currency]
    
    # Sort components by order_of_application
    components.sort(key=lambda c: c['order_of_application'])
    
    # Find applicable components based on rules
    applicable_components = []
    for component in components:
        # Get rules for this component
        component_rules = [r for r in fee_config['rules'] if r['fee_component_id'] == component['id']]
        
        # Check if all rules are satisfied
        rules_satisfied = True
        for rule in component_rules:
            if rule['rule_type'] == 'CURRENCY':
                if not compare_values(currency, rule['operator'], rule['comparison_value']):
                    rules_satisfied = False
                    break
            elif rule['rule_type'] == 'PRICE_THRESHOLD':
                if not compare_values(order_total, rule['operator'], float(rule['comparison_value'])):
                    rules_satisfied = False
                    break
        
        if rules_satisfied:
            applicable_components.append(component)
    
    # Calculate fees
    total_fees = 0
    for component in applicable_components:
        if component['component_type'] == 'PERCENTAGE':
            fee = order_total * component['value']
        else:  # FIXED
            fee = component['value']
        
        total_fees += round(fee, 2)
    
    return total_fees

def compare_values(value1, operator, value2):
    if operator == '<':
        return value1 < value2
    elif operator == '>=':
        return value1 >= value2
    elif operator == '=':
        return value1 == value2
    return False
```

## Implementation Recommendations for Fee Calculation Fix

When implementing the fix for the `/initiate-series-payment` endpoint, consider the following approach:

1. **Isolate Fee Calculation Logic**: Extract the fee calculation into a separate function that takes order total, currency, and fee config as parameters.

2. **Add Detailed Logging**: Log each step of the fee calculation process for easier debugging:
   ```python
   # Example logging approach
   logging.info(f"Processing order: {order_total} {currency}")
   logging.info(f"Selected fee components: {applicable_components}")
   logging.info(f"Fee calculation details: processor={processor_fee}, transaction={transaction_fee}, platform={platform_fee}")
   ```

3. **Create Unit Tests**: Develop unit tests with various order amounts in both currencies to verify correct fee calculations.

4. **Compare with Expected Results**: Use the example calculations provided in this document to validate your implementation.

5. **Gradual Implementation**: Start by fixing one currency's fee calculation, verify it works correctly, then implement the other currency.

## Troubleshooting Common Issues

1. **Missing Currency Rules**: Ensure that for each fee component, you're checking if there are any currency-specific rules that must be satisfied.

2. **Incorrect Operator Usage**: Double-check that you're using the exact operator from the rules (`<`, `>=`, `=`) and not substituting similar ones (`<=`, `>`, `==`).

3. **Order of Application**: Verify that fees are being applied in the correct sequence (1, 2, 3) and not all at once.

4. **Rule Evaluation Logic**: Make sure you're applying an AND logic between rules (all rules must be satisfied) not OR logic.

5. **Rounding Errors**: Check for rounding errors by logging values before and after rounding operations.
