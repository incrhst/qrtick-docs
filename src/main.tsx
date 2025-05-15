import React from 'react';
import { createRoot } from 'react-dom/client';
import FeeCalculator from './FeeCalculator';

const root = createRoot(document.getElementById('root')!);
root.render(<FeeCalculator />); 