import React, { useState } from 'react';

// QRTick branding colors
const COLORS = {
  primary: '#1A73E8', // blue
  accent: '#00C853', // green
  background: '#F8FAFC', // light gray
  text: '#222',
  border: '#E0E7EF',
  error: '#D32F2F',
};

// Hardcoded fee config per spec
const FEE_CONFIG = {
  components: [
    // JMD
    {
      component_name: 'processor_fee_jmd',
      component_type: 'PERCENTAGE',
      currency: 'JMD',
      order_of_application: 1,
      value: 0.0425,
      id: 'processor_fee_jmd',
    },
    {
      component_name: 'transaction_fee_jmd',
      component_type: 'FIXED',
      currency: 'JMD',
      order_of_application: 2,
      value: 135.0,
      id: 'transaction_fee_jmd',
    },
    {
      component_name: 'platform_fee_small_jmd',
      component_type: 'FIXED',
      currency: 'JMD',
      order_of_application: 3,
      value: 100.0,
      id: 'platform_fee_small_jmd',
    },
    {
      component_name: 'platform_fee_large_jmd',
      component_type: 'PERCENTAGE',
      currency: 'JMD',
      order_of_application: 3,
      value: 0.027,
      id: 'platform_fee_large_jmd',
    },
    // USD
    {
      component_name: 'processor_fee_usd',
      component_type: 'PERCENTAGE',
      currency: 'USD',
      order_of_application: 1,
      value: 0.0425,
      id: 'processor_fee_usd',
    },
    {
      component_name: 'transaction_fee_usd',
      component_type: 'FIXED',
      currency: 'USD',
      order_of_application: 2,
      value: 0.99,
      id: 'transaction_fee_usd',
    },
    {
      component_name: 'platform_fee_small_usd',
      component_type: 'FIXED',
      currency: 'USD',
      order_of_application: 3,
      value: 0.75,
      id: 'platform_fee_small_usd',
    },
    {
      component_name: 'platform_fee_large_usd',
      component_type: 'PERCENTAGE',
      currency: 'USD',
      order_of_application: 3,
      value: 0.027,
      id: 'platform_fee_large_usd',
    },
  ],
};

function round2(val: number) {
  return Math.round(val * 100) / 100;
}

function calculateFees(orderTotal: number, currency: 'JMD' | 'USD') {
  // Select components for this currency
  const components = FEE_CONFIG.components.filter(c => c.currency === currency);
  // Sort by order_of_application
  components.sort((a, b) => a.order_of_application - b.order_of_application);

  // Determine which platform fee applies
  let platformFeeComponent;
  if (currency === 'JMD') {
    platformFeeComponent = orderTotal < 4000
      ? components.find(c => c.id === 'platform_fee_small_jmd')
      : components.find(c => c.id === 'platform_fee_large_jmd');
  } else {
    platformFeeComponent = orderTotal < 30
      ? components.find(c => c.id === 'platform_fee_small_usd')
      : components.find(c => c.id === 'platform_fee_large_usd');
  }

  // Build fee breakdown
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

export const FeeCalculator: React.FC = () => {
  const [orderTotal, setOrderTotal] = useState('');
  const [currency, setCurrency] = useState<'JMD' | 'USD'>('JMD');
  const [touched, setTouched] = useState(false);

  const parsedOrderTotal = parseFloat(orderTotal);
  const isValid = !isNaN(parsedOrderTotal) && parsedOrderTotal >= 0;
  const fees = isValid ? calculateFees(parsedOrderTotal, currency) : null;

  return (
    <div style={{
      background: COLORS.background,
      borderRadius: 12,
      maxWidth: 420,
      margin: '2rem auto',
      boxShadow: '0 2px 12px rgba(26,115,232,0.07)',
      padding: 32,
      fontFamily: 'Inter, Roboto, Arial, sans-serif',
      color: COLORS.text,
      border: `1px solid ${COLORS.border}`,
    }}>
      <h2 style={{ color: COLORS.primary, marginBottom: 8 }}>QRTick Fee Calculator</h2>
      <p style={{ color: '#555', fontSize: 15, marginBottom: 24 }}>
        Enter your order total and select currency to see a detailed fee breakdown.
      </p>
      <form
        onSubmit={e => e.preventDefault()}
        style={{ display: 'flex', flexDirection: 'column', gap: 18 }}
        autoComplete="off"
      >
        <label style={{ fontWeight: 500 }}>
          Order Total
          <input
            type="number"
            min="0"
            step="0.01"
            value={orderTotal}
            onChange={e => {
              setOrderTotal(e.target.value);
              setTouched(true);
            }}
            onBlur={() => setTouched(true)}
            placeholder="e.g. 3500"
            style={{
              marginTop: 6,
              padding: '8px 12px',
              border: `1px solid ${COLORS.border}`,
              borderRadius: 6,
              fontSize: 16,
              width: '100%',
              outline: 'none',
              boxSizing: 'border-box',
            }}
          />
        </label>
        <label style={{ fontWeight: 500 }}>
          Currency
          <select
            value={currency}
            onChange={e => setCurrency(e.target.value as 'JMD' | 'USD')}
            style={{
              marginTop: 6,
              padding: '8px 12px',
              border: `1px solid ${COLORS.border}`,
              borderRadius: 6,
              fontSize: 16,
              width: '100%',
              background: '#fff',
            }}
          >
            <option value="JMD">JMD (J$)</option>
            <option value="USD">USD ($)</option>
          </select>
        </label>
      </form>
      {touched && !isValid && (
        <div style={{ color: COLORS.error, marginTop: 12, fontSize: 15 }}>
          Please enter a valid order total.
        </div>
      )}
      {isValid && fees && (
        <div style={{ marginTop: 28 }}>
          <div style={{ fontWeight: 600, fontSize: 17, marginBottom: 10, color: COLORS.primary }}>
            Fee Breakdown
          </div>
          <table style={{ width: '100%', fontSize: 15, borderCollapse: 'collapse' }}>
            <tbody>
              <tr>
                <td>Processor Fee (4.25%)</td>
                <td style={{ textAlign: 'right' }}>{currency} {fees.processorFee.toFixed(2)}</td>
              </tr>
              <tr>
                <td>Transaction Fee</td>
                <td style={{ textAlign: 'right' }}>{currency} {fees.transactionFee.toFixed(2)}</td>
              </tr>
              <tr>
                <td>
                  Platform Fee
                  <span style={{ color: '#888', fontWeight: 400, fontSize: 13, marginLeft: 4 }}>
                    ({fees.platformFeeType === 'PERCENTAGE' ? '2.7%' : 'fixed'})
                  </span>
                </td>
                <td style={{ textAlign: 'right' }}>{currency} {fees.platformFee.toFixed(2)}</td>
              </tr>
              <tr>
                <td colSpan={2}><hr style={{ border: 0, borderTop: `1px solid ${COLORS.border}` }} /></td>
              </tr>
              <tr style={{ fontWeight: 600 }}>
                <td>Total Fees</td>
                <td style={{ textAlign: 'right', color: COLORS.primary }}>{currency} {fees.totalFees.toFixed(2)}</td>
              </tr>
              <tr style={{ fontWeight: 600 }}>
                <td>Final Amount</td>
                <td style={{ textAlign: 'right', color: COLORS.accent }}>{currency} {fees.finalAmount.toFixed(2)}</td>
              </tr>
            </tbody>
          </table>
        </div>
      )}
      <div style={{ marginTop: 32, fontSize: 13, color: '#888', textAlign: 'center' }}>
        Powered by <span style={{ color: COLORS.primary, fontWeight: 600 }}>QRTick</span>
      </div>
    </div>
  );
};

export default FeeCalculator; 