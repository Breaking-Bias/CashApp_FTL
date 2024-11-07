import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';  // Import this to use custom matchers
import Button from './Button';

test('renders Button', () => {
    render(<Button />);
    const butttonComponent = screen.getByText(/Dashboard Button/i);
    expect(butttonComponent).toBeInTheDocument(); 
});
