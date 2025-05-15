import React, { useState } from 'react';

// QRTick brand colors
const COLORS = {
  primary: '#3D3939', // Brand Dark Gray
  gold: '#FDC230',    // Brand Gold
  background: '#FFF9EA', // Off White
  card: '#fff',
  text: '#3D3939',
  border: '#EEEEEE', // Light Gray
  error: '#D32F2F',
};

// Hardcoded fee config per spec
const FEE_CONFIG = {
  components: [
    // JMD
    { component_name: 'processor_fee_jmd', component_type: 'PERCENTAGE', currency: 'JMD', order_of_application: 1, value: 0.0425, id: 'processor_fee_jmd' },
    { component_name: 'transaction_fee_jmd', component_type: 'FIXED', currency: 'JMD', order_of_application: 2, value: 135.0, id: 'transaction_fee_jmd' },
    { component_name: 'platform_fee_small_jmd', component_type: 'FIXED', currency: 'JMD', order_of_application: 3, value: 50.0, id: 'platform_fee_small_jmd' },
    { component_name: 'platform_fee_large_jmd', component_type: 'PERCENTAGE', currency: 'JMD', order_of_application: 3, value: 0.027, id: 'platform_fee_large_jmd' },
    // USD
    { component_name: 'processor_fee_usd', component_type: 'PERCENTAGE', currency: 'USD', order_of_application: 1, value: 0.0425, id: 'processor_fee_usd' },
    { component_name: 'transaction_fee_usd', component_type: 'FIXED', currency: 'USD', order_of_application: 2, value: 0.99, id: 'transaction_fee_usd' },
    { component_name: 'platform_fee_small_usd', component_type: 'FIXED', currency: 'USD', order_of_application: 3, value: 0.75, id: 'platform_fee_small_usd' },
    { component_name: 'platform_fee_large_usd', component_type: 'PERCENTAGE', currency: 'USD', order_of_application: 3, value: 0.027, id: 'platform_fee_large_usd' },
  ],
};

function round2(val: number) {
  return Math.round(val * 100) / 100;
}

function calculateFees(orderTotal: number, currency: 'JMD' | 'USD') {
  const components = FEE_CONFIG.components.filter(c => c.currency === currency);
  components.sort((a, b) => a.order_of_application - b.order_of_application);
  let platformFeeComponent;
  if (currency === 'JMD') {
    platformFeeComponent = orderTotal < 3000
      ? components.find(c => c.id === 'platform_fee_small_jmd')
      : components.find(c => c.id === 'platform_fee_large_jmd');
  } else {
    platformFeeComponent = orderTotal < 30
      ? components.find(c => c.id === 'platform_fee_small_usd')
      : components.find(c => c.id === 'platform_fee_large_usd');
  }
  const processor = components.find(c => c.order_of_application === 1)!;
  const transaction = components.find(c => c.order_of_application === 2)!;
  const processorFee = round2(orderTotal * processor.value);
  const transactionFee = round2(transaction.value);
  let platformFee = 0;
  if (platformFeeComponent) {
    platformFee = platformFeeComponent.component_type === 'PERCENTAGE'
      ? round2(orderTotal * platformFeeComponent.value)
      : round2(platformFeeComponent.value);
  }
  const totalFees = round2(processorFee + transactionFee + platformFee);
  const finalAmount = round2(orderTotal + totalFees);
  return {
    processorFee,
    transactionFee,
    platformFee,
    totalFees,
    finalAmount,
    platformFeeType: platformFeeComponent?.component_type,
    platformFeeLabel: platformFeeComponent?.component_name.replace(/_/g, ' ').replace(/\b(jmd|usd)\b/i, '').trim(),
  };
}

const SLIDER_CONFIG = {
  JMD: { min: 1000, max: 100000, step: 100, default: 1000 },
  USD: { min: 60, max: 2000, step: 5, default: 60 },
};

export const FeeCalculator: React.FC = () => {
  const [currency, setCurrency] = useState<'JMD' | 'USD'>('JMD');
  const [orderTotal, setOrderTotal] = useState<number>(SLIDER_CONFIG['JMD'].default);
  const [touched, setTouched] = useState(false);

  const slider = SLIDER_CONFIG[currency];
  const isValid = !isNaN(orderTotal) && orderTotal >= slider.min;
  const fees = isValid ? calculateFees(orderTotal, currency) : null;

  const handleCurrencyChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newCurrency = e.target.value as 'JMD' | 'USD';
    setCurrency(newCurrency);
    setOrderTotal(SLIDER_CONFIG[newCurrency].default);
    setTouched(false);
  };

  const handleSliderChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setOrderTotal(Number(e.target.value));
    setTouched(true);
  };

  return (
    <div style={{
      background: COLORS.card,
      borderRadius: 16,
      maxWidth: 480,
      margin: '2.5rem auto',
      boxShadow: '0 2px 12px rgba(61,57,57,0.07)',
      padding: 36,
      fontFamily: 'Inter, Roboto, Arial, sans-serif',
      color: COLORS.text,
      border: `2px solid ${COLORS.border}`,
    }}>
      <h2 style={{ color: COLORS.primary, marginBottom: 8, fontWeight: 700, fontSize: 28, letterSpacing: '-0.5px' }}>QRTick Fee Comparison</h2>
      <p style={{ color: COLORS.primary, fontSize: 16, marginBottom: 28, fontWeight: 500 }}>
        Enter your order total and select currency to see how QRTick compares to a flat 10% fee.
      </p>
      <form
        onSubmit={e => e.preventDefault()}
        style={{ display: 'flex', flexDirection: 'column', gap: 22 }}
        autoComplete="off"
      >
        <div style={{ display: 'flex', gap: 22, alignItems: 'center', marginBottom: 8 }}>
          <label style={{ fontWeight: 600, display: 'flex', alignItems: 'center', gap: 6, fontSize: 16 }}>
            <input
              type="radio"
              name="currency"
              value="JMD"
              checked={currency === 'JMD'}
              onChange={handleCurrencyChange}
              style={{ accentColor: COLORS.gold, marginRight: 4 }}
            />
            JMD (J$)
          </label>
          <label style={{ fontWeight: 600, display: 'flex', alignItems: 'center', gap: 6, fontSize: 16 }}>
            <input
              type="radio"
              name="currency"
              value="USD"
              checked={currency === 'USD'}
              onChange={handleCurrencyChange}
              style={{ accentColor: COLORS.gold, marginRight: 4 }}
            />
            USD ($)
          </label>
        </div>
        <label style={{ fontWeight: 600, width: '100%' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 }}>
            <span>Order Total</span>
            <span style={{ color: COLORS.gold, fontWeight: 700, fontSize: 20 }}>{currency} {orderTotal.toLocaleString(undefined, { minimumFractionDigits: 0, maximumFractionDigits: 0 })}</span>
          </div>
          <input
            type="range"
            min={slider.min}
            max={slider.max}
            step={slider.step}
            value={orderTotal}
            onChange={handleSliderChange}
            style={{ width: '100%', accentColor: COLORS.gold }}
          />
          <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 14, color: COLORS.primary, marginTop: 2 }}>
            <span>{currency} {slider.min.toLocaleString()}</span>
            <span>{currency} {slider.max.toLocaleString()}</span>
          </div>
        </label>
      </form>
      {touched && !isValid && (
        <div style={{ color: COLORS.error, marginTop: 14, fontSize: 16 }}>
          Please enter a valid order total.
        </div>
      )}
      {isValid && fees && (
        <div style={{ marginTop: 34 }}>
          <div style={{
            marginTop: 0,
            background: COLORS.background,
            border: `2px solid ${COLORS.gold}`,
            borderRadius: 12,
            boxShadow: '0 2px 8px rgba(61,57,57,0.07)',
            padding: 22,
            textAlign: 'center',
          }}>
            <div style={{ fontWeight: 700, color: COLORS.primary, fontSize: 17, marginBottom: 12 }}>
              QRTick vs Flat 10% Fee Comparison
            </div>
            <table style={{ width: '100%', fontSize: 15, borderCollapse: 'collapse', margin: '0 auto', background: COLORS.card, borderRadius: 8 }}>
              <thead>
                <tr style={{ background: COLORS.background }}>
                  <th style={{ padding: 7, borderRadius: 7, color: COLORS.primary, fontWeight: 700, border: 'none' }}></th>
                  <th style={{ padding: 7, color: COLORS.primary, fontWeight: 700, border: 'none' }}>QRTick</th>
                  <th style={{ padding: 7, color: COLORS.primary, fontWeight: 700, border: 'none' }}>Flat 10% Fee</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style={{ textAlign: 'left', padding: 7 }}>Order Total (You Receive)</td>
                  <td style={{ textAlign: 'right', padding: 7 }}>{currency} {orderTotal.toLocaleString(undefined, { minimumFractionDigits: 0, maximumFractionDigits: 0 })}</td>
                  <td style={{ textAlign: 'right', padding: 7 }}>{currency} {orderTotal.toLocaleString(undefined, { minimumFractionDigits: 0, maximumFractionDigits: 0 })}</td>
                </tr>
                <tr>
                  <td style={{ textAlign: 'left', padding: 7 }}>Total Fees (Customer Pays)</td>
                  <td style={{ textAlign: 'right', padding: 7 }}>{currency} {fees.totalFees.toFixed(2)}</td>
                  <td style={{ textAlign: 'right', padding: 7 }}>{currency} {(round2(orderTotal * 0.10)).toFixed(2)}</td>
                </tr>
                <tr>
                  <td style={{ textAlign: 'left', padding: 7 }}>Final Amount (Customer Pays)</td>
                  <td style={{ textAlign: 'right', padding: 7 }}>{currency} {fees.finalAmount.toFixed(2)}</td>
                  <td style={{ textAlign: 'right', padding: 7 }}>{currency} {(round2(orderTotal * 1.10)).toFixed(2)}</td>
                </tr>
                <tr>
                  <td style={{ textAlign: 'left', padding: 7 }}>Effective Fee %</td>
                  <td style={{ textAlign: 'right', padding: 7 }}>{((fees.totalFees / orderTotal) * 100).toFixed(2)}%</td>
                  <td style={{ textAlign: 'right', padding: 7 }}>10.00%</td>
                </tr>
              </tbody>
            </table>
            <div style={{ color: COLORS.primary, fontSize: 14, marginTop: 12, fontWeight: 500 }}>
              In both cases, <b>the customer pays the fees</b> and <b>you always receive the full order total</b>.
            </div>
          </div>
        </div>
      )}
      <div style={{ marginTop: 36, fontSize: 14, color: COLORS.primary, textAlign: 'center' }}>
        Powered by <span style={{ color: COLORS.gold, fontWeight: 700 }}>QRTick</span>
      </div>
    </div>
  );
};

export default FeeCalculator; 