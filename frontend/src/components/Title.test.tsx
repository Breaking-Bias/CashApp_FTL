
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';  // Import this to use custom matchers
import Title from './Title';

test('renders Breaking Bias title', () => {
    render(<Title />);
    const titleElement = screen.getByText(/breaking bias/i);
    expect(titleElement).toBeInTheDocument();  // Check if the title is in the document
    expect(titleElement).toHaveStyle('color: green');  // Check if the color is green
});