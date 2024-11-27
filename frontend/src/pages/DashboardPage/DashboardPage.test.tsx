// import { render, screen, fireEvent, waitFor } from '@testing-library/react';
// import DashboardPage from './DashboardPage';
// import { getGraphDataAPICall } from '../../services/ApiCalls';

// jest.mock('../../services/ApiCalls', () => ({
//     getGraphDataAPICall: jest.fn(),
//     getPastDataAPICall: jest.fn(),
// }));

// describe('DashboardPage', () => {

//     // it('renders the dashboard page correctly', async () => {

//     //     // Wait for graph to render
//     //     await waitFor(() => expect(screen.getByTestId('graph')).toBeInTheDocument());

//     //     // Test presence of filter elements
//     //     expect(screen.getByLabelText(/gender to analyse/i)).toBeInTheDocument();
//     //     expect(screen.getByLabelText(/race to analyse/i)).toBeInTheDocument();
//     // });

//     it('updates prediction on slider change', async () => {
//         render(<DashboardPage />);

//         // Test slider behavior
//         // const slider = screen.getByRole('slider');
//         // fireEvent.change(slider, { target: { value: 50 } });

//         // Test that graph updates accordingly
//         await waitFor(() => expect(getGraphDataAPICall).toHaveBeenCalled());
//     });
// });
