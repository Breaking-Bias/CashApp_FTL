import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';  // Import this to use custom matchers
import Button from './Button';

test('ButtonTest', () => {
    render(<Button label="Hi" backgroundColor="Green" fontSize={8} />);
    const buttonComponent = screen.getByText(/Dashboard Button/i);
    expect(buttonComponent).toBeInTheDocument(); 
});
